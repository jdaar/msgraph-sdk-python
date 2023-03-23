from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

json = lazy_import('msgraph.generated.models.json')

class EoMonthPostRequestBody(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new eoMonthPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The months property
        self._months: Optional[json.Json] = None
        # The startDate property
        self._start_date: Optional[json.Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EoMonthPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EoMonthPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EoMonthPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "months": lambda n : setattr(self, 'months', n.get_object_value(json.Json)),
            "startDate": lambda n : setattr(self, 'start_date', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def months(self,) -> Optional[json.Json]:
        """
        Gets the months property value. The months property
        Returns: Optional[json.Json]
        """
        return self._months
    
    @months.setter
    def months(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the months property value. The months property
        Args:
            value: Value to set for the months property.
        """
        self._months = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("months", self.months)
        writer.write_object_value("startDate", self.start_date)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def start_date(self,) -> Optional[json.Json]:
        """
        Gets the startDate property value. The startDate property
        Returns: Optional[json.Json]
        """
        return self._start_date
    
    @start_date.setter
    def start_date(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the startDate property value. The startDate property
        Args:
            value: Value to set for the start_date property.
        """
        self._start_date = value
    
