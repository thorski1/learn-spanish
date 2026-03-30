"""
Daily Life skill pack — La Vida Diaria
Teaches daily routines, school/work, hobbies, weather, shopping, and health.
Guided by Sofia, a warm and encouraging Spanish teacher.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ____    _  ___ _  __   __
 |  _ \  / \|_ _| | \ \ / /
 | | | |/ _ \| || |  \ V /
 | |_| / ___ \ || |___| |
 |____/_/   \_\___|_____|_|
"""

SKILL_PACK = SkillPack(
    id="daily_es",
    title="La Vida Diaria",
    subtitle="Routines, hobbies, weather, shopping, and health",
    save_file_name="daily_es_quest",
    intro_story=INTRO_STORY,
    quit_message="Sofia closes her daily planner. Your progress is saved -- hasta manana!",
    name_prompt="[bold cyan]What's your name, learner?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "morning_routine": "early_bird",
        "school_work": "scholar",
        "hobbies": "hobby_master",
        "weather": "weather_watcher",
        "shopping": "smart_shopper",
        "body_health": "health_hero",
    },
    achievements={
        "early_bird":       ("Early Bird", "Can describe your entire morning routine in Spanish!"),
        "scholar":          ("Scholar", "Mastered school and work vocabulary!"),
        "hobby_master":     ("Hobby Master", "Can talk about hobbies and free time in Spanish!"),
        "weather_watcher":  ("Weather Watcher", "Knows how to discuss weather in any season!"),
        "smart_shopper":    ("Smart Shopper", "Can navigate any store and haggle like a pro!"),
        "health_hero":      ("Health Hero", "Knows body parts and health vocabulary!"),
        "no_hints":         ("Solo Learner", "Completed a zone without any hints!"),
        "speed_reader":     ("Quick Thinker", "Answered a question in under 10 seconds!"),
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
