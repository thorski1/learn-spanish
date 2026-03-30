"""
Culture skill pack — El Mundo Hispanohablante
Teaches Spanish-speaking countries, festivals, music, famous people, traditions,
and differences between Spain and Latin American Spanish.
Guided by Sofia, a warm and encouraging Spanish teacher.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
   ____ _   _ _   _____ _   _ ____  _____
  / ___| | | | | |_   _| | | |  _ \| ____|
 | |   | | | | |   | | | | | | |_) |  _|
 | |___| |_| | |___| | | |_| |  _ <| |___
  \____|\___/|_____|_|  \___/|_| \_\_____|
"""

SKILL_PACK = SkillPack(
    id="culture_es",
    title="El Mundo Hispanohablante",
    subtitle="Countries, festivals, music, traditions, and regional differences",
    save_file_name="culture_es_quest",
    intro_story=INTRO_STORY,
    quit_message="Sofia rolls up the world map. Your progress is saved -- the world awaits your return!",
    name_prompt="[bold cyan]What's your name, learner?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "spanish_countries": "world_mapper",
        "festivals": "fiesta_lover",
        "music_dance": "rhythm_master",
        "famous_people": "culture_scholar",
        "traditions": "tradition_keeper",
        "spanish_vs_latin": "dialect_detective",
    },
    achievements={
        "world_mapper":      ("World Mapper", "Located all 20+ Spanish-speaking countries!"),
        "fiesta_lover":      ("Fiesta Lover", "Explored the greatest festivals in the Spanish-speaking world!"),
        "rhythm_master":     ("Rhythm Master", "Knows salsa, flamenco, reggaeton, and mariachi!"),
        "culture_scholar":   ("Culture Scholar", "Learned about Frida, Garcia Marquez, Messi, and more!"),
        "tradition_keeper":  ("Tradition Keeper", "Understands siesta, quinceañera, and cultural traditions!"),
        "dialect_detective":  ("Dialect Detective", "Spotted the differences between Spain and Latin American Spanish!"),
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
