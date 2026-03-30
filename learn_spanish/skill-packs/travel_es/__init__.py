"""
Travel skill pack — Viajando por el Mundo
Teaches transportation, directions, hotels, airports, and emergency phrases.
Guided by Sofia, a warm and encouraging Spanish teacher.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 __     ___    _    _ _____
 \ \   / / \  | |  | | ____|
  \ \ / / _ \ | |  | |  _|
   \ V / ___ \| |__| | |___
    \_/_/   \_\____/|_____|
"""

SKILL_PACK = SkillPack(
    id="travel_es",
    title="Viajando por el Mundo",
    subtitle="Navigate transportation, hotels, directions, and emergencies",
    save_file_name="travel_es_quest",
    intro_story=INTRO_STORY,
    quit_message="Sofia folds the map. Your progress is saved -- buen viaje when you return!",
    name_prompt="[bold cyan]What's your name, learner?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "transportation": "road_warrior",
        "directions": "compass_master",
        "hotel": "hotel_guest",
        "asking_directions": "pathfinder",
        "airport": "jet_setter",
        "emergencies": "safety_first",
    },
    achievements={
        "road_warrior":    ("Road Warrior", "Knows every mode of transportation in Spanish!"),
        "compass_master":  ("Compass Master", "Mastered left, right, straight, and all cardinal directions!"),
        "hotel_guest":     ("Hotel Guest", "Can check in, ask about amenities, and navigate any hotel!"),
        "pathfinder":      ("Pathfinder", "Can ask for and understand directions in Spanish!"),
        "jet_setter":      ("Jet Setter", "Navigates airports like a seasoned traveler!"),
        "safety_first":    ("Safety First", "Knows essential emergency phrases in Spanish!"),
        "no_hints":        ("Solo Learner", "Completed a zone without any hints!"),
        "speed_reader":    ("Quick Thinker", "Answered a question in under 10 seconds!"),
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
