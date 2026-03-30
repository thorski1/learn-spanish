"""
Greetings skill pack — Hola y Adios
Teaches Spanish greetings, introductions, politeness, and formal vs informal speech.
Guided by Sofia, a warm and encouraging Spanish teacher.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  _  _  ___  _      _
 | || |/ _ \| |    / \
 | __ | | | | |   / _ \
 |_||_|_|_|_|_|__/_/ \_\
"""

SKILL_PACK = SkillPack(
    id="greetings_es",
    title="Hola y Adios",
    subtitle="Greet, introduce yourself, and be polite in Spanish",
    save_file_name="greetings_es_quest",
    intro_story=INTRO_STORY,
    quit_message="Sofia waves warmly. Hasta luego -- your progress is saved!",
    name_prompt="[bold cyan]What's your name, learner?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "hello_goodbye": "greeting_star",
        "introductions": "introduction_pro",
        "how_are_you": "empathy_speaker",
        "please_thanks": "polite_soul",
        "formal_informal": "register_master",
        "classroom_phrases": "classroom_hero",
    },
    achievements={
        "greeting_star":     ("Greeting Star", "Mastered hello, goodbye, and every time-of-day greeting!"),
        "introduction_pro":  ("Introduction Pro", "Can introduce yourself and others with confidence!"),
        "empathy_speaker":   ("Empathy Speaker", "Can ask and answer 'How are you?' naturally!"),
        "polite_soul":       ("Polite Soul", "Learned please, thank you, sorry, and all polite expressions!"),
        "register_master":   ("Register Master", "Understands when to use tu vs usted!"),
        "classroom_hero":    ("Classroom Hero", "Knows essential classroom and learning phrases!"),
        "no_hints":          ("Solo Learner", "Completed a zone without any hints!"),
        "speed_reader":      ("Quick Thinker", "Answered a question in under 10 seconds!"),
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
