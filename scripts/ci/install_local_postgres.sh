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
  sudo pg_ctlcluster 16 main start || true
fi

sudo -u postgres psql -v ON_ERROR_STOP=1 -c "ALTER USER ${DB_USER} WITH PASSWORD '${DB_PASS}';"
sudo -u postgres psql -v ON_ERROR_STOP=1 -tc "SELECT 1 FROM pg_database WHERE datname='${DB_NAME}'" | grep -q 1 || \
  sudo -u postgres psql -v ON_ERROR_STOP=1 -c "CREATE DATABASE ${DB_NAME};"

POSTGRES_URL="postgresql://${DB_USER}:${DB_PASS}@${DB_HOST}:${DB_PORT}/${DB_NAME}"
echo "POSTGRES_URL=${POSTGRES_URL}" >> "${GITHUB_ENV:-/dev/null}" || true
echo "POSTGRES_URL=${POSTGRES_URL}"
pg_isready -h "${DB_HOST}" -p "${DB_PORT}"
