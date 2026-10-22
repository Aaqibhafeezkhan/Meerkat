import discord
from discord import app_commands
from discord.ext import commands


class Ping(commands.Cog):
    """A minimal cog containing the /ping command."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="ping", description="Responds with Pong!")
    async def ping(self, interaction: discord.Interaction) -> None:
        """A simple health-check command."""
        await interaction.response.send_message("Pong!")


async def setup(bot: commands.Bot) -> None:
    """Entry point for the cog loader."""
    await bot.add_cog(Ping(bot))