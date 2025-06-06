"""Utils"""
import attr
from typing import Any

def create_attrs_instance_from_dict(cls: Any, data: dict) -> Any:
    """
    A simple helper to instantiate an Attrs class from a dictionary,
    respecting aliases defined in metadata.
    This mimics Pydantic's alias behavior for dict input.
    """
    mapped_data = {}
    for field in attr.fields(cls):
        alias = field.metadata.get('alias')
        if alias and alias in data:
            mapped_data[field.name] = data[alias]
        elif field.name in data:
            mapped_data[field.name] = data[field.name]
        elif field.default is attr.NOTHING and not field.init:
            pass
        elif field.default is attr.NOTHING and field.init and not field.name in data:
            pass
        elif field.default is not attr.NOTHING and not field.name in data:
            pass

    return cls(**mapped_data)
