> [!WARNING]
> Archived historical reference. This document is retained for audit history only and is **not** an authoritative current-state artifact.
> Use `docs/compliance/AUTHORITATIVE_CURRENT_DOCS.md` for the current source of truth.

# Browser Session and Logout Flows

## Browser session establishment

```mermaid
sequenceDiagram
    participant Browser
    participant Login as /login
    participant Session as AuthSession
    Browser->>Login: username + password
    Login->>Session: create durable session
    Session-->>Login: session id + cookie secret hash + salt
    Login-->>Browser: opaque sid cookie + access/refresh/id token
```

## Authorization with session_state

```mermaid
sequenceDiagram
    participant Browser
    participant Authorize as /authorize
    participant Session as Session Management
    Browser->>Authorize: authorize request + opaque sid cookie
    Authorize->>Session: resolve durable session and validate cookie secret hash
    Session-->>Authorize: active session + optional rotated secret
    Authorize-->>Browser: redirect with code/id_token/session_state
```

## Logout with fanout planning

```mermaid
sequenceDiagram
    participant Browser
    participant Logout as /logout
    participant Session as Logout Planner
    participant Store as logout_state
    Browser->>Logout: id_token_hint/post_logout_redirect_uri/client_id
    Logout->>Session: validate redirect and build/reuse logout plan
    Session->>Store: persist frontchannel/backchannel fanout metadata
    Logout-->>Browser: clear cookie + redirect or JSON response
```

## Abuse-case handling

- malformed opaque cookies are rejected during browser-session resolution
- unregistered `post_logout_redirect_uri` values are rejected
- repeated logout attempts reuse the durable logout record instead of fanout duplication
- cross-site cookie mode is explicit and only enabled when configured or required for logout interoperability
