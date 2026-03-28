import asyncio
from uuid import uuid4

import pytest

from tigrbl_auth.standards.oidc import backchannel_logout


class _Registration:
    registration_metadata = {
        "backchannel_logout_uri": "https://rp.example/backchannel",
        "backchannel_logout_session_required": True,
    }


class _Persistence:
    async def get_client_registration_async(self, client_id):
        return _Registration()


def test_backchannel_descriptor_and_logout_token_validation(monkeypatch):
    monkeypatch.setattr(backchannel_logout, "_persistence", lambda: _Persistence())
    descriptor = asyncio.run(
        backchannel_logout.build_backchannel_descriptor(
            client_id=uuid4(),
            sid="sid-1",
            sub="user-1",
            iss="https://issuer.example",
            logout_id=uuid4(),
        )
    )
    assert descriptor["delivery"]["status"] == "pending"
    claims = asyncio.run(
        backchannel_logout.validate_backchannel_logout_token(
            descriptor["logout_token"],
            client_id=descriptor["client_id"],
            issuer="https://issuer.example",
        )
    )
    assert claims["events"]
    with pytest.raises(ValueError):
        asyncio.run(
            backchannel_logout.validate_backchannel_logout_token(
                descriptor["logout_token"],
                client_id=descriptor["client_id"],
                issuer="https://issuer.example",
            )
        )
