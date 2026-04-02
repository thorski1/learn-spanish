"""
Colors & Clothing skill pack — Colors & Clothing
Teaches Spanish colors, shades, clothing vocabulary, adjective agreement,
and shopping phrases. Guided by Carmen in a vibrant sunset market.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
   ____      _
  / ___|___ | | ___  _ __ ___  ___
 | |   / _ \| |/ _ \| '__/ _ \/ __|
 | |__| (_) | | (_) | | |  __/\__ \
  \____\___/|_|\___/|_|  \___||___/
"""

SKILL_PACK = SkillPack(
    id="colors_clothing",
    title="Colors & Clothing",
    subtitle="Name colors, describe outfits, and shop for clothes in Spanish",
    save_file_name="colors_clothing_quest",
    intro_story=INTRO_STORY,
    quit_message="Carmen waves from the market. Hasta la proxima -- your progress is saved!",
    name_prompt="[bold cyan]What's your name, learner?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "basic_colors": "color_basics_star",
        "more_colors_shades": "palette_master",
        "clothing_items": "wardrobe_builder",
        "describing_what_you_wear": "fashion_describer",
        "shopping_for_clothes": "market_shopper",
    },
    achievements={
        "color_basics_star":   ("Color Basics Star", "Mastered the six essential Spanish colors!"),
        "palette_master":      ("Palette Master", "Knows every shade from light to dark!"),
        "wardrobe_builder":    ("Wardrobe Builder", "Can name all common clothing items in Spanish!"),
        "fashion_describer":   ("Fashion Describer", "Describes outfits with perfect adjective agreement!"),
        "market_shopper":      ("Market Shopper", "Can shop for clothes like a local in any mercado!"),
        "no_hints":            ("Solo Learner", "Completed a zone without any hints!"),
        "speed_reader":        ("Quick Thinker", "Answered a question in under 10 seconds!"),
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
