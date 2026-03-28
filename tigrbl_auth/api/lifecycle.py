from __future__ import annotations

import inspect

from tigrbl import TigrblApp

from tigrbl_auth.api.surfaces import surface_api
from tigrbl_auth.migrations import apply_all_async


async def _startup() -> None:
    await apply_all_async()
    init = surface_api.initialize()
    if inspect.isawaitable(init):
        await init


def register_lifecycle(app: TigrblApp) -> None:
    app.add_event_handler("startup", _startup)
