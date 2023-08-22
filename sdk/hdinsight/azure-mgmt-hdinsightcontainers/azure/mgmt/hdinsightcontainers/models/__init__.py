# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AksClusterProfile
from ._models_py3 import AksClusterProfileAksClusterAgentPoolIdentityProfile
from ._models_py3 import AuthorizationProfile
from ._models_py3 import AutoscaleProfile
from ._models_py3 import CatalogOptions
from ._models_py3 import Cluster
from ._models_py3 import ClusterComponentsItem
from ._models_py3 import ClusterConfigFile
from ._models_py3 import ClusterInstanceViewProperties
from ._models_py3 import ClusterInstanceViewPropertiesStatus
from ._models_py3 import ClusterInstanceViewResult
from ._models_py3 import ClusterInstanceViewResultProperties
from ._models_py3 import ClusterInstanceViewStatus
from ._models_py3 import ClusterInstanceViewsResult
from ._models_py3 import ClusterJob
from ._models_py3 import ClusterJobList
from ._models_py3 import ClusterJobProperties
from ._models_py3 import ClusterListResult
from ._models_py3 import ClusterLogAnalyticsApplicationLogs
from ._models_py3 import ClusterLogAnalyticsProfile
from ._models_py3 import ClusterPatch
from ._models_py3 import ClusterPool
from ._models_py3 import ClusterPoolComputeProfile
from ._models_py3 import ClusterPoolListResult
from ._models_py3 import ClusterPoolLogAnalyticsProfile
from ._models_py3 import ClusterPoolNetworkProfile
from ._models_py3 import ClusterPoolProfile
from ._models_py3 import ClusterPoolResourcePropertiesAksClusterProfile
from ._models_py3 import ClusterPoolResourcePropertiesClusterPoolProfile
from ._models_py3 import ClusterPoolResourcePropertiesComputeProfile
from ._models_py3 import ClusterPoolResourcePropertiesLogAnalyticsProfile
from ._models_py3 import ClusterPoolResourcePropertiesNetworkProfile
from ._models_py3 import ClusterPoolVersion
from ._models_py3 import ClusterPoolVersionsListResult
from ._models_py3 import ClusterProfile
from ._models_py3 import ClusterPrometheusProfile
from ._models_py3 import ClusterResizeData
from ._models_py3 import ClusterServiceConfig
from ._models_py3 import ClusterServiceConfigsProfile
from ._models_py3 import ClusterVersion
from ._models_py3 import ClusterVersionsListResult
from ._models_py3 import ComparisonRule
from ._models_py3 import ComputeProfile
from ._models_py3 import ComputeResourceDefinition
from ._models_py3 import ConnectivityProfile
from ._models_py3 import ConnectivityProfileWeb
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorResponse
from ._models_py3 import FlinkCatalogOptions
from ._models_py3 import FlinkHiveCatalogOption
from ._models_py3 import FlinkJobProperties
from ._models_py3 import FlinkProfile
from ._models_py3 import FlinkStorageProfile
from ._models_py3 import HiveCatalogOption
from ._models_py3 import IdentityProfile
from ._models_py3 import LoadBasedConfig
from ._models_py3 import NameAvailabilityParameters
from ._models_py3 import NameAvailabilityResult
from ._models_py3 import NodeProfile
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import ProxyResource
from ._models_py3 import Resource
from ._models_py3 import ScalingRule
from ._models_py3 import Schedule
from ._models_py3 import ScheduleBasedConfig
from ._models_py3 import ScriptActionProfile
from ._models_py3 import SecretReference
from ._models_py3 import SecretsProfile
from ._models_py3 import ServiceConfigListResult
from ._models_py3 import ServiceConfigListResultProperties
from ._models_py3 import ServiceConfigListResultValueEntity
from ._models_py3 import ServiceConfigResult
from ._models_py3 import ServiceConfigResultProperties
from ._models_py3 import ServiceStatus
from ._models_py3 import SparkMetastoreSpec
from ._models_py3 import SparkProfile
from ._models_py3 import SparkUserPlugin
from ._models_py3 import SparkUserPlugins
from ._models_py3 import SshConnectivityEndpoint
from ._models_py3 import SshProfile
from ._models_py3 import SystemData
from ._models_py3 import TagsObject
from ._models_py3 import TrackedResource
from ._models_py3 import TrinoCoordinator
from ._models_py3 import TrinoProfile
from ._models_py3 import TrinoTelemetryConfig
from ._models_py3 import TrinoUserPlugin
from ._models_py3 import TrinoUserPlugins
from ._models_py3 import TrinoUserTelemetry
from ._models_py3 import TrinoWorker
from ._models_py3 import UpdatableClusterProfile
from ._models_py3 import WebConnectivityEndpoint

from ._hd_insight_containers_mgmt_client_enums import Action
from ._hd_insight_containers_mgmt_client_enums import ActionType
from ._hd_insight_containers_mgmt_client_enums import AutoscaleType
from ._hd_insight_containers_mgmt_client_enums import ComparisonOperator
from ._hd_insight_containers_mgmt_client_enums import ContentEncoding
from ._hd_insight_containers_mgmt_client_enums import CreatedByType
from ._hd_insight_containers_mgmt_client_enums import JobType
from ._hd_insight_containers_mgmt_client_enums import KeyVaultObjectType
from ._hd_insight_containers_mgmt_client_enums import Origin
from ._hd_insight_containers_mgmt_client_enums import ProvisioningStatus
from ._hd_insight_containers_mgmt_client_enums import ScaleActionType
from ._hd_insight_containers_mgmt_client_enums import ScheduleDay
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AksClusterProfile",
    "AksClusterProfileAksClusterAgentPoolIdentityProfile",
    "AuthorizationProfile",
    "AutoscaleProfile",
    "CatalogOptions",
    "Cluster",
    "ClusterComponentsItem",
    "ClusterConfigFile",
    "ClusterInstanceViewProperties",
    "ClusterInstanceViewPropertiesStatus",
    "ClusterInstanceViewResult",
    "ClusterInstanceViewResultProperties",
    "ClusterInstanceViewStatus",
    "ClusterInstanceViewsResult",
    "ClusterJob",
    "ClusterJobList",
    "ClusterJobProperties",
    "ClusterListResult",
    "ClusterLogAnalyticsApplicationLogs",
    "ClusterLogAnalyticsProfile",
    "ClusterPatch",
    "ClusterPool",
    "ClusterPoolComputeProfile",
    "ClusterPoolListResult",
    "ClusterPoolLogAnalyticsProfile",
    "ClusterPoolNetworkProfile",
    "ClusterPoolProfile",
    "ClusterPoolResourcePropertiesAksClusterProfile",
    "ClusterPoolResourcePropertiesClusterPoolProfile",
    "ClusterPoolResourcePropertiesComputeProfile",
    "ClusterPoolResourcePropertiesLogAnalyticsProfile",
    "ClusterPoolResourcePropertiesNetworkProfile",
    "ClusterPoolVersion",
    "ClusterPoolVersionsListResult",
    "ClusterProfile",
    "ClusterPrometheusProfile",
    "ClusterResizeData",
    "ClusterServiceConfig",
    "ClusterServiceConfigsProfile",
    "ClusterVersion",
    "ClusterVersionsListResult",
    "ComparisonRule",
    "ComputeProfile",
    "ComputeResourceDefinition",
    "ConnectivityProfile",
    "ConnectivityProfileWeb",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "FlinkCatalogOptions",
    "FlinkHiveCatalogOption",
    "FlinkJobProperties",
    "FlinkProfile",
    "FlinkStorageProfile",
    "HiveCatalogOption",
    "IdentityProfile",
    "LoadBasedConfig",
    "NameAvailabilityParameters",
    "NameAvailabilityResult",
    "NodeProfile",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "ProxyResource",
    "Resource",
    "ScalingRule",
    "Schedule",
    "ScheduleBasedConfig",
    "ScriptActionProfile",
    "SecretReference",
    "SecretsProfile",
    "ServiceConfigListResult",
    "ServiceConfigListResultProperties",
    "ServiceConfigListResultValueEntity",
    "ServiceConfigResult",
    "ServiceConfigResultProperties",
    "ServiceStatus",
    "SparkMetastoreSpec",
    "SparkProfile",
    "SparkUserPlugin",
    "SparkUserPlugins",
    "SshConnectivityEndpoint",
    "SshProfile",
    "SystemData",
    "TagsObject",
    "TrackedResource",
    "TrinoCoordinator",
    "TrinoProfile",
    "TrinoTelemetryConfig",
    "TrinoUserPlugin",
    "TrinoUserPlugins",
    "TrinoUserTelemetry",
    "TrinoWorker",
    "UpdatableClusterProfile",
    "WebConnectivityEndpoint",
    "Action",
    "ActionType",
    "AutoscaleType",
    "ComparisonOperator",
    "ContentEncoding",
    "CreatedByType",
    "JobType",
    "KeyVaultObjectType",
    "Origin",
    "ProvisioningStatus",
    "ScaleActionType",
    "ScheduleDay",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()