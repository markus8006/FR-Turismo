"""Repository helpers for the ``Viagens`` model."""
from __future__ import annotations

from typing import List

from src.models.Viagens import Viagens
from src.repository.base_repo import BaseRepository


class ViagensRepository(BaseRepository[Viagens]):
    def __init__(self) -> None:
        super().__init__(Viagens)

    def find_by_cliente(self, user_id: int) -> List[Viagens]:
        """List all trips requested by a given user."""
        return self.filter_by(client_id=user_id)

    def find_by_motorista(self, motorista_id: int) -> List[Viagens]:
        """List all trips assigned to a specific driver."""
        return self.filter_by(motorista_id=motorista_id)
