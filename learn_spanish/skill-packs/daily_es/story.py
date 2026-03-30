"""
story.py — Narrative for the Daily Life skill pack.

Sofia guides you through everyday Spanish vocabulary for routines, hobbies, and more.
"""

INTRO_STORY = """
[bold red]LEARN SPANISH[/bold red]
[bold yellow]Chapter: La Vida Diaria[/bold yellow]

Sofia pulled out a day planner filled with colorful
notes, stickers, and little drawings of suns, clouds,
and shopping bags.

[bold cyan]"This is where language really comes alive,"[/bold cyan] Sofia said,
flipping through the pages. [bold cyan]"Every single day, you wake up,
get ready, go to work or school, enjoy hobbies, check the
weather, go shopping, and take care of your health.
These are the words you'll use EVERY day."[/bold cyan]

She tapped a page showing a morning routine.

[bold cyan]"Reflexive verbs, weather expressions, body parts,
shopping phrases -- this is practical, real-world Spanish
that you'll use from day one. No more textbook phrases --
this is how real people talk about real life."[/bold cyan]

[bold white]Learn the Spanish of everyday life.[/bold white]
"""

ZONE_INTROS = {
    "morning_routine": """
Sofia drew a sunrise and an alarm clock.

[bold cyan]"Every day starts the same way,"[/bold cyan] Sofia said.
[bold cyan]"Levantarse, ducharse, vestirse, desayunar --
these are reflexive verbs, and they're the backbone
of talking about your daily routine. The 'se' at the end
means you do the action to yourself."[/bold cyan]

[bold white]Let's learn your morning routine in Spanish![/bold white]
""",
    "school_work": """
Sofia drew a school and an office building.

[bold cyan]"Where do you spend your day?"[/bold cyan] Sofia asked.
[bold cyan]"Escuela, trabajo, clase, oficina -- whether you're
a student or a professional, you need these words.
Plus the verbs: estudiar, aprender, trabajar, ensenar."[/bold cyan]

[bold white]Let's learn school and work vocabulary![/bold white]
""",
    "hobbies": """
Sofia spread out cards showing various activities.

[bold cyan]"What do you do for fun?"[/bold cyan] Sofia asked with a grin.
[bold cyan]"Leer, bailar, cantar, cocinar, jugar, nadar --
hobbies are the perfect conversation topic. Everyone
loves talking about what they enjoy!"[/bold cyan]

[bold white]Let's learn hobby vocabulary![/bold white]
""",
    "weather": """
Sofia looked out the window at the sky.

[bold cyan]"Que tiempo hace?"[/bold cyan] Sofia asked.
[bold cyan]"Weather is universal small talk. In Spanish,
we use 'hacer' (to make/do) for most weather expressions.
'Hace calor' -- it makes heat. 'Hace frio' -- it makes cold.
It's different from English but very logical."[/bold cyan]

[bold white]Let's talk about the weather![/bold white]
""",
    "shopping": """
Sofia held up shopping bags and a wallet.

[bold cyan]"Let's go shopping!"[/bold cyan] Sofia said.
[bold cyan]"Tienda, comprar, precio, barato, caro --
whether you're at a market, a mall, or a small shop,
you need these words. And the all-important question:
'Cuanto cuesta?' -- How much does it cost?"[/bold cyan]

[bold white]Let's learn shopping vocabulary![/bold white]
""",
    "body_health": """
Sofia pointed to a diagram of the human body.

[bold cyan]"Knowing body parts is essential,"[/bold cyan] Sofia said.
[bold cyan]"Not just for health emergencies, but for everyday life.
'Me duele la cabeza' -- my head hurts. 'Tengo dolor de
estomago' -- I have a stomachache. These phrases
will serve you well."[/bold cyan]

[bold white]Let's learn body and health vocabulary![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "morning_routine": """
[bold green]Sofia set an alarm clock and gave a thumbs up![/bold green]

[bold cyan]"You can describe your entire morning routine in Spanish!
Levantarse, ducharse, vestirse, desayunar -- and you understand
reflexive verbs. That's a huge milestone. Buenos dias, indeed!"[/bold cyan]
""",
    "school_work": """
[bold green]Sofia handed you a gold star sticker![/bold green]

[bold cyan]"School and work vocabulary -- mastered! Escuela, trabajo,
estudiar, aprender -- you can talk about your daily life
as a student or professional. Knowledge is power!"[/bold cyan]
""",
    "hobbies": """
[bold green]Sofia did a little dance of celebration![/bold green]

[bold cyan]"You can talk about all your hobbies! Reading, dancing,
singing, cooking, playing, swimming -- the fun stuff that
makes life worth living. Now conversations will flow
naturally when people ask 'Que te gusta hacer?'"[/bold cyan]
""",
    "weather": """
[bold green]Sofia opened an umbrella and twirled it![/bold green]

[bold cyan]"Rain or shine, hot or cold -- you can talk about the weather!
'Hace calor,' 'hace frio,' 'llueve,' 'nieva' -- small talk
in Spanish just got a lot easier. Que buen tiempo!"[/bold cyan]
""",
    "shopping": """
[bold green]Sofia held up bags full of great deals![/bold green]

[bold cyan]"You're a shopping pro! You can ask prices, compare items,
and navigate any store. 'Cuanto cuesta?' rolls off your tongue.
The markets of the Spanish-speaking world await you!"[/bold cyan]
""",
    "body_health": """
[bold green]Sofia gave you a clean bill of health![/bold green]

[bold cyan]"Body parts, symptoms, and health phrases -- all mastered!
You can describe how you feel, tell a doctor what hurts,
and understand basic health vocabulary. Salud!"[/bold cyan]
""",
}

BOSS_INTROS = {
    "morning_routine": """
Sofia described a busy morning with complications.

[bold cyan]"Describe your morning from alarm to leaving the house.
But the shower is cold, you can't find your clothes,
and you're running late. Handle it all in Spanish!"[/bold cyan]
""",
    "school_work": """
Sofia set up a mock job interview scenario.

[bold cyan]"Tell me about your work or school in Spanish.
What do you do? Where? What subjects or tasks?
Show me you can talk about your daily professional life!"[/bold cyan]
""",
    "hobbies": """
Sofia asked rapid-fire questions about free time.

[bold cyan]"What do you like? What do you do on weekends?
What's your favorite hobby? Answer everything
in Spanish -- natural and flowing!"[/bold cyan]
""",
    "weather": """
Sofia showed photos of extreme weather conditions.

[bold cyan]"Describe the weather in each photo!
Blazing sun, pouring rain, heavy snow, perfect spring day --
give me the complete weather report in Spanish!"[/bold cyan]
""",
    "shopping": """
Sofia set up a market stall with price tags.

[bold cyan]"You're at a market. Ask prices, compare items,
say something is too expensive, and negotiate.
Show me your shopping skills in Spanish!"[/bold cyan]
""",
    "body_health": """
Sofia played a doctor in a medical office.

[bold cyan]"You're at the doctor. Describe your symptoms --
head hurts, stomach aches, you feel dizzy.
Can you communicate your health needs clearly?"[/bold cyan]
""",
}
