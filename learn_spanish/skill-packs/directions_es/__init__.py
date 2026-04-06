"""
Getting Around skill pack — Getting Around
Teaches Spanish direction and navigation vocabulary: basic directions,
city places, asking for directions, transportation, and describing locations.
Guided by Elena on a walking tour at sunset.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ____      _   _   _                  _                            _
 / ___| ___| |_| |_(_)_ __   __ _    / \   _ __ ___  _   _ _ __  __| |
| |  _ / _ \ __| __| | '_ \ / _` |  / _ \ | '__/ _ \| | | | '_ \/ _` |
| |_| |  __/ |_| |_| | | | | (_| | / ___ \| | | (_) | |_| | | | (_| |
 \____|\___|\__|\__|_|_| |_|\__, |/_/   \_\_|  \___/ \__,_|_| |_|\__,_|
                             |___/
"""

SKILL_PACK = SkillPack(
    id="directions_es",
    title="Getting Around",
    subtitle="Navigate any Spanish-speaking city with confidence",
    save_file_name="directions_es_quest",
    intro_story=INTRO_STORY,
    quit_message="Elena waves from the plaza. Hasta pronto -- your progress is saved!",
    name_prompt="[bold cyan]What's your name, explorer?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "basic_directions": "direction_master",
        "places_in_city": "city_expert",
        "asking_directions": "confident_asker",
        "transportation": "transit_navigator",
        "describing_locations": "location_describer",
    },
    achievements={
        "direction_master":    ("Direction Master", "Knows left, right, straight, and turn like a native!"),
        "city_expert":         ("City Expert", "Can name every important place in a Spanish city!"),
        "confident_asker":     ("Confident Asker", "Asks for directions politely and clearly in Spanish!"),
        "transit_navigator":   ("Transit Navigator", "Navigates buses, metros, and taxis with ease!"),
        "location_describer":  ("Location Describer", "Describes any location with pinpoint precision!"),
        "no_hints":            ("Solo Explorer", "Completed a zone without any hints!"),
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
