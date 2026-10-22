def test_smoke() -> None:
    """A trivial test to confirm pytest is configured and running."""
    assert True


def test_ping_command_exists() -> None:
    """Smoke-test that the ping cog defines a /ping command."""
    from bot.cogs.ping import Ping
    from discord import app_commands

    command = Ping.ping
    assert isinstance(command, app_commands.Command)
    assert command.name == "ping"
