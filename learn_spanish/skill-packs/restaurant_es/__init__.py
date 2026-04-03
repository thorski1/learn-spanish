"""
At the Restaurant skill pack — At the Restaurant
Teaches Spanish restaurant vocabulary: reservations, menus, ordering food,
dietary needs, and paying & tipping.
Guided by Carlos in a hilltop restaurant at sunset.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ____           _                              _
 |  _ \ ___  ___| |_ __ _ _   _ _ __ __ _ _ __ | |_ ___
 | |_) / _ \/ __| __/ _` | | | | '__/ _` | '_ \| __/ _ \
 |  _ <  __/\__ \ || (_| | |_| | | | (_| | | | | ||  __/
 |_| \_\___||___/\__\__,_|\__,_|_|  \__,_|_| |_|\__\___|
"""

SKILL_PACK = SkillPack(
    id="restaurant_es",
    title="At the Restaurant",
    subtitle="Reserve a table, order food, and pay the bill in Spanish",
    save_file_name="restaurant_es_quest",
    intro_story=INTRO_STORY,
    quit_message="Carlos waves from the restaurant entrance. Hasta la proxima -- your progress is saved!",
    name_prompt="[bold cyan]What's your name, learner?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "making_reservation": "reservation_master",
        "reading_menu": "menu_reader",
        "ordering_food": "confident_orderer",
        "dietary_needs": "dietary_advocate",
        "paying_tipping": "graceful_payer",
    },
    achievements={
        "reservation_master":   ("Reservation Master", "Books a table at any Spanish restaurant with ease!"),
        "menu_reader":          ("Menu Reader", "Decodes any Spanish menu like a local!"),
        "confident_orderer":    ("Confident Orderer", "Orders a full meal politely and naturally in Spanish!"),
        "dietary_advocate":     ("Dietary Advocate", "Communicates allergies and dietary needs clearly in Spanish!"),
        "graceful_payer":       ("Graceful Payer", "Handles the bill, payment, and tipping like a pro!"),
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
