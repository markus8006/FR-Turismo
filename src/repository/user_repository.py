"""Repository helpers for the ``User`` model."""
from __future__ import annotations

from typing import Optional

from src.models.Users import User
from src.repository.base_repo import BaseRepository


class UserRepository(BaseRepository[User]):
    def __init__(self) -> None:
        super().__init__(User)

    def get_by_email(self, email: str) -> Optional[User]:
        """Return a user by their email address."""
        return self.first_by(email=email)

    def get_by_cpf(self, cpf: str) -> Optional[User]:
        """Return a user by CPF."""
        return self.first_by(CPF=cpf)
