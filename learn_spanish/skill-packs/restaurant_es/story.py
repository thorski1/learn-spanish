"""
story.py — Narrative for the At the Restaurant skill pack.

Carlos guides you through a Spanish restaurant at sunset, teaching vocabulary
for reservations, menus, ordering, dietary needs, and paying the bill.
"""

INTRO_STORY = """
[bold red]LEARN SPANISH[/bold red]
[bold yellow]Chapter: At the Restaurant[/bold yellow]

Golden light poured through the floor-to-ceiling windows
of a restaurant perched on a hilltop, the sunset painting
the white tablecloths in shades of amber and rose.
The clink of glasses and murmur of conversation
filled the warm evening air.

[bold cyan]"Bienvenido al Restaurante del Atardecer,"[/bold cyan] said Carlos,
adjusting his immaculate waistcoat as he stepped forward
with the quiet confidence of a man who had spent decades
making every guest feel at home.
[bold cyan]"I've been a maitre d' for thirty years in this city,
and I can tell you -- the language of dining
is the language of connection."[/bold cyan]

He gestured toward the terrace where the sun
was melting into the horizon like liquid gold.
[bold yellow]"Quisiera una mesa para dos... en la terraza.
That's where we begin."[/bold yellow]

[bold cyan]"By the time dessert arrives, you'll know
how to reserve, order, handle allergies,
and pay the bill -- all in Spanish.
Shall we be seated?"[/bold cyan]

[bold white]Learn to dine out with confidence in Spanish.[/bold white]
"""

ZONE_INTROS = {
    "making_reservation": """
Carlos led you to the host stand where a leather-bound
reservation book lay open beside a flickering candle.

[bold cyan]"Every great meal begins before you arrive,"[/bold cyan]
Carlos said, running his finger along the evening's bookings.
[bold cyan]"Knowing how to make a reservation -- the time,
the party size, your name -- opens doors.
Literally."[/bold cyan]

[bold white]Let's learn to make a restaurant reservation![/bold white]
""",
    "reading_menu": """
Carlos placed an elegant menu in your hands,
its pages warm from the candlelight.

[bold cyan]"La carta,"[/bold cyan] Carlos announced with a flourish.
[bold cyan]"Starters, mains, desserts, drinks --
a Spanish menu tells a story from beginning to end.
Once you can read it, the whole culinary world
of Spain is yours to explore."[/bold cyan]

[bold white]Let's learn to navigate a Spanish menu![/bold white]
""",
    "ordering_food": """
Carlos nodded to the approaching waiter
as the sunset deepened to a rich copper.

[bold cyan]"Now comes the art of ordering,"[/bold cyan] Carlos said,
straightening a napkin with practiced precision.
[bold cyan]"Polite, clear, confident -- that's how
a good diner communicates. The right words
turn a meal into an experience."[/bold cyan]

[bold white]Let's learn to order food and drinks in Spanish![/bold white]
""",
    "dietary_needs": """
Carlos grew serious for a moment, his voice
dropping to a careful, deliberate tone as the
last rays of sun streaked across the dining room.

[bold cyan]"This may be the most important lesson,"[/bold cyan]
Carlos said, meeting your eyes steadily.
[bold cyan]"Allergies, intolerances, dietary choices --
knowing how to communicate these clearly
can make the difference between a wonderful meal
and a dangerous one."[/bold cyan]

[bold white]Let's learn to communicate dietary needs in Spanish![/bold white]
""",
    "paying_tipping": """
Carlos glanced at the bill presenter on a nearby table
as the sky outside turned to deep violet and the first
stars appeared above the terrace.

[bold cyan]"The final act of any meal,"[/bold cyan] Carlos said
with a knowing smile.
[bold cyan]"The bill, the payment, the tip --
handle it smoothly and you leave
the kind of impression that earns you
the best table next time."[/bold cyan]

[bold white]Let's learn to handle the bill and tipping in Spanish![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "making_reservation": """
[bold green]Carlos marked your name in the reservation book with a smile![/bold green]

[bold cyan]"Reserva, mesa para dos, a las nueve, a nombre de... --
you've got it all! You can now walk into any restaurant
in the Spanish-speaking world and secure your table.
The first step to a great meal is taken!"[/bold cyan]
""",
    "reading_menu": """
[bold green]Carlos closed the menu with a satisfied nod![/bold green]

[bold cyan]"Entrantes, plato principal, postres, bebidas --
you can decode any Spanish menu now.
From the menu del dia to the carta de vinos,
nothing on the page is a mystery anymore!"[/bold cyan]
""",
    "ordering_food": """
[bold green]Carlos signaled the waiter with an approving gesture![/bold green]

[bold cyan]"Quisiera, para mi, de primero, de segundo, de beber --
your ordering is polished and natural.
You sound like someone who's been dining in Spain
for years. The kitchen awaits your command!"[/bold cyan]
""",
    "dietary_needs": """
[bold green]Carlos gave you a respectful nod of acknowledgment![/bold green]

[bold cyan]"Vegetariano, alergico, sin gluten, intolerancia --
you can communicate any dietary need clearly and safely.
This knowledge protects you and shows respect
for the kitchen. Well done -- this truly matters."[/bold cyan]
""",
    "paying_tipping": """
[bold green]Carlos stood and gave you a warm handshake as the night sky glittered![/bold green]

[bold cyan]"La cuenta, efectivo, tarjeta, propina --
you've mastered the complete dining experience
from the first reservation to the final tip.
You'll never feel lost in a Spanish restaurant again.
Enhorabuena -- congratulations!"[/bold cyan]
""",
}

BOSS_INTROS = {
    "making_reservation": """
Carlos picked up the phone and handed it to you.

[bold cyan]"Imagine you're calling to reserve.
Party size, time, name -- can you put it all
together in one smooth, polite request?
Show me the perfect reservation."[/bold cyan]
""",
    "reading_menu": """
Carlos pointed to an item on the specials board.

[bold cyan]"Here's a real menu description --
the kind you'll see in any Spanish restaurant.
Can you decode every word and know
exactly what's arriving at your table?"[/bold cyan]
""",
    "ordering_food": """
Carlos gestured to the waiter approaching your table.

[bold cyan]"First course, second course, drink --
the waiter is ready and so are you.
Put it all together in one complete order.
Make it polite, make it clear, make it natural."[/bold cyan]
""",
    "dietary_needs": """
Carlos leaned forward with a serious expression.

[bold cyan]"You have a real allergy and the waiter
needs to understand -- clearly and completely.
This isn't just vocabulary, it's safety.
Show me you can handle this."[/bold cyan]
""",
    "paying_tipping": """
Carlos looked at the empty plates and smiled.

[bold cyan]"The meal was magnificent. Now for the finale --
the bill, the compliment, the payment, the tip.
Can you wrap it all up gracefully?
One last challenge. You're ready."[/bold cyan]
""",
}
