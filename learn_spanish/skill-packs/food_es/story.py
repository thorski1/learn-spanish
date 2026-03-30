"""
story.py — Narrative for the Food skill pack.

Sofia guides you through Spanish food vocabulary, ordering, and culinary culture.
"""

INTRO_STORY = """
[bold red]LEARN SPANISH[/bold red]
[bold yellow]Chapter: La Cocina Espanola[/bold yellow]

The aroma of freshly baked bread and sizzling garlic drifted
through the air as Sofia led you into a bustling market.
Stalls overflowed with colorful fruits, fragrant spices,
and handmade cheeses.

[bold cyan]"Food is the heart of Spanish-speaking cultures,"[/bold cyan] Sofia said,
picking up a bright red tomato. [bold cyan]"Every country has its own
dishes, but the vocabulary connects them all. Whether you're
ordering tapas in Madrid, tacos in Mexico City, or empanadas
in Buenos Aires, you need the same food words."[/bold cyan]

She gestured toward a nearby restaurant.

[bold cyan]"Let's learn everything -- from naming fruits and vegetables
to ordering a full meal, cooking your own dishes, and
understanding the culinary traditions that make
each Spanish-speaking country unique."[/bold cyan]

[bold white]Explore the delicious world of Spanish food vocabulary.[/bold white]
"""

ZONE_INTROS = {
    "fruits_vegetables": """
Sofia stopped at a colorful fruit and vegetable stand.

[bold cyan]"Look at all these colors!"[/bold cyan] Sofia exclaimed.
[bold cyan]"Manzanas, platanos, tomates, lechugas -- the market
is the perfect classroom. Let's learn the names of the
most common fruits and vegetables in Spanish."[/bold cyan]

[bold white]Let's explore fruits and vegetables![/bold white]
""",
    "drinks": """
Sofia sat down at a sunny cafe terrace.

[bold cyan]"What would you like to drink?"[/bold cyan] Sofia asked.
[bold cyan]"Agua, cafe, jugo, cerveza -- every drink has its name,
and knowing them is essential whether you're at a cafe,
a restaurant, or someone's home. Let's learn them all!"[/bold cyan]

[bold white]Let's learn Spanish drink vocabulary![/bold white]
""",
    "meals": """
Sofia pointed to a clock showing different mealtimes.

[bold cyan]"Spanish-speaking countries have their own meal schedule,"[/bold cyan]
Sofia explained. [bold cyan]"Desayuno in the morning, almuerzo at midday
(which can be very late!), merienda in the afternoon, and
cena in the evening. The timing and size of each meal
varies by country -- it's fascinating!"[/bold cyan]

[bold white]Let's learn about Spanish meals![/bold white]
""",
    "ordering": """
Sofia handed you a menu written entirely in Spanish.

[bold cyan]"Time to order!"[/bold cyan] Sofia said with a smile.
[bold cyan]"Quisiera... Me gustaria... La cuenta, por favor...
These phrases will get you through any restaurant in
the Spanish-speaking world. Let's practice ordering
like a confident traveler."[/bold cyan]

[bold white]Let's learn to order food in Spanish![/bold white]
""",
    "cooking": """
Sofia put on an apron and picked up a wooden spoon.

[bold cyan]"Now let's get into the kitchen!"[/bold cyan] Sofia said.
[bold cyan]"Cocinar, hervir, freir, cortar, mezclar -- these are
the cooking verbs you'll see in every recipe.
Plus the tools and ingredients that bring it all together."[/bold cyan]

[bold white]Let's learn Spanish cooking vocabulary![/bold white]
""",
    "food_culture": """
Sofia spread out a map showing Spanish-speaking countries with food icons.

[bold cyan]"Every country has its signature dishes,"[/bold cyan] Sofia said proudly.
[bold cyan]"Tapas from Spain, tacos from Mexico, empanadas from Argentina,
paella from Valencia, churros from... well, everywhere!
Let's explore the culinary traditions that define cultures."[/bold cyan]

[bold white]Let's explore food culture across the Spanish-speaking world![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "fruits_vegetables": """
[bold green]Sofia tossed you a perfect manzana![/bold green]

[bold cyan]"You know all the fruits and vegetables! From manzana to cebolla,
from platano to lechuga -- you can navigate any market in the
Spanish-speaking world. Buen provecho!"[/bold cyan]
""",
    "drinks": """
[bold green]Sofia raised her glass in a toast![/bold green]

[bold cyan]"Salud! You know every drink from agua to vino.
Whether you're ordering a cafe con leche in the morning
or a cerveza in the evening, you've got it covered."[/bold cyan]
""",
    "meals": """
[bold green]Sofia set a beautiful table with all four meals![/bold green]

[bold cyan]"Desayuno, almuerzo, merienda, cena -- you understand
the rhythm of Spanish meals. Food culture is about more
than just words -- it's about how people live!"[/bold cyan]
""",
    "ordering": """
[bold green]Sofia pretended to be a waiter and served you perfectly![/bold green]

[bold cyan]"You can order with confidence! Quisiera..., Tiene...,
La cuenta por favor -- you'll never go hungry in a
Spanish-speaking country. The world is your restaurant!"[/bold cyan]
""",
    "cooking": """
[bold green]Sofia took off her apron and took a bow![/bold green]

[bold cyan]"Cocinar, hervir, freir, cortar, mezclar -- you've mastered
the kitchen vocabulary! Now you can follow recipes,
watch cooking shows, and talk about food preparation
all in Spanish."[/bold cyan]
""",
    "food_culture": """
[bold green]Sofia spread out photos of beautiful dishes from around the world![/bold green]

[bold cyan]"From tapas to tacos, paella to empanadas -- you've explored
the incredible diversity of Spanish-speaking food cultures.
Food tells the story of a people, and now you know
those stories. Increible!"[/bold cyan]
""",
}

BOSS_INTROS = {
    "fruits_vegetables": """
Sofia placed a basket of mixed produce on the table.

[bold cyan]"Name every fruit and vegetable in this basket!
I'll test you on colors, categories, and those tricky
ones that look similar. Ready for the produce challenge?"[/bold cyan]
""",
    "drinks": """
Sofia lined up glasses with different beverages.

[bold cyan]"Hot drinks, cold drinks, alcoholic and non-alcoholic --
I'll test you on all of them. Can you name every
beverage and know when each is typically served?"[/bold cyan]
""",
    "meals": """
Sofia set up a timeline of the day with empty plates.

[bold cyan]"What goes where? I'll give you dishes and you tell me
which meal they belong to. Plus the cultural context
that makes Spanish eating habits unique!"[/bold cyan]
""",
    "ordering": """
Sofia sat across from you, notepad ready, playing a waiter.

[bold cyan]"Welcome to Restaurante Sofia! Order a complete meal --
appetizer, main course, drink, and dessert. Ask for the check.
Handle every situation a restaurant can throw at you!"[/bold cyan]
""",
    "cooking": """
Sofia handed you a recipe card written in Spanish.

[bold cyan]"Read this recipe and tell me what to do!
Every cooking verb, every technique, every tool --
show me you can run a Spanish kitchen!"[/bold cyan]
""",
    "food_culture": """
Sofia displayed flags and dishes side by side.

[bold cyan]"Match the dish to the country! Tapas, tacos, empanadas,
ceviche, churros -- where did they originate?
This is the ultimate food culture challenge!"[/bold cyan]
""",
}
