"""Repository package exposing helpers for database access."""
from src.repository.base_repo import BaseRepository
from src.repository.user_repository import UserRepository
from src.repository.depoimentos_repository import DepoimentosRepository
from src.repository.viagens_repository import ViagensRepository
from src.repository.motoristas_repository import MotoristasRepository

__all__ = [
    "BaseRepository",
    "UserRepository",
    "DepoimentosRepository",
    "ViagensRepository",
    "MotoristasRepository",
]
