"""Service-layer package.

This package intentionally avoids eager re-export of runtime-heavy modules so
checkpoint tooling can import lightweight operator services without requiring the
full database/runtime dependency set.
"""

__all__: list[str] = []
