"""
Food skill pack — La Cocina Espanola
Teaches food vocabulary, ordering at restaurants, cooking, and food culture.
Guided by Sofia, a warm and encouraging Spanish teacher.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  _____ ___   ___  ____
 |  ___/ _ \ / _ \|  _ \
 | |_ | | | | | | | | | |
 |  _|| |_| | |_| | |_| |
 |_|   \___/ \___/|____/
"""

SKILL_PACK = SkillPack(
    id="food_es",
    title="La Cocina Espanola",
    subtitle="Food, drinks, restaurants, and culinary culture",
    save_file_name="food_es_quest",
    intro_story=INTRO_STORY,
    quit_message="Sofia folds the menu. Your progress is saved -- buen provecho for next time!",
    name_prompt="[bold cyan]What's your name, learner?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "fruits_vegetables": "produce_expert",
        "drinks": "drink_master",
        "meals": "meal_planner",
        "ordering": "restaurant_pro",
        "cooking": "kitchen_chef",
        "food_culture": "food_explorer",
    },
    achievements={
        "produce_expert":   ("Produce Expert", "Named every fruit and vegetable in Spanish!"),
        "drink_master":     ("Drink Master", "Knows every beverage from agua to vino!"),
        "meal_planner":     ("Meal Planner", "Understands desayuno, almuerzo, cena, and merienda!"),
        "restaurant_pro":   ("Restaurant Pro", "Can order food confidently in any Spanish restaurant!"),
        "kitchen_chef":     ("Kitchen Chef", "Mastered cooking verbs and kitchen vocabulary!"),
        "food_explorer":    ("Food Explorer", "Explored culinary traditions across the Spanish-speaking world!"),
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
