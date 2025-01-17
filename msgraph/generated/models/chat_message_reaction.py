from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet

@dataclass
class ChatMessageReaction(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    created_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Supported values are like, angry, sad, laugh, heart, surprised.
    reaction_type: Optional[str] = None
    # The user property
    user: Optional[ChatMessageReactionIdentitySet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChatMessageReaction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ChatMessageReaction
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ChatMessageReaction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet

        from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "reactionType": lambda n : setattr(self, 'reaction_type', n.get_str_value()),
            "user": lambda n : setattr(self, 'user', n.get_object_value(ChatMessageReactionIdentitySet)),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("reactionType", self.reaction_type)
        writer.write_object_value("user", self.user)
        writer.write_additional_data_value(self.additional_data)
    

