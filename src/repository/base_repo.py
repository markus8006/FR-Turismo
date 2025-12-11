"""Infraestrutura simples de repositórios baseada em SQLAlchemy."""

from __future__ import annotations

from typing import Any, Iterable, List, Optional, Type

from src.app import db



class BaseRepo:
    """Implementa operações CRUD básicas com tratamento de erros consistente."""

    def __init__(self, model: Type[Any], session) -> None:
        self.model = model
        self.session = session or db.session

  