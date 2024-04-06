from typing import Any

from ._component import Component as Component

# Re-export imports so they look like they live directly in this package
key: str
value: Any
for key, value in list(locals().items()):
    if getattr(value, "__module__", "").startswith(f"{__name__}."):
        value.__module__ = __name__
