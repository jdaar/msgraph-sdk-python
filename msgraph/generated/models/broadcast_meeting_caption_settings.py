from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class BroadcastMeetingCaptionSettings(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Indicates whether captions are enabled for this Teams live event.
    is_caption_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The spoken language.
    spoken_language: Optional[str] = None
    # The translation languages (choose up to 6).
    translation_languages: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BroadcastMeetingCaptionSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BroadcastMeetingCaptionSettings
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return BroadcastMeetingCaptionSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "isCaptionEnabled": lambda n : setattr(self, 'is_caption_enabled', n.get_bool_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "spokenLanguage": lambda n : setattr(self, 'spoken_language', n.get_str_value()),
            "translationLanguages": lambda n : setattr(self, 'translation_languages', n.get_collection_of_primitive_values(str)),
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
        writer.write_bool_value("isCaptionEnabled", self.is_caption_enabled)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("spokenLanguage", self.spoken_language)
        writer.write_collection_of_primitive_values("translationLanguages", self.translation_languages)
        writer.write_additional_data_value(self.additional_data)
    

