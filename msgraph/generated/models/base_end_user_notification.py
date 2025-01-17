from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .end_user_notification import EndUserNotification
    from .positive_reinforcement_notification import PositiveReinforcementNotification
    from .simulation_notification import SimulationNotification
    from .training_reminder_notification import TrainingReminderNotification

@dataclass
class BaseEndUserNotification(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The defaultLanguage property
    default_language: Optional[str] = None
    # The endUserNotification property
    end_user_notification: Optional[EndUserNotification] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BaseEndUserNotification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BaseEndUserNotification
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.positiveReinforcementNotification".casefold():
            from .positive_reinforcement_notification import PositiveReinforcementNotification

            return PositiveReinforcementNotification()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.simulationNotification".casefold():
            from .simulation_notification import SimulationNotification

            return SimulationNotification()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.trainingReminderNotification".casefold():
            from .training_reminder_notification import TrainingReminderNotification

            return TrainingReminderNotification()
        return BaseEndUserNotification()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .end_user_notification import EndUserNotification
        from .positive_reinforcement_notification import PositiveReinforcementNotification
        from .simulation_notification import SimulationNotification
        from .training_reminder_notification import TrainingReminderNotification

        from .end_user_notification import EndUserNotification
        from .positive_reinforcement_notification import PositiveReinforcementNotification
        from .simulation_notification import SimulationNotification
        from .training_reminder_notification import TrainingReminderNotification

        fields: Dict[str, Callable[[Any], None]] = {
            "defaultLanguage": lambda n : setattr(self, 'default_language', n.get_str_value()),
            "endUserNotification": lambda n : setattr(self, 'end_user_notification', n.get_object_value(EndUserNotification)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("defaultLanguage", self.default_language)
        writer.write_object_value("endUserNotification", self.end_user_notification)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

