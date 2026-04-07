"""
learn_spanish/main.py — Entry points for Learn Spanish.

Sets the skill-packs directory for the engine, then launches
the appropriate pack.
"""

import os
import sys
from pathlib import Path

# Ensure UTF-8 output (handles Spanish characters, accent marks, etc.)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

_HERE = Path(__file__).parent
os.environ.setdefault("QUEST_SKILL_PACKS_DIR", str(_HERE / "skill-packs"))

from engine.main import run, run_campaign          # noqa: E402
from engine.updater import check_and_prompt        # noqa: E402

_PACKAGE = "learn-spanish"
_PACKS_DIR = str(_HERE / "skill-packs")

_WEB = "--web" in sys.argv

SPANISH_PACKS = [
    "basics", "greetings_es", "numbers_es", "food_es",
    "family_es", "travel_es", "daily_es", "culture_es", "colors_clothing", "weather_es", "restaurant_es", "directions_es", "health_es",
]


def _web(pack_name: str, port: int = 8080):
    """Launch the web interface for *pack_name*."""
    from engine.web.server import serve
    serve(pack_name, port=port, packs_dir=_PACKS_DIR)


def main_spanish():
    if _WEB:
        from engine.web.hub import serve_hub
        serve_hub(SPANISH_PACKS, port=8080, packs_dir=_PACKS_DIR)
        return
    check_and_prompt(_PACKAGE)
    run_campaign("learn_spanish")


def main_basics():
    if _WEB:
        _web("basics")
        return
    check_and_prompt(_PACKAGE)
    run("basics")


def main_greetings_es():
    if _WEB:
        _web("greetings_es")
        return
    check_and_prompt(_PACKAGE)
    run("greetings_es")


def main_numbers_es():
    if _WEB:
        _web("numbers_es")
        return
    check_and_prompt(_PACKAGE)
    run("numbers_es")


def main_food_es():
    if _WEB:
        _web("food_es")
        return
    check_and_prompt(_PACKAGE)
    run("food_es")


def main_family_es():
    if _WEB:
        _web("family_es")
        return
    check_and_prompt(_PACKAGE)
    run("family_es")


def main_travel_es():
    if _WEB:
        _web("travel_es")
        return
    check_and_prompt(_PACKAGE)
    run("travel_es")


def main_daily_es():
    if _WEB:
        _web("daily_es")
        return
    check_and_prompt(_PACKAGE)
    run("daily_es")


def main_culture_es():
    if _WEB:
        _web("culture_es")
        return
    check_and_prompt(_PACKAGE)
    run("culture_es")
