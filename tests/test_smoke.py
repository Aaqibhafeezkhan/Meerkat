import pytest


def test_smoke() -> None:
    """A trivial test to confirm pytest is configured and running."""
    assert True


@pytest.mark.asyncio
async def test_ping_command_exists() -> None:
    """Smoke-test that the ping cog defines a /ping command."""
    from bot.cogs.ping import Ping

    command = getattr(Ping.ping, "__discord_app_commands_command__", None)
    assert command is not None, "Ping.ping should be an app_commands command"
    assert command.name == "ping"
