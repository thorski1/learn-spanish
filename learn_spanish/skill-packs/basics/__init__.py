"""
Basics skill pack — The Foundation of Spanish
Teaches the alphabet, gender, articles, ser vs estar, conjugation, adjectives,
question words, and basic sentence structure.
Guided by Sofia, a warm and encouraging Spanish teacher.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ____    _    ____  _  ____ ____
 | __ )  / \  / ___|| |/ ___/ ___|
 |  _ \ / _ \ \___ \| | |   \___ \
 | |_) / ___ \ ___) | | |___ ___) |
 |____/_/   \_\____/|_|\____|____/
"""

SKILL_PACK = SkillPack(
    id="basics",
    title="The Foundation of Spanish",
    subtitle="Master the building blocks of the Spanish language",
    save_file_name="basics_quest",
    intro_story=INTRO_STORY,
    quit_message="Sofia closes her notebook with a warm smile. Your progress is saved -- vuelve pronto!",
    name_prompt="[bold cyan]What's your name, learner?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "alphabet_pronunciation": "alphabet_ace",
        "gender_articles": "article_master",
        "ser_vs_estar": "being_expert",
        "basic_conjugation": "verb_dancer",
        "common_adjectives": "color_painter",
        "question_words": "curious_mind",
        "basic_sentences": "sentence_builder",
    },
    achievements={
        "alphabet_ace":      ("Alphabet Ace", "Mastered the Spanish alphabet and pronunciation!"),
        "article_master":    ("Article Master", "Conquered el, la, un, una and gender rules!"),
        "being_expert":      ("Being Expert", "Understood the difference between ser and estar!"),
        "verb_dancer":       ("Verb Dancer", "Conjugated -ar, -er, and -ir verbs with ease!"),
        "color_painter":     ("Color Painter", "Learned colors, sizes, and adjective agreement!"),
        "curious_mind":      ("Curious Mind", "Mastered all the Spanish question words!"),
        "sentence_builder":  ("Sentence Builder", "Built complete Spanish sentences from scratch!"),
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
