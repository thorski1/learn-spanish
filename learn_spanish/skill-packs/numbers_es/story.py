"""
story.py — Narrative for the Numbers skill pack.

Sofia guides you through Spanish numbers, time, and dates.
"""

INTRO_STORY = """
[bold red]LEARN SPANISH[/bold red]
[bold yellow]Chapter: Counting in Spanish[/bold yellow]

Sofia pulled out a colorful abacus and a small clock,
setting them on the table alongside a calendar covered
in Spanish writing.

[bold cyan]"Numbers are everywhere,"[/bold cyan] Sofia said, sliding beads across the abacus.
[bold cyan]"Prices, phone numbers, addresses, ages, time, dates --
you can't get through a single day without them.
The good news? Spanish numbers follow clear patterns.
Once you learn the first 30, the rest build on themselves."[/bold cyan]

She pointed to the clock, which showed 3:15.

[bold cyan]"And telling time in Spanish has its own charming logic.
Plus, did you know that in Spanish, days of the week
and months are NOT capitalized? Little details like
that make all the difference."[/bold cyan]

[bold white]Let's master numbers, time, and dates in Spanish.[/bold white]
"""

ZONE_INTROS = {
    "numbers_1_20": """
Sofia held up her hands, fingers spread wide.

[bold cyan]"Let's start at the very beginning -- uno, dos, tres,"[/bold cyan]
Sofia counted. [bold cyan]"Numbers 1 through 15 are all unique words
you need to memorize. But from 16 to 19, a beautiful
pattern emerges: diez y seis becomes dieciseis.
And veinte is our gateway to the twenties!"[/bold cyan]

[bold white]Let's count from uno to veinte![/bold white]
""",
    "numbers_21_100": """
Sofia wrote the tens on the board: 30, 40, 50...

[bold cyan]"From 21 to 29, Spanish has a special merged form --
veintiuno, veintidos..."[/bold cyan] Sofia explained.
[bold cyan]"After 30, the pattern changes to 'treinta y uno,'
'treinta y dos' -- tens + y + ones. Simple and logical
all the way to cien!"[/bold cyan]

[bold white]Let's master numbers up to 100![/bold white]
""",
    "big_numbers": """
Sofia wrote increasingly large numbers on the board.

[bold cyan]"Ready to think big?"[/bold cyan] Sofia grinned.
[bold cyan]"Ciento is 100 (when followed by more numbers),
mil is 1,000, and millon is 1,000,000. Prices,
populations, distances -- big numbers open up
the real world of Spanish."[/bold cyan]

[bold white]Let's tackle the big numbers![/bold white]
""",
    "telling_time_es": """
Sofia pointed to the clock on the wall.

[bold cyan]"Telling time in Spanish is an art,"[/bold cyan] Sofia said.
[bold cyan]"It starts with 'son las' for most hours, but 'es la'
for one o'clock. 'Y media' for half past, 'y cuarto'
for quarter past. And instead of AM/PM, we often say
'de la manana,' 'de la tarde,' or 'de la noche.'"[/bold cyan]

[bold white]Let's learn to tell time in Spanish![/bold white]
""",
    "days_months": """
Sofia opened her calendar to show the full year.

[bold cyan]"Here's a fun fact,"[/bold cyan] Sofia said, tapping the calendar.
[bold cyan]"In Spanish, days of the week and months are NOT
capitalized! 'Lunes' is Monday, 'enero' is January --
all lowercase. The week starts with lunes (Monday),
not Sunday like in the US."[/bold cyan]

[bold white]Let's learn the Spanish calendar![/bold white]
""",
    "ordinal_numbers": """
Sofia held up a podium showing 1st, 2nd, 3rd places.

[bold cyan]"First, second, third -- ordinal numbers tell you
the ORDER of things,"[/bold cyan] Sofia explained.
[bold cyan]"In Spanish, they change for gender! Primero/primera,
segundo/segunda. And here's a secret -- after decimo (10th),
most Spanish speakers just use regular numbers."[/bold cyan]

[bold white]Let's master ordinal numbers![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "numbers_1_20": """
[bold green]Sofia counted to twenty on her fingers -- and toes![/bold green]

[bold cyan]"Uno to veinte -- all yours! These twenty numbers are the
foundation for everything. You'll use them hundreds of times
a day in any Spanish-speaking country."[/bold cyan]
""",
    "numbers_21_100": """
[bold green]Sofia wrote a big '100' on the board and circled it![/bold green]

[bold cyan]"All the way to cien! You understand the patterns now --
the twenties merge together, and everything after 30 follows
'tens + y + ones.' You can count anything!"[/bold cyan]
""",
    "big_numbers": """
[bold green]Sofia drew dollar signs and big price tags![/bold green]

[bold cyan]"Ciento, mil, millon -- the big leagues! You can now talk
about prices, populations, distances, and anything else
that requires large numbers. The world just got bigger!"[/bold cyan]
""",
    "telling_time_es": """
[bold green]Sofia set all the clocks in the room to different times![/bold green]

[bold cyan]"You can tell time like a native speaker! Es la una,
son las tres y media, son las diez y cuarto -- you know
it all. No more missing appointments in Spanish!"[/bold cyan]
""",
    "days_months": """
[bold green]Sofia circled every day on the calendar![/bold green]

[bold cyan]"Lunes through domingo, enero through diciembre, and all
four seasons -- the whole Spanish calendar is yours. And you
know the secret: no capital letters for days and months!"[/bold cyan]
""",
    "ordinal_numbers": """
[bold green]Sofia placed you on the first-place podium![/bold green]

[bold cyan]"Primero to decimo -- you've mastered the ordinal numbers!
And you know the gender agreement trick: primero/primera,
segundo/segunda. You're number one -- el primero!"[/bold cyan]
""",
}

BOSS_INTROS = {
    "numbers_1_20": """
Sofia held up flash cards with numbers.

[bold cyan]"Speed round! I'll show you numbers and you name them.
Uno to veinte, random order. Can you get them all
without hesitation?"[/bold cyan]
""",
    "numbers_21_100": """
Sofia wrote complex number expressions on the board.

[bold cyan]"Big challenge! I'll test you on the tricky numbers --
the ones where the pattern changes, the teens that merge,
and the tens that stand alone. Ready?"[/bold cyan]
""",
    "big_numbers": """
Sofia displayed prices and statistics.

[bold cyan]"Real-world numbers! Prices in pesos, population counts,
distances in kilometers. Can you read and understand
big Spanish numbers in context?"[/bold cyan]
""",
    "telling_time_es": """
Sofia pointed to clocks showing different times.

[bold cyan]"What time is it? I'll show you tricky times --
quarter to, five past, midnight, noon. Can you
express every time correctly in Spanish?"[/bold cyan]
""",
    "days_months": """
Sofia mixed up calendar cards on the table.

[bold cyan]"Days, months, seasons -- all mixed together!
Put them in order, name the right ones, and remember:
lowercase! This is the calendar boss challenge!"[/bold cyan]
""",
    "ordinal_numbers": """
Sofia set up a race with numbered lanes.

[bold cyan]"First through tenth, masculine and feminine.
I'll throw curveballs with gender agreement.
Can you handle primero AND primera in context?"[/bold cyan]
""",
}
