from datetime import datetime, timezone
from xml.etree import ElementTree

import pytest

from scripts.profile_render import CHARCOAL, CREAM, _SEAL_GLYPH, render_hero


@pytest.mark.parametrize("theme", [CREAM, CHARCOAL])
def test_render_hero_uses_current_abstract_and_only_streak_stat(theme):
    svg = render_hero(
        streak=123,
        theme=theme,
        now=datetime(2026, 6, 20, tzinfo=timezone.utc),
    )

    ElementTree.fromstring(svg)
    assert "Building software and shipping open source projects." in svg
    assert "Focused on modern software engineering and developer tooling." in svg
    assert "CONTRIBUTIONS" not in svg
    assert ">DAY STREAK<" in svg
    assert ">123</tspan>" in svg
    assert ">current</text>" in svg
    assert 'x="966"' in svg
    assert 'text-anchor="middle"' in svg

