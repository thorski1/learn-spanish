"""
story.py — Narrative for the Getting Around skill pack.

Elena guides you through a Spanish city at sunset, teaching vocabulary
for directions, places, asking for help, transportation, and describing locations.
"""

INTRO_STORY = """
[bold red]LEARN SPANISH[/bold red]
[bold yellow]Chapter: Getting Around[/bold yellow]

The sun hung low over the terracotta rooftops,
casting long golden shadows across the cobblestone streets.
Church bells echoed in the distance as the city
settled into the warm glow of evening.

[bold cyan]"Bienvenido a la ciudad,"[/bold cyan] said Elena,
adjusting the brim of her sun hat as she stepped
out from beneath a jasmine-covered archway.
Her eyes sparkled with the easy confidence
of someone who knew every alley and shortcut by heart.
[bold cyan]"I've been giving walking tours here
for fifteen years, and I can tell you --
the real adventure starts when you can find
your own way."[/bold cyan]

She pointed down a winding street where the sunset
painted the old stone walls in shades of copper and rose.
[bold yellow]"Siga todo recto... luego gire a la izquierda.
That's how every journey begins."[/bold yellow]

[bold cyan]"By the time the stars come out, you'll know
how to ask for directions, catch a bus,
describe any location, and navigate
this city like a local. Ready to explore?"[/bold cyan]

[bold white]Learn to navigate any Spanish-speaking city with confidence.[/bold white]
"""

ZONE_INTROS = {
    "basic_directions": """
Elena stopped at a crossroads where four streets met
beneath an old iron street lamp flickering to life.

[bold cyan]"Every journey starts with the basics,"[/bold cyan]
Elena said, gesturing left and right as the sunset
glowed behind her.
[bold cyan]"Izquierda, derecha, recto, girar --
these four words will carry you
through any city in the Spanish-speaking world."[/bold cyan]

[bold white]Let's learn the essential direction words![/bold white]
""",
    "places_in_city": """
Elena led you into a wide plaza where the last rays
of sunlight illuminated a fountain surrounded by shops,
a church, and a row of old buildings.

[bold cyan]"A city is made of places,"[/bold cyan] Elena said,
sweeping her arm across the square.
[bold cyan]"The station, the hospital, the bank, the market --
knowing their names is like having a map
already drawn in your mind."[/bold cyan]

[bold white]Let's learn the names of important city places![/bold white]
""",
    "asking_directions": """
Elena paused beside a map board on the edge of
a busy avenue as the sky turned to deep amber.

[bold cyan]"Knowing words is one thing,"[/bold cyan] Elena said,
tapping the map with her finger.
[bold cyan]"But asking a stranger for help --
politely, clearly, confidently --
that's the real skill. And Spanish speakers
love helping someone who makes the effort."[/bold cyan]

[bold white]Let's learn to ask for and understand directions![/bold white]
""",
    "transportation": """
Elena walked you to a bustling transit hub
where buses hummed and a metro sign glowed
in the fading twilight.

[bold cyan]"You can't always walk,"[/bold cyan] Elena said
with a practical smile as a bus rumbled past.
[bold cyan]"Buses, metros, taxis, trains --
Spanish cities have it all.
And once you know the words,
the whole system opens up to you."[/bold cyan]

[bold white]Let's learn to navigate public transportation in Spanish![/bold white]
""",
    "describing_locations": """
Elena brought you to a rooftop mirador where
the entire city spread out below, its lights
beginning to twinkle against the violet sky.

[bold cyan]"Now for the finishing touch,"[/bold cyan] Elena said,
leaning on the railing as the last sliver of sun
dipped below the horizon.
[bold cyan]"Al lado de, enfrente de, cerca, lejos --
these little phrases let you describe
exactly where anything is.
With these, you'll never be lost again."[/bold cyan]

[bold white]Let's learn to describe locations precisely in Spanish![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "basic_directions": """
[bold green]Elena clapped her hands together with delight![/bold green]

[bold cyan]"Izquierda, derecha, recto, girar --
you've got the foundation!
These four directions will guide you
through any street, any city, any country
where Spanish is spoken. Bien hecho!"[/bold cyan]
""",
    "places_in_city": """
[bold green]Elena gestured proudly across the illuminated plaza![/bold green]

[bold cyan]"Estacion, hospital, banco, supermercado --
you know them all now.
Drop me in any Spanish city and you'll
find everything you need.
The city is no longer a mystery!"[/bold cyan]
""",
    "asking_directions": """
[bold green]Elena gave you an approving nod as a local waved back at you![/bold green]

[bold cyan]"Donde esta, como llego, esta lejos --
you can ask anyone for help now,
politely and clearly.
Spanish speakers will be happy to guide you,
and you'll understand every word they say!"[/bold cyan]
""",
    "transportation": """
[bold green]Elena high-fived you as a metro train whooshed past below![/bold green]

[bold cyan]"Autobus, metro, taxi, billete --
the whole transit system is yours.
You can buy tickets, ask about schedules,
and get anywhere you need to go.
The city is now your playground!"[/bold cyan]
""",
    "describing_locations": """
[bold green]Elena spread her arms wide as the city lights sparkled below![/bold green]

[bold cyan]"Al lado de, enfrente de, cerca, lejos, entre --
you can describe any location with precision.
From rooftop to street corner,
you know exactly how to say where things are.
You'll never be lost in a Spanish city again.
Enhorabuena -- congratulations!"[/bold cyan]
""",
}

BOSS_INTROS = {
    "basic_directions": """
Elena stopped at a corner and turned to you.

[bold cyan]"Someone is lost and needs your help.
Can you give clear, step-by-step directions
using everything you've learned?
Straight, left, right, landmarks --
put it all together."[/bold cyan]
""",
    "places_in_city": """
Elena pointed to a confused tourist studying a map.

[bold cyan]"That traveler needs to find three places.
Can you name them all correctly in Spanish?
Show me you know this city
like the back of your hand."[/bold cyan]
""",
    "asking_directions": """
Elena gestured toward a busy intersection.

[bold cyan]"You're lost and need to find the train station.
Can you ask for directions -- politely,
completely, and with a follow-up question?
Show me the perfect request."[/bold cyan]
""",
    "transportation": """
Elena checked her watch and looked at you.

[bold cyan]"You need to get to the airport.
Can you ask the right questions
to figure out the best way there?
Options, routes, timing -- cover it all."[/bold cyan]
""",
    "describing_locations": """
Elena pulled out her phone to share your hotel location.

[bold cyan]"Describe where your hotel is
using as many location phrases as you can.
Street, landmarks, relative positions --
paint a picture with words.
This is your final challenge."[/bold cyan]
""",
}
