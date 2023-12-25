from __future__ import annotations

import pytest

from checkov.common.bridgecrew.bc_source import SourceType
from checkov.common.bridgecrew.platform_integration import BcPlatformIntegration, bc_integration


@pytest.fixture()
def mock_bc_integration() -> BcPlatformIntegration:
    bc_integration.bc_api_key = "abcd1234-abcd-1234-abcd-1234abcd1234"
    bc_integration.setup_bridgecrew_credentials(
        repo_id="bridgecrewio/checkov",
        skip_fixes=True,
        skip_download=True,
        source=SourceType("Github", False),
        source_version="1.0",
        repo_branch="master",
    )
    yield bc_integration
    bc_integration.bc_api_key = None
    bc_integration.repo_id = None
    bc_integration.repo_branch = None
    bc_integration.bc_source = None
    bc_integration.skip_fixes = False
    bc_integration.bc_source_version = None
    bc_integration.bucket = None
    bc_integration.repo_path = None 
    bc_integration.credentials = None
    bc_integration.support_bucket = None
    bc_integration.support_repo_path = None
    bc_integration.use_s3_integration = False
    bc_integration.platform_integration_configured = False
    bc_integration.credentials = None
