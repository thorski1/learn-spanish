"""
story.py — Narrative for the Culture skill pack.

Sofia guides you through the rich cultural tapestry of the Spanish-speaking world.
"""

INTRO_STORY = """
[bold red]LEARN SPANISH[/bold red]
[bold yellow]Chapter: El Mundo Hispanohablante[/bold yellow]

Sofia unrolled an enormous map of the world, dotted with
colorful pins marking countries from Spain to Argentina,
from Mexico to the Philippines.

[bold cyan]"Spanish is spoken by over 500 million people
in more than 20 countries,"[/bold cyan] Sofia said, her eyes bright.
[bold cyan]"It's the second most spoken native language in the world.
But it's not just a language -- it's a doorway to an
incredible tapestry of cultures, traditions, music,
art, and history."[/bold cyan]

She pointed to different pins on the map.

[bold cyan]"From the flamenco of Spain to the tango of Argentina,
from the Day of the Dead in Mexico to the carnivals
of Colombia, from Frida Kahlo to Gabriel Garcia Marquez --
the Spanish-speaking world is endlessly fascinating.
And understanding the culture makes your Spanish
come alive in ways a textbook never could."[/bold cyan]

[bold white]Explore the incredible diversity of the Spanish-speaking world.[/bold white]
"""

ZONE_INTROS = {
    "spanish_countries": """
Sofia highlighted countries on the map one by one.

[bold cyan]"Did you know there are over 20 countries where Spanish
is the official language?"[/bold cyan] Sofia asked.
[bold cyan]"From Spain in Europe to 18 countries in the Americas,
plus Equatorial Guinea in Africa. Each one has its own
accent, slang, food, and identity -- but they all
share this beautiful language."[/bold cyan]

[bold white]Let's explore the Spanish-speaking world![/bold white]
""",
    "festivals": """
Sofia pulled out photos of colorful celebrations.

[bold cyan]"Spanish-speaking cultures know how to celebrate!"[/bold cyan]
Sofia said with a grin. [bold cyan]"The Day of the Dead, La Tomatina,
the Running of the Bulls, Carnival -- every festival tells
a story about the people who celebrate it.
Let's explore the most famous ones!"[/bold cyan]

[bold white]Let's discover Spanish-speaking world festivals![/bold white]
""",
    "music_dance": """
Sofia played a clip of salsa music and swayed to the rhythm.

[bold cyan]"Music and dance are the soul of Spanish-speaking cultures,"[/bold cyan]
Sofia said. [bold cyan]"Salsa from the Caribbean, flamenco from Spain,
tango from Argentina, reggaeton from Puerto Rico,
mariachi from Mexico -- each genre tells a story
and connects to a place."[/bold cyan]

[bold white]Let's explore music and dance![/bold white]
""",
    "famous_people": """
Sofia displayed portraits of iconic Spanish-speaking figures.

[bold cyan]"The Spanish-speaking world has produced some of the most
influential artists, writers, scientists, and athletes
in history,"[/bold cyan] Sofia said. [bold cyan]"Frida Kahlo, Gabriel Garcia
Marquez, Pablo Picasso, Lionel Messi -- their contributions
have shaped the entire world."[/bold cyan]

[bold white]Let's learn about famous Spanish-speaking figures![/bold white]
""",
    "traditions": """
Sofia set up a miniature scene of a family celebration.

[bold cyan]"Beyond the big festivals, everyday traditions define
Spanish-speaking cultures,"[/bold cyan] Sofia explained.
[bold cyan]"The siesta, the quinceanera, the tradition of eating
12 grapes at midnight on New Year's Eve -- these customs
give you insight into how people live and think."[/bold cyan]

[bold white]Let's explore cultural traditions![/bold white]
""",
    "spanish_vs_latin": """
Sofia drew a line between Spain and Latin America on the map.

[bold cyan]"Here's where it gets really interesting,"[/bold cyan] Sofia said.
[bold cyan]"Spanish from Spain and Spanish from Latin America
are the same language, but with fascinating differences.
Vocabulary, pronunciation, grammar -- there are patterns
to the differences that help you understand both."[/bold cyan]

[bold white]Let's compare Spain and Latin American Spanish![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "spanish_countries": """
[bold green]Sofia placed the final pin on the map![/bold green]

[bold cyan]"You know all the Spanish-speaking countries! From Mexico to
Argentina, from Spain to Equatorial Guinea. Each one is unique,
but they're all connected by this incredible language.
The world just got a lot bigger for you!"[/bold cyan]
""",
    "festivals": """
[bold green]Sofia threw confetti in celebration![/bold green]

[bold cyan]"Dia de los Muertos, La Tomatina, San Fermin, Carnaval --
you've explored the most vibrant celebrations in the
Spanish-speaking world. Culture is what makes language
come alive. Que viva la fiesta!"[/bold cyan]
""",
    "music_dance": """
[bold green]Sofia danced a quick salsa step![/bold green]

[bold cyan]"Salsa, flamenco, tango, reggaeton, mariachi -- you know them all!
Music and dance are windows into the soul of a culture.
Now when you hear these rhythms, you understand the
stories behind them. Olé!"[/bold cyan]
""",
    "famous_people": """
[bold green]Sofia created a wall of fame with all the figures you learned about![/bold green]

[bold cyan]"Frida, Marquez, Messi, Picasso, Neruda -- you know the giants
of the Spanish-speaking world. Their art, writing, and achievements
inspire millions. And now you can talk about them in Spanish!"[/bold cyan]
""",
    "traditions": """
[bold green]Sofia lit a candle for tradition![/bold green]

[bold cyan]"Siesta, quinceañera, Nochevieja grapes, sobremesa --
you understand the traditions that shape daily life.
These customs are the heart of Spanish-speaking cultures.
Respecting them shows you truly understand the language."[/bold cyan]
""",
    "spanish_vs_latin": """
[bold green]Sofia drew a bridge connecting Spain and Latin America![/bold green]

[bold cyan]"You can spot the differences between Spain and Latin American
Spanish! Vosotros vs ustedes, coger vs tomar, vale vs dale --
this awareness makes you a more sophisticated speaker.
You understand not just Spanish, but all its beautiful varieties!"[/bold cyan]
""",
}

BOSS_INTROS = {
    "spanish_countries": """
Sofia covered the map and tested from memory.

[bold cyan]"Name the countries! Match capitals! Tell me which
continent they're on! I'll test your knowledge of
every corner of the Spanish-speaking world!"[/bold cyan]
""",
    "festivals": """
Sofia described celebrations without naming them.

[bold cyan]"I'll describe a festival -- you name it and tell me
which country it comes from. Colors, traditions, dates --
show me you know the celebrations of the Hispanic world!"[/bold cyan]
""",
    "music_dance": """
Sofia described musical styles without naming them.

[bold cyan]"I'll describe the rhythm, the instruments, the movement.
You tell me the genre and where it comes from.
Can you identify every musical tradition?"[/bold cyan]
""",
    "famous_people": """
Sofia described achievements without naming the person.

[bold cyan]"I'll describe what they did -- you tell me who they are.
Painters, writers, athletes, scientists -- the greatest
figures of the Spanish-speaking world. Who's who?"[/bold cyan]
""",
    "traditions": """
Sofia described customs and asked you to explain them.

[bold cyan]"What's a quinceañera? Why do they eat grapes on New Year's?
What is sobremesa? I want the cultural context --
show me you truly understand these traditions!"[/bold cyan]
""",
    "spanish_vs_latin": """
Sofia gave you phrases and asked which variety they belong to.

[bold cyan]"Spain or Latin America? I'll give you vocabulary,
pronunciation patterns, and grammar differences.
Can you identify the origin of each?"[/bold cyan]
""",
}
