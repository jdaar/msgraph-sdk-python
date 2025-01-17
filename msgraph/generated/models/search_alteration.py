from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .altered_query_token import AlteredQueryToken

@dataclass
class SearchAlteration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Defines the altered highlighted query string with spelling correction. The annotation around the corrected segment is: /ue000, /ue001.
    altered_highlighted_query_string: Optional[str] = None
    # Defines the altered query string with spelling correction.
    altered_query_string: Optional[str] = None
    # Represents changed segments related to an original user query.
    altered_query_tokens: Optional[List[AlteredQueryToken]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SearchAlteration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SearchAlteration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SearchAlteration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .altered_query_token import AlteredQueryToken

        from .altered_query_token import AlteredQueryToken

        fields: Dict[str, Callable[[Any], None]] = {
            "alteredHighlightedQueryString": lambda n : setattr(self, 'altered_highlighted_query_string', n.get_str_value()),
            "alteredQueryString": lambda n : setattr(self, 'altered_query_string', n.get_str_value()),
            "alteredQueryTokens": lambda n : setattr(self, 'altered_query_tokens', n.get_collection_of_object_values(AlteredQueryToken)),
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
        writer.write_str_value("alteredHighlightedQueryString", self.altered_highlighted_query_string)
        writer.write_str_value("alteredQueryString", self.altered_query_string)
        writer.write_collection_of_object_values("alteredQueryTokens", self.altered_query_tokens)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

