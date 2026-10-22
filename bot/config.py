import logging
import os

from dotenv import load_dotenv

# Load variables from .env into the environment.
load_dotenv()

# Configure logging based on the LOG_LEVEL environment variable.
log_level = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    level=getattr(logging, log_level, logging.INFO),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


def get_token() -> str:
    """Return the Discord token, or raise a clear error if it's missing."""
    token = os.getenv("DISCORD_TOKEN")
    if not token or token == "your-bot-token-here":
        raise RuntimeError(
            "DISCORD_TOKEN is not set. Copy .env.example to .env and add your bot token."
        )
    return token


def get_guild_id() -> int | None:
    """Return the optional test guild ID, or None if unset."""
    raw = os.getenv("GUILD_ID")
    if not raw:
        return None
    try:
        return int(raw)
    except ValueError:
        raise RuntimeError(f"GUILD_ID must be a number, got: {raw!r}")