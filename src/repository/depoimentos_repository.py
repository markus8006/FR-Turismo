"""Repository helpers for the ``Depoimentos`` model."""
from __future__ import annotations

from typing import List

from src.models.Depoimentos import Depoimentos
from src.repository.base_repo import BaseRepository


class DepoimentosRepository(BaseRepository[Depoimentos]):
    def __init__(self) -> None:
        super().__init__(Depoimentos)

    def find_by_user(self, user_id: int) -> List[Depoimentos]:
        """List all testimonials authored by a specific user."""
        return self.filter_by(client_id=user_id)

    def find_by_viagem(self, viagem_id: int) -> List[Depoimentos]:
        """List all testimonials linked to a trip."""
        return self.filter_by(viagem_id=viagem_id)
