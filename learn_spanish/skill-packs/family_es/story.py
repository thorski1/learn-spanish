"""
story.py — Narrative for the Family skill pack.

Sofia guides you through family vocabulary, descriptions, home, and relationships.
"""

INTRO_STORY = """
[bold red]LEARN SPANISH[/bold red]
[bold yellow]Chapter: Mi Familia[/bold yellow]

Sofia pulled out a leather-bound photo album and set it
on the cafe table. Inside were photos of a large, happy
family gathered around tables, celebrating birthdays,
and posing in front of colorful houses.

[bold cyan]"Family is everything in Spanish-speaking cultures,"[/bold cyan]
Sofia said, turning the pages with care.
[bold cyan]"La familia is the center of social life. Extended families
stay close, grandparents often live nearby or in the same house,
and Sunday dinners can have 20 people at the table."[/bold cyan]

She pointed to a group photo.

[bold cyan]"Let's learn to talk about everyone -- parents, siblings,
grandparents, cousins. Then we'll describe people,
tour the house, meet the pets, and talk about all the
relationships that fill our lives."[/bold cyan]

[bold white]Explore the world of family and home in Spanish.[/bold white]
"""

ZONE_INTROS = {
    "immediate_family": """
Sofia pointed to the center of the family photo.

[bold cyan]"Let's start with the people closest to you,"[/bold cyan]
Sofia said. [bold cyan]"Padre, madre, hermano, hermana, hijo, hija --
these are the words for your immediate family.
Notice how Spanish has different words for male and female
family members -- it's very specific!"[/bold cyan]

[bold white]Let's learn immediate family vocabulary![/bold white]
""",
    "extended_family": """
Sofia spread the family tree across the table.

[bold cyan]"Now let's go wider,"[/bold cyan] Sofia said.
[bold cyan]"Abuelo, abuela, tio, tia, primo, prima -- the extended
family is huge in Spanish-speaking cultures. Family reunions
can have dozens of people, and everyone knows exactly
how they're related!"[/bold cyan]

[bold white]Let's explore the extended family![/bold white]
""",
    "descriptions": """
Sofia held up photos of different people.

[bold cyan]"How do you describe someone?"[/bold cyan] Sofia asked.
[bold cyan]"Alto or bajo? Joven or viejo? Guapo or feo?
Spanish has rich vocabulary for describing people --
their appearance, personality, and character.
And remember, adjectives need to agree in gender!"[/bold cyan]

[bold white]Let's learn to describe people in Spanish![/bold white]
""",
    "house_rooms": """
Sofia sketched a floor plan on a napkin.

[bold cyan]"Let's take a tour of a Spanish-speaking home,"[/bold cyan]
Sofia said, drawing rooms. [bold cyan]"La cocina, el bano,
el dormitorio, la sala, el jardin -- every room has
its name. And homes in different countries can look
very different!"[/bold cyan]

[bold white]Let's explore the rooms of a house![/bold white]
""",
    "pets": """
Sofia showed a photo of a family with their pets.

[bold cyan]"Mascotas!"[/bold cyan] Sofia said with a smile.
[bold cyan]"Perro, gato, pez, pajaro -- pets are family members too!
Let's learn the names of common pets and the vocabulary
around taking care of them."[/bold cyan]

[bold white]Let's learn about pets in Spanish![/bold white]
""",
    "relationships": """
Sofia opened to a page showing people in various social situations.

[bold cyan]"Beyond family, there are so many important relationships,"[/bold cyan]
Sofia explained. [bold cyan]"Amigo, novio, vecino, companero --
each word carries a specific meaning. And in Spanish,
the way you describe a relationship tells a lot about
how close people are."[/bold cyan]

[bold white]Let's learn relationship vocabulary![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "immediate_family": """
[bold green]Sofia placed a golden frame around the family photo![/bold green]

[bold cyan]"Padre, madre, hermano, hermana, hijo, hija -- you know them all!
You can now talk about your immediate family in Spanish.
That's the inner circle, and you've mastered it."[/bold cyan]
""",
    "extended_family": """
[bold green]Sofia drew a complete family tree and stepped back to admire it![/bold green]

[bold cyan]"The entire family tree is yours! Abuelos, tios, primos --
you can trace every branch. In Spanish-speaking families,
knowing these relationships is essential for every gathering."[/bold cyan]
""",
    "descriptions": """
[bold green]Sofia held up a perfect portrait sketch![/bold green]

[bold cyan]"You can describe anyone! Tall, short, young, old, friendly,
serious -- and you know how to make every adjective agree.
You paint pictures with words now. Que talento!"[/bold cyan]
""",
    "house_rooms": """
[bold green]Sofia completed the floor plan with a flourish![/bold green]

[bold cyan]"Every room in the house -- named and described! From la cocina
to el jardin, you can give a full house tour in Spanish.
Bienvenidos a mi casa!"[/bold cyan]
""",
    "pets": """
[bold green]Sofia made adorable animal sounds![/bold green]

[bold cyan]"Perro, gato, pez, pajaro, conejo -- you know all the pets!
Animals bring joy to every family, and now you can talk
about your mascotas in Spanish. Guau guau!"[/bold cyan]
""",
    "relationships": """
[bold green]Sofia drew a web of connected hearts![/bold green]

[bold cyan]"Friends, partners, neighbors, classmates -- you understand
every relationship word. People are the heart of language,
and now you can describe every connection. Maravilloso!"[/bold cyan]
""",
}

BOSS_INTROS = {
    "immediate_family": """
Sofia held up a family photo with labels removed.

[bold cyan]"Name every family member! I'll describe the relationship
and you give me the Spanish word. Mother, father, brother,
sister, son, daughter -- plus the tricky plurals!"[/bold cyan]
""",
    "extended_family": """
Sofia drew a complex family tree with blank labels.

[bold cyan]"Fill in the family tree! I'll give you relationship clues
and you name them in Spanish. Grandmother, uncle, cousin --
the extended family challenge is here!"[/bold cyan]
""",
    "descriptions": """
Sofia described several people in detail.

[bold cyan]"I'll describe someone. You pick the right Spanish words.
Remember -- gender agreement, personality AND appearance.
Can you paint a complete portrait in Spanish?"[/bold cyan]
""",
    "house_rooms": """
Sofia described activities and you name the room.

[bold cyan]"Where do you cook? Where do you sleep? Where do you shower?
I'll describe what happens in each room, and you name it
in Spanish. Give me the full house tour!"[/bold cyan]
""",
    "pets": """
Sofia played animal sounds and showed silhouettes.

[bold cyan]"What animal is this? Match the sound, the description,
and the Spanish name. From perro to conejo --
can you identify them all?"[/bold cyan]
""",
    "relationships": """
Sofia described social scenarios.

[bold cyan]"Your mother's brother is your...? Your friend's friend is your...?
I'll give you relationship puzzles and you give me
the Spanish word. Show me you know the social web!"[/bold cyan]
""",
}
