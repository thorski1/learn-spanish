"""
Family skill pack — Mi Familia
Teaches family members, descriptions, house vocabulary, pets, and relationships.
Guided by Sofia, a warm and encouraging Spanish teacher.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  _____ _    __  __ ___ _  __   __
 |  ___/ \  |  \/  |_ _| | \ \ / /
 | |_ / _ \ | |\/| || || |  \ V /
 |  _/ ___ \| |  | || || |___| |
 |_|/_/   \_\_|  |_|___|_____|_|
"""

SKILL_PACK = SkillPack(
    id="family_es",
    title="Mi Familia",
    subtitle="Family, home, descriptions, and the people in your life",
    save_file_name="family_es_quest",
    intro_story=INTRO_STORY,
    quit_message="Sofia closes the family album. Your progress is saved -- la familia siempre te espera!",
    name_prompt="[bold cyan]What's your name, learner?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "immediate_family": "family_heart",
        "extended_family": "family_tree",
        "descriptions": "portrait_painter",
        "house_rooms": "home_builder",
        "pets": "animal_friend",
        "relationships": "social_butterfly",
    },
    achievements={
        "family_heart":      ("Family Heart", "Named every immediate family member in Spanish!"),
        "family_tree":       ("Family Tree", "Mapped the entire extended family in Spanish!"),
        "portrait_painter":  ("Portrait Painter", "Can describe anyone using Spanish adjectives!"),
        "home_builder":      ("Home Builder", "Knows every room in a Spanish-speaking home!"),
        "animal_friend":     ("Animal Friend", "Learned all the pet vocabulary in Spanish!"),
        "social_butterfly":  ("Social Butterfly", "Mastered relationship vocabulary in Spanish!"),
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
