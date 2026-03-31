#!/usr/bin/env bash
set -euo pipefail

DB_NAME="${TIGRBL_AUTH_LOCAL_POSTGRES_DB:-tigrbl_auth_ci}"
DB_USER="${TIGRBL_AUTH_LOCAL_POSTGRES_USER:-postgres}"
DB_PASS="${TIGRBL_AUTH_LOCAL_POSTGRES_PASSWORD:-postgres}"
DB_HOST="${TIGRBL_AUTH_LOCAL_POSTGRES_HOST:-127.0.0.1}"
DB_PORT="${TIGRBL_AUTH_LOCAL_POSTGRES_PORT:-5432}"

if ! command -v psql >/dev/null 2>&1; then
  sudo apt-get update
  sudo apt-get install -y postgresql postgresql-contrib
fi

if ! pg_isready -h "${DB_HOST}" -p "${DB_PORT}" >/dev/null 2>&1; then
  if command -v pg_ctlcluster >/dev/null 2>&1; then
    sudo pg_ctlcluster 16 main start || true
  fi
fi

if ! pg_isready -h "${DB_HOST}" -p "${DB_PORT}" >/dev/null 2>&1; then
  echo "PostgreSQL is not reachable at ${DB_HOST}:${DB_PORT}" >&2
  exit 1
fi

export PGPASSWORD="${DB_PASS}"

if ! psql -h "${DB_HOST}" -p "${DB_PORT}" -U "${DB_USER}" -d postgres -c "SELECT 1" >/dev/null 2>&1; then
  if id postgres >/dev/null 2>&1; then
    sudo -u postgres psql -d postgres -v ON_ERROR_STOP=1 -c "ALTER USER ${DB_USER} WITH PASSWORD '${DB_PASS}';"
  fi
fi

psql -h "${DB_HOST}" -p "${DB_PORT}" -U "${DB_USER}" -d postgres -v ON_ERROR_STOP=1 -c "ALTER USER ${DB_USER} WITH PASSWORD '${DB_PASS}';"
psql -h "${DB_HOST}" -p "${DB_PORT}" -U "${DB_USER}" -d postgres -v ON_ERROR_STOP=1 -tc "SELECT 1 FROM pg_database WHERE datname='${DB_NAME}'" | grep -q 1 || \
  psql -h "${DB_HOST}" -p "${DB_PORT}" -U "${DB_USER}" -d postgres -v ON_ERROR_STOP=1 -c "CREATE DATABASE ${DB_NAME};"

POSTGRES_URL="postgresql://${DB_USER}:${DB_PASS}@${DB_HOST}:${DB_PORT}/${DB_NAME}"
if [ -n "${GITHUB_ENV:-}" ]; then
  echo "POSTGRES_URL=${POSTGRES_URL}" >> "${GITHUB_ENV}"
fi

echo "POSTGRES_URL=${POSTGRES_URL}"
pg_isready -h "${DB_HOST}" -p "${DB_PORT}"
