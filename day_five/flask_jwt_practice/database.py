from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from contextlib import contextmanager
from typing import Generator

from config import Config


class Base(DeclarativeBase):
    pass


engine = create_engine(Config.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


@contextmanager
def get_db() -> Generator:
    """Provides a transactional DB session and ensures it is closed after use."""
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
