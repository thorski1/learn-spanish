"""
story.py — Narrative for the Colors & Clothing skill pack.

Carmen guides you through a vibrant sunset market, teaching colors,
clothing, and how to shop like a local in Spanish.
"""

INTRO_STORY = """
[bold red]LEARN SPANISH[/bold red]
[bold yellow]Chapter: Colors & Clothing[/bold yellow]

The sun hung low over the open-air market, painting everything
in shades of gold and amber. Stalls overflowed with fabrics
in every color imaginable -- crimson scarves, emerald shawls,
and indigo dresses that caught the fading light.

[bold cyan]"Welcome to the Mercado del Atardecer,"[/bold cyan] said Carmen,
adjusting her wide-brimmed hat against the sunset glow.
[bold cyan]"This is where color and fashion come alive.
Every stall tells a story, and every outfit
starts with knowing how to say what you see."[/bold cyan]

She held up a bolt of deep red fabric and smiled.
[bold yellow]"Rojo. That's where we begin."[/bold yellow]

[bold cyan]"By the time the sun sets, you'll be able to name
every color, describe any outfit, and shop for clothes
like a true local. Shall we?"[/bold cyan]

[bold white]Learn colors, clothing, and how to shop in Spanish.[/bold white]
"""

ZONE_INTROS = {
    "basic_colors": """
Carmen led you to the first row of stalls where fabrics
hung like banners against the sunset sky.

[bold cyan]"Every artist starts with the basics,"[/bold cyan]
Carmen said, running her fingers over the cloth.
[bold cyan]"Red, blue, green, yellow, white, black --
these are the building blocks. Once you know these six,
you can describe almost anything you see."[/bold cyan]

[bold white]Let's learn the essential Spanish colors![/bold white]
""",
    "more_colors_shades": """
Carmen guided you deeper into the market where dyes
and pigments filled the air with earthy scents.

[bold cyan]"Now let's expand your palette,"[/bold cyan] Carmen said,
gesturing at rows of purple, orange, and pink fabrics.
[bold cyan]"And I'll teach you a trick -- how to make
any color lighter or darker with just one word.
Dark blue, light green, soft pink -- all within reach."[/bold cyan]

[bold white]Let's explore more colors and learn shades![/bold white]
""",
    "clothing_items": """
Carmen stopped at a stall bursting with hats, shirts,
dresses, and shoes of every style.

[bold cyan]"Now that you can see in color,"[/bold cyan] Carmen laughed,
[bold cyan]"let's name what people actually wear.
Shirts, pants, dresses, shoes, hats --
the vocabulary of your wardrobe.
Every piece has a name, a gender, and a story."[/bold cyan]

[bold white]Let's learn the names of common clothing![/bold white]
""",
    "describing_what_you_wear": """
Carmen pulled out a sketchpad and began drawing outfits
as the sunset painted long shadows across the market.

[bold cyan]"Knowing the words isn't enough,"[/bold cyan] Carmen explained.
[bold cyan]"You need to put them together. 'I wear a red dress.'
'He has on black shoes.' In Spanish, the colors must
agree with the clothing -- masculine, feminine,
singular, plural. It's like a dance."[/bold cyan]

[bold white]Let's learn to describe outfits in Spanish![/bold white]
""",
    "shopping_for_clothes": """
Carmen walked you to the busiest corner of the market
where vendors called out prices and shoppers haggled.

[bold cyan]"This is the real test,"[/bold cyan] Carmen said with a grin.
[bold cyan]"How much does it cost? What size? Can I try it on?
These phrases turn you from a tourist into a shopper.
By the time we're done, you'll bargain
like you were born in this market."[/bold cyan]

[bold white]Let's learn to shop for clothes in Spanish![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "basic_colors": """
[bold green]Carmen held up six colored ribbons like a fan![/bold green]

[bold cyan]"Rojo, azul, verde, amarillo, blanco, negro --
you've got the essential six! You can describe the sky,
the flowers, the cars, anything around you.
And you know where the colors go and how they agree.
The world just got more colorful!"[/bold cyan]
""",
    "more_colors_shades": """
[bold green]Carmen draped a sunset-colored scarf over your shoulders![/bold green]

[bold cyan]"Morado, naranja, rosa, gris, oscuro, claro --
your palette is complete! You can now describe
any shade you see. Light blue sky, dark green forest,
soft pink flowers -- the whole spectrum is yours."[/bold cyan]
""",
    "clothing_items": """
[bold green]Carmen tipped her sombrero in respect![/bold green]

[bold cyan]"Camisa, pantalon, vestido, zapatos, sombrero --
you can name every piece of an outfit! You know
the gender of each item and how to use 'ropa'
for clothing in general. You're building a real
wardrobe of Spanish words!"[/bold cyan]
""",
    "describing_what_you_wear": """
[bold green]Carmen sketched a gold star on her notepad for you![/bold green]

[bold cyan]"You can use 'llevar,' 'ponerse,' and 'tener puesto'
to describe any outfit. And your adjective agreement
is spot-on -- masculine, feminine, singular, plural.
You sound like someone who truly knows their Spanish fashion!"[/bold cyan]
""",
    "shopping_for_clothes": """
[bold green]Carmen handed you a tiny shopping bag as a trophy![/bold green]

[bold cyan]"Cuanto cuesta? Que talla? Puedo probarme esto?
Me lo llevo! You've mastered the full shopping experience.
From asking prices to bargaining for discounts,
you can shop in any Spanish-speaking market, boutique,
or mall with total confidence. Felicidades!"[/bold cyan]
""",
}

BOSS_INTROS = {
    "basic_colors": """
Carmen held up a colorful quilt with a mischievous smile.

[bold cyan]"You've learned the six essential colors.
Now let's see if you truly understand how they work --
where they go in a sentence and how they change.
Gender agreement is the real test of a color master!"[/bold cyan]
""",
    "more_colors_shades": """
Carmen mixed imaginary paints on her palm.

[bold cyan]"Purple, orange, pink, gray, light, dark --
you know them all. But here's the tricky part:
what happens when you combine a color with a shade?
The grammar changes! Let's see if you caught that."[/bold cyan]
""",
    "clothing_items": """
Carmen gestured to a mannequin wearing a full outfit.

[bold cyan]"Name every piece. Shirt, pants, dress, shoes, hat --
and tell me which are hiding in a list of random words.
A true fashionista knows clothing vocabulary cold!"[/bold cyan]
""",
    "describing_what_you_wear": """
Carmen pointed to people walking through the market.

[bold cyan]"Describe what she's wearing. Translate this outfit.
Remember -- the color agrees with the clothing item,
not with the person! This trips up even advanced learners.
Show me you've got it!"[/bold cyan]
""",
    "shopping_for_clothes": """
Carmen nudged you toward a busy vendor's stall.

[bold cyan]"It's time to put it all together. Ask the price,
ask for your size, try it on, and decide to buy.
A full shopping conversation from start to finish.
Can you handle the Mercado del Atardecer?"[/bold cyan]
""",
}
