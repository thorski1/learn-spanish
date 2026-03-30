"""
story.py — Narrative for the Greetings skill pack.

Sofia guides you through Spanish greetings, introductions, and polite expressions.
"""

INTRO_STORY = """
[bold red]LEARN SPANISH[/bold red]
[bold yellow]Chapter: Hola y Adios[/bold yellow]

Sofia stood at the entrance of a bustling Spanish plaza,
the sound of laughter and conversation filling the air.
Cafe tables lined the sidewalks, and people greeted each
other with warm smiles and kisses on the cheek.

[bold cyan]"This is where it all begins,"[/bold cyan] Sofia said, spreading her arms wide.
[bold cyan]"Greetings are the gateway to every conversation.
In Spanish-speaking cultures, how you say hello
matters just as much as what you say next.
It shows respect, warmth, and connection."[/bold cyan]

A friend walked by and Sofia called out,
[bold yellow]"Hola! Buenos dias! Como estas?"[/bold yellow]

[bold cyan]"See? Three phrases and you've already started
a real conversation. Let me teach you all of them."[/bold cyan]

[bold white]Learn to greet, introduce, and connect in Spanish.[/bold white]
"""

ZONE_INTROS = {
    "hello_goodbye": """
Sofia pointed to the cafe where friends were meeting and parting.

[bold cyan]"Every conversation starts with hello and ends with goodbye,"[/bold cyan]
Sofia said. [bold cyan]"In Spanish, we change our greeting based on
the time of day. Morning, afternoon, and evening each have
their own special greeting. Let's learn them all!"[/bold cyan]

[bold white]Let's master Spanish hellos and goodbyes![/bold white]
""",
    "introductions": """
Sofia gestured toward two strangers shaking hands in the plaza.

[bold cyan]"Now that you can say hello, let's learn to introduce yourself,"[/bold cyan]
Sofia said. [bold cyan]"You'll learn to say your name, ask someone else's,
tell people where you're from, and make that great first impression
that opens every door."[/bold cyan]

[bold white]Let's learn to introduce ourselves in Spanish![/bold white]
""",
    "how_are_you": """
Sofia sat down at a cafe table and ordered two coffees.

[bold cyan]"After hello, the next question is always 'How are you?'"[/bold cyan]
Sofia explained. [bold cyan]"In Spanish, there are several ways to ask,
and even more ways to answer. Let's learn the natural ones
that real Spanish speakers use every day."[/bold cyan]

[bold white]Let's learn to ask and answer 'How are you?'![/bold white]
""",
    "please_thanks": """
Sofia held up a small card with polite phrases written in gold.

[bold cyan]"Politeness opens every door,"[/bold cyan] Sofia said warmly.
[bold cyan]"Please, thank you, excuse me, I'm sorry -- these words
show respect and make people want to help you.
Spanish-speaking cultures value courtesy highly."[/bold cyan]

[bold white]Let's learn the magic words of Spanish politeness![/bold white]
""",
    "formal_informal": """
Sofia drew two figures on her notepad -- one in casual clothes, one in a suit.

[bold cyan]"This is crucial,"[/bold cyan] Sofia said seriously.
[bold cyan]"Spanish has two ways to say 'you.' 'Tu' is for friends,
family, and people your age. 'Usted' is for elders, strangers,
and formal situations. Using the wrong one can be awkward!"[/bold cyan]

[bold white]Let's master formal vs informal speech![/bold white]
""",
    "classroom_phrases": """
Sofia set up a mini classroom at the cafe table.

[bold cyan]"As a language learner, you need special phrases,"[/bold cyan]
Sofia said with a smile. [bold cyan]"How do you say...? I don't understand.
Can you repeat that? Slower please. These are your survival
phrases -- they keep the conversation going even when you're lost."[/bold cyan]

[bold white]Let's learn essential classroom and learning phrases![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "hello_goodbye": """
[bold green]Sofia gave you a warm high-five![/bold green]

[bold cyan]"Hola, buenos dias, buenas tardes, buenas noches, adios,
hasta luego -- you've got them all! You can now greet anyone
at any time of day. That's a real superpower!"[/bold cyan]
""",
    "introductions": """
[bold green]Sofia shook your hand with a proud smile![/bold green]

[bold cyan]"You can introduce yourself like a natural! Me llamo, soy de,
mucho gusto -- these phrases will serve you in every Spanish-speaking
country in the world. First impressions, mastered!"[/bold cyan]
""",
    "how_are_you": """
[bold green]Sofia raised her coffee cup in a toast![/bold green]

[bold cyan]"You can ask how someone is doing and respond naturally.
Bien, mal, mas o menos, y tu -- these are the building blocks
of every casual conversation. You sound like a real speaker!"[/bold cyan]
""",
    "please_thanks": """
[bold green]Sofia placed her hand over her heart![/bold green]

[bold cyan]"Por favor, gracias, de nada, lo siento -- you've mastered
the words that make people smile. Politeness in any language
shows respect, and in Spanish it's absolutely essential."[/bold cyan]
""",
    "formal_informal": """
[bold green]Sofia nodded with deep approval![/bold green]

[bold cyan]"You understand tu and usted! This is something many
learners struggle with for years, but you've got the cultural
awareness to know when each is appropriate. Impresionante!"[/bold cyan]
""",
    "classroom_phrases": """
[bold green]Sofia applauded enthusiastically![/bold green]

[bold cyan]"Now you have your language-learning survival kit!
You can ask for help, ask for clarification, and keep
any conversation going. These phrases will save you
countless times on your Spanish journey."[/bold cyan]
""",
}

BOSS_INTROS = {
    "hello_goodbye": """
Sofia glanced at her watch and then back at you.

[bold cyan]"Quick -- what greeting matches the time of day?
I'll test you on every hello and goodbye we've learned.
Timing matters in Spanish greetings!"[/bold cyan]
""",
    "introductions": """
Sofia gestured to an imaginary group of people.

[bold cyan]"Pretend you just arrived at a party in Madrid.
Introduce yourself, ask names, tell them where you're from.
Can you handle the full introduction sequence?"[/bold cyan]
""",
    "how_are_you": """
Sofia put on different expressions -- happy, sad, tired.

[bold cyan]"I'll describe how someone feels. You tell me
what they'd say in Spanish. Natural responses only --
let's see if you sound like a real Spanish speaker!"[/bold cyan]
""",
    "please_thanks": """
Sofia set up different social scenarios.

[bold cyan]"Someone helps you. Someone bumps into you.
You need to ask for something. What polite phrase
fits each situation? Courtesy is an art!"[/bold cyan]
""",
    "formal_informal": """
Sofia described different people and situations.

[bold cyan]"Your friend's grandmother. A police officer.
Your classmate. A job interview. Tu or usted?
Every situation demands the right register!"[/bold cyan]
""",
    "classroom_phrases": """
Sofia spoke rapidly in Spanish, then paused.

[bold cyan]"You didn't catch that? Perfect -- that's the point!
What do you say when you're lost? When you need
something repeated? When you need help? Show me
your survival skills!"[/bold cyan]
""",
}
