"""
Home & Housing skill pack -- Home & Housing
Teaches Spanish home vocabulary: rooms, furniture, chores,
descriptions, and renting & moving.
Guided by Señora Carmen in a charming neighborhood at sunset.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  _   _                         ___    _   _                 _
 | | | | ___  _ __ ___   ___   ( _ )  | | | | ___  _   _ ___(_)_ __   __ _
 | |_| |/ _ \| '_ ` _ \ / _ \  / _ \  | |_| |/ _ \| | | / __| | '_ \ / _` |
 |  _  | (_) | | | | | |  __/ | (_) | |  _  | (_) | |_| \__ \ | | | | (_| |
 |_| |_|\___/|_| |_| |_|\___|  \___/  |_| |_|\___/ \__,_|___/_|_| |_|\__, |
                                                                      |___/
"""

SKILL_PACK = SkillPack(
    id="home_es",
    title="Home & Housing",
    subtitle="Name rooms, describe furniture, talk about chores, and rent an apartment in Spanish",
    save_file_name="home_es_quest",
    intro_story=INTRO_STORY,
    quit_message="Señora Carmen waves from the balcony. ¡Tu hogar te espera -- your progress is saved!",
    name_prompt="[bold cyan]What's your name, learner?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "rooms_of_the_house": "room_navigator",
        "furniture_objects": "furniture_master",
        "household_chores": "chore_champion",
        "describing_your_home": "description_artist",
        "renting_moving": "rental_ready",
    },
    achievements={
        "room_navigator":     ("Room Navigator", "Names every room in the house without hesitation!"),
        "furniture_master":   ("Furniture Master", "Identifies all household furniture and objects in Spanish!"),
        "chore_champion":     ("Chore Champion", "Describes a full cleaning routine in Spanish!"),
        "description_artist": ("Description Artist", "Paints vivid pictures of homes with Spanish adjectives!"),
        "rental_ready":       ("Rental Ready", "Navigates apartment hunting and renting entirely in Spanish!"),
        "no_hints":           ("Solo Learner", "Completed a zone without any hints!"),
        "speed_reader":       ("Quick Thinker", "Answered a question in under 10 seconds!"),
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
