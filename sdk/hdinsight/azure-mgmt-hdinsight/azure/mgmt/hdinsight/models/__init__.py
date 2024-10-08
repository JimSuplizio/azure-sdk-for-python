# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AaddsResourceDetails
from ._models_py3 import Application
from ._models_py3 import ApplicationGetEndpoint
from ._models_py3 import ApplicationGetHttpsEndpoint
from ._models_py3 import ApplicationListResult
from ._models_py3 import ApplicationProperties
from ._models_py3 import AsyncOperationResult
from ._models_py3 import Autoscale
from ._models_py3 import AutoscaleCapacity
from ._models_py3 import AutoscaleConfigurationUpdateParameter
from ._models_py3 import AutoscaleRecurrence
from ._models_py3 import AutoscaleSchedule
from ._models_py3 import AutoscaleTimeAndCapacity
from ._models_py3 import AzureMonitorRequest
from ._models_py3 import AzureMonitorResponse
from ._models_py3 import AzureMonitorSelectedConfigurations
from ._models_py3 import AzureMonitorTableConfiguration
from ._models_py3 import BillingMeters
from ._models_py3 import BillingResources
from ._models_py3 import BillingResponseListResult
from ._models_py3 import CapabilitiesResult
from ._models_py3 import ClientGroupInfo
from ._models_py3 import Cluster
from ._models_py3 import ClusterConfigurations
from ._models_py3 import ClusterCreateParametersExtended
from ._models_py3 import ClusterCreateProperties
from ._models_py3 import ClusterCreateRequestValidationParameters
from ._models_py3 import ClusterCreateValidationResult
from ._models_py3 import ClusterDefinition
from ._models_py3 import ClusterDiskEncryptionParameters
from ._models_py3 import ClusterGetProperties
from ._models_py3 import ClusterIdentity
from ._models_py3 import ClusterListPersistedScriptActionsResult
from ._models_py3 import ClusterListResult
from ._models_py3 import ClusterMonitoringRequest
from ._models_py3 import ClusterMonitoringResponse
from ._models_py3 import ClusterPatchParameters
from ._models_py3 import ClusterResizeParameters
from ._models_py3 import ComputeIsolationProperties
from ._models_py3 import ComputeProfile
from ._models_py3 import ConnectivityEndpoint
from ._models_py3 import DataDisksGroups
from ._models_py3 import Dimension
from ._models_py3 import DiskBillingMeters
from ._models_py3 import DiskEncryptionProperties
from ._models_py3 import EncryptionInTransitProperties
from ._models_py3 import ErrorResponse
from ._models_py3 import Errors
from ._models_py3 import ExcludedServicesConfig
from ._models_py3 import ExecuteScriptActionParameters
from ._models_py3 import Extension
from ._models_py3 import GatewaySettings
from ._models_py3 import HardwareProfile
from ._models_py3 import HostInfo
from ._models_py3 import IPConfiguration
from ._models_py3 import IpTag
from ._models_py3 import KafkaRestProperties
from ._models_py3 import LinuxOperatingSystemProfile
from ._models_py3 import LocalizedName
from ._models_py3 import MetricSpecifications
from ._models_py3 import NameAvailabilityCheckRequestParameters
from ._models_py3 import NameAvailabilityCheckResult
from ._models_py3 import NetworkProperties
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import OperationProperties
from ._models_py3 import OsProfile
from ._models_py3 import PrivateEndpoint
from ._models_py3 import PrivateEndpointConnection
from ._models_py3 import PrivateEndpointConnectionListResult
from ._models_py3 import PrivateLinkConfiguration
from ._models_py3 import PrivateLinkResource
from ._models_py3 import PrivateLinkResourceListResult
from ._models_py3 import PrivateLinkServiceConnectionState
from ._models_py3 import ProxyResource
from ._models_py3 import QuotaCapability
from ._models_py3 import QuotaInfo
from ._models_py3 import RegionalQuotaCapability
from ._models_py3 import RegionsCapability
from ._models_py3 import Resource
from ._models_py3 import ResourceAutoGenerated
from ._models_py3 import ResourceId
from ._models_py3 import Role
from ._models_py3 import RuntimeScriptAction
from ._models_py3 import RuntimeScriptActionDetail
from ._models_py3 import ScriptAction
from ._models_py3 import ScriptActionExecutionHistoryList
from ._models_py3 import ScriptActionExecutionSummary
from ._models_py3 import ScriptActionPersistedGetResponseSpec
from ._models_py3 import ScriptActionsList
from ._models_py3 import SecurityProfile
from ._models_py3 import ServiceSpecification
from ._models_py3 import SshProfile
from ._models_py3 import SshPublicKey
from ._models_py3 import StorageAccount
from ._models_py3 import StorageProfile
from ._models_py3 import SystemData
from ._models_py3 import TrackedResource
from ._models_py3 import UpdateClusterIdentityCertificateParameters
from ._models_py3 import UpdateGatewaySettingsParameters
from ._models_py3 import Usage
from ._models_py3 import UsagesListResult
from ._models_py3 import UserAssignedIdentity
from ._models_py3 import ValidationErrorInfo
from ._models_py3 import VersionSpec
from ._models_py3 import VersionsCapability
from ._models_py3 import VirtualNetworkProfile
from ._models_py3 import VmSizeCompatibilityFilterV2
from ._models_py3 import VmSizeProperty

from ._hd_insight_management_client_enums import AsyncOperationState
from ._hd_insight_management_client_enums import CreatedByType
from ._hd_insight_management_client_enums import DaysOfWeek
from ._hd_insight_management_client_enums import DirectoryType
from ._hd_insight_management_client_enums import FilterMode
from ._hd_insight_management_client_enums import HDInsightClusterProvisioningState
from ._hd_insight_management_client_enums import JsonWebKeyEncryptionAlgorithm
from ._hd_insight_management_client_enums import OSType
from ._hd_insight_management_client_enums import OutboundDependenciesManagedType
from ._hd_insight_management_client_enums import PrivateEndpointConnectionProvisioningState
from ._hd_insight_management_client_enums import PrivateIPAllocationMethod
from ._hd_insight_management_client_enums import PrivateLink
from ._hd_insight_management_client_enums import PrivateLinkConfigurationProvisioningState
from ._hd_insight_management_client_enums import PrivateLinkServiceConnectionStatus
from ._hd_insight_management_client_enums import ResourceIdentityType
from ._hd_insight_management_client_enums import ResourceProviderConnection
from ._hd_insight_management_client_enums import RoleName
from ._hd_insight_management_client_enums import Tier
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AaddsResourceDetails",
    "Application",
    "ApplicationGetEndpoint",
    "ApplicationGetHttpsEndpoint",
    "ApplicationListResult",
    "ApplicationProperties",
    "AsyncOperationResult",
    "Autoscale",
    "AutoscaleCapacity",
    "AutoscaleConfigurationUpdateParameter",
    "AutoscaleRecurrence",
    "AutoscaleSchedule",
    "AutoscaleTimeAndCapacity",
    "AzureMonitorRequest",
    "AzureMonitorResponse",
    "AzureMonitorSelectedConfigurations",
    "AzureMonitorTableConfiguration",
    "BillingMeters",
    "BillingResources",
    "BillingResponseListResult",
    "CapabilitiesResult",
    "ClientGroupInfo",
    "Cluster",
    "ClusterConfigurations",
    "ClusterCreateParametersExtended",
    "ClusterCreateProperties",
    "ClusterCreateRequestValidationParameters",
    "ClusterCreateValidationResult",
    "ClusterDefinition",
    "ClusterDiskEncryptionParameters",
    "ClusterGetProperties",
    "ClusterIdentity",
    "ClusterListPersistedScriptActionsResult",
    "ClusterListResult",
    "ClusterMonitoringRequest",
    "ClusterMonitoringResponse",
    "ClusterPatchParameters",
    "ClusterResizeParameters",
    "ComputeIsolationProperties",
    "ComputeProfile",
    "ConnectivityEndpoint",
    "DataDisksGroups",
    "Dimension",
    "DiskBillingMeters",
    "DiskEncryptionProperties",
    "EncryptionInTransitProperties",
    "ErrorResponse",
    "Errors",
    "ExcludedServicesConfig",
    "ExecuteScriptActionParameters",
    "Extension",
    "GatewaySettings",
    "HardwareProfile",
    "HostInfo",
    "IPConfiguration",
    "IpTag",
    "KafkaRestProperties",
    "LinuxOperatingSystemProfile",
    "LocalizedName",
    "MetricSpecifications",
    "NameAvailabilityCheckRequestParameters",
    "NameAvailabilityCheckResult",
    "NetworkProperties",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "OperationProperties",
    "OsProfile",
    "PrivateEndpoint",
    "PrivateEndpointConnection",
    "PrivateEndpointConnectionListResult",
    "PrivateLinkConfiguration",
    "PrivateLinkResource",
    "PrivateLinkResourceListResult",
    "PrivateLinkServiceConnectionState",
    "ProxyResource",
    "QuotaCapability",
    "QuotaInfo",
    "RegionalQuotaCapability",
    "RegionsCapability",
    "Resource",
    "ResourceAutoGenerated",
    "ResourceId",
    "Role",
    "RuntimeScriptAction",
    "RuntimeScriptActionDetail",
    "ScriptAction",
    "ScriptActionExecutionHistoryList",
    "ScriptActionExecutionSummary",
    "ScriptActionPersistedGetResponseSpec",
    "ScriptActionsList",
    "SecurityProfile",
    "ServiceSpecification",
    "SshProfile",
    "SshPublicKey",
    "StorageAccount",
    "StorageProfile",
    "SystemData",
    "TrackedResource",
    "UpdateClusterIdentityCertificateParameters",
    "UpdateGatewaySettingsParameters",
    "Usage",
    "UsagesListResult",
    "UserAssignedIdentity",
    "ValidationErrorInfo",
    "VersionSpec",
    "VersionsCapability",
    "VirtualNetworkProfile",
    "VmSizeCompatibilityFilterV2",
    "VmSizeProperty",
    "AsyncOperationState",
    "CreatedByType",
    "DaysOfWeek",
    "DirectoryType",
    "FilterMode",
    "HDInsightClusterProvisioningState",
    "JsonWebKeyEncryptionAlgorithm",
    "OSType",
    "OutboundDependenciesManagedType",
    "PrivateEndpointConnectionProvisioningState",
    "PrivateIPAllocationMethod",
    "PrivateLink",
    "PrivateLinkConfigurationProvisioningState",
    "PrivateLinkServiceConnectionStatus",
    "ResourceIdentityType",
    "ResourceProviderConnection",
    "RoleName",
    "Tier",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
