import pytest

from bot.cogs.initiate import channel_slug, owned_channel_topic
from bot.config import get_optional_id


def test_channel_slug_is_discord_safe() -> None:
    member = type("MemberStub", (), {"display_name": "Aaqib Khan / Test"})()
    assert channel_slug(member) == "aaqib-khan-test"


def test_owned_channel_topic_is_unique_per_member_and_kind() -> None:
    assert owned_channel_topic(123, "tdl") == "meerkat-owner:123:tdl"
    assert owned_channel_topic(123, "monthlies") != owned_channel_topic(123, "tdl")
    assert owned_channel_topic(456, "tdl") != owned_channel_topic(123, "tdl")


def test_get_optional_id_returns_none_when_unset(monkeypatch) -> None:
    monkeypatch.delenv("TDL_CATEGORY_ID", raising=False)
    assert get_optional_id("TDL_CATEGORY_ID") is None


def test_get_optional_id_parses_discord_id(monkeypatch) -> None:
    monkeypatch.setenv("TDL_CATEGORY_ID", "123456789012345678")
    assert get_optional_id("TDL_CATEGORY_ID") == 123456789012345678


def test_get_optional_id_rejects_invalid_value(monkeypatch) -> None:
    monkeypatch.setenv("TDL_CATEGORY_ID", "not-a-number")
    with pytest.raises(RuntimeError, match="TDL_CATEGORY_ID must be a number"):
        get_optional_id("TDL_CATEGORY_ID")
