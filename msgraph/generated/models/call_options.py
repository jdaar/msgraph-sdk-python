from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .incoming_call_options import IncomingCallOptions
    from .outgoing_call_options import OutgoingCallOptions

@dataclass
class CallOptions(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Indicates whether to hide the app after the call is escalated.
    hide_bot_after_escalation: Optional[bool] = None
    # Indicates whether content sharing notifications should be enabled for the call.
    is_content_sharing_notification_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CallOptions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CallOptions
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.incomingCallOptions".casefold():
            from .incoming_call_options import IncomingCallOptions

            return IncomingCallOptions()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.outgoingCallOptions".casefold():
            from .outgoing_call_options import OutgoingCallOptions

            return OutgoingCallOptions()
        return CallOptions()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .incoming_call_options import IncomingCallOptions
        from .outgoing_call_options import OutgoingCallOptions

        from .incoming_call_options import IncomingCallOptions
        from .outgoing_call_options import OutgoingCallOptions

        fields: Dict[str, Callable[[Any], None]] = {
            "hideBotAfterEscalation": lambda n : setattr(self, 'hide_bot_after_escalation', n.get_bool_value()),
            "isContentSharingNotificationEnabled": lambda n : setattr(self, 'is_content_sharing_notification_enabled', n.get_bool_value()),
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
        writer.write_bool_value("hideBotAfterEscalation", self.hide_bot_after_escalation)
        writer.write_bool_value("isContentSharingNotificationEnabled", self.is_content_sharing_notification_enabled)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

