"""User model for the authentication service."""

from __future__ import annotations

import uuid

from tigrbl_auth.framework import (
    UserBase,
    LargeBinary,
    Mapped,
    String,
    relationship,
    F,
    IO,
    S,
    acol,
    ColumnSpec,
)


class User(UserBase):
    __table_args__ = ({"extend_existing": True, "schema": "authn"},)

    username: Mapped[str] = acol(
        spec=ColumnSpec(
            storage=S(String(32), nullable=False),
            field=F(constraints={"max_length": 32}, required_in=("create",)),
            io=IO(
                in_verbs=("create", "update", "replace"),
                out_verbs=("read", "list"),
                filter_ops=("eq", "ilike"),
                sortable=True,
            ),
        )
    )
    email: Mapped[str] = acol(
        spec=ColumnSpec(
            storage=S(String(120), nullable=False, unique=True),
            field=F(constraints={"max_length": 120}, required_in=("create",)),
            io=IO(
                in_verbs=("create", "update", "replace"),
                out_verbs=("read", "list"),
                filter_ops=("eq", "ilike"),
                sortable=True,
            ),
        )
    )
    password_hash: Mapped[bytes | None] = acol(
        spec=ColumnSpec(storage=S(LargeBinary(60)), io=IO(in_verbs=("create", "update", "replace")))
    )

    _api_keys = relationship("ApiKey", back_populates="_user", cascade="all, delete-orphan")
    tenant = relationship("Tenant", back_populates="users")

    @classmethod
    def new(cls, *, tenant_id: uuid.UUID, username: str, email: str, password: str):
        return cls(
            tenant_id=tenant_id,
            username=username,
            email=email,
            password_hash=None if password is not None else None,
        )

    def verify_password(self, plain: str) -> bool:
        from tigrbl_auth.services.key_management import verify_pw
        if self.password_hash is None:
            return False
        return verify_pw(plain, self.password_hash)


__all__ = ["User"]
