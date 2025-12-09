"""Base repository providing common CRUD operations."""
from __future__ import annotations

from typing import Generic, Iterable, Optional, Type, TypeVar

from src.app import db

ModelType = TypeVar("ModelType", bound=db.Model)


class BaseRepository(Generic[ModelType]):
    """Generic repository with helpers to interact with SQLAlchemy models."""

    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get_all(self) -> list[ModelType]:
        """Return all records for the model."""
        return self.model.query.all()

    def get_by_id(self, entity_id: int) -> Optional[ModelType]:
        """Retrieve a single record by its primary key."""
        return self.model.query.get(entity_id)

    def add(self, **kwargs) -> ModelType:
        """Create and persist a new record."""
        instance = self.model(**kwargs)
        db.session.add(instance)
        db.session.commit()
        return instance

    def update(self, instance: ModelType, **kwargs) -> ModelType:
        """Update fields on an existing record and persist changes."""
        for attr, value in kwargs.items():
            setattr(instance, attr, value)
        db.session.commit()
        return instance

    def delete(self, instance: ModelType) -> None:
        """Delete a record from the database."""
        db.session.delete(instance)
        db.session.commit()

    def filter_by(self, **kwargs) -> list[ModelType]:
        """Filter results using SQLAlchemy's ``filter_by`` helper."""
        return self.model.query.filter_by(**kwargs).all()

    def first_by(self, **kwargs) -> Optional[ModelType]:
        """Return the first record matching the provided filters."""
        return self.model.query.filter_by(**kwargs).first()

    def add_many(self, items: Iterable[dict]) -> list[ModelType]:
        """Create and persist multiple records in a single transaction."""
        instances = [self.model(**data) for data in items]
        db.session.add_all(instances)
        db.session.commit()
        return instances
