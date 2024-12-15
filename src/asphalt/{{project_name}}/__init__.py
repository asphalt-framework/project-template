from ._component import Component as Component

# Re-export imports so they look like they live directly in this package
for __value in list(locals().values()):
    if getattr(__value, "__module__", "").startswith(f"{__name__}."):
        __value.__module__ = __name__

del __value
