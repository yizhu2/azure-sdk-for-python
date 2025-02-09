# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from six import with_metaclass
from azure.core import CaseInsensitiveEnumMeta


class BillingType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Configures whether billing will be only on the cluster or each workspace will be billed by its
    proportional use. This does not change the overall billing, only how it will be distributed.
    Default value is 'Cluster'
    """

    CLUSTER = "Cluster"
    WORKSPACES = "Workspaces"

class Capacity(with_metaclass(CaseInsensitiveEnumMeta, int, Enum)):
    """The capacity value
    """

    FIVE_HUNDRED = 500
    TEN_HUNDRED = 1000
    TWO_THOUSAND = 2000
    FIVE_THOUSAND = 5000

class CapacityReservationLevel(with_metaclass(CaseInsensitiveEnumMeta, int, Enum)):
    """The capacity reservation level in GB for this workspace, when CapacityReservation sku is
    selected.
    """

    ONE_HUNDRED = 100
    TWO_HUNDRED = 200
    THREE_HUNDRED = 300
    FOUR_HUNDRED = 400
    FIVE_HUNDRED = 500
    TEN_HUNDRED = 1000
    TWO_THOUSAND = 2000
    FIVE_THOUSAND = 5000

class ClusterEntityStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The provisioning state of the cluster.
    """

    CREATING = "Creating"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    DELETING = "Deleting"
    PROVISIONING_ACCOUNT = "ProvisioningAccount"
    UPDATING = "Updating"

class ClusterSkuNameEnum(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The name of the SKU.
    """

    CAPACITY_RESERVATION = "CapacityReservation"

class ColumnDataTypeHintEnum(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Column data type logical hint.
    """

    #: A string that matches the pattern of a URI, for example,
    #: scheme://username:password@host:1234/this/is/a/path?k1=v1&k2=v2#fragment.
    URI = "uri"
    #: A standard 128-bit GUID following the standard shape, xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
    GUID = "guid"
    #: An Azure Resource Model (ARM) path:
    #: /subscriptions/{...}/resourceGroups/{...}/providers/Microsoft.{...}/{...}/{...}/{...}...
    ARM_PATH = "armPath"
    #: A standard V4/V6 ip address following the standard shape, x.x.x.x/y:y:y:y:y:y:y:y.
    IP = "ip"

class ColumnTypeEnum(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Column data type.
    """

    STRING = "string"
    INT = "int"
    LONG = "long"
    REAL = "real"
    BOOLEAN = "boolean"
    DATE_TIME = "dateTime"
    GUID = "guid"
    DYNAMIC = "dynamic"

class CreatedByType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class DataIngestionStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The status of data ingestion for this workspace.
    """

    #: Ingestion enabled following daily cap quota reset, or subscription enablement.
    RESPECT_QUOTA = "RespectQuota"
    #: Ingestion started following service setting change.
    FORCE_ON = "ForceOn"
    #: Ingestion stopped following service setting change.
    FORCE_OFF = "ForceOff"
    #: Reached daily cap quota, ingestion stopped.
    OVER_QUOTA = "OverQuota"
    #: Ingestion stopped following suspended subscription.
    SUBSCRIPTION_SUSPENDED = "SubscriptionSuspended"
    #: 80% of daily cap quota reached.
    APPROACHING_QUOTA = "ApproachingQuota"

class DataSourceKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The kind of the DataSource.
    """

    WINDOWS_EVENT = "WindowsEvent"
    WINDOWS_PERFORMANCE_COUNTER = "WindowsPerformanceCounter"
    IIS_LOGS = "IISLogs"
    LINUX_SYSLOG = "LinuxSyslog"
    LINUX_SYSLOG_COLLECTION = "LinuxSyslogCollection"
    LINUX_PERFORMANCE_OBJECT = "LinuxPerformanceObject"
    LINUX_PERFORMANCE_COLLECTION = "LinuxPerformanceCollection"
    CUSTOM_LOG = "CustomLog"
    CUSTOM_LOG_COLLECTION = "CustomLogCollection"
    AZURE_AUDIT_LOG = "AzureAuditLog"
    AZURE_ACTIVITY_LOG = "AzureActivityLog"
    GENERIC_DATA_SOURCE = "GenericDataSource"
    CHANGE_TRACKING_CUSTOM_PATH = "ChangeTrackingCustomPath"
    CHANGE_TRACKING_PATH = "ChangeTrackingPath"
    CHANGE_TRACKING_SERVICES = "ChangeTrackingServices"
    CHANGE_TRACKING_DATA_TYPE_CONFIGURATION = "ChangeTrackingDataTypeConfiguration"
    CHANGE_TRACKING_DEFAULT_REGISTRY = "ChangeTrackingDefaultRegistry"
    CHANGE_TRACKING_REGISTRY = "ChangeTrackingRegistry"
    CHANGE_TRACKING_LINUX_PATH = "ChangeTrackingLinuxPath"
    LINUX_CHANGE_TRACKING_PATH = "LinuxChangeTrackingPath"
    CHANGE_TRACKING_CONTENT_LOCATION = "ChangeTrackingContentLocation"
    WINDOWS_TELEMETRY = "WindowsTelemetry"
    OFFICE365 = "Office365"
    SECURITY_WINDOWS_BASELINE_CONFIGURATION = "SecurityWindowsBaselineConfiguration"
    SECURITY_CENTER_SECURITY_WINDOWS_BASELINE_CONFIGURATION = "SecurityCenterSecurityWindowsBaselineConfiguration"
    SECURITY_EVENT_COLLECTION_CONFIGURATION = "SecurityEventCollectionConfiguration"
    SECURITY_INSIGHTS_SECURITY_EVENT_COLLECTION_CONFIGURATION = "SecurityInsightsSecurityEventCollectionConfiguration"
    IMPORT_COMPUTER_GROUP = "ImportComputerGroup"
    NETWORK_MONITORING = "NetworkMonitoring"
    ITSM = "Itsm"
    DNS_ANALYTICS = "DnsAnalytics"
    APPLICATION_INSIGHTS = "ApplicationInsights"
    SQL_DATA_CLASSIFICATION = "SqlDataClassification"

class DataSourceType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Linked storage accounts type.
    """

    CUSTOM_LOGS = "CustomLogs"
    AZURE_WATSON = "AzureWatson"
    QUERY = "Query"
    ALERTS = "Alerts"

class IdentityType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of managed service identity.
    """

    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    NONE = "None"

class LinkedServiceEntityStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The provisioning state of the linked service.
    """

    SUCCEEDED = "Succeeded"
    DELETING = "Deleting"
    PROVISIONING_ACCOUNT = "ProvisioningAccount"
    UPDATING = "Updating"

class ProvisioningStateEnum(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Table's current provisioning state. If set to 'updating', indicates a resource lock due to
    ongoing operation, forbidding any update to the table until the ongoing operation is concluded.
    """

    #: Table schema is still being built and updated, table is currently locked for any changes till
    #: the procedure is done.
    UPDATING = "Updating"
    #: Table schema is stable and without changes, table data is being updated.
    IN_PROGRESS = "InProgress"
    #: Table state is stable and without changes, table is unlocked and open for new updates.
    SUCCEEDED = "Succeeded"

class PublicNetworkAccessType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The network access type for operating on the Log Analytics Workspace. By default it is Enabled
    """

    #: Enables connectivity to Log Analytics through public DNS.
    ENABLED = "Enabled"
    #: Disables public connectivity to Log Analytics through public DNS.
    DISABLED = "Disabled"

class PurgeState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Status of the operation represented by the requested Id.
    """

    PENDING = "pending"
    COMPLETED = "completed"

class SearchSortEnum(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The sort order of the search.
    """

    ASC = "asc"
    DESC = "desc"

class SkuNameEnum(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The name of the Service Tier.
    """

    FREE = "Free"
    STANDARD = "Standard"
    PREMIUM = "Premium"
    PER_NODE = "PerNode"
    PER_GB2018 = "PerGB2018"
    STANDALONE = "Standalone"
    CAPACITY_RESERVATION = "CapacityReservation"

class SourceEnum(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Table's creator.
    """

    #: Tables provisioned by the system, as collected via Diagnostic Settings, the Agents, or any
    #: other standard data collection means.
    MICROSOFT = "microsoft"
    #: Tables created by the owner of the Workspace, and only found in this Workspace.
    CUSTOMER = "customer"

class StorageInsightState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The state of the storage insight connection to the workspace
    """

    OK = "OK"
    ERROR = "ERROR"

class TablePlanEnum(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The table plan.
    """

    #: Basic - logs that are adjusted to support high volume / low value verbose logs.
    BASIC = "Basic"
    #: Analytics - logs that allow monitoring and analytics.
    ANALYTICS = "Analytics"

class TableSubTypeEnum(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The subtype describes what APIs can be used to interact with the table, and what features are
    available against it.
    """

    #: The default subtype with which built-in tables are created.
    ANY = "Any"
    #: Indicates a table created through the Data Collector API or with the custom logs feature of the
    #: MMA agent, or any table against which Custom Fields were created.
    CLASSIC = "Classic"
    #: A table eligible to have data sent into it via any of the means supported by Data Collection
    #: Rules: the Data Collection Endpoint API, ingestion-time transformations, or any other mechanism
    #: provided by Data Collection Rules.
    DATA_COLLECTION_RULE_BASED = "DataCollectionRuleBased"

class TableTypeEnum(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Table's creator.
    """

    #: Standard data collected by Azure Monitor.
    MICROSOFT = "Microsoft"
    #: Custom log table.
    CUSTOM_LOG = "CustomLog"
    #: Restored data.
    RESTORED_LOGS = "RestoredLogs"
    #: Data collected by a search job.
    SEARCH_RESULTS = "SearchResults"

class Type(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of the destination resource
    """

    STORAGE_ACCOUNT = "StorageAccount"
    EVENT_HUB = "EventHub"

class WorkspaceEntityStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The provisioning state of the workspace.
    """

    CREATING = "Creating"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    DELETING = "Deleting"
    PROVISIONING_ACCOUNT = "ProvisioningAccount"
    UPDATING = "Updating"

class WorkspaceSkuNameEnum(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The name of the SKU.
    """

    FREE = "Free"
    STANDARD = "Standard"
    PREMIUM = "Premium"
    PER_NODE = "PerNode"
    PER_GB2018 = "PerGB2018"
    STANDALONE = "Standalone"
    CAPACITY_RESERVATION = "CapacityReservation"
    LA_CLUSTER = "LACluster"
