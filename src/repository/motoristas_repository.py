"""Repository helpers for the ``Motorista`` model."""
from __future__ import annotations

from typing import Optional

from src.models.Motorista import Motorista
from src.repository.base_repo import BaseRepository


class MotoristasRepository(BaseRepository[Motorista]):
    def __init__(self) -> None:
        super().__init__(Motorista)

    def get_by_email(self, email: str) -> Optional[Motorista]:
        """Return a driver by their email address."""
        return self.first_by(email=email)

    def get_by_cpf(self, cpf: str) -> Optional[Motorista]:
        """Return a driver by CPF."""
        return self.first_by(CPF=cpf)
