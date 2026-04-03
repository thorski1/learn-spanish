"""
Weather & Seasons skill pack — Weather & Seasons
Teaches Spanish weather expressions, seasons, months, temperature, climate,
weather conversations, and making plans with weather.
Guided by Sofia on a sunset coastal promenade.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 __        __         _   _
 \ \      / /__  __ _| |_| |__   ___ _ __
  \ \ /\ / / _ \/ _` | __| '_ \ / _ \ '__|
   \ V  V /  __/ (_| | |_| | | |  __/ |
    \_/\_/ \___|\__,_|\__|_| |_|\___|_|
"""

SKILL_PACK = SkillPack(
    id="weather_es",
    title="Weather & Seasons",
    subtitle="Describe the weather, name the seasons, and make plans in Spanish",
    save_file_name="weather_es_quest",
    intro_story=INTRO_STORY,
    quit_message="Sofia waves from the promenade. Hasta la proxima -- your progress is saved!",
    name_prompt="[bold cyan]What's your name, learner?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "weather_basics": "weather_watcher",
        "seasons_months": "calendar_keeper",
        "temperature_climate": "thermometer_reader",
        "weather_conversations": "small_talk_star",
        "making_plans_weather": "plan_maker",
    },
    achievements={
        "weather_watcher":      ("Weather Watcher", "Mastered the essential Spanish weather expressions!"),
        "calendar_keeper":      ("Calendar Keeper", "Knows every season and month in Spanish!"),
        "thermometer_reader":   ("Thermometer Reader", "Can discuss temperature and climate like a meteorologist!"),
        "small_talk_star":      ("Small Talk Star", "Chats about weather naturally in Spanish!"),
        "plan_maker":           ("Plan Maker", "Makes weather-based plans fluently in Spanish!"),
        "no_hints":             ("Solo Learner", "Completed a zone without any hints!"),
        "speed_reader":         ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="sunset",
    level_titles=[
        (1, "Beginner"),
        (6, "Apprentice"),
        (11, "Speaker"),
        (16, "Conversant"),
        (21, "Fluent Thinker"),
        (26, "Language Sage"),
    ],
)
