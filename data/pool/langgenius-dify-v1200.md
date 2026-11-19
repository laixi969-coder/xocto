---
slug: langgenius-dify-v1200
name: 'langgenius/dify: v1.20.0'
builder: langgenius
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
url: https://github.com/langgenius/dify/releases/tag/1.20.0
canonical_url: https://github.com/langgenius/dify/releases/tag/1.20.0
summary: "**Dify 1.20.0 keeps your traces flowing and your knowledge bases safer.** Export traces to any\
  \ OpenTelemetry collector, keep Langfuse working after its legacy ingestion endpoint retirement, and\
  \ scan uploaded knowledge files for malware before they are indexed. Chatflows can show Agent tool activity\
  \ as it happens, and personal access tokens let scripts and agents call the Dify OpenAPI on your behalf.\
  \ The bundled plugin daemon is upgraded to **0.6.15-local**.\r\n\r\n[New Features](#user-content-new-features)\
  \ · [Configuration and Integration Changes](#user-content-configuration-and-integration-changes) · [Database\
  \ Migrations](#user-content-database-migrations) · [Upgrade Guide](#user-content-upgrade-guide)\r\n\r\
  \n## New Features\r\n\r\n### New HITL: bring approvals into your team's messaging tools\r\n\r\n**Integrate\
  \ human review into your workflows via email and the messaging tools your team already uses.** New HITL\
  \ introduces shared channels, centralized contacts, notification templates, and verified approval forms—allowing\
  \ your team to configure recipients once and reuse them across Human Input nodes, and is now enabled\
  \ by default (`NEXT_PUBLIC_ENABLE_HITL_IM=true`). (#44864, #45945)\r\n\r\n* **Reach approvers where\
  \ they work.** Configure email and an IM platform—**Slack, Feishu/Lark, Microsoft Teams, DingTalk, or\
  \ WeCom**—to deliver workflow review requests through your team's existing channels.\r\n* **Manage recipients\
  \ in Contacts.** Sync IM directories and select approvers from a shared contact list. Workflows can\
  \ also address the initiator or use one-time and dynamic email recipients.\r\n* **Approve in cards or\
  \ forms.** Recipients can review requests directly in supported IM cards or open standalone forms, with\
  \ Dify login or email verification to verify their identity.\r\n* **Customize notifications with workflow\
  \ context.** Use templates and workflow variables to include essential context in notification subjects\
  \ and bodies.\r\n* **Test and track delivery.** Send test notifications to verify your setup and inspect\
  \ delivery records to troubleshoot requests that did not arrive as expected.\r\n* **Adopt New HITL in\
  \ existing workflows.** Use opt-in migration to upgrade legacy Human Input nodes when your workflow\
  \ is ready.\r\n\r\nDeployment requirements are listed under [Configuration and Integration Changes](#user-content-configuration-and-integration-changes).\r\
  \n\r\n### Export traces to any OpenTelemetry collector\r\n\r\nBring Dify execution traces into your\
  \ existing observability stack. The new **OpenTelemetry provider** exports app and Agent traces to any\
  \ compatible collector, allowing you to track workflow steps, model calls, and tool activity together\
  \ in your preferred platform. Use these traces to inspect request execution and diagnose failures without\
  \ requiring a vendor-specific Dify integration. (#45659)\r\n\r\n**Langfuse tracing now supports Langfuse\
  \ v4 and the current Langfuse Cloud ingestion service.** Existing Langfuse configurations continue to\
  \ work. (#45606)\r\n\r\n> [!IMPORTANT]\r\n> Langfuse Cloud retired its legacy ingestion endpoint on\
  \ **November 16, 2026**, and self-hosted Langfuse v4 rejects events sent to it. Upgrade to 1.20.0 to\
  \ keep delivering traces to those deployments.\r\n\r\n### Scan knowledge uploads for malware\r\n\r\n\
  Protect your knowledge bases by scanning uploaded files for malware before they are extracted or indexed.\
  \ When enabled (`FILE_SCAN_ENABLED=true`), workspace owners and admins can configure scanners once under\
  \ **Integrations → File Security Scan**, then define how each knowledge base uses them. Supported scanners\
  \ include **Cloudmersive, Scanii, OPSWAT MetaDefender Cloud**, and a **Custom Endpoint**. (#46090, #46492)\r\
  \n\r\n* **Choose protection per knowledge base.** Select a scanner and configure fallback behavior when\
  \ scanning is unavailable or a file cannot be scanned.\r\n* **Protect knowledge uploads across Dify.**\
  \ Scanning covers classic knowledge bases, RAG Pipeline local-file sources, and Agent Knowledge Base\
  \ uploads.\r\n* **See why files were blocked.** Scan failures appear in the document list for review.\r\
  \n\r\n### Watch Agent tools work in Chatflow\r\n\r\nWhen a Chatflow delegates tasks to an Agent v2 node\
  \ (requires `NEXT_PUBLIC_ENABLE_AGENT_V2_IN_CHATFLOW=true`), users can now see which tools it invokes\
  \ in real time. Tool activity appears alongside the response in both previews and published chats, making\
  \ it easier to follow the Agent's progress. Expand any tool card to inspect what it requested and returned.\
  \ (#46220)\r\n\r\n### Automate OpenAPI calls with personal access tokens\r\n\r\nGrant scripts, CI jobs,\
  \ and personal agents access to the Dify OpenAPI on your behalf without sharing your Console session.\
  \ Create a personal access token from your **Account** page and scope it to specific workspaces and\
  \ resources. You can set an optional expiration date, update its scope as your automation evolves, or\
  \ revoke it when it is no longer needed. (#45540, #46606)\r\n\r\n### Choose GitHub knowledge sources\
  \ from a tree\r\n\r\nBrowse and select the GitHub content you want to add to a knowledge base from an\
  \ expandable tree of repositories, directories, issues, and pull requests. Explore the source structure\
  \ and pick the exact pages to import, whether you are creating a new knowledge base or adding a source\
  \ to an existing one. (#45990)\r\n\r\n### Search and navigate on smaller screens\r\n\r\nSearch across\
  \ content and narrow results using selectable scopes in **Goto Anything**. On smaller screens, search\
  \ and navigation open in drawers to preserve space for the current page. (#45675, #45650)\r\n\r\nDirect\
  \ links can now open Studio's blank-app or template creation flows. (#45717)\r\n\r\n### More flexible\
  \ knowledge descriptions and metadata\r\n\r\n* **Longer knowledge base descriptions.** Increased description\
  \ length limits allow you to provide more context for each knowledge base. (#45075)\r\n* **External\
  \ knowledge metadata.** External knowledge retrieval now returns document metadata alongside content.\
  \ (#22496)\r\n\r\n## Improvements\r\n\r\n**Lower database and startup overhead.** Node execution updates\
  \ avoid reloading stored rows, credential policies are evaluated once per provider configuration, model\
  \ defaults use short-lived sessions, and embedding calls no longer hold open a database session. Web\
  \ feature dependencies also load more lazily. (#46410, #46441, #45806, #45788, #46145)\r\n\r\n**Clearer\
  \ document failures and steadier layouts.** Knowledge documents now report specific failure reasons\
  \ and processing stages. Dialogs adapt to narrow viewports and maintain consistent lifecycles across\
  \ accounts, knowledge, apps, Skills, and workflows. Authentication pages load faster, fit smaller screens,\
  \ and keep keyboard focus accessible. Segmented controls animate smoothly while preserving compact layouts\
  \ and respecting reduced-motion preferences. (#45128, #46487, #45686, #45668, #45634, #45600, #45640,\
  \ #45974)\r\n\r\n## Bug Fixes\r\n\r\n* **Safer file previews and signed links.** Sandbox inline SVG\
  \ previews and verify the original signature before renewing expired file links. (#46505)\r\n* **Stronger\
  \ access protection.** Redact node-retry details from public streams, prevent OAuth callback reuse,\
  \ enforce member-role permissions, and scope vector deletion to the target dataset. (#46517, #46001,\
  \ #46053, #45586)\r\n* **Security dependency updates.** Upgrade `github.com/klauspost/compress` in `dify-agent-runtime`\
  \ to address CVE-2026-116591, and update Node.js in runtime images to security release 24.22.3. (#46544,\
  \ #46206, #46064)\r\n* **Reliable blocking workflows.** Release database connections before execution\
  \ and return preparation failures immediately, preventing connection-pool exhaustion and hanging requests\
  \ that wait until timeout. (#46254)\r\n* **More stable workers.** Resolve the Redis `BRPOP` busy loop\
  \ and prevent overlapping plugin upgrade checks, capping concurrency at 20 checks across workers. (#45940,\
  \ #46500)\r\n* **Complete Chatflow streams.** Properly close streams after direct replies and reset\
  \ the reconnect budget when a stream resumes. (#45552, #46110)\r\n* **Correct Agent execution.** Preserve\
  \ parallel calls to the same plugin tool, pass declared app inputs to Agent runs, and deliver uploaded\
  \ images to vision models. (#45207, #45425, #45745)\r\n* **Accurate knowledge retrieval.** Restore Weaviate\
  \ keyword/hybrid results by returning BM25 scores, and keep embedding vectors aligned when a batch item\
  \ is dropped. (#45642, #45569)\r\n* **Reliable custom API tools.** Resolve OpenAPI server variables,\
  \ percent-encode path parameters, and support OpenAPI 3.1 nullable unions. (#46504, #45965, #45895)\r\
  \n\r\n## Configuration and Integration Changes\r\n\r\n### New and changed settings\r\n\r\n| Setting\
  \ | Default / change | Purpose |\r\n| --- | --- | --- |\r\n| `OPENAPI_ENABLED` | `true` (was `false`)\
  \ | Enable `/openapi/v1/*` endpoints by default so personal access tokens and `difyctl` work out of\
  \ the box. Set to `false` to disable. (#46606) |\r\n| `NEXT_PUBLIC_ENABLE_HITL_IM` | `true` (was `false`)\
  \ | Enable New HITL IM, Contacts, V2 editing/migration, and the approval UI. Restart Web and reload\
  \ the page after changing this value. |\r\n| `HUMAN_INPUT_GLOBAL_TIMEOUT_SECONDS` | `604800` seconds\
  \ (7 days) | Maximum duration a workflow can remain paused while awaiting human input. |\r\n| `HUMAN_INPUT_IM_EVENT_TRANSPORT_MODE`\
  \ | `WEBHOOK` | Deployment-wide IM event transport mode. Webhook callbacks require an externally reachable\
  \ API. Only `WEBHOOK` mode is available now. |\r\n| `TRIGGER_URL` | Set to the public HTTPS API origin\
  \ for IM callbacks | Used to generate channel Callback URLs. Update the IM provider configuration when\
  \ this origin changes. |\r\n| `NEXT_PUBLIC_ENABLE_AGENT_V2_IN_CHATFLOW` | `false` | Enable Agent v2\
  \ nodes in Chatflow, including live tool activity. |\r\n| `FILE_SCAN_ENABLED` | `false` | Enable knowledge-file\
  \ malware scanning globally; individual knowledge bases must also opt in. |\r\n| `FILE_SCAN_REQUEST_TIMEOUT_SECONDS`\
  \ | `300` | Timeout for a scanner request. |\r\n| `FILE_SCAN_MAX_ATTEMPTS` | `3` | Maximum attempts\
  \ when a scanner is temporarily unreachable. |\r\n| `FILE_SCAN_CLEAN_VERDICT_TTL_HOURS` | `24` | Reuse\
  \ period for a clean verdict on the same file content and scanner. |\r\n| `DATASET_DESCRIPTION_MAX_LENGTH`\
  \ | `400` | Maximum character length for knowledge base descriptions. Restart the API after changing\
  \ this value. |\r\n| `DEEPEVAL_DISABLE_DOTENV` / `DEEPEVAL_TELEMETRY_OPT_OUT` | `1` | Shared backend\
  \ environment defaults prevent DeepEval from loading dotenv files or exporting telemetry. |\r\n| `DIFY_AGENT_OPENSHELL_SHARED_MOUNT_PATH`\
  \ | Removed | Shared-volume Home Snapshots are no longer supported by the OpenShell backend. |\r\n|\
  \ `DIFY_AGENT_OPENSHELL_DRIVER_CONFIG` | Now optional | When left empty, an empty driver configuration\
  \ is sent. |\r\n| `EXPERIMENTAL_ENABLE_VINEXT` | Removed | Removed from `web.defaults` and Web Docker\
  \ image builds. (#46616) |\r\n\r\nFor Docker Compose, configure shared backend overrides in `envs/core-services/api-worker.env`\
  \ and Web overrides in `envs/core-services/web.env`. Root `docker/.env` takes precedence. Apply changes\
  \ with `docker compose up -d`; a plain restart does not reload environment files.\r\n\r\nThe OpenTelemetry\
  \ provider supports OTLP/HTTP with protobuf; gRPC is not supported. Live Agent tool activity requires\
  \ streaming output, is unavailable for buffered-output paths, and is not replayed from chat history.\r\
  \n\r\nFile scanning is disabled by default at the deployment level and must also be enabled per knowledge\
  \ base. Policies for scanner unavailability and unscannable files both default to blocking the file.\r\
  \n\r\nDisabling `NEXT_PUBLIC_ENABLE_HITL_IM` does not roll back saved data or halt server-side work\
  \ already in progress.\r\n\r\n### Reverse proxy and worker configuration\r\n\r\n* **New API route:**\
  \ In `WEBHOOK` mode, forward `/callbacks/human-input/v2/im/` to the API service (`api:5001` in Docker\
  \ Compose), preserving the request path, raw body, and provider signature headers. The bundled nginx\
  \ template already includes this rule; add its equivalent to custom nginx, Ingress, or other reverse\
  \ proxy configurations. Configure the IM provider with the channel's generated Callback URL. (#44864)\r\
  \n* **New Celery queues:** Include `human_input_delivery` for asynchronous IM callback processing and\
  \ post-submission card updates, and `human_input_contact_sync` for IM contact directory synchronization.\
  \ The default Docker worker list includes both. Custom `CELERY_QUEUES`, `CELERY_WORKER_QUEUES`, or Celery\
  \ `--queues` lists must provide an active consumer for each queue alongside existing subscriptions.\
  \ (#44864)\r\n\r\n### Docker environment files\r\n\r\n`docker/envs/core-services/shared.env` is **no\
  \ longer loaded**. Move common API, worker, and Beat settings to `api-worker.env` before recreating\
  \ containers. Preserve any service-specific settings in the override file used by that service. (#46497)\r\
  \n\r\nPublic URLs are shared by Web, API, and workers through the new `envs/core-services/urls.defaults`\
  \ and optional `urls.env`:\r\n\r\n* `CONSOLE_API_URL`\r\n* `CONSOLE_WEB_URL`\r\n* `SERVICE_API_URL`\r\
  \n* `APP_API_URL`\r\n* `APP_WEB_URL`\r\n\r\nSet browser-accessible base URLs without `/console/api`,\
  \ `/api`, or `/v1` suffixes. Explicit values in `urls.env` override service-specific URL settings; root\
  \ `docker/.env` overrides both. Web's internal `SERVER_CONSOLE_API_URL` remains in `web.env`. This also\
  \ resolves an issue where generated icon links pointed to `127.0.0.1:5001` on fresh installations. (#46497)\r\
  \n\r\n## Database Migrations\r\n\r\nUpgrading from **1.19.0** adds **six migration revisions**, moving\
  \ the migration head from `53c10126d551` to `f8b6e2c4a901`. Apply the complete Alembic chain through\
  \ the normal migration runner.\r\n\r\n| Revision | Change |\r\n| --- | --- |\r\n| `6b7e2a9c4d10` | Add\
  \ nullable `started_by_sys_user_id` to `human_input_im_sync_runs` and require exactly one initiating\
  \ identity per row. |\r\n| `b2e4c6d8a013` | Add personal access tokens and their resource/workspace\
  \ scope tables. |\r\n| `8c2f5d7a1e30` | Add file scanner, scan policy, and scan-result tables. |\r\n\
  | `91f4b2d7c8e0` | Add Evaluation configuration, run, and run-item tables. |\r\n| `c7e4a1b2d9f0` | Add\
  \ the Evaluation framework column with a default value. |\r\n| `f8b6e2c4a901` | Merge the Evaluation\
  \ and main migration branches. |\r\n\r\nThe Evaluation migrations apply to the **Community Edition**\
  \ as well, even though CE does not expose the Evaluation feature. Include these revisions when applying\
  \ the migration chain; none of the six revisions require a separate manual backfill command. (#45945,\
  \ #45540, #46090, #46141)\r\n\r\nNew HITL introduces the necessary database schema and automatically\
  \ backfills Contact identities for existing accounts with no extra commands required. These migrations\
  \ are already included in 1.19.0—existing 1.19.0 deployments need no action, while older versions should\
  \ run the full migration chain. Legacy Human Input nodes are not automatically migrated and remain opt-in.\r\
  \n\r\n## Upgrade Guide\r\n\r\n> [!IMPORTANT]\r\n> Move settings out of the retired `shared.env` before\
  \ recreating containers. Review public URLs, custom HITL callback routing, and worker subscriptions.\
  \ OpenShell deployments require a compatible gateway upgrade and no longer restore Home Snapshots. The\
  \ bundled plugin daemon is updated to **0.6.15-local**.\r\n\r\n### Prepare the deployment\r\n\r\n1.\
  \ **Back up data and configuration.** Back up your database, vector-store data, uploaded files, plugin\
  \ daemon storage, Agent workspace storage, deployment secrets, and environment files. Schedule a maintenance\
  \ window for a single-stack upgrade.\r\n2. **Upgrade the Dify components together.** Use matching `1.20.0`\
  \ API, worker, Web, Agent Backend, and Local sandbox images, alongside plugin daemon `0.6.15-local`.\
  \ Keep `SECRET_KEY`, any configured `PASSWORD_PEPPER`, and the Local sandbox authentication token unchanged.\
  \ Personal access tokens depend on `SECRET_KEY`; ensure the same value is used across all API replicas.\
  \ If upgrading from a version earlier than 1.19.0, also follow the [1.19.0 upgrade guide](https://github.com/langgenius/dify/releases/tag/1.19.0).\r\
  \n3. **Migrate `shared.env`.** If `envs/core-services/api-worker.env` does not exist, rename `envs/core-services/shared.env`\
  \ to that path. If both exist, merge only missing settings and preserve existing `api-worker.env` values,\
  \ including intentional empty assignments. Retain service-specific settings in the appropriate service\
  \ override file. Deployments without `shared.env` require no migration.\r\n4. **Consolidate public URLs.**\
  \ Create `envs/core-services/urls.env` from `urls.defaults` only if it does not already exist. Move\
  \ the intended public URL values there, then remove duplicate assignments from individual service files.\
  \ Existing root `.env` values retain precedence. Keep internal Web API routing in `web.env`.\r\n5. **Apply\
  \ environment, route, and queue changes.** Follow [Configuration and Integration Changes](#user-content-configuration-and-integration-changes),\
  \ including the New HITL settings, IM callback route, and both Celery queues.\r\n6. **Let plugin storage\
  \ initialization run.** `init_permissions` now also prepares `./volumes/plugin_daemon` for the daemon's\
  \ UID 1001, and the daemon waits for it to complete. Recreate the deployment with `docker compose up\
  \ -d` so the init service runs. (#45615)\r\n\r\n### OpenShell deployments\r\n\r\nUpgrade the OpenShell\
  \ gateway and SDK together to **0.1.3 or later within the supported 0.1.x line**, and upgrade the Dify\
  \ API and Agent Backend together. The gateway must support native service exposure and bearer passthrough,\
  \ preserving the per-sandbox authorization token derived from `DIFY_AGENT_OPENSHELL_SHELLCTL_AUTH_TOKEN`.\
  \ Keep that master secret identical across Agent Backend replicas. (#45862)\r\n\r\nBuild the OpenShell\
  \ runtime image from the release checkout and set `DIFY_AGENT_OPENSHELL_SANDBOX_IMAGE` to the exact\
  \ image reference available to the gateway's compute nodes. The image must include both `shellctl` and\
  \ `iproute2`; an older cached runtime image may lack the required networking tools.\r\n\r\nWhen upgrading\
  \ from the previous shared deployment-wide `shellctl` token, generate a fresh high-entropy master secret\
  \ and update all Agent Backend replicas together. Drain active work, then stop and restart existing\
  \ sandboxes so `shellctl` restarts with the derived credential. Reacquiring an already healthy sandbox\
  \ does not refresh its credential.\r\n\r\nShared-volume Home Snapshots and `DIFY_AGENT_OPENSHELL_SHARED_MOUNT_PATH`\
  \ are removed. Existing running sandboxes retain their state across stop/restart cycles, whereas newly\
  \ created Bindings start from the image's default Home. `DIFY_AGENT_OPENSHELL_DRIVER_CONFIG` is now\
  \ optional. Review the [OpenShell deployment guide](https://github.com/langgenius/dify/blob/1.20.0/dify-agent/docs/dify-agent/guide/openshell.md),\
  \ including its runtime-image requirements, before upgrading. Other sandbox backends are unaffected.\r\
  \n\r\n### Docker Compose\r\n\r\nOnce the `1.20.0` tag and images are published, stop the deployment\
  \ gracefully, switch to the release, migrate local configuration files, and then pull and start the\
  \ updated services:\r\n\r\n```bash\r\ncd dify/docker\r\ndocker compose stop -t -1\r\ngit fetch --tags\r\
  \ngit checkout 1.20.0\r\n# Migrate shared.env, public URLs, and any custom proxy/worker configuration.\r\
  \ndocker compose pull\r\ndocker compose up -d\r\n```\r\n\r\nKeep API startup migrations enabled (`MIGRATION_ENABLED=true`),\
  \ or apply the full migration chain through your managed migration process before starting new workers.\
  \ Use `docker compose up -d` after changing environment files; a plain restart does not reload them.\r\
  \n\r\n### Source deployments\r\n\r\nUse **Python 3.13**, **Node.js 24.22.3 or later in the 24.x line**,\
  \ and **pnpm 12.18.0**. After stopping the services and switching to the release, run the following\
  \ commands from the repository root:\r\n\r\n```bash\r\nuv sync --project api --frozen\r\nuv run --directory\
  \ api flask db upgrade\r\npnpm install --frozen-lockfile\r\n```\r\n\r\nRebuild Web and restart the API,\
  \ workers, scheduler, and Agent services from the same release. Update the standalone Agent Backend's\
  \ locked dependencies if deploying it separately. Preserve existing worker subscriptions and add the\
  \ two HITL queues where needed.\r\n\r\n**Full Changelog:** [1.19.0 → 1.20.0](https://github.com/langgenius/dify/compare/1.19.0...1.20.0)"
first_seen: '2026-11-19T03:28:05Z'
last_seen: '2026-11-19T03:28:05Z'
status: pending_filter
sources:
- github
sightings:
- source: github
  url: https://github.com/langgenius/dify/releases/tag/1.20.0
  seen_at: '2026-11-19T03:28:05Z'
  metrics:
    reactions: 1
  kind: news
---

# langgenius/dify: v1.20.0

**Dify 1.20.0 keeps your traces flowing and your knowledge bases safer.** Export traces to any OpenTelemetry collector, keep Langfuse working after its legacy ingestion endpoint retirement, and scan uploaded knowledge files for malware before they are indexed. Chatflows can show Agent tool activity as it happens, and personal access tokens let scripts and agents call the Dify OpenAPI on your behalf. The bundled plugin daemon is upgraded to **0.6.15-local**.

[New Features](#user-content-new-features) · [Configuration and Integration Changes](#user-content-configuration-and-integration-changes) · [Database Migrations](#user-content-database-migrations) · [Upgrade Guide](#user-content-upgrade-guide)

## New Features

### New HITL: bring approvals into your team's messaging tools

**Integrate human review into your workflows via email and the messaging tools your team already uses.** New HITL introduces shared channels, centralized contacts, notification templates, and verified approval forms—allowing your team to configure recipients once and reuse them across Human Input nodes, and is now enabled by default (`NEXT_PUBLIC_ENABLE_HITL_IM=true`). (#44864, #45945)

* **Reach approvers where they work.** Configure email and an IM platform—**Slack, Feishu/Lark, Microsoft Teams, DingTalk, or WeCom**—to deliver workflow review requests through your team's existing channels.
* **Manage recipients in Contacts.** Sync IM directories and select approvers from a shared contact list. Workflows can also address the initiator or use one-time and dynamic email recipients.
* **Approve in cards or forms.** Recipients can review requests directly in supported IM cards or open standalone forms, with Dify login or email verification to verify their identity.
* **Customize notifications with workflow context.** Use templates and workflow variables to include essential context in notification subjects and bodies.
* **Test and track delivery.** Send test notifications to verify your setup and inspect delivery records to troubleshoot requests that did not arrive as expected.
* **Adopt New HITL in existing workflows.** Use opt-in migration to upgrade legacy Human Input nodes when your workflow is ready.

Deployment requirements are listed under [Configuration and Integration Changes](#user-content-configuration-and-integration-changes).

### Export traces to any OpenTelemetry collector

Bring Dify execution traces into your existing observability stack. The new **OpenTelemetry provider** exports app and Agent traces to any compatible collector, allowing you to track workflow steps, model calls, and tool activity together in your preferred platform. Use these traces to inspect request execution and diagnose failures without requiring a vendor-specific Dify integration. (#45659)

**Langfuse tracing now supports Langfuse v4 and the current Langfuse Cloud ingestion service.** Existing Langfuse configurations continue to work. (#45606)

> [!IMPORTANT]
> Langfuse Cloud retired its legacy ingestion endpoint on **November 16, 2026**, and self-hosted Langfuse v4 rejects events sent to it. Upgrade to 1.20.0 to keep delivering traces to those deployments.

### Scan knowledge uploads for malware

Protect your knowledge bases by scanning uploaded files for malware before they are extracted or indexed. When enabled (`FILE_SCAN_ENABLED=true`), workspace owners and admins can configure scanners once under **Integrations → File Security Scan**, then define how each knowledge base uses them. Supported scanners include **Cloudmersive, Scanii, OPSWAT MetaDefender Cloud**, and a **Custom Endpoint**. (#46090, #46492)

* **Choose protection per knowledge base.** Select a scanner and configure fallback behavior when scanning is unavailable or a file cannot be scanned.
* **Protect knowledge uploads across Dify.** Scanning covers classic knowledge bases, RAG Pipeline local-file sources, and Agent Knowledge Base uploads.
* **See why files were blocked.** Scan failures appear in the document list for review.

### Watch Agent tools work in Chatflow

When a Chatflow delegates tasks to an Agent v2 node (requires `NEXT_PUBLIC_ENABLE_AGENT_V2_IN_CHATFLOW=true`), users can now see which tools it invokes in real time. Tool activity appears alongside the response in both previews and published chats, making it easier to follow the Agent's progress. Expand any tool card to inspect what it requested and returned. (#46220)

### Automate OpenAPI calls with personal access tokens

Grant scripts, CI jobs, and personal agents access to the Dify OpenAPI on your behalf without sharing your Console session. Create a personal access token from your **Account** page and scope it to specific workspaces and resources. You can set an optional expiration date, update its scope as your automation evolves, or revoke it when it is no longer needed. (#45540, #46606)

### Choose GitHub knowledge sources from a tree

Browse and select the GitHub content you want to add to a knowledge base from an expandable tree of repositories, directories, issues, and pull requests. Explore the source structure and pick the exact pages to import, whether you are creating a new knowledge base or adding a source to an existing one. (#45990)

### Search and navigate on smaller screens

Search across content and narrow results using selectable scopes in **Goto Anything**. On smaller screens, search and navigation open in drawers to preserve space for the current page. (#45675, #45650)

Direct links can now open Studio's blank-app or template creation flows. (#45717)

### More flexible knowledge descriptions and metadata

* **Longer knowledge base descriptions.** Increased description length limits allow you to provide more context for each knowledge base. (#45075)
* **External knowledge metadata.** External knowledge retrieval now returns document metadata alongside content. (#22496)

## Improvements

**Lower database and startup overhead.** Node execution updates avoid reloading stored rows, credential policies are evaluated once per provider configuration, model defaults use short-lived sessions, and embedding calls no longer hold open a database session. Web feature dependencies also load more lazily. (#46410, #46441, #45806, #45788, #46145)

**Clearer document failures and steadier layouts.** Knowledge documents now report specific failure reasons and processing stages. Dialogs adapt to narrow viewports and maintain consistent lifecycles across accounts, knowledge, apps, Skills, and workflows. Authentication pages load faster, fit smaller screens, and keep keyboard focus accessible. Segmented controls animate smoothly while preserving compact layouts and respecting reduced-motion preferences. (#45128, #46487, #45686, #45668, #45634, #45600, #45640, #45974)

## Bug Fixes

* **Safer file previews and signed links.** Sandbox inline SVG previews and verify the original signature before renewing expired file links. (#46505)
* **Stronger access protection.** Redact node-retry details from public streams, prevent OAuth callback reuse, enforce member-role permissions, and scope vector deletion to the target dataset. (#46517, #46001, #46053, #45586)
* **Security dependency updates.** Upgrade `github.com/klauspost/compress` in `dify-agent-runtime` to address CVE-2026-116591, and update Node.js in runtime images to security release 24.22.3. (#46544, #46206, #46064)
* **Reliable blocking workflows.** Release database connections before execution and return preparation failures immediately, preventing connection-pool exhaustion and hanging requests that wait until timeout. (#46254)
* **More stable workers.** Resolve the Redis `BRPOP` busy loop and prevent overlapping plugin upgrade checks, capping concurrency at 20 checks across workers. (#45940, #46500)
* **Complete Chatflow streams.** Properly close streams after direct replies and reset the reconnect budget when a stream resumes. (#45552, #46110)
* **Correct Agent execution.** Preserve parallel calls to the same plugin tool, pass declared app inputs to Agent runs, and deliver uploaded images to vision models. (#45207, #45425, #45745)
* **Accurate knowledge retrieval.** Restore Weaviate keyword/hybrid results by returning BM25 scores, and keep embedding vectors aligned when a batch item is dropped. (#45642, #45569)
* **Reliable custom API tools.** Resolve OpenAPI server variables, percent-encode path parameters, and support OpenAPI 3.1 nullable unions. (#46504, #45965, #45895)

## Configuration and Integration Changes

### New and changed settings

| Setting | Default / change | Purpose |
| --- | --- | --- |
| `OPENAPI_ENABLED` | `true` (was `false`) | Enable `/openapi/v1/*` endpoints by default so personal access tokens and `difyctl` work out of the box. Set to `false` to disable. (#46606) |
| `NEXT_PUBLIC_ENABLE_HITL_IM` | `true` (was `false`) | Enable New HITL IM, Contacts, V2 editing/migration, and the approval UI. Restart Web and reload the page after changing this value. |
| `HUMAN_INPUT_GLOBAL_TIMEOUT_SECONDS` | `604800` seconds (7 days) | Maximum duration a workflow can remain paused while awaiting human input. |
| `HUMAN_INPUT_IM_EVENT_TRANSPORT_MODE` | `WEBHOOK` | Deployment-wide IM event transport mode. Webhook callbacks require an externally reachable API. Only `WEBHOOK` mode is available now. |
| `TRIGGER_URL` | Set to the public HTTPS API origin for IM callbacks | Used to generate channel Callback URLs. Update the IM provider configuration when this origin changes. |
| `NEXT_PUBLIC_ENABLE_AGENT_V2_IN_CHATFLOW` | `false` | Enable Agent v2 nodes in Chatflow, including live tool activity. |
| `FILE_SCAN_ENABLED` | `false` | Enable knowledge-file malware scanning globally; individual knowledge bases must also opt in. |
| `FILE_SCAN_REQUEST_TIMEOUT_SECONDS` | `300` | Timeout for a scanner request. |
| `FILE_SCAN_MAX_ATTEMPTS` | `3` | Maximum attempts when a scanner is temporarily unreachable. |
| `FILE_SCAN_CLEAN_VERDICT_TTL_HOURS` | `24` | Reuse period for a clean verdict on the same file content and scanner. |
| `DATASET_DESCRIPTION_MAX_LENGTH` | `400` | Maximum character length for knowledge base descriptions. Restart the API after changing this value. |
| `DEEPEVAL_DISABLE_DOTENV` / `DEEPEVAL_TELEMETRY_OPT_OUT` | `1` | Shared backend environment defaults prevent DeepEval from loading dotenv files or exporting telemetry. |
| `DIFY_AGENT_OPENSHELL_SHARED_MOUNT_PATH` | Removed | Shared-volume Home Snapshots are no longer supported by the OpenShell backend. |
| `DIFY_AGENT_OPENSHELL_DRIVER_CONFIG` | Now optional | When left empty, an empty driver configuration is sent. |
| `EXPERIMENTAL_ENABLE_VINEXT` | Removed | Removed from `web.defaults` and Web Docker image builds. (#46616) |

For Docker Compose, configure shared backend overrides in `envs/core-services/api-worker.env` and Web overrides in `envs/core-services/web.env`. Root `docker/.env` takes precedence. Apply changes with `docker compose up -d`; a plain restart does not reload environment files.

The OpenTelemetry provider supports OTLP/HTTP with protobuf; gRPC is not supported. Live Agent tool activity requires streaming output, is unavailable for buffered-output paths, and is not replayed from chat history.

File scanning is disabled by default at the deployment level and must also be enabled per knowledge base. Policies for scanner unavailability and unscannable files both default to blocking the file.

Disabling `NEXT_PUBLIC_ENABLE_HITL_IM` does not roll back saved data or halt server-side work already in progress.

### Reverse proxy and worker configuration

* **New API route:** In `WEBHOOK` mode, forward `/callbacks/human-input/v2/im/` to the API service (`api:5001` in Docker Compose), preserving the request path, raw body, and provider signature headers. The bundled nginx template already includes this rule; add its equivalent to custom nginx, Ingress, or other reverse proxy configurations. Configure the IM provider with the channel's generated Callback URL. (#44864)
* **New Celery queues:** Include `human_input_delivery` for asynchronous IM callback processing and post-submission card updates, and `human_input_contact_sync` for IM contact directory synchronization. The default Docker worker list includes both. Custom `CELERY_QUEUES`, `CELERY_WORKER_QUEUES`, or Celery `--queues` lists must provide an active consumer for each queue alongside existing subscriptions. (#44864)

### Docker environment files

`docker/envs/core-services/shared.env` is **no longer loaded**. Move common API, worker, and Beat settings to `api-worker.env` before recreating containers. Preserve any service-specific settings in the override file used by that service. (#46497)

Public URLs are shared by Web, API, and workers through the new `envs/core-services/urls.defaults` and optional `urls.env`:

* `CONSOLE_API_URL`
* `CONSOLE_WEB_URL`
* `SERVICE_API_URL`
* `APP_API_URL`
* `APP_WEB_URL`

Set browser-accessible base URLs without `/console/api`, `/api`, or `/v1` suffixes. Explicit values in `urls.env` override service-specific URL settings; root `docker/.env` overrides both. Web's internal `SERVER_CONSOLE_API_URL` remains in `web.env`. This also resolves an issue where generated icon links pointed to `127.0.0.1:5001` on fresh installations. (#46497)

## Database Migrations

Upgrading from **1.19.0** adds **six migration revisions**, moving the migration head from `53c10126d551` to `f8b6e2c4a901`. Apply the complete Alembic chain through the normal migration runner.

| Revision | Change |
| --- | --- |
| `6b7e2a9c4d10` | Add nullable `started_by_sys_user_id` to `human_input_im_sync_runs` and require exactly one initiating identity per row. |
| `b2e4c6d8a013` | Add personal access tokens and their resource/workspace scope tables. |
| `8c2f5d7a1e30` | Add file scanner, scan policy, and scan-result tables. |
| `91f4b2d7c8e0` | Add Evaluation configuration, run, and run-item tables. |
| `c7e4a1b2d9f0` | Add the Evaluation framework column with a default value. |
| `f8b6e2c4a901` | Merge the Evaluation and main migration branches. |

The Evaluation migrations apply to the **Community Edition** as well, even though CE does not expose the Evaluation feature. Include these revisions when applying the migration chain; none of the six revisions require a separate manual backfill command. (#45945, #45540, #46090, #46141)

New HITL introduces the necessary database schema and automatically backfills Contact identities for existing accounts with no extra commands required. These migrations are already included in 1.19.0—existing 1.19.0 deployments need no action, while older versions should run the full migration chain. Legacy Human Input nodes are not automatically migrated and remain opt-in.

## Upgrade Guide

> [!IMPORTANT]
> Move settings out of the retired `shared.env` before recreating containers. Review public URLs, custom HITL callback routing, and worker subscriptions. OpenShell deployments require a compatible gateway upgrade and no longer restore Home Snapshots. The bundled plugin daemon is updated to **0.6.15-local**.

### Prepare the deployment

1. **Back up data and configuration.** Back up your database, vector-store data, uploaded files, plugin daemon storage, Agent workspace storage, deployment secrets, and environment files. Schedule a maintenance window for a single-stack upgrade.
2. **Upgrade the Dify components together.** Use matching `1.20.0` API, worker, Web, Agent Backend, and Local sandbox images, alongside plugin daemon `0.6.15-local`. Keep `SECRET_KEY`, any configured `PASSWORD_PEPPER`, and the Local sandbox authentication token unchanged. Personal access tokens depend on `SECRET_KEY`; ensure the same value is used across all API replicas. If upgrading from a version earlier than 1.19.0, also follow the [1.19.0 upgrade guide](https://github.com/langgenius/dify/releases/tag/1.19.0).
3. **Migrate `shared.env`.** If `envs/core-services/api-worker.env` does not exist, rename `envs/core-services/shared.env` to that path. If both exist, merge only missing settings and preserve existing `api-worker.env` values, including intentional empty assignments. Retain service-specific settings in the appropriate service override file. Deployments without `shared.env` require no migration.
4. **Consolidate public URLs.** Create `envs/core-services/urls.env` from `urls.defaults` only if it does not already exist. Move the intended public URL values there, then remove duplicate assignments from individual service files. Existing root `.env` values retain precedence. Keep internal Web API routing in `web.env`.
5. **Apply environment, route, and queue changes.** Follow [Configuration and Integration Changes](#user-content-configuration-and-integration-changes), including the New HITL settings, IM callback route, and both Celery queues.
6. **Let plugin storage initialization run.** `init_permissions` now also prepares `./volumes/plugin_daemon` for the daemon's UID 1001, and the daemon waits for it to complete. Recreate the deployment with `docker compose up -d` so the init service runs. (#45615)

### OpenShell deployments

Upgrade the OpenShell gateway and SDK together to **0.1.3 or later within the supported 0.1.x line**, and upgrade the Dify API and Agent Backend together. The gateway must support native service exposure and bearer passthrough, preserving the per-sandbox authorization token derived from `DIFY_AGENT_OPENSHELL_SHELLCTL_AUTH_TOKEN`. Keep that master secret identical across Agent Backend replicas. (#45862)

Build the OpenShell runtime image from the release checkout and set `DIFY_AGENT_OPENSHELL_SANDBOX_IMAGE` to the exact image reference available to the gateway's compute nodes. The image must include both `shellctl` and `iproute2`; an older cached runtime image may lack the required networking tools.

When upgrading from the previous shared deployment-wide `shellctl` token, generate a fresh high-entropy master secret and update all Agent Backend replicas together. Drain active work, then stop and restart existing sandboxes so `shellctl` restarts with the derived credential. Reacquiring an already healthy sandbox does not refresh its credential.

Shared-volume Home Snapshots and `DIFY_AGENT_OPENSHELL_SHARED_MOUNT_PATH` are removed. Existing running sandboxes retain their state across stop/restart cycles, whereas newly created Bindings start from the image's default Home. `DIFY_AGENT_OPENSHELL_DRIVER_CONFIG` is now optional. Review the [OpenShell deployment guide](https://github.com/langgenius/dify/blob/1.20.0/dify-agent/docs/dify-agent/guide/openshell.md), including its runtime-image requirements, before upgrading. Other sandbox backends are unaffected.

### Docker Compose

Once the `1.20.0` tag and images are published, stop the deployment gracefully, switch to the release, migrate local configuration files, and then pull and start the updated services:

```bash
cd dify/docker
docker compose stop -t -1
git fetch --tags
git checkout 1.20.0
# Migrate shared.env, public URLs, and any custom proxy/worker configuration.
docker compose pull
docker compose up -d
```

Keep API startup migrations enabled (`MIGRATION_ENABLED=true`), or apply the full migration chain through your managed migration process before starting new workers. Use `docker compose up -d` after changing environment files; a plain restart does not reload them.

### Source deployments

Use **Python 3.13**, **Node.js 24.22.3 or later in the 24.x line**, and **pnpm 12.18.0**. After stopping the services and switching to the release, run the following commands from the repository root:

```bash
uv sync --project api --frozen
uv run --directory api flask db upgrade
pnpm install --frozen-lockfile
```

Rebuild Web and restart the API, workers, scheduler, and Agent services from the same release. Update the standalone Agent Backend's locked dependencies if deploying it separately. Preserve existing worker subscriptions and add the two HITL queues where needed.

**Full Changelog:** [1.19.0 → 1.20.0](https://github.com/langgenius/dify/compare/1.19.0...1.20.0)

## 笔记


