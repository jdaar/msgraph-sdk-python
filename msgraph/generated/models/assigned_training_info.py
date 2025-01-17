from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class AssignedTrainingInfo(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Number of users who were assigned the training in an attack simulation and training campaign.
    assigned_user_count: Optional[int] = None
    # Number of users who completed the training in an attack simulation and training campaign.
    completed_user_count: Optional[int] = None
    # Display name of the training in an attack simulation and training campaign.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AssignedTrainingInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AssignedTrainingInfo
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AssignedTrainingInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "assignedUserCount": lambda n : setattr(self, 'assigned_user_count', n.get_int_value()),
            "completedUserCount": lambda n : setattr(self, 'completed_user_count', n.get_int_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
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
        writer.write_int_value("assignedUserCount", self.assigned_user_count)
        writer.write_int_value("completedUserCount", self.completed_user_count)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

