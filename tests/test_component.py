from __future__ import annotations

import pytest

from asphalt.core import Context
from asphalt.example import ExampleComponent

pytestmark = pytest.mark.anyio


async def test_component() -> None:
    component = ExampleComponent()
    async with Context() as ctx:
        await component.start(ctx)
