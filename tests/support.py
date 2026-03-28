from __future__ import annotations

from httpx import ASGITransport, Client


class TestClient(Client):
    __test__ = False

    """Minimal ASGI test client used to avoid framework-specific test clients."""

    def __init__(self, app, base_url: str = "http://testserver", **kwargs):
        transport = ASGITransport(app=app)
        super().__init__(transport=transport, base_url=base_url, **kwargs)
