from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class UserTrainingContentEventInfo(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Browser of the user from where the training event was generated.
    browser: Optional[str] = None
    # Date and time of the training content playback by the user.
    content_date_time: Optional[datetime.datetime] = None
    # IP address of the user for the training event.
    ip_address: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The operating system, platform, and device details of the user for the training event.
    os_platform_device_details: Optional[str] = None
    # Potential improvement in the tenant security posture after completion of the training by the user.
    potential_score_impact: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserTrainingContentEventInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserTrainingContentEventInfo
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserTrainingContentEventInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "browser": lambda n : setattr(self, 'browser', n.get_str_value()),
            "contentDateTime": lambda n : setattr(self, 'content_date_time', n.get_datetime_value()),
            "ipAddress": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "osPlatformDeviceDetails": lambda n : setattr(self, 'os_platform_device_details', n.get_str_value()),
            "potentialScoreImpact": lambda n : setattr(self, 'potential_score_impact', n.get_float_value()),
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
        writer.write_str_value("browser", self.browser)
        writer.write_datetime_value("contentDateTime", self.content_date_time)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("osPlatformDeviceDetails", self.os_platform_device_details)
        writer.write_float_value("potentialScoreImpact", self.potential_score_impact)
        writer.write_additional_data_value(self.additional_data)
    

