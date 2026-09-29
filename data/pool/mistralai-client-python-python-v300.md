---
slug: mistralai-client-python-python-v300
name: mistralai Python SDK
builder: mistralai
category: ''
summary_zh: ''
inspiration: ''
summary_en: ''
inspiration_en: ''
priority_review: false
project_type: open_source
industries: []
industries_en: []
jobs: []
jobs_en: []
regions: []
regions_en: []
open_source: true
url: https://github.com/mistralai/client-python/releases/tag/v3.0.0
canonical_url: https://github.com/mistralai/client-python/releases/tag/v3.0.0
summary: "### Generated SDK baseline differences\r\nThe published SDK or generator baseline differs from\
  \ the baseline used by the OpenAPI changelog.\r\n\r\n<details>\r\n<summary>Generated surface details</summary>\r\
  \n\r\n#### Stable compatibility changes\r\nRemoved from the stable API surface (24):\r\n- `DeploymentKoyebBackendSpec`\r\
  \n- `UnknownDeploymentWorkerSpecResponseBackendSpec`\r\n- `DeploymentKoyebBackendSpec.build_directory`\r\
  \n- `DeploymentKoyebBackendSpec.dockerfile_path`\r\n- `DeploymentKoyebBackendSpec.type`\r\n- `DeploymentResourceConfig.cpu_limit`\r\
  \n- `DeploymentResourceConfig.cpu_request`\r\n- `DeploymentResourceConfig.memory_limit`\r\n- `DeploymentResourceConfig.memory_request`\r\
  \n- `DeploymentResourceConfigUpdate.cpu_limit`\r\n- `DeploymentResourceConfigUpdate.cpu_request`\r\n\
  - `DeploymentResourceConfigUpdate.memory_limit`\r\n- `DeploymentResourceConfigUpdate.memory_request`\r\
  \n- `DeploymentWorkerSpecInput.entrypoint`\r\n- `DeploymentWorkerSpecInput.working_dir`\r\n- `DeploymentWorkerSpecResponse.commit_sha`\r\
  \n- `DeploymentWorkerSpecResponse.entrypoint`\r\n- `DeploymentWorkerSpecResponse.working_dir`\r\n- `UnknownDeploymentWorkerSpecResponseBackendSpec.is_unknown`\r\
  \n- `UnknownDeploymentWorkerSpecResponseBackendSpec.raw`\r\n- `UnknownDeploymentWorkerSpecResponseBackendSpec.type`\r\
  \n- `WorkflowsWorkerSpecUpdate.entrypoint`\r\n- `WorkflowsWorkerSpecUpdate.working_dir`\r\n- `DeploymentKoyebBackendSpec.serialize_model`\r\
  \n#### Stable type changes\r\nChanged types or signatures on the stable surface (143):\r\n- `ActivityTaskCompletedResponse.chain_run_id:\
  \ Nullable[str] -> OptionalNullable[str]`\r\n- `ActivityTaskCompletedResponse.continued_run_id: Nullable[str]\
  \ -> OptionalNullable[str]`\r\n- `ActivityTaskCompletedResponse.first_execution_run_id: Nullable[str]\
  \ -> OptionalNullable[str]`\r\n- `ActivityTaskCompletedResponse.schedule_id: Nullable[str] -> OptionalNullable[str]`\r\
  \n- `ActivityTaskCompletedResponseTypedDict.chain_run_id: Nullable[str] -> NotRequired[Nullable[str]]`\r\
  \n- `ActivityTaskCompletedResponseTypedDict.continued_run_id: Nullable[str] -> NotRequired[Nullable[str]]`\r\
  \n- `ActivityTaskCompletedResponseTypedDict.first_execution_run_id: Nullable[str] -> NotRequired[Nullable[str]]`\r\
  \n- `ActivityTaskCompletedResponseTypedDict.schedule_id: Nullable[str] -> NotRequired[Nullable[str]]`\r\
  \n- `ActivityTaskFailedResponse.chain_run_id: Nullable[str] -> OptionalNullable[str]`\r\n- `ActivityTaskFailedResponse.continued_run_id:\
  \ Nullable[str] -> OptionalNullable[str]`\r\n- `ActivityTaskFailedResponse.first_execution_run_id: Nullable[str]\
  \ -> OptionalNullable[str]`\r\n- `ActivityTaskFailedResponse.schedule_id: Nullable[str] -> OptionalNullable[str]`\r\
  \n- `ActivityTaskFailedResponseTypedDict.chain_run_id: Nullable[str] -> NotRequired[Nullable[str]]`\r\
  \n- `ActivityTaskFailedResponseTypedDict.continued_run_id: Nullable[str] -> NotRequired[Nullable[str]]`\r\
  \n- `ActivityTaskFailedResponseTypedDict.first_execution_run_id: Nullable[str] -> NotRequired[Nullable[str]]`\r\
  \n- `ActivityTaskFailedResponseTypedDict.schedule_id: Nullable[str] -> NotRequired[Nullable[str]]`\r\
  \n- `ActivityTaskRetryingResponse.chain_run_id: Nullable[str] -> OptionalNullable[str]`\r\n- `ActivityTaskRetryingResponse.continued_run_id:\
  \ Nullable[str] -> OptionalNullable[str]`\r\n- `ActivityTaskRetryingResponse.first_execution_run_id:\
  \ Nullable[str] -> OptionalNullable[str]`\r\n- `ActivityTaskRetryingResponse.schedule_id: Nullable[str]\
  \ -> OptionalNullable[str]`\r\n- `ActivityTaskRetryingResponseTypedDict.chain_run_id: Nullable[str]\
  \ -> NotRequired[Nullable[str]]`\r\n- `ActivityTaskRetryingResponseTypedDict.continued_run_id: Nullable[str]\
  \ -> NotRequired[Nullable[str]]`\r\n- `ActivityTaskRetryingResponseTypedDict.first_execution_run_id:\
  \ Nullable[str] -> NotRequired[Nullable[str]]`\r\n- `ActivityTaskRetryingResponseTypedDict.schedule_id:\
  \ Nullable[str] -> NotRequired[Nullable[str]]`\r\n- `ActivityTaskStartedResponse.chain_run_id: Nullable[str]\
  \ -> OptionalNullable[str]`\r\n- ...and 118 more\r\n#### Beta surface changes\r\nRemoved from the beta\
  \ surface (20):\r\n- `ConnectorDeleteOrganizationCredentialsV1Request`\r\n- `ConnectorDeleteUserCredentialsV1Request`\r\
  \n- `ConnectorDeleteWorkspaceCredentialsV1Request`\r\n- `ConnectorDeleteOrganizationCredentialsV1Request.connector_id_or_name`\r\
  \n- `ConnectorDeleteOrganizationCredentialsV1Request.credentials_name`\r\n- `ConnectorDeleteUserCredentialsV1Request.connector_id_or_name`\r\
  \n- `ConnectorDeleteUserCredentialsV1Request.credentials_name`\r\n- `ConnectorDeleteWorkspaceCredentialsV1Request.connector_id_or_name`\r\
  \n- `ConnectorDeleteWorkspaceCredentialsV1Request.credentials_name`\r\n- `ConnectorGetV1Request.fetch_customer_data`\r\
  \n- `ConnectorListToolsV1Request.page`\r\n- `ConnectorsQueryFilters.active`\r\n- `CreatePipelineConfigRequest.definitions`\r\
  \n- `UpdatePipelineConfigRequest.definitions`\r\n- `Connectors.delete_organization_credentials`\r\n\
  - `Connectors.delete_organization_credentials_async`\r\n- `Connectors.delete_user_credentials`\r\n-\
  \ `Connectors.delete_user_credentials_async`\r\n- `Connectors.delete_workspace_credentials`\r\n- `Connectors.delete_workspace_credentials_async`\r\
  \n\r\nChanged types or signatures in beta (10):\r\n- `PipelineConfig.definitions: List[PipelineConfigDefinition]\
  \ -> Optional[List[PipelineConfigDefinition]]`\r\n- `PipelineConfigTypedDict.definitions: List[PipelineConfigDefinitionTypedDict]\
  \ -> NotRequired[List[PipelineConfigDefinitionTypedDict]]`\r\n- `SearchRequest.retriever: Retriever\
  \ -> SearchRequestRetriever`\r\n- `SearchRequestTypedDict.retriever: RetrieverTypedDict -> SearchRequestRetrieverTypedDict`\r\
  \n- `UsersAPIGetIdentitySecurity.dashboard_user_context_auth: Annotated[str, FieldMetadata(security=SecurityMetadata(scheme=True,\
  \ scheme_type='apiKey', sub_type='header', field_name='x-api-key'))] -> Annotated[Optional[str], FieldMetadata(security=SecurityMetadata(scheme=True,\
  \ scheme_type='apiKey', sub_type='header', field_name='x-api-key'))]`\r\n- `UsersAPIGetIdentitySecurityTypedDict.dashboard_user_context_auth:\
  \ str -> NotRequired[str]`\r\n- `UsersAPIListOrganizationsSecurity.dashboard_user_context_auth: Annotated[str,\
  \ FieldMetadata(security=SecurityMetadata(scheme=True, scheme_type='apiKey', sub_type='header', field_name='x-api-key'))]\
  \ -> Annotated[Optional[str], FieldMetadata(security=SecurityMetadata(scheme=True, scheme_type='apiKey',\
  \ sub_type='header', field_name='x-api-key'))]`\r\n- `UsersAPIListOrganizationsSecurityTypedDict.dashboard_user_context_auth:\
  \ str -> NotRequired[str]`\r\n- `UsersAPIListWorkspacesSecurity.dashboard_user_context_auth: Annotated[str,\
  \ FieldMetadata(security=SecurityMetadata(scheme=True, scheme_type='apiKey', sub_type='header', field_name='x-api-key'))]\
  \ -> Annotated[Optional[str], FieldMetadata(security=SecurityMetadata(scheme=True, scheme_type='apiKey',\
  \ sub_type='header', field_name='x-api-key'))]`\r\n- `UsersAPIListWorkspacesSecurityTypedDict.dashboard_user_context_auth:\
  \ str -> NotRequired[str]`\r\n\r\nNow required on an existing beta model (4):\r\n- `CreatePipelineConfigRequest.definition`\r\
  \n- `ManagedIndexResponse.creator_id`\r\n- `PipelineConfig.definition`\r\n- `UpdatePipelineConfigRequest.definition`\r\
  \n</details>\r\n\r\n### API changes\r\n#### Highlights\r\n\r\n- The SDK uses HTTPX2 instead of HTTPX,\
  \ and the `mcp` and `agents` extras MCP 2.2. A client passed as `client=` or `async_client=` must be\
  \ an `httpx2` client, and raw requests, responses and transport errors are `httpx2` types. See [MIGRATION.md](MIGRATION.md)\
  \ for every breaking change in this release.\r\n- Chat and agents completions no longer accept the `code_interpreter`,\
  \ `web_search` and `web_search_premium` tools; use them through the Conversations API or an agent.\r\
  \n- Workflow deployments: the `koyeb` backend is now `mistral_cloud` (`DeploymentKoyebBackendSpec` is\
  \ replaced by `DeploymentMistralCloudBackendSpec`), the Kubernetes backend can no longer be set, the\
  \ CPU/memory, `entrypoint`, `working_dir` and `commit_sha` fields are removed, and `UnknownDeploymentWorkerSpecResponseBackendSpec`\
  \ is renamed `UnknownBackendSpec`.\r\n- New: `Mistral()` authenticates from a service-account token\
  \ at `MISTRAL_SA_TOKEN_PATH`; `beta.connectors.mcp_client()` and `beta.connectors.http_client()` call\
  \ connectors directly through the Connectors Gateway, whose own failures raise `ConnectorsGatewayError`.\r\
  \n\r\n#### Breaking changes\r\n\r\n- Removed fields `cpu_limit`, `cpu_request`, `memory_limit`, and\
  \ `memory_request` from response `resources` across workflows deployments (6 operations).\r\n- Changed\
  \ field `type` across workflows deployments (6 operations).\r\n- Removed fields `commit_sha`, `entrypoint`,\
  \ and `working_dir` from response `spec` across workflows deployments (6 operations).\r\n- Removed fields\
  \ `cpu_limit`, `cpu_request`, `memory_limit`, and `memory_request` from request `resources` in `sdk.workflows.deployments.update_deployment()`\
  \ and `sdk.workflows.deployments.create_deployment()`.\r\n- Changed field `backend_spec` in `sdk.workflows.deployments.update_deployment()`\
  \ and `sdk.workflows.deployments.create_deployment()`.\r\n- Removed fields `entrypoint` and `working_dir`\
  \ from request `spec` in `sdk.workflows.deployments.update_deployment()` and `sdk.workflows.deployments.create_deployment()`.\r\
  \n- Removed fields `cpu_limit`, `cpu_request`, `memory_limit`, and `memory_request` from response `managed.resources`\
  \ in `sdk.workflows.deployments.get_deployment()`.\r\n- Changed field `type` in `sdk.workflows.deployments.get_deployment()`.\r\
  \n- Removed fields `commit_sha`, `entrypoint`, and `working_dir` from response `managed.spec` in `sdk.workflows.deployments.get_deployment()`.\r\
  \n- Removed fields `cpu_limit`, `cpu_request`, `memory_limit`, and `memory_request` from response `deployments[].managed.resources`\
  \ in `sdk.workflows.deployments.list_deployments()`.\r\n- Changed field `type` in `sdk.workflows.deployments.list_deployments()`.\r\
  \n- Removed fields `commit_sha`, `entrypoint`, and `working_dir` from response `deployments[].managed.spec`\
  \ in `sdk.workflows.deployments.list_deployments()`.\r\n- Removed variants `code_interpreter`, `web_search`,\
  \ and `web_search_premium` from request `tools[]` in `sdk.chat.complete()`, `sdk.chat.stream()`, `sdk.agents.complete()`,\
  \ and `sdk.agents.stream()`.\r\n\r\n#### Beta API changes\r\n\r\n- `sdk.beta.connectors`: removed `delete_workspace_credentials()`,\
  \ `delete_organization_credentials()`, and `delete_user_credentials()`; added `delete_credentials()`.\r\
  \n- Removed field `fetch_customer_data` from request in `sdk.beta.connectors.get()`.\r\n- Added required\
  \ field `definition` to request in `sdk.beta.observability.evaluations.create_pipeline_config()` and\
  \ `sdk.beta.observability.evaluations.update_pipeline_config()`.\r\n- Removed field `definitions` from\
  \ request in `sdk.beta.observability.evaluations.create_pipeline_config()` and `sdk.beta.observability.evaluations.update_pipeline_config()`.\r\
  \n- Removed field `page` from request in `sdk.beta.connectors.list_tools()`.\r\n- Removed field `active`\
  \ from request `query_filters` in `sdk.beta.connectors.list()`.\r\n\r\n#### Added operations\r\n\r\n\
  Stable:\r\n\r\n- `sdk.workflows.deployments.unharden_deployment()`\r\n- `sdk.audio.voices.search()`\r\
  \n\r\nBeta:\r\n\r\n- `sdk.beta.observability.evaluations.list_pipelines()`\r\n- `sdk.beta.observability.datasets.import_from_spans()`\r\
  \n- `sdk.beta.rag.managed_indexes.get_chunk()`\r\n- `sdk.beta.rag.managed_indexes.grep()`\r\n- `sdk.beta.rag.managed_indexes.read()`\r\
  \n- `sdk.beta.rag.managed_indexes.navigate()`\r\n- `sdk.beta.observability.spans.aggregate_span_evaluations()`\r\
  \n- `sdk.beta.observability.evaluations.delete_pipeline()`\r\n- `sdk.beta.observability.evaluations.update_pipeline()`\r\
  \n- `sdk.beta.observability.evaluations.get_pipeline()`\r\n- `sdk.beta.observability.evaluations.create_pipeline()`\r\
  \n\r\n#### Deprecated operations\r\n\r\nBeta:\r\n\r\n- `sdk.beta.connectors.call_tool()`\r\n\r\n####\
  \ Schema changes\r\n\r\n- Added response field `definition` in `sdk.beta.observability.evaluations.create_pipeline_config()`,\
  \ `sdk.beta.observability.evaluations.update_pipeline_config()`, `sdk.beta.observability.evaluations.list_pipeline_configs()`,\
  \ and `sdk.beta.observability.evaluations.get_pipeline_config()`.\r\n- Changed response field `definitions`\
  \ in `sdk.beta.observability.evaluations.create_pipeline_config()`, `sdk.beta.observability.evaluations.update_pipeline_config()`,\
  \ `sdk.beta.observability.evaluations.list_pipeline_configs()`, and `sdk.beta.observability.evaluations.get_pipeline_config()`.\r\
  \n- Added enum values `PIPELINE_ALREADY_EXISTS` and `PIPELINE_NOT_FOUND` across beta observability evaluations,\
  \ beta observability traces, beta observability judges, beta observability datasets, beta observability\
  \ datasets records, beta observability spans, beta observability logs (48 operations).\r\n- Added response\
  \ fields `runtime_credential_id`, `runtime_principal_type`, and `secrets` across workflows deployments\
  \ (8 operations).\r\n- Added request field `owner` in `sdk.workflows.deployments.list_deployments()`.\r\
  \n- Added request enum value `mistral_mcp` across chat, agents, beta conversations, classifiers (7 operations).\r\
  \n- Added response enum value `mistral_mcp` across chat, agents, beta conversations, FIM (8 operations).\r\
  \n- Added response field `source_attribute_key` in `sdk.beta.observability.traces.get_trace_fields()`,\
  \ `sdk.beta.observability.logs.list()`, `sdk.beta.observability.spans.list_span_fields()`, and `sdk.beta.observability.spans.list_span_eval_fields()`.\r\
  \n- Added request fields `order` and `q` in `sdk.beta.service_accounts.list()`.\r\n- Added response\
  \ field `result` across beta observability datasets (5 operations).\r\n- Added request field `client_scopes`\
  \ in `sdk.beta.connectors.create()` and `sdk.beta.connectors.update()`.\r\n- Added request fields `creator_id`,\
  \ `name`, and `status` in `sdk.beta.rag.managed_indexes.list()`.\r\n- Added response field `creator_id`\
  \ in `sdk.beta.rag.managed_indexes.list()`, `sdk.beta.rag.managed_indexes.create()`, `sdk.beta.rag.managed_indexes.get()`,\
  \ and `sdk.beta.rag.managed_indexes.update()`.\r\n- Added request field `max_candidates` in `sdk.beta.rag.managed_indexes.search()`.\r\
  \n- Added request variant `rrf` in `sdk.beta.rag.managed_indexes.search()`.\r\n- Added request field\
  \ `bearer_user_context_auth` in `sdk.beta.users.get_identity()`, `sdk.beta.users.list_organizations()`,\
  \ and `sdk.beta.users.list_workspaces()`.\r\n- Changed request field `dashboard_user_context_auth` in\
  \ `sdk.beta.users.get_identity()`, `sdk.beta.users.list_organizations()`, and `sdk.beta.users.list_workspaces()`.\r\
  \n- Changed response fields `chain_run_id`, `continued_run_id`, `first_execution_run_id`, and `schedule_id`\
  \ in `sdk.workflows.events.get_workflow_events()` and `sdk.events.get_workflow_events()`.\r\n- Added\
  \ request field `log_type` in `sdk.workflows.deployments.get_deployment_logs()`.\r\n\r\n### Changes\r\
  \nBased on:\r\n- OpenAPI Doc\r\n- Speakeasy CLI 1.796.4 (2.935.1) https://github.com/speakeasy-api/speakeasy\r\
  \n### Generated\r\n- [python v3.0.0] .\r\n### Releases\r\n- [PyPI v3.0.0] https://pypi.org/project/mistralai/3.0.0\
  \ - .\r\n\r\nPublishing Completed"
first_seen: '2026-09-28T18:35:32Z'
last_seen: '2026-09-29T01:57:46Z'
status: rejected
sources:
- github
sightings:
- source: github
  url: https://github.com/mistralai/client-python/releases/tag/v3.0.0
  seen_at: '2026-09-29T01:57:46Z'
  metrics:
    reactions: 0
  kind: news
---

# mistralai Python SDK

### Generated SDK baseline differences
The published SDK or generator baseline differs from the baseline used by the OpenAPI changelog.

<details>
<summary>Generated surface details</summary>

#### Stable compatibility changes
Removed from the stable API surface (24):
- `DeploymentKoyebBackendSpec`
- `UnknownDeploymentWorkerSpecResponseBackendSpec`
- `DeploymentKoyebBackendSpec.build_directory`
- `DeploymentKoyebBackendSpec.dockerfile_path`
- `DeploymentKoyebBackendSpec.type`
- `DeploymentResourceConfig.cpu_limit`
- `DeploymentResourceConfig.cpu_request`
- `DeploymentResourceConfig.memory_limit`
- `DeploymentResourceConfig.memory_request`
- `DeploymentResourceConfigUpdate.cpu_limit`
- `DeploymentResourceConfigUpdate.cpu_request`
- `DeploymentResourceConfigUpdate.memory_limit`
- `DeploymentResourceConfigUpdate.memory_request`
- `DeploymentWorkerSpecInput.entrypoint`
- `DeploymentWorkerSpecInput.working_dir`
- `DeploymentWorkerSpecResponse.commit_sha`
- `DeploymentWorkerSpecResponse.entrypoint`
- `DeploymentWorkerSpecResponse.working_dir`
- `UnknownDeploymentWorkerSpecResponseBackendSpec.is_unknown`
- `UnknownDeploymentWorkerSpecResponseBackendSpec.raw`
- `UnknownDeploymentWorkerSpecResponseBackendSpec.type`
- `WorkflowsWorkerSpecUpdate.entrypoint`
- `WorkflowsWorkerSpecUpdate.working_dir`
- `DeploymentKoyebBackendSpec.serialize_model`
#### Stable type changes
Changed types or signatures on the stable surface (143):
- `ActivityTaskCompletedResponse.chain_run_id: Nullable[str] -> OptionalNullable[str]`
- `ActivityTaskCompletedResponse.continued_run_id: Nullable[str] -> OptionalNullable[str]`
- `ActivityTaskCompletedResponse.first_execution_run_id: Nullable[str] -> OptionalNullable[str]`
- `ActivityTaskCompletedResponse.schedule_id: Nullable[str] -> OptionalNullable[str]`
- `ActivityTaskCompletedResponseTypedDict.chain_run_id: Nullable[str] -> NotRequired[Nullable[str]]`
- `ActivityTaskCompletedResponseTypedDict.continued_run_id: Nullable[str] -> NotRequired[Nullable[str]]`
- `ActivityTaskCompletedResponseTypedDict.first_execution_run_id: Nullable[str] -> NotRequired[Nullable[str]]`
- `ActivityTaskCompletedResponseTypedDict.schedule_id: Nullable[str] -> NotRequired[Nullable[str]]`
- `ActivityTaskFailedResponse.chain_run_id: Nullable[str] -> OptionalNullable[str]`
- `ActivityTaskFailedResponse.continued_run_id: Nullable[str] -> OptionalNullable[str]`
- `ActivityTaskFailedResponse.first_execution_run_id: Nullable[str] -> OptionalNullable[str]`
- `ActivityTaskFailedResponse.schedule_id: Nullable[str] -> OptionalNullable[str]`
- `ActivityTaskFailedResponseTypedDict.chain_run_id: Nullable[str] -> NotRequired[Nullable[str]]`
- `ActivityTaskFailedResponseTypedDict.continued_run_id: Nullable[str] -> NotRequired[Nullable[str]]`
- `ActivityTaskFailedResponseTypedDict.first_execution_run_id: Nullable[str] -> NotRequired[Nullable[str]]`
- `ActivityTaskFailedResponseTypedDict.schedule_id: Nullable[str] -> NotRequired[Nullable[str]]`
- `ActivityTaskRetryingResponse.chain_run_id: Nullable[str] -> OptionalNullable[str]`
- `ActivityTaskRetryingResponse.continued_run_id: Nullable[str] -> OptionalNullable[str]`
- `ActivityTaskRetryingResponse.first_execution_run_id: Nullable[str] -> OptionalNullable[str]`
- `ActivityTaskRetryingResponse.schedule_id: Nullable[str] -> OptionalNullable[str]`
- `ActivityTaskRetryingResponseTypedDict.chain_run_id: Nullable[str] -> NotRequired[Nullable[str]]`
- `ActivityTaskRetryingResponseTypedDict.continued_run_id: Nullable[str] -> NotRequired[Nullable[str]]`
- `ActivityTaskRetryingResponseTypedDict.first_execution_run_id: Nullable[str] -> NotRequired[Nullable[str]]`
- `ActivityTaskRetryingResponseTypedDict.schedule_id: Nullable[str] -> NotRequired[Nullable[str]]`
- `ActivityTaskStartedResponse.chain_run_id: Nullable[str] -> OptionalNullable[str]`
- ...and 118 more
#### Beta surface changes
Removed from the beta surface (20):
- `ConnectorDeleteOrganizationCredentialsV1Request`
- `ConnectorDeleteUserCredentialsV1Request`
- `ConnectorDeleteWorkspaceCredentialsV1Request`
- `ConnectorDeleteOrganizationCredentialsV1Request.connector_id_or_name`
- `ConnectorDeleteOrganizationCredentialsV1Request.credentials_name`
- `ConnectorDeleteUserCredentialsV1Request.connector_id_or_name`
- `ConnectorDeleteUserCredentialsV1Request.credentials_name`
- `ConnectorDeleteWorkspaceCredentialsV1Request.connector_id_or_name`
- `ConnectorDeleteWorkspaceCredentialsV1Request.credentials_name`
- `ConnectorGetV1Request.fetch_customer_data`
- `ConnectorListToolsV1Request.page`
- `ConnectorsQueryFilters.active`
- `CreatePipelineConfigRequest.definitions`
- `UpdatePipelineConfigRequest.definitions`
- `Connectors.delete_organization_credentials`
- `Connectors.delete_organization_credentials_async`
- `Connectors.delete_user_credentials`
- `Connectors.delete_user_credentials_async`
- `Connectors.delete_workspace_credentials`
- `Connectors.delete_workspace_credentials_async`

Changed types or signatures in beta (10):
- `PipelineConfig.definitions: List[PipelineConfigDefinition] -> Optional[List[PipelineConfigDefinition]]`
- `PipelineConfigTypedDict.definitions: List[PipelineConfigDefinitionTypedDict] -> NotRequired[List[PipelineConfigDefinitionTypedDict]]`
- `SearchRequest.retriever: Retriever -> SearchRequestRetriever`
- `SearchRequestTypedDict.retriever: RetrieverTypedDict -> SearchRequestRetrieverTypedDict`
- `UsersAPIGetIdentitySecurity.dashboard_user_context_auth: Annotated[str, FieldMetadata(security=SecurityMetadata(scheme=True, scheme_type='apiKey', sub_type='header', field_name='x-api-key'))] -> Annotated[Optional[str], FieldMetadata(security=SecurityMetadata(scheme=True, scheme_type='apiKey', sub_type='header', field_name='x-api-key'))]`
- `UsersAPIGetIdentitySecurityTypedDict.dashboard_user_context_auth: str -> NotRequired[str]`
- `UsersAPIListOrganizationsSecurity.dashboard_user_context_auth: Annotated[str, FieldMetadata(security=SecurityMetadata(scheme=True, scheme_type='apiKey', sub_type='header', field_name='x-api-key'))] -> Annotated[Optional[str], FieldMetadata(security=SecurityMetadata(scheme=True, scheme_type='apiKey', sub_type='header', field_name='x-api-key'))]`
- `UsersAPIListOrganizationsSecurityTypedDict.dashboard_user_context_auth: str -> NotRequired[str]`
- `UsersAPIListWorkspacesSecurity.dashboard_user_context_auth: Annotated[str, FieldMetadata(security=SecurityMetadata(scheme=True, scheme_type='apiKey', sub_type='header', field_name='x-api-key'))] -> Annotated[Optional[str], FieldMetadata(security=SecurityMetadata(scheme=True, scheme_type='apiKey', sub_type='header', field_name='x-api-key'))]`
- `UsersAPIListWorkspacesSecurityTypedDict.dashboard_user_context_auth: str -> NotRequired[str]`

Now required on an existing beta model (4):
- `CreatePipelineConfigRequest.definition`
- `ManagedIndexResponse.creator_id`
- `PipelineConfig.definition`
- `UpdatePipelineConfigRequest.definition`
</details>

### API changes
#### Highlights

- The SDK uses HTTPX2 instead of HTTPX, and the `mcp` and `agents` extras MCP 2.2. A client passed as `client=` or `async_client=` must be an `httpx2` client, and raw requests, responses and transport errors are `httpx2` types. See [MIGRATION.md](MIGRATION.md) for every breaking change in this release.
- Chat and agents completions no longer accept the `code_interpreter`, `web_search` and `web_search_premium` tools; use them through the Conversations API or an agent.
- Workflow deployments: the `koyeb` backend is now `mistral_cloud` (`DeploymentKoyebBackendSpec` is replaced by `DeploymentMistralCloudBackendSpec`), the Kubernetes backend can no longer be set, the CPU/memory, `entrypoint`, `working_dir` and `commit_sha` fields are removed, and `UnknownDeploymentWorkerSpecResponseBackendSpec` is renamed `UnknownBackendSpec`.
- New: `Mistral()` authenticates from a service-account token at `MISTRAL_SA_TOKEN_PATH`; `beta.connectors.mcp_client()` and `beta.connectors.http_client()` call connectors directly through the Connectors Gateway, whose own failures raise `ConnectorsGatewayError`.

#### Breaking changes

- Removed fields `cpu_limit`, `cpu_request`, `memory_limit`, and `memory_request` from response `resources` across workflows deployments (6 operations).
- Changed field `type` across workflows deployments (6 operations).
- Removed fields `commit_sha`, `entrypoint`, and `working_dir` from response `spec` across workflows deployments (6 operations).
- Removed fields `cpu_limit`, `cpu_request`, `memory_limit`, and `memory_request` from request `resources` in `sdk.workflows.deployments.update_deployment()` and `sdk.workflows.deployments.create_deployment()`.
- Changed field `backend_spec` in `sdk.workflows.deployments.update_deployment()` and `sdk.workflows.deployments.create_deployment()`.
- Removed fields `entrypoint` and `working_dir` from request `spec` in `sdk.workflows.deployments.update_deployment()` and `sdk.workflows.deployments.create_deployment()`.
- Removed fields `cpu_limit`, `cpu_request`, `memory_limit`, and `memory_request` from response `managed.resources` in `sdk.workflows.deployments.get_deployment()`.
- Changed field `type` in `sdk.workflows.deployments.get_deployment()`.
- Removed fields `commit_sha`, `entrypoint`, and `working_dir` from response `managed.spec` in `sdk.workflows.deployments.get_deployment()`.
- Removed fields `cpu_limit`, `cpu_request`, `memory_limit`, and `memory_request` from response `deployments[].managed.resources` in `sdk.workflows.deployments.list_deployments()`.
- Changed field `type` in `sdk.workflows.deployments.list_deployments()`.
- Removed fields `commit_sha`, `entrypoint`, and `working_dir` from response `deployments[].managed.spec` in `sdk.workflows.deployments.list_deployments()`.
- Removed variants `code_interpreter`, `web_search`, and `web_search_premium` from request `tools[]` in `sdk.chat.complete()`, `sdk.chat.stream()`, `sdk.agents.complete()`, and `sdk.agents.stream()`.

#### Beta API changes

- `sdk.beta.connectors`: removed `delete_workspace_credentials()`, `delete_organization_credentials()`, and `delete_user_credentials()`; added `delete_credentials()`.
- Removed field `fetch_customer_data` from request in `sdk.beta.connectors.get()`.
- Added required field `definition` to request in `sdk.beta.observability.evaluations.create_pipeline_config()` and `sdk.beta.observability.evaluations.update_pipeline_config()`.
- Removed field `definitions` from request in `sdk.beta.observability.evaluations.create_pipeline_config()` and `sdk.beta.observability.evaluations.update_pipeline_config()`.
- Removed field `page` from request in `sdk.beta.connectors.list_tools()`.
- Removed field `active` from request `query_filters` in `sdk.beta.connectors.list()`.

#### Added operations

Stable:

- `sdk.workflows.deployments.unharden_deployment()`
- `sdk.audio.voices.search()`

Beta:

- `sdk.beta.observability.evaluations.list_pipelines()`
- `sdk.beta.observability.datasets.import_from_spans()`
- `sdk.beta.rag.managed_indexes.get_chunk()`
- `sdk.beta.rag.managed_indexes.grep()`
- `sdk.beta.rag.managed_indexes.read()`
- `sdk.beta.rag.managed_indexes.navigate()`
- `sdk.beta.observability.spans.aggregate_span_evaluations()`
- `sdk.beta.observability.evaluations.delete_pipeline()`
- `sdk.beta.observability.evaluations.update_pipeline()`
- `sdk.beta.observability.evaluations.get_pipeline()`
- `sdk.beta.observability.evaluations.create_pipeline()`

#### Deprecated operations

Beta:

- `sdk.beta.connectors.call_tool()`

#### Schema changes

- Added response field `definition` in `sdk.beta.observability.evaluations.create_pipeline_config()`, `sdk.beta.observability.evaluations.update_pipeline_config()`, `sdk.beta.observability.evaluations.list_pipeline_configs()`, and `sdk.beta.observability.evaluations.get_pipeline_config()`.
- Changed response field `definitions` in `sdk.beta.observability.evaluations.create_pipeline_config()`, `sdk.beta.observability.evaluations.update_pipeline_config()`, `sdk.beta.observability.evaluations.list_pipeline_configs()`, and `sdk.beta.observability.evaluations.get_pipeline_config()`.
- Added enum values `PIPELINE_ALREADY_EXISTS` and `PIPELINE_NOT_FOUND` across beta observability evaluations, beta observability traces, beta observability judges, beta observability datasets, beta observability datasets records, beta observability spans, beta observability logs (48 operations).
- Added response fields `runtime_credential_id`, `runtime_principal_type`, and `secrets` across workflows deployments (8 operations).
- Added request field `owner` in `sdk.workflows.deployments.list_deployments()`.
- Added request enum value `mistral_mcp` across chat, agents, beta conversations, classifiers (7 operations).
- Added response enum value `mistral_mcp` across chat, agents, beta conversations, FIM (8 operations).
- Added response field `source_attribute_key` in `sdk.beta.observability.traces.get_trace_fields()`, `sdk.beta.observability.logs.list()`, `sdk.beta.observability.spans.list_span_fields()`, and `sdk.beta.observability.spans.list_span_eval_fields()`.
- Added request fields `order` and `q` in `sdk.beta.service_accounts.list()`.
- Added response field `result` across beta observability datasets (5 operations).
- Added request field `client_scopes` in `sdk.beta.connectors.create()` and `sdk.beta.connectors.update()`.
- Added request fields `creator_id`, `name`, and `status` in `sdk.beta.rag.managed_indexes.list()`.
- Added response field `creator_id` in `sdk.beta.rag.managed_indexes.list()`, `sdk.beta.rag.managed_indexes.create()`, `sdk.beta.rag.managed_indexes.get()`, and `sdk.beta.rag.managed_indexes.update()`.
- Added request field `max_candidates` in `sdk.beta.rag.managed_indexes.search()`.
- Added request variant `rrf` in `sdk.beta.rag.managed_indexes.search()`.
- Added request field `bearer_user_context_auth` in `sdk.beta.users.get_identity()`, `sdk.beta.users.list_organizations()`, and `sdk.beta.users.list_workspaces()`.
- Changed request field `dashboard_user_context_auth` in `sdk.beta.users.get_identity()`, `sdk.beta.users.list_organizations()`, and `sdk.beta.users.list_workspaces()`.
- Changed response fields `chain_run_id`, `continued_run_id`, `first_execution_run_id`, and `schedule_id` in `sdk.workflows.events.get_workflow_events()` and `sdk.events.get_workflow_events()`.
- Added request field `log_type` in `sdk.workflows.deployments.get_deployment_logs()`.

### Changes
Based on:
- OpenAPI Doc
- Speakeasy CLI 1.796.4 (2.935.1) https://github.com/speakeasy-api/speakeasy
### Generated
- [python v3.0.0] .
### Releases
- [PyPI v3.0.0] https://pypi.org/project/mistralai/3.0.0 - .

Publishing Completed

## 笔记


