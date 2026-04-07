"""
story.py -- Narrative for the Home & Housing skill pack.

Señora Carmen guides you through a beautiful Spanish neighborhood at sunset,
teaching vocabulary for rooms, furniture, chores, descriptions, and renting.
"""

INTRO_STORY = """
[bold red]LEARN SPANISH[/bold red]
[bold yellow]Chapter: Home & Housing[/bold yellow]

Golden light poured through the arched windows
of a charming townhouse perched above the city,
the sunset painting terracotta rooftops in shades
of amber and rose. A warm breeze carried the scent
of jasmine through the open balcony doors.

[bold cyan]"Bienvenido a mi barrio,"[/bold cyan] said Señora Carmen,
stepping onto the tiled terrace with a welcoming smile
and a ring of old brass keys in her hand.
Her warmth was immediate -- the kind of person
who makes any place feel like home.
[bold cyan]"I've been helping people find their perfect
home in this city for fifteen years,
and I'll tell you something -- knowing how to talk
about a house in another language
opens doors everywhere."[/bold cyan]

She gestured to the sun-drenched street below,
where balconies overflowed with geraniums.
[bold yellow]"La sala, la cocina, el dormitorio...
Let's start with the rooms."[/bold yellow]

[bold cyan]"By the time we're done, you'll know how to
name every room, describe your furniture,
talk about chores, describe your dream home,
and even rent an apartment --
all in Spanish. Ready for the tour?"[/bold cyan]

[bold white]Learn to talk about home and housing in Spanish.[/bold white]
"""

ZONE_INTROS = {
    "rooms_of_the_house": """
Señora Carmen opened the front door wide,
the warm sunset light flooding the entrance hall.

[bold cyan]"Every home has its rooms,"[/bold cyan]
she said, gesturing down the hallway.
[bold cyan]"Kitchen, living room, bedroom, bathroom --
if you can name them, you can navigate
any house, any listing, any conversation
about where you live."[/bold cyan]

[bold white]Let's learn the rooms of the house in Spanish![/bold white]
""",
    "furniture_objects": """
Señora Carmen ran her hand along a polished
wooden table, the sunset light catching its grain.

[bold cyan]"A room is just four walls without furniture,"[/bold cyan]
she said, settling into an armchair.
[bold cyan]"Tables, chairs, beds, sofas, lamps --
these are the things that make a house a home.
Let me teach you what to call them."[/bold cyan]

[bold white]Let's learn furniture and household objects in Spanish![/bold white]
""",
    "household_chores": """
Señora Carmen picked up a broom leaning
against the kitchen wall and gave it a playful twirl.

[bold cyan]"A beautiful home needs care,"[/bold cyan] she laughed,
setting the broom down.
[bold cyan]"Cleaning, cooking, washing, sweeping --
everyone has chores. And being able to talk
about them in Spanish? That's everyday life.
Let's get to work."[/bold cyan]

[bold white]Let's learn household chores in Spanish![/bold white]
""",
    "describing_your_home": """
Señora Carmen leaned on the balcony railing
as the sky turned from gold to soft purple.

[bold cyan]"Now comes the fun part,"[/bold cyan] she said,
her eyes bright with enthusiasm.
[bold cyan]"Big or small, new or old, pretty or plain --
adjectives bring a home to life.
Whether you're describing your place to a friend
or reading a listing, these words are essential."[/bold cyan]

[bold white]Let's learn to describe your home in Spanish![/bold white]
""",
    "renting_moving": """
Señora Carmen held up a set of keys,
the last rays of sunset glinting off the metal.

[bold cyan]"This is where it all comes together,"[/bold cyan]
she said, her voice turning practical.
[bold cyan]"Renting, contracts, deposits, neighbors --
the real-world vocabulary you need
to find a place and make it yours.
In any Spanish-speaking city."[/bold cyan]

[bold white]Let's learn about renting and moving in Spanish![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "rooms_of_the_house": """
[bold green]Señora Carmen clapped her hands in delight![/bold green]

[bold cyan]"Sala, cocina, dormitorio, baño, comedor --
you know every room in the house!
Now you can give a tour, follow directions,
and understand any floor plan.
Welcome home."[/bold cyan]
""",
    "furniture_objects": """
[bold green]Señora Carmen patted the sofa cushion proudly![/bold green]

[bold cyan]"Mesa, silla, cama, sofá, lámpara --
you've furnished the whole house with words!
Now you can describe what's in any room,
shop for furniture, and make
a space truly yours."[/bold cyan]
""",
    "household_chores": """
[bold green]Señora Carmen hung up the apron with a satisfied smile![/bold green]

[bold cyan]"Limpiar, cocinar, lavar, barrer, planchar --
you've mastered the language of keeping
a home running. Not the most glamorous
vocabulary, but absolutely the most
useful in daily life."[/bold cyan]
""",
    "describing_your_home": """
[bold green]Señora Carmen gazed at the twilight skyline![/bold green]

[bold cyan]"Grande, pequeño, nuevo, viejo, bonito --
you paint pictures with adjectives now.
You can describe any home, any neighborhood,
any room with color and detail.
That's real communication."[/bold cyan]
""",
    "renting_moving": """
[bold green]Señora Carmen handed you the keys with a warm handshake![/bold green]

[bold cyan]"Alquilar, mudarse, contrato, fianza, vecino --
you're ready to find a home in any
Spanish-speaking city. From room names
to rental contracts, you've learned it all.
¡Bienvenido a tu nuevo hogar!"[/bold cyan]
""",
}

BOSS_INTROS = {
    "rooms_of_the_house": """
Señora Carmen stood at the foot of the stairs.

[bold cyan]"A friend is visiting your home for the
first time. Can you give them a proper tour --
naming each room and where it is?
Show me you know the whole house."[/bold cyan]
""",
    "furniture_objects": """
Señora Carmen gestured around the empty room.

[bold cyan]"Picture your perfect living room.
Can you describe everything in it --
every piece of furniture, where it goes?
Fill this room with words."[/bold cyan]
""",
    "household_chores": """
Señora Carmen looked at the Saturday to-do list.

[bold cyan]"It's cleaning day and there's a lot to do.
Can you plan out all the chores --
in order, start to finish?
Show me a full cleaning routine."[/bold cyan]
""",
    "describing_your_home": """
Señora Carmen pulled out a blank listing form.

[bold cyan]"You're putting your home on the market.
Can you write the perfect description --
size, light, rooms, neighborhood?
Make someone fall in love with it."[/bold cyan]
""",
    "renting_moving": """
Señora Carmen opened the door to a rental apartment.

[bold cyan]"You're face to face with the landlord.
Rent, deposit, utilities, move-in date --
can you ask all the right questions
to seal the deal? This is the real test."[/bold cyan]
""",
}
