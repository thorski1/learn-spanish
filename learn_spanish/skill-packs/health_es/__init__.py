"""
Health & Body skill pack — Health & Body
Teaches Spanish health vocabulary: body parts, feelings, doctor visits,
pharmacy terms, and healthy habits.
Guided by Doctora Elena in a warm clinic at sunset.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  _   _            _ _   _        ___    ____            _
 | | | | ___  __ _| | |_| |__    ( _ )  | __ )  ___   __| |_   _
 | |_| |/ _ \/ _` | | __| '_ \   / _ \  |  _ \ / _ \ / _` | | | |
 |  _  |  __/ (_| | | |_| | | | | (_) | | |_) | (_) | (_| | |_| |
 |_| |_|\___|\__,_|_|\__|_| |_|  \___/  |____/ \___/ \__,_|\__, |
                                                            |___/
"""

SKILL_PACK = SkillPack(
    id="health_es",
    title="Health & Body",
    subtitle="Describe symptoms, visit the doctor, and talk about healthy habits in Spanish",
    save_file_name="health_es_quest",
    intro_story=INTRO_STORY,
    quit_message="Doctora Elena waves from the clinic door. Cuida tu salud -- your progress is saved!",
    name_prompt="[bold cyan]What's your name, learner?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "body_parts": "anatomy_ace",
        "feelings_emotions": "emotion_expert",
        "at_the_doctor": "clinic_confident",
        "pharmacy_medicine": "pharmacy_pro",
        "healthy_habits": "wellness_warrior",
    },
    achievements={
        "anatomy_ace":       ("Anatomy Ace", "Names every body part in Spanish without hesitation!"),
        "emotion_expert":    ("Emotion Expert", "Expresses any feeling naturally in Spanish!"),
        "clinic_confident":  ("Clinic Confident", "Navigates a doctor visit entirely in Spanish!"),
        "pharmacy_pro":      ("Pharmacy Pro", "Gets the right medicine at any Spanish farmacia!"),
        "wellness_warrior":  ("Wellness Warrior", "Talks about healthy habits fluently in Spanish!"),
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
