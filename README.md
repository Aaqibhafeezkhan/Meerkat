# Meerkat

> NOTE: Setup is in progress. we are not open to contributions yet. 

> A community‑built bot for Accountability Corner

[![CI](https://github.com/Myst1cS04p/Meerkat/actions/workflows/ci.yml/badge.svg)](https://github.com/Myst1cS04p/Meerkat/actions/workflows/ci.yml)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[License: GNU 3.0](LICENSE)

## About

Meerkat is a custom bot built for our community. It handles newbie initiation, todo list management, strike system, and more. 


## Features

- **Initiate people:** When a new person joins the server, they can run a command to automatically set up their tdl and monthlies channel
- **Better task management:** Allows people to generate tdls that you can mark stuff out on. (I'm thinking embeds + buttons)
- **Automatically assign strikes:** When somebody misses a tdl, they automatically get a strike. (And the bot can track this since it's creating the tdls from the command)
- **Reminders:** People can set it up sot hat the bot pings them if after a certain point if a task is not done. 
- **TDL templates:** Since people like customizability.
- **External linking:** The bot has an API that you can use to hook up your local on-device tdl to the bot so that everything stays in sync. (MAYBE)

> Check the [Issues](../../issues) tab for what's being worked on.


## Getting Started

Follow these steps to run the bot locally.

### Prerequisites

- [Python 3.12+](https://www.python.org/)
- [Git](https://git-scm.com/)
- A bot token from the [Discord Developer Portal](https://discord.com/developers/applications)

### Installation

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/Myst1cS04p/Meerkat.git
   cd Meerkat
   ```


2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv

   # Linux / macOS
   source .venv/bin/activate

   # Windows (PowerShell)
   .venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   > Contributing? Also install the dev dependencies so you can run the linter and tests:
   > ```bash
   > pip install -r requirements-dev.txt
   > ```

4. **Configure environment variables**

   Copy the example file and fill in your values:
   ```bash
   cp .env.example .env
   ```

   | Variable | Description |
   |----------|-------------|
   | `DISCORD_TOKEN` | Your bot token from the Developer Portal |
   | `GUILD_ID` | (Optional) A test server ID for faster slash‑command sync |
   | `LOG_LEVEL` | Logging verbosity (`DEBUG`, `INFO`, `WARNING`, `ERROR`) |

   > **Never commit your `.env` file or token.** `.env` is already in `.gitignore`.

5. **Start the bot**
   ```bash
   python -m bot
   ```

   You should see a log line confirming the bot has connected. Try running a command in your test server.

### Available Commands

| Command | What it does |
|---------|--------------|
| `python -m bot` | Start the bot |
| `ruff check .` | Lint the codebase |
| `ruff format .` | Format the codebase |
| `ruff check --fix .` | Lint and auto‑fix what's fixable |
| `pytest` | Run the test suite |

> If you use `uv` or `make`, wrap these in `uv run ...` or a `Makefile`—but plain commands are fine to start.

## Project Structure

```
.
├── bot/
│   ├── __init__.py
│   ├── __main__.py      # Entry point (python -m bot)
│   ├── cogs/            # Command groups / extensions, one file per feature
│   ├── events/          # Event handlers (on_ready, on_message, etc.)
│   └── services/        # Business logic (API calls, database, etc.)
├── tests/               # Test files
├── .env.example         # Example environment variables
├── pyproject.toml       # Project metadata + Ruff/pytest config
├── requirements.txt     # Runtime dependencies
├── requirements-dev.txt # Dev dependencies (ruff, pytest, ...)
└── CONTRIBUTING.md      # How to contribute
```

## Contributing

We'd love your help! This project is designed for **casual, drop‑in contributions**. You don't need to be a maintainer or commit to a schedule.

1. **Browse the [Issues](../../issues)** and find something labeled `good first issue`.
2. **Comment to claim it** so we know it's being worked on.
3. **Open a pull request** when you're done.

For the full workflow—branch naming, commit style, review process, and our labeling system—see **[CONTRIBUTING.md](CONTRIBUTING.md)**.

### Code Style

We use **Ruff** for both linting and formatting. Before opening a PR:

```bash
ruff check --fix .
ruff format .
```

Most editors have a Ruff extension that does this on save. Our rules live in `pyproject.toml` under `[tool.ruff]`.
