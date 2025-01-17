from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .email_payload_detail import EmailPayloadDetail
    from .payload_coachmark import PayloadCoachmark

@dataclass
class PayloadDetail(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The coachmarks property
    coachmarks: Optional[List[PayloadCoachmark]] = None
    # The content property
    content: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The phishingUrl property
    phishing_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PayloadDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PayloadDetail
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.emailPayloadDetail".casefold():
            from .email_payload_detail import EmailPayloadDetail

            return EmailPayloadDetail()
        return PayloadDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .email_payload_detail import EmailPayloadDetail
        from .payload_coachmark import PayloadCoachmark

        from .email_payload_detail import EmailPayloadDetail
        from .payload_coachmark import PayloadCoachmark

        fields: Dict[str, Callable[[Any], None]] = {
            "coachmarks": lambda n : setattr(self, 'coachmarks', n.get_collection_of_object_values(PayloadCoachmark)),
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "phishingUrl": lambda n : setattr(self, 'phishing_url', n.get_str_value()),
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
        writer.write_collection_of_object_values("coachmarks", self.coachmarks)
        writer.write_str_value("content", self.content)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("phishingUrl", self.phishing_url)
        writer.write_additional_data_value(self.additional_data)
    

