"""Generated message classes for cloudasset version v1p1alpha1.

The cloud asset API manages the history and inventory of cloud resources.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'cloudasset'


class Asset(_messages.Message):
  r"""Cloud asset. This includes all Google Cloud Platform resources, Cloud
  IAM policies, and other non-GCP assets.

  Fields:
    assetType: Type of the asset. Example: "compute.googleapis.com/Disk".
    iamPolicy: Representation of the actual Cloud IAM policy set on a cloud
      resource. For each resource, there must be at most one Cloud IAM policy
      set on it.
    iamPolicyName: Cloud IAM policy name of the Cloud IAM policy set on a
      cloud resource. For each resource, there must be at most one Cloud IAM
      policy name associated with it.
    name: The full name of the asset. For example: `//compute.googleapis.com/p
      rojects/my_project_123/zones/zone1/instances/instance1`. See [Resource N
      ames](https://cloud.google.com/apis/design/resource_names#full_resource_
      name) for more information.
    resource: Representation of the resource.
  """

  assetType = _messages.StringField(1)
  iamPolicy = _messages.MessageField('Policy', 2)
  iamPolicyName = _messages.BytesField(3)
  name = _messages.StringField(4)
  resource = _messages.MessageField('Resource', 5)


class AuditConfig(_messages.Message):
  r"""Specifies the audit configuration for a service. The configuration
  determines which permission types are logged, and what identities, if any,
  are exempted from logging. An AuditConfig must have one or more
  AuditLogConfigs.  If there are AuditConfigs for both `allServices` and a
  specific service, the union of the two AuditConfigs is used for that
  service: the log_types specified in each AuditConfig are enabled, and the
  exempted_members in each AuditLogConfig are exempted.  Example Policy with
  multiple AuditConfigs:      {       "audit_configs": [         {
  "service": "allServices"           "audit_log_configs": [             {
  "log_type": "DATA_READ",               "exempted_members": [
  "user:foo@gmail.com"               ]             },             {
  "log_type": "DATA_WRITE",             },             {
  "log_type": "ADMIN_READ",             }           ]         },         {
  "service": "fooservice.googleapis.com"           "audit_log_configs": [
  {               "log_type": "DATA_READ",             },             {
  "log_type": "DATA_WRITE",               "exempted_members": [
  "user:bar@gmail.com"               ]             }           ]         }
  ]     }  For fooservice, this policy enables DATA_READ, DATA_WRITE and
  ADMIN_READ logging. It also exempts foo@gmail.com from DATA_READ logging,
  and bar@gmail.com from DATA_WRITE logging.

  Fields:
    auditLogConfigs: The configuration for logging of each type of permission.
    service: Specifies a service that will be enabled for audit logging. For
      example, `storage.googleapis.com`, `cloudsql.googleapis.com`.
      `allServices` is a special value that covers all services.
  """

  auditLogConfigs = _messages.MessageField('AuditLogConfig', 1, repeated=True)
  service = _messages.StringField(2)


class AuditLogConfig(_messages.Message):
  r"""Provides the configuration for logging a type of permissions. Example:
  {       "audit_log_configs": [         {           "log_type": "DATA_READ",
  "exempted_members": [             "user:foo@gmail.com"           ]
  },         {           "log_type": "DATA_WRITE",         }       ]     }
  This enables 'DATA_READ' and 'DATA_WRITE' logging, while exempting
  foo@gmail.com from DATA_READ logging.

  Enums:
    LogTypeValueValuesEnum: The log type that this config enables.

  Fields:
    exemptedMembers: Specifies the identities that do not cause logging for
      this type of permission. Follows the same format of Binding.members.
    logType: The log type that this config enables.
  """

  class LogTypeValueValuesEnum(_messages.Enum):
    r"""The log type that this config enables.

    Values:
      LOG_TYPE_UNSPECIFIED: Default case. Should never be this.
      ADMIN_READ: Admin reads. Example: CloudIAM getIamPolicy
      DATA_WRITE: Data writes. Example: CloudSQL Users create
      DATA_READ: Data reads. Example: CloudSQL Users list
    """
    LOG_TYPE_UNSPECIFIED = 0
    ADMIN_READ = 1
    DATA_WRITE = 2
    DATA_READ = 3

  exemptedMembers = _messages.StringField(1, repeated=True)
  logType = _messages.EnumField('LogTypeValueValuesEnum', 2)


class BatchGetAssetsHistoryResponse(_messages.Message):
  r"""Batch get assets history response.

  Fields:
    assets: A list of assets with valid time windows.
  """

  assets = _messages.MessageField('TemporalAsset', 1, repeated=True)


class BigQueryDestination(_messages.Message):
  r"""A BigQuery destination.

  Fields:
    dataset: Required. The BigQuery dataset in format
      "projects/projectId/datasets/datasetId", to which the snapshot result
      should be exported. If this dataset does not exist, the export call
      returns an error.
    force: If the destination table already exists and this flag is `TRUE`,
      the table will be overwritten by the contents of assets snapshot. If the
      flag is not set and the destination table already exists, the export
      call returns an error.
    table: Required. The BigQuery table to which the snapshot result should be
      written. If this table does not exist, a new table with the given name
      will be created.
  """

  dataset = _messages.StringField(1)
  force = _messages.BooleanField(2)
  table = _messages.StringField(3)


class Binding(_messages.Message):
  r"""Associates `members` with a `role`.

  Fields:
    condition: The condition that is associated with this binding. NOTE: An
      unsatisfied condition will not allow user access via current binding.
      Different bindings, including their conditions, are examined
      independently.
    members: Specifies the identities requesting access for a Cloud Platform
      resource. `members` can have the following values:  * `allUsers`: A
      special identifier that represents anyone who is    on the internet;
      with or without a Google account.  * `allAuthenticatedUsers`: A special
      identifier that represents anyone    who is authenticated with a Google
      account or a service account.  * `user:{emailid}`: An email address that
      represents a specific Google    account. For example, `alice@gmail.com`
      .   * `serviceAccount:{emailid}`: An email address that represents a
      service    account. For example, `my-other-
      app@appspot.gserviceaccount.com`.  * `group:{emailid}`: An email address
      that represents a Google group.    For example, `admins@example.com`.
      * `domain:{domain}`: The G Suite domain (primary) that represents all
      the    users of that domain. For example, `google.com` or `example.com`.
    role: Role that is assigned to `members`. For example, `roles/viewer`,
      `roles/editor`, or `roles/owner`.
  """

  condition = _messages.MessageField('Expr', 1)
  members = _messages.StringField(2, repeated=True)
  role = _messages.StringField(3)


class CloudassetBatchGetAssetsHistoryRequest(_messages.Message):
  r"""A CloudassetBatchGetAssetsHistoryRequest object.

  Enums:
    ContentTypeValueValuesEnum: Required. The content type.

  Fields:
    assetNames: A list of the full names of the assets. For example: `//comput
      e.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1
      `. See [Resource Names](https://cloud.google.com/apis/design/resource_na
      mes#full_resource_name) and [Resource Name
      Format](https://cloud.google.com/resource-manager/docs/cloud-asset-
      inventory/resource-name-format) for more info.  The request becomes a
      no-op if the asset name list is empty, and the max size of the asset
      name list is 100 in one request.
    contentType: Required. The content type.
    parent: Required. The relative name of the root asset. It can only be an
      organization number (such as "organizations/123"), a project ID (such as
      "projects/my-project-id")", or a project number (such as
      "projects/12345").
    readTimeWindow_endTime: End time of the time window (inclusive). Current
      timestamp if not specified.
    readTimeWindow_startTime: Start time of the time window (exclusive).
  """

  class ContentTypeValueValuesEnum(_messages.Enum):
    r"""Required. The content type.

    Values:
      CONTENT_TYPE_UNSPECIFIED: <no description>
      RESOURCE: <no description>
      IAM_POLICY: <no description>
      IAM_POLICY_NAME: <no description>
      ORG_POLICY: <no description>
      ACCESS_POLICY: <no description>
    """
    CONTENT_TYPE_UNSPECIFIED = 0
    RESOURCE = 1
    IAM_POLICY = 2
    IAM_POLICY_NAME = 3
    ORG_POLICY = 4
    ACCESS_POLICY = 5

  assetNames = _messages.StringField(1, repeated=True)
  contentType = _messages.EnumField('ContentTypeValueValuesEnum', 2)
  parent = _messages.StringField(3, required=True)
  readTimeWindow_endTime = _messages.StringField(4)
  readTimeWindow_startTime = _messages.StringField(5)


class CloudassetExportAssetsRequest(_messages.Message):
  r"""A CloudassetExportAssetsRequest object.

  Fields:
    exportAssetsRequest: A ExportAssetsRequest resource to be passed as the
      request body.
    parent: Required. The relative name of the root asset. This can only be an
      organization number (such as "organizations/123"), a project ID (such as
      "projects/my-project-id"), or a project number (such as
      "projects/12345").
  """

  exportAssetsRequest = _messages.MessageField('ExportAssetsRequest', 1)
  parent = _messages.StringField(2, required=True)


class CloudassetIamPoliciesSearchRequest(_messages.Message):
  r"""A CloudassetIamPoliciesSearchRequest object.

  Fields:
    pageSize: Optional. The page size for search result pagination. Returned
      results may be fewer than requested. The maximum is 2000. If set to the
      zero value, the server will pick an appropriate default.
    pageToken: Optional. If present, retrieve the next batch of results from
      the preceding call to this method. `page_token` must be the value of
      `next_page_token` from the previous response. The values of all other
      method parameters must be identical to those in the previous call.
    query: Required. The query statement. Examples: *
      "policy:myuser@mydomain.com" * "policy:(myuser@mydomain.com viewer)"
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  query = _messages.StringField(3)


class CloudassetOperationsGetRequest(_messages.Message):
  r"""A CloudassetOperationsGetRequest object.

  Fields:
    name: The name of the operation resource.
  """

  name = _messages.StringField(1, required=True)


class ExportAssetsRequest(_messages.Message):
  r"""Export asset request.

  Enums:
    ContentTypeValueValuesEnum: Asset content type. If not specified, no
      content but the asset name will be returned.

  Fields:
    assetTypes: A list of asset types of which to take a snapshot for. For
      example: "compute.googleapis.com/Disk". If specified, only matching
      assets will be returned. See [Introduction to Cloud Asset
      Inventory](https://cloud.google.com/resource-manager/docs/cloud-asset-
      inventory/overview) for all supported asset types.
    contentType: Asset content type. If not specified, no content but the
      asset name will be returned.
    outputConfig: Required. Output configuration indicating where the results
      will be output to. All results will be in newline delimited JSON format.
    readTime: Timestamp to take an asset snapshot. This can only be set to a
      timestamp between 2018-10-02 UTC (inclusive) and the current time. If
      not specified, the current time will be used. Due to delays in resource
      data collection and indexing, there is a volatile window during which
      running the same query may get different results.
  """

  class ContentTypeValueValuesEnum(_messages.Enum):
    r"""Asset content type. If not specified, no content but the asset name
    will be returned.

    Values:
      CONTENT_TYPE_UNSPECIFIED: Unspecified content type.
      RESOURCE: Resource metadata.
      IAM_POLICY: The actual IAM policy set on a resource.
      IAM_POLICY_NAME: The IAM policy name for the IAM policy set on a
        resource.
      ORG_POLICY: The Cloud Organization Policy set on an asset.
      ACCESS_POLICY: The Cloud Access context mananger Policy set on an asset.
    """
    CONTENT_TYPE_UNSPECIFIED = 0
    RESOURCE = 1
    IAM_POLICY = 2
    IAM_POLICY_NAME = 3
    ORG_POLICY = 4
    ACCESS_POLICY = 5

  assetTypes = _messages.StringField(1, repeated=True)
  contentType = _messages.EnumField('ContentTypeValueValuesEnum', 2)
  outputConfig = _messages.MessageField('OutputConfig', 3)
  readTime = _messages.StringField(4)


class Expr(_messages.Message):
  r"""Represents an expression text. Example:      title: "User account
  presence"     description: "Determines whether the request has a user
  account"     expression: "size(request.user) > 0"

  Fields:
    description: An optional description of the expression. This is a longer
      text which describes the expression, e.g. when hovered over it in a UI.
    expression: Textual representation of an expression in Common Expression
      Language syntax.  The application context of the containing message
      determines which well-known feature set of CEL is supported.
    location: An optional string indicating the location of the expression for
      error reporting, e.g. a file name and a position in the file.
    title: An optional title for the expression, i.e. a short string
      describing its purpose. This can be used e.g. in UIs which allow to
      enter the expression.
  """

  description = _messages.StringField(1)
  expression = _messages.StringField(2)
  location = _messages.StringField(3)
  title = _messages.StringField(4)


class GcsDestination(_messages.Message):
  r"""A Cloud Storage location.

  Fields:
    uri: The uri of the Cloud Storage object. It's the same uri that is used
      by gsutil. For example: "gs://bucket_name/object_name". See [Viewing and
      Editing Object Metadata](https://cloud.google.com/storage/docs/viewing-
      editing-metadata) for more information.
    uriPrefix: The uri prefix of all generated Cloud Storage objects. For
      example: "gs://bucket_name/object_name_prefix". Each object uri is in
      format: "gs://bucket_name/object_name_prefix/<asset type>/<shard number>
      and only contains assets for that type. <shard number> starts from 0.
      For example:
      "gs://bucket_name/object_name_prefix/compute.googleapis.com/Disk/0" is
      the first shard of output objects containing all
      compute.googleapis.com/Disk assets. An INVALID_ARGUMENT error will be
      returned if file with the same name
      "gs://bucket_name/object_name_prefix" already exists.
  """

  uri = _messages.StringField(1)
  uriPrefix = _messages.StringField(2)


class IamPolicySearchResult(_messages.Message):
  r"""The result for a IAM Policy search.

  Fields:
    policy: Representation of the actual Cloud IAM policy set on a cloud
      resource. For each resource, there must be at most one Cloud IAM policy
      set on it.
    project: The project that the associated GCP resource belongs to, in the
      form of `projects/{project_number}`. If an IAM policy is set on a
      resource (like VM instance, Cloud Storage bucket), the project field
      will indicate the project that contains the resource. If an IAM policy
      is set on a folder or orgnization, the project field will be empty.
    resource: The [full resource name](https://cloud.google.com/apis/design/re
      source_names#full_resource_name) of the resource associated with this
      IAM policy.
  """

  policy = _messages.MessageField('Policy', 1)
  project = _messages.StringField(2)
  resource = _messages.StringField(3)


class Operation(_messages.Message):
  r"""This resource represents a long-running operation that is the result of
  a network API call.

  Messages:
    MetadataValue: Service-specific metadata associated with the operation.
      It typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    ResponseValue: The normal response of the operation in case of success.
      If the original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

  Fields:
    done: If the value is `false`, it means the operation is still in
      progress. If `true`, the operation is completed, and either `error` or
      `response` is available.
    error: The error result of the operation in case of failure or
      cancellation.
    metadata: Service-specific metadata associated with the operation.  It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    name: The server-assigned name, which is only unique within the same
      service that originally returns it. If you use the default HTTP mapping,
      the `name` should be a resource name ending with
      `operations/{unique_id}`.
    response: The normal response of the operation in case of success.  If the
      original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Service-specific metadata associated with the operation.  It typically
    contains progress information and common metadata such as create time.
    Some services might not provide such metadata.  Any method that returns a
    long-running operation should document the metadata type, if any.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ResponseValue(_messages.Message):
    r"""The normal response of the operation in case of success.  If the
    original method returns no data on success, such as `Delete`, the response
    is `google.protobuf.Empty`.  If the original method is standard
    `Get`/`Create`/`Update`, the response should be the resource.  For other
    methods, the response should have the type `XxxResponse`, where `Xxx` is
    the original method name.  For example, if the original method name is
    `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

    Messages:
      AdditionalProperty: An additional property for a ResponseValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a ResponseValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  done = _messages.BooleanField(1)
  error = _messages.MessageField('Status', 2)
  metadata = _messages.MessageField('MetadataValue', 3)
  name = _messages.StringField(4)
  response = _messages.MessageField('ResponseValue', 5)


class OutputConfig(_messages.Message):
  r"""Output configuration for export assets destination.

  Fields:
    bigqueryDestination: Destination on BigQuery. The output table stores the
      fields in asset proto as columns in BigQuery. The resource/iam_policy
      field is converted to a record with each field to a column, except
      metadata to a single JSON string.
    gcsDestination: Destination on Cloud Storage.
  """

  bigqueryDestination = _messages.MessageField('BigQueryDestination', 1)
  gcsDestination = _messages.MessageField('GcsDestination', 2)


class Policy(_messages.Message):
  r"""Defines an Identity and Access Management (IAM) policy. It is used to
  specify access control policies for Cloud Platform resources.   A `Policy`
  consists of a list of `bindings`. A `binding` binds a list of `members` to a
  `role`, where the members can be user accounts, Google groups, Google
  domains, and service accounts. A `role` is a named list of permissions
  defined by IAM.  **JSON Example**      {       "bindings": [         {
  "role": "roles/owner",           "members": [
  "user:mike@example.com",             "group:admins@example.com",
  "domain:google.com",             "serviceAccount:my-other-
  app@appspot.gserviceaccount.com"           ]         },         {
  "role": "roles/viewer",           "members": ["user:sean@example.com"]
  }       ]     }  **YAML Example**      bindings:     - members:       -
  user:mike@example.com       - group:admins@example.com       -
  domain:google.com       - serviceAccount:my-other-
  app@appspot.gserviceaccount.com       role: roles/owner     - members:
  - user:sean@example.com       role: roles/viewer   For a description of IAM
  and its features, see the [IAM developer's
  guide](https://cloud.google.com/iam/docs).

  Fields:
    auditConfigs: Specifies cloud audit logging configuration for this policy.
    bindings: Associates a list of `members` to a `role`. `bindings` with no
      members will result in an error.
    etag: `etag` is used for optimistic concurrency control as a way to help
      prevent simultaneous updates of a policy from overwriting each other. It
      is strongly suggested that systems make use of the `etag` in the read-
      modify-write cycle to perform policy updates in order to avoid race
      conditions: An `etag` is returned in the response to `getIamPolicy`, and
      systems are expected to put that etag in the request to `setIamPolicy`
      to ensure that their change will be applied to the same version of the
      policy.  If no `etag` is provided in the call to `setIamPolicy`, then
      the existing policy is overwritten blindly.
    version: Deprecated.
  """

  auditConfigs = _messages.MessageField('AuditConfig', 1, repeated=True)
  bindings = _messages.MessageField('Binding', 2, repeated=True)
  etag = _messages.BytesField(3)
  version = _messages.IntegerField(4, variant=_messages.Variant.INT32)


class Resource(_messages.Message):
  r"""Representation of a cloud resource.

  Messages:
    DataValue: The content of the resource, in which some sensitive fields are
      scrubbed away and may not be present.
    InternalDataValue: The actual metadata content for the resource, only
      visible for internal users.

  Fields:
    data: The content of the resource, in which some sensitive fields are
      scrubbed away and may not be present.
    discoveryDocumentUri: The URL of the discovery document containing the
      resource's JSON schema. For example:
      `"https://www.googleapis.com/discovery/v1/apis/compute/v1/rest"`. It
      will be left unspecified for resources without a discovery-based API,
      such as Cloud Bigtable.
    discoveryName: The JSON schema name listed in the discovery document.
      Example: "Project". It will be left unspecified for resources (such as
      Cloud Bigtable) without a discovery-based API.
    internalData: The actual metadata content for the resource, only visible
      for internal users.
    parent: The full name of the immediate parent of this resource. See
      [Resource Names](https://cloud.google.com/apis/design/resource_names#ful
      l_resource_name) for more information.  For GCP assets, it is the parent
      resource defined in the [Cloud IAM policy
      hierarchy](https://cloud.google.com/iam/docs/overview#policy_hierarchy).
      For example:
      `"//cloudresourcemanager.googleapis.com/projects/my_project_123"`.  For
      third-party assets, it is up to the users to define.
    resourceUrl: The REST URL for accessing the resource. An HTTP GET
      operation using this URL returns the resource itself. Example:
      `https://cloudresourcemanager.googleapis.com/v1/projects/my-
      project-123`. It will be left unspecified for resources without a REST
      API.
    version: The API version. Example: "v1".
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DataValue(_messages.Message):
    r"""The content of the resource, in which some sensitive fields are
    scrubbed away and may not be present.

    Messages:
      AdditionalProperty: An additional property for a DataValue object.

    Fields:
      additionalProperties: Properties of the object.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a DataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class InternalDataValue(_messages.Message):
    r"""The actual metadata content for the resource, only visible for
    internal users.

    Messages:
      AdditionalProperty: An additional property for a InternalDataValue
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a InternalDataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  data = _messages.MessageField('DataValue', 1)
  discoveryDocumentUri = _messages.StringField(2)
  discoveryName = _messages.StringField(3)
  internalData = _messages.MessageField('InternalDataValue', 4)
  parent = _messages.StringField(5)
  resourceUrl = _messages.StringField(6)
  version = _messages.StringField(7)


class SearchIamPoliciesResponse(_messages.Message):
  r"""Search IAM policies response.

  Fields:
    nextPageToken: Set if there are more results than those appearing in this
      response; to get the next set of results, call this method again, using
      this value as the `page_token`.
    results: A list of IamPolicy that match the search query. Related
      information such as the assocated resource is returned along with the
      policy.
  """

  nextPageToken = _messages.StringField(1)
  results = _messages.MessageField('IamPolicySearchResult', 2, repeated=True)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


class Status(_messages.Message):
  r"""The `Status` type defines a logical error model that is suitable for
  different programming environments, including REST APIs and RPC APIs. It is
  used by [gRPC](https://github.com/grpc). Each `Status` message contains
  three pieces of data: error code, error message, and error details.  You can
  find out more about this error model and how to work with it in the [API
  Design Guide](https://cloud.google.com/apis/design/errors).

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: The status code, which should be an enum value of google.rpc.Code.
    details: A list of messages that carry the error details.  There is a
      common set of message types for APIs to use.
    message: A developer-facing error message, which should be in English. Any
      user-facing error message should be localized and sent in the
      google.rpc.Status.details field, or localized by the client.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    r"""A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a DetailsValueListEntry object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  code = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  details = _messages.MessageField('DetailsValueListEntry', 2, repeated=True)
  message = _messages.StringField(3)


class TemporalAsset(_messages.Message):
  r"""Temporal asset. In addition to the asset, the temporal asset includes
  the status of the asset and valid from and to time of it.

  Fields:
    asset: Asset.
    deleted: If the asset is deleted or not.
    window: The time window when the asset data and state was observed.
  """

  asset = _messages.MessageField('Asset', 1)
  deleted = _messages.BooleanField(2)
  window = _messages.MessageField('TimeWindow', 3)


class TimeWindow(_messages.Message):
  r"""A time window of (start_time, end_time].

  Fields:
    endTime: End time of the time window (inclusive). Current timestamp if not
      specified.
    startTime: Start time of the time window (exclusive).
  """

  endTime = _messages.StringField(1)
  startTime = _messages.StringField(2)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
