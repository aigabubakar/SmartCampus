from typing import Any
from sqlalchemy.orm import as_declarative, declared_attr

@as_declarative()
class Base:
    id: Any
    __name__: str

    # Automatically generate __tablename__ based on class name in lowercase
    @declared_attr
    def __tablename__(cls) -> str:
        name = cls.__name__.lower()
        if name.endswith("y"):
            return name[:-1] + "ies"
        elif not name.endswith("s"):
            return name + "s"
        return name
