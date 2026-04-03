"""
story.py — Narrative for the Weather & Seasons skill pack.

Sofia guides you through a coastal Spanish town at sunset, teaching weather
vocabulary, seasons, temperature, and how to make plans around the weather.
"""

INTRO_STORY = """
[bold red]LEARN SPANISH[/bold red]
[bold yellow]Chapter: Weather & Seasons[/bold yellow]

The sky blazed with streaks of copper and violet as the sun
sank toward the sea. Waves lapped against the stone promenade
of the coastal town, and the evening breeze carried the scent
of salt and orange blossoms.

[bold cyan]"Welcome to the Paseo del Atardecer,"[/bold cyan] said Sofia,
tucking a strand of windblown hair behind her ear.
She gestured at the sky with the easy confidence
of someone who spent her life reading the heavens.
[bold cyan]"I'm a meteorologist -- but really, I'm a storyteller.
The weather has a language of its own,
and tonight I'll teach you to speak it."[/bold cyan]

She pointed to the horizon where clouds gathered
at the edge of the sunset glow.
[bold yellow]"Hace sol ahora... pero parece que va a llover.
That's where we begin."[/bold yellow]

[bold cyan]"By the time the last light fades, you'll know
every season, every forecast, and how to plan
your life around the weather -- all in Spanish.
Shall we?"[/bold cyan]

[bold white]Learn weather, seasons, and how to make plans in Spanish.[/bold white]
"""

ZONE_INTROS = {
    "weather_basics": """
Sofia led you to the edge of the promenade where the sky
was a canvas of gold and deepening blue.

[bold cyan]"Every conversation about weather starts here,"[/bold cyan]
Sofia said, watching the clouds shift overhead.
[bold cyan]"Sunny, rainy, snowy, cloudy, windy --
these are the building blocks. Once you master these,
you can describe any sky in any country."[/bold cyan]

[bold white]Let's learn the essential weather expressions![/bold white]
""",
    "seasons_months": """
Sofia walked you along the waterfront where flower beds
marked the changing of the seasons in bursts of color.

[bold cyan]"Spring, summer, autumn, winter,"[/bold cyan] Sofia recited,
touching the petals of a late-blooming rose.
[bold cyan]"And twelve months to hold them all.
The calendar is your map through the year --
let me teach you to read it in Spanish."[/bold cyan]

[bold white]Let's learn the seasons and months![/bold white]
""",
    "temperature_climate": """
Sofia tapped the weather station mounted on the harbor wall,
its thermometer glinting in the last rays of sunlight.

[bold cyan]"Numbers bring weather to life,"[/bold cyan] she explained.
[bold cyan]"Forty degrees and you're melting.
Zero degrees and you're freezing.
Understanding temperature and climate types
turns you from a tourist into a local."[/bold cyan]

[bold white]Let's learn about temperature and climate![/bold white]
""",
    "weather_conversations": """
Sofia sat down at a cafe terrace overlooking the darkening sea,
where locals chatted and sipped their evening drinks.

[bold cyan]"Weather is the world's favorite small talk,"[/bold cyan]
Sofia said with a knowing smile.
[bold cyan]"How to ask about it, how to react to it,
how to compare today with yesterday --
these are the phrases that make you sound natural."[/bold cyan]

[bold white]Let's learn to talk about weather in conversation![/bold white]
""",
    "making_plans_weather": """
Sofia pulled out her phone and showed you
the week's forecast as streetlights flickered on
along the promenade.

[bold cyan]"This is where it all comes together,"[/bold cyan]
Sofia said, her eyes bright with purpose.
[bold cyan]"If it rains, we do this. When it's sunny,
we do that. Making plans around the weather
is real-world Spanish -- the kind that matters."[/bold cyan]

[bold white]Let's learn to make plans using weather in Spanish![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "weather_basics": """
[bold green]Sofia traced a sun shape in the air with her finger![/bold green]

[bold cyan]"Hace sol, llueve, nieva, esta nublado, hace viento --
you've got the essentials! You can describe any sky now.
And you know the difference between 'hacer' and 'estar'
for weather. That's a detail many learners miss!"[/bold cyan]
""",
    "seasons_months": """
[bold green]Sofia handed you a small calendar decorated with seasonal flowers![/bold green]

[bold cyan]"Primavera, verano, otono, invierno --
and every month from enero to diciembre.
You can talk about any time of year now.
The whole Spanish calendar is yours!"[/bold cyan]
""",
    "temperature_climate": """
[bold green]Sofia gave you a mini thermometer keychain as a memento![/bold green]

[bold cyan]"Calor, frio, grados, clima, humedo, seco --
you understand temperature and climate like a true
meteorologist. You can read any Spanish weather report
and know exactly what to expect!"[/bold cyan]
""",
    "weather_conversations": """
[bold green]Sofia clinked her glass against yours in celebration![/bold green]

[bold cyan]"Que tiempo hace? Que dia tan bonito! Parece que va a llover --
you can chat about weather like a local now.
The forecast, comparisons, yesterday and tomorrow --
your weather small talk is impeccable!"[/bold cyan]
""",
    "making_plans_weather": """
[bold green]Sofia stood and applauded as the last stars appeared![/bold green]

[bold cyan]"Si llueve, cuando hace sol, por si acaso --
you can plan around any weather in Spanish!
From beach days to rainy backup plans,
you think and speak about weather like a native.
The sky is no longer a mystery. Felicidades!"[/bold cyan]
""",
}

BOSS_INTROS = {
    "weather_basics": """
Sofia pointed to the shifting clouds on the horizon.

[bold cyan]"You know sunny, rainy, snowy, cloudy, windy.
Now let's see if you can put it all together --
a mini weather report for today and tomorrow.
Show me you can forecast like a pro!"[/bold cyan]
""",
    "seasons_months": """
Sofia opened a world map showing different climate zones.

[bold cyan]"You know every season and every month.
Now combine them -- tell me what the weather
does in spring, what happens in summer.
Link the seasons to the sky!"[/bold cyan]
""",
    "temperature_climate": """
Sofia held up an imaginary thermometer and squinted.

[bold cyan]"Degrees, hot, cold, climate types --
you know the vocabulary. But can you put
a temperature and a feeling together
in one natural sentence? Let's find out!"[/bold cyan]
""",
    "weather_conversations": """
Sofia nodded toward a stranger at the next table.

[bold cyan]"Imagine you're starting a conversation.
The weather is your opening line.
Which sounds natural? Which sounds like a textbook?
Show me you can chat, not just recite!"[/bold cyan]
""",
    "making_plans_weather": """
Sofia showed you a weekend forecast on her phone.

[bold cyan]"Saturday sun, Sunday rain -- your friend
wants to know the plan. This is everything:
reading a forecast, suggesting activities,
and adapting when the weather changes.
One final challenge. You've got this!"[/bold cyan]
""",
}
