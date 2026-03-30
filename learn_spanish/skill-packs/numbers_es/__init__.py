"""
Numbers skill pack — Counting in Spanish
Teaches numbers, telling time, days, months, and ordinal numbers.
Guided by Sofia, a warm and encouraging Spanish teacher.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  _  _ _   _ __  __ ____  _____ ____  ____
 | \| | | | |  \/  | __ )| ____|  _ \/ ___|
 | .` | | | | |\/| |  _ \|  _| | |_) \___ \
 |_|\_|\___/|_|  |_|____/|_____|____/ ___) |
"""

SKILL_PACK = SkillPack(
    id="numbers_es",
    title="Counting in Spanish",
    subtitle="Numbers, time, dates, and everything you can count",
    save_file_name="numbers_es_quest",
    intro_story=INTRO_STORY,
    quit_message="Sofia puts down the clock. Your progress is saved -- every number counts!",
    name_prompt="[bold cyan]What's your name, learner?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "numbers_1_20": "number_starter",
        "numbers_21_100": "counter_pro",
        "big_numbers": "big_counter",
        "telling_time_es": "time_keeper",
        "days_months": "calendar_master",
        "ordinal_numbers": "order_expert",
    },
    achievements={
        "number_starter":   ("Number Starter", "Counted from uno to veinte!"),
        "counter_pro":      ("Counter Pro", "Mastered numbers all the way to cien!"),
        "big_counter":      ("Big Counter", "Can handle ciento, mil, and millon!"),
        "time_keeper":      ("Time Keeper", "Tells time like a native Spanish speaker!"),
        "calendar_master":  ("Calendar Master", "Knows every day and month in Spanish!"),
        "order_expert":     ("Order Expert", "Mastered ordinal numbers from primero to decimo!"),
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
