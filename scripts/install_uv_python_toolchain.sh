#!/usr/bin/env bash
set -euo pipefail

PY_VERSIONS=("3.10" "3.11" "3.12")
INSTALL_TOOLS=true

while [[ $# -gt 0 ]]; do
  case "$1" in
    --python)
      PY_VERSIONS+=("$2")
      shift 2
      ;;
    --no-tools)
      INSTALL_TOOLS=false
      shift
      ;;
    *)
      echo "Unknown argument: $1" >&2
      exit 2
      ;;
  esac
done

seen=''
UNIQ=()
for v in "${PY_VERSIONS[@]}"; do
  [[ -z "$v" ]] && continue
  case ",$seen," in
    *",$v,"*) ;;
    *) UNIQ+=("$v"); seen+="${seen:+,}$v" ;;
  esac
done

if ! command -v uv >/dev/null 2>&1; then
  python3 -m pip install --user --upgrade uv
fi

if [[ "$INSTALL_TOOLS" == true ]]; then
  python3 -m pip install --user --upgrade pip tox
fi

uv python install "${UNIQ[@]}"

echo "[uv-toolchain] Installed Python interpreters: ${UNIQ[*]}"
