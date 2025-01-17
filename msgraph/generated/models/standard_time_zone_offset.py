from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .daylight_time_zone_offset import DaylightTimeZoneOffset
    from .day_of_week import DayOfWeek

@dataclass
class StandardTimeZoneOffset(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Represents the nth occurrence of the day of week that the transition from daylight saving time to standard time occurs.
    day_occurrence: Optional[int] = None
    # Represents the day of the week when the transition from daylight saving time to standard time.
    day_of_week: Optional[DayOfWeek] = None
    # Represents the month of the year when the transition from daylight saving time to standard time occurs.
    month: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the time of day when the transition from daylight saving time to standard time occurs.
    time: Optional[datetime.time] = None
    # Represents how frequently in terms of years the change from daylight saving time to standard time occurs. For example, a value of 0 means every year.
    year: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> StandardTimeZoneOffset:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StandardTimeZoneOffset
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.daylightTimeZoneOffset".casefold():
            from .daylight_time_zone_offset import DaylightTimeZoneOffset

            return DaylightTimeZoneOffset()
        return StandardTimeZoneOffset()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .daylight_time_zone_offset import DaylightTimeZoneOffset
        from .day_of_week import DayOfWeek

        from .daylight_time_zone_offset import DaylightTimeZoneOffset
        from .day_of_week import DayOfWeek

        fields: Dict[str, Callable[[Any], None]] = {
            "dayOccurrence": lambda n : setattr(self, 'day_occurrence', n.get_int_value()),
            "dayOfWeek": lambda n : setattr(self, 'day_of_week', n.get_enum_value(DayOfWeek)),
            "month": lambda n : setattr(self, 'month', n.get_int_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "time": lambda n : setattr(self, 'time', n.get_time_value()),
            "year": lambda n : setattr(self, 'year', n.get_int_value()),
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
        writer.write_int_value("dayOccurrence", self.day_occurrence)
        writer.write_enum_value("dayOfWeek", self.day_of_week)
        writer.write_int_value("month", self.month)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_time_value("time", self.time)
        writer.write_int_value("year", self.year)
        writer.write_additional_data_value(self.additional_data)
    

