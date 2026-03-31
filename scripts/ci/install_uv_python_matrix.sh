#!/usr/bin/env bash
set -euo pipefail

PY_VERSIONS=("3.10" "3.11" "3.12")

if ! command -v uv >/dev/null 2>&1; then
  python -m pip install --upgrade uv
fi

uv python install "${PY_VERSIONS[@]}"
uv python list
