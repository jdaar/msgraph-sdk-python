from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class UserExperienceAnalyticsCloudManagementDevicesSummary(AdditionalDataHolder, BackedModel, Parsable):
    """
    The user experience work from anywhere Cloud management devices summary.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Total number of  co-managed devices. Read-only.
    co_managed_device_count: Optional[int] = None
    # The count of intune devices that are not autopilot registerd. Read-only.
    intune_device_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Total count of tenant attach devices. Read-only.
    tenant_attach_device_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsCloudManagementDevicesSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsCloudManagementDevicesSummary
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsCloudManagementDevicesSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "coManagedDeviceCount": lambda n : setattr(self, 'co_managed_device_count', n.get_int_value()),
            "intuneDeviceCount": lambda n : setattr(self, 'intune_device_count', n.get_int_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "tenantAttachDeviceCount": lambda n : setattr(self, 'tenant_attach_device_count', n.get_int_value()),
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
        writer.write_int_value("coManagedDeviceCount", self.co_managed_device_count)
        writer.write_int_value("intuneDeviceCount", self.intune_device_count)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_int_value("tenantAttachDeviceCount", self.tenant_attach_device_count)
        writer.write_additional_data_value(self.additional_data)
    

