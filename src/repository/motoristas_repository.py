"""Repository helpers for the ``Motoristas`` model."""
from __future__ import annotations

from typing import Optional

from src.models.Motorista import Motoristas
from src.repository.base_repo import BaseRepository


class MotoristasRepository(BaseRepository[Motoristas]):
    def __init__(self) -> None:
        super().__init__(Motoristas)

    def get_by_email(self, email: str) -> Optional[Motoristas]:
        """Return a driver by their email address."""
        return self.first_by(email=email)

    def get_by_cpf(self, cpf: str) -> Optional[Motoristas]:
        """Return a driver by CPF."""
        return self.first_by(CPF=cpf)
