"""
story.py — Narrative for the Travel skill pack.

Sofia guides you through travel vocabulary for getting around in Spanish-speaking countries.
"""

INTRO_STORY = """
[bold red]LEARN SPANISH[/bold red]
[bold yellow]Chapter: Viajando por el Mundo[/bold yellow]

Sofia unfolded a large, colorful map across the table,
covered with routes connecting cities across Spain,
Mexico, Colombia, Argentina, and beyond.

[bold cyan]"Traveling is the ultimate test of your Spanish,"[/bold cyan]
Sofia said, tracing a route with her finger.
[bold cyan]"You need to buy tickets, ask for directions,
check into hotels, navigate airports, and -- hopefully
never, but just in case -- handle emergencies.
These are the phrases that turn a tourist into a traveler."[/bold cyan]

She pointed to different cities on the map.

[bold cyan]"From the metro in Madrid to the colectivos in Buenos Aires,
from beach hotels in Cancun to hostels in Bogota --
every situation has its own vocabulary.
Let's make sure you're ready for all of them."[/bold cyan]

[bold white]Prepare for your Spanish-speaking adventure.[/bold white]
"""

ZONE_INTROS = {
    "transportation": """
Sofia pointed to different vehicles on the map.

[bold cyan]"How do you get around?"[/bold cyan] Sofia asked.
[bold cyan]"Avion, tren, autobus, taxi, bicicleta, a pie --
every mode of transportation has its name.
And the vocabulary varies by country! A 'bus' can be
autobus, camion, colectivo, guagua, or micro
depending on where you are."[/bold cyan]

[bold white]Let's learn transportation vocabulary![/bold white]
""",
    "directions": """
Sofia held up a compass and a simple map.

[bold cyan]"Izquierda, derecha, recto,"[/bold cyan] Sofia said, pointing in each direction.
[bold cyan]"Knowing directions is essential. Whether a local is
guiding you to a restaurant or you're reading a map,
you need these words. Plus the cardinal directions --
norte, sur, este, oeste."[/bold cyan]

[bold white]Let's master directions in Spanish![/bold white]
""",
    "hotel": """
Sofia walked up to an imaginary hotel reception desk.

[bold cyan]"Checking into a hotel is a rite of passage,"[/bold cyan]
Sofia said with a smile. [bold cyan]"Habitacion, llave,
recepcion -- and the all-important question:
'Tiene wifi?' Every traveler needs hotel vocabulary."[/bold cyan]

[bold white]Let's learn hotel vocabulary![/bold white]
""",
    "asking_directions": """
Sofia stood at a crossroads on the map.

[bold cyan]"You're lost in a new city. What do you do?"[/bold cyan]
Sofia asked. [bold cyan]"You ask for directions!
'Donde esta...?', 'Como llego a...?' -- these phrases
will save you every time. And you need to understand
the answers: cerca, lejos, al lado de, enfrente de."[/bold cyan]

[bold white]Let's learn to ask for and understand directions![/bold white]
""",
    "airport": """
Sofia pulled out a mock boarding pass.

[bold cyan]"The airport has its own language,"[/bold cyan] Sofia said.
[bold cyan]"Pasaporte, equipaje, vuelo, puerta de embarque,
tarjeta de embarque -- these words are everywhere
in any Spanish-speaking airport. Let's make sure
you breeze through."[/bold cyan]

[bold white]Let's navigate the airport in Spanish![/bold white]
""",
    "emergencies": """
Sofia's expression turned serious but reassuring.

[bold cyan]"I hope you never need these phrases,"[/bold cyan] Sofia said gently.
[bold cyan]"But if you do, they could save your life.
'Ayuda!', 'Necesito un medico', 'Donde esta el hospital?'
-- emergency vocabulary is non-negotiable for any traveler."[/bold cyan]

[bold white]Let's learn essential emergency phrases![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "transportation": """
[bold green]Sofia stamped an imaginary ticket![/bold green]

[bold cyan]"Avion, tren, autobus, taxi, bicicleta, a pie --
you can get anywhere now! You know every mode of
transportation and how to talk about getting around.
The world is open to you!"[/bold cyan]
""",
    "directions": """
[bold green]Sofia spun the compass and it pointed right at you![/bold green]

[bold cyan]"Left, right, straight, north, south, east, west --
you'll never be lost with these words. You can read maps,
follow signs, and understand when someone points the way."[/bold cyan]
""",
    "hotel": """
[bold green]Sofia handed you a golden room key![/bold green]

[bold cyan]"Check in, check out, ask about wifi, request an extra pillow --
you can handle any hotel in the Spanish-speaking world.
Dulces suenos -- sweet dreams!"[/bold cyan]
""",
    "asking_directions": """
[bold green]Sofia drew a perfect map from memory![/bold green]

[bold cyan]"You can ask anyone for directions and understand the answer!
Cerca, lejos, al lado de, enfrente de -- you know all the
spatial vocabulary. No more getting lost!"[/bold cyan]
""",
    "airport": """
[bold green]Sofia stamped your passport with a big smile![/bold green]

[bold cyan]"Passport, luggage, boarding pass, gate -- you navigate
airports like a pro now! From check-in to boarding,
you've got every phrase covered. Buen vuelo!"[/bold cyan]
""",
    "emergencies": """
[bold green]Sofia nodded with quiet pride![/bold green]

[bold cyan]"You have the emergency vocabulary that could truly make
a difference. Ayuda, policia, hospital, medico, ambulancia --
I hope you never need them, but you're prepared.
Safety first, always. Estoy muy orgullosa."[/bold cyan]
""",
}

BOSS_INTROS = {
    "transportation": """
Sofia described different travel scenarios.

[bold cyan]"You need to get from the airport to your hotel,
then to a restaurant across town, then to a beach.
What transportation do you use for each? Name them
all in Spanish!"[/bold cyan]
""",
    "directions": """
Sofia blindfolded you (figuratively) and described a route.

[bold cyan]"I'll give you directions. Can you follow them
and tell me where you end up? Left, right, straight,
two blocks, turn -- it's all in Spanish!"[/bold cyan]
""",
    "hotel": """
Sofia played the role of a difficult hotel receptionist.

[bold cyan]"You're checking in, but things aren't perfect.
The room has no wifi, you need extra towels,
the key doesn't work. Handle every situation
in Spanish!"[/bold cyan]
""",
    "asking_directions": """
Sofia gave you rapid directions in Spanish.

[bold cyan]"Siga recto, gire a la izquierda, pase el parque,
esta al lado de la farmacia... Did you follow that?
Can you understand real-speed directions?"[/bold cyan]
""",
    "airport": """
Sofia created an airport scenario with complications.

[bold cyan]"Your flight is delayed, you can't find your gate,
and your luggage is missing. Handle every airport
crisis in Spanish. Vamos!"[/bold cyan]
""",
    "emergencies": """
Sofia described urgent scenarios requiring quick thinking.

[bold cyan]"Someone is hurt. You're lost at night. You need
a doctor. The right words at the right time can
change everything. Show me your emergency Spanish!"[/bold cyan]
""",
}
