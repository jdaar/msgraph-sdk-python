from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows_information_protection_desktop_app import WindowsInformationProtectionDesktopApp
    from .windows_information_protection_store_app import WindowsInformationProtectionStoreApp

@dataclass
class WindowsInformationProtectionApp(AdditionalDataHolder, BackedModel, Parsable):
    """
    App for Windows information protection
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # If true, app is denied protection or exemption.
    denied: Optional[bool] = None
    # The app's description.
    description: Optional[str] = None
    # App display name.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The product name.
    product_name: Optional[str] = None
    # The publisher name
    publisher_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsInformationProtectionApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsInformationProtectionApp
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsInformationProtectionDesktopApp".casefold():
            from .windows_information_protection_desktop_app import WindowsInformationProtectionDesktopApp

            return WindowsInformationProtectionDesktopApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsInformationProtectionStoreApp".casefold():
            from .windows_information_protection_store_app import WindowsInformationProtectionStoreApp

            return WindowsInformationProtectionStoreApp()
        return WindowsInformationProtectionApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .windows_information_protection_desktop_app import WindowsInformationProtectionDesktopApp
        from .windows_information_protection_store_app import WindowsInformationProtectionStoreApp

        from .windows_information_protection_desktop_app import WindowsInformationProtectionDesktopApp
        from .windows_information_protection_store_app import WindowsInformationProtectionStoreApp

        fields: Dict[str, Callable[[Any], None]] = {
            "denied": lambda n : setattr(self, 'denied', n.get_bool_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "productName": lambda n : setattr(self, 'product_name', n.get_str_value()),
            "publisherName": lambda n : setattr(self, 'publisher_name', n.get_str_value()),
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
        writer.write_bool_value("denied", self.denied)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("productName", self.product_name)
        writer.write_str_value("publisherName", self.publisher_name)
        writer.write_additional_data_value(self.additional_data)
    

