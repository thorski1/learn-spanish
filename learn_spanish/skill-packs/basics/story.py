"""
story.py — Narrative for the Basics skill pack.

Sofia guides you through the foundations of Spanish,
from the alphabet to building your first sentences.
"""

INTRO_STORY = """
[bold red]LEARN SPANISH[/bold red]
[bold yellow]Chapter: The Foundation of Spanish[/bold yellow]

A sun-drenched courtyard appeared before you, filled with the scent of
orange blossoms. At a wooden table sat a woman with warm brown eyes
and an inviting smile, a well-worn notebook open in front of her.

[bold cyan]"Bienvenido!"[/bold cyan] she said, gesturing to the empty chair across from her.
[bold cyan]"I'm Sofia, and I'm going to help you learn Spanish.
It's one of the most beautiful languages in the world --
spoken by over 500 million people across more than 20 countries."[/bold cyan]

She opened her notebook to a page filled with colorful notes.

[bold cyan]"We'll start with the basics -- the alphabet, how words work,
and how to build your very first sentences. Spanish is actually
one of the easiest languages for English speakers to learn.
Many words are similar, the spelling is logical, and
the pronunciation rules barely have any exceptions."[/bold cyan]

Sofia tapped the table with her pen and smiled.

[bold cyan]"Ready? Let's begin your journey into Spanish.
By the end, you'll be surprised how much you understand."[/bold cyan]

[bold white]Your journey into the Spanish language begins now.[/bold white]
"""

ZONE_INTROS = {
    "alphabet_pronunciation": """
Sofia wrote the Spanish alphabet across the top of a fresh page.

[bold cyan]"The Spanish alphabet has 27 letters,"[/bold cyan] Sofia explained.
[bold cyan]"That's the English 26 plus one special letter: the n with
a tilde -- that's the n-yeh sound. Spanish vowels are pure and
consistent -- each one always makes the same sound. And the letter h?
It's always silent!"[/bold cyan]

[bold white]Let's master the sounds of Spanish![/bold white]
""",
    "gender_articles": """
Sofia drew two columns on the page, one blue and one red.

[bold cyan]"In Spanish, every noun has a gender -- masculine or feminine,"[/bold cyan]
Sofia said. [bold cyan]"This is one of the biggest differences from English.
'The book' is 'el libro' (masculine), but 'the table' is 'la mesa'
(feminine). Don't worry -- there are patterns that make it easier!"[/bold cyan]

[bold white]Let's learn about gender and articles![/bold white]
""",
    "ser_vs_estar": """
Sofia wrote two large words: SER and ESTAR.

[bold cyan]"Here's something that confuses every English speaker,"[/bold cyan]
Sofia said with a knowing smile. [bold cyan]"Spanish has TWO verbs that
mean 'to be.' Ser is for permanent things -- who you are, where
you're from. Estar is for temporary things -- how you feel,
where you are right now."[/bold cyan]

[bold white]Let's master the two ways to say 'to be'![/bold white]
""",
    "basic_conjugation": """
Sofia drew three verb endings on the board: -AR, -ER, -IR.

[bold cyan]"Spanish verbs change their endings based on who's doing the action,"[/bold cyan]
Sofia explained. [bold cyan]"But here's the good news -- regular verbs follow
predictable patterns. Learn the pattern once, and you can conjugate
thousands of verbs. We'll start with the present tense."[/bold cyan]

[bold white]Let's learn to conjugate Spanish verbs![/bold white]
""",
    "common_adjectives": """
Sofia held up cards with colorful drawings and descriptions.

[bold cyan]"Adjectives in Spanish usually come AFTER the noun,"[/bold cyan] Sofia said.
[bold cyan]"And they have to agree in gender and number! 'The red car' is
'el carro rojo,' but 'the red house' is 'la casa roja.'
The adjective changes to match. Let's learn the most useful ones."[/bold cyan]

[bold white]Let's explore Spanish adjectives![/bold white]
""",
    "question_words": """
Sofia wrote a row of question marks -- both regular and inverted.

[bold cyan]"Spanish is one of the few languages that uses an upside-down
question mark at the beginning of a question,"[/bold cyan] Sofia noted.
[bold cyan]"And the question words themselves are straightforward.
Once you know them, you can ask about anything!"[/bold cyan]

[bold white]Let's learn how to ask questions in Spanish![/bold white]
""",
    "basic_sentences": """
Sofia opened to a fresh page with simple sentence diagrams.

[bold cyan]"Time to put it all together!"[/bold cyan] Sofia said excitedly.
[bold cyan]"Spanish sentence structure is similar to English --
Subject + Verb + Object. But you can also drop the subject
since the verb ending tells you who's doing the action.
And negation? Just put 'no' before the verb!"[/bold cyan]

[bold white]Let's build complete Spanish sentences![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "alphabet_pronunciation": """
[bold green]Sofia clapped her hands together![/bold green]

[bold cyan]"Excelente! You know the Spanish alphabet and all its sounds.
The five pure vowels, the silent h, the rolling rr, and our
special friend -- you've got the foundation for perfect pronunciation!"[/bold cyan]
""",
    "gender_articles": """
[bold green]Sofia drew a golden star on the page![/bold green]

[bold cyan]"You've mastered gender and articles! El, la, los, las -- you know
when to use each one. This is one of the trickiest parts of Spanish
for English speakers, and you've already conquered it."[/bold cyan]
""",
    "ser_vs_estar": """
[bold green]Sofia raised both hands in celebration![/bold green]

[bold cyan]"Ser and estar -- mastered! You understand the difference between
permanent identity and temporary states. This distinction is the
heart of how Spanish sees the world. Incredible progress!"[/bold cyan]
""",
    "basic_conjugation": """
[bold green]Sofia spun her pen like a baton![/bold green]

[bold cyan]"You can conjugate verbs in all three families! -AR, -ER, -IR --
the patterns are yours now. This unlocks thousands of verbs.
You're building sentences already!"[/bold cyan]
""",
    "common_adjectives": """
[bold green]Sofia held up a vibrant, colorful page![/bold green]

[bold cyan]"Colors, sizes, descriptions -- you've learned them all,
AND you know how to make them agree with the noun. Masculine,
feminine, singular, plural -- you handle it like a natural!"[/bold cyan]
""",
    "question_words": """
[bold green]Sofia pointed to the inverted question mark with pride![/bold green]

[bold cyan]"You can ask any question now! What, who, where, when, how,
why, how much -- the whole set. Curiosity is the best tool
for learning a language, and now you have the words for it."[/bold cyan]
""",
    "basic_sentences": """
[bold green]Sofia closed her notebook and beamed![/bold green]

[bold cyan]"You're building real Spanish sentences! Subject, verb, object,
negation, questions -- you have all the tools. The foundation is
solid. From here, everything else is just adding vocabulary
and practicing. Estoy muy orgullosa de ti!"[/bold cyan]
""",
}

BOSS_INTROS = {
    "alphabet_pronunciation": """
Sofia tapped her pen on the desk with a playful grin.

[bold cyan]"Final alphabet challenge! I'm going to test you on the trickiest
sounds -- the ones that trip up every English speaker.
Can you tell me about every special sound in Spanish?"[/bold cyan]
""",
    "gender_articles": """
Sofia shuffled a stack of noun cards.

[bold cyan]"The ultimate gender challenge! I'll give you nouns and you tell me
their articles. Some follow the rules perfectly, and some are
the sneaky exceptions. Let's see how sharp you are!"[/bold cyan]
""",
    "ser_vs_estar": """
Sofia wrote a series of sentences with blanks.

[bold cyan]"Ser or estar? This is the question that defines your Spanish.
I'm mixing tricky cases together -- location, emotion, identity,
profession. Choose wisely!"[/bold cyan]
""",
    "basic_conjugation": """
Sofia opened to a page full of infinitive verbs.

[bold cyan]"Conjugation showdown! I'll throw verbs from all three families
at you, in different persons. Can you give me the correct
present tense form every time? Vamos a ver!"[/bold cyan]
""",
    "common_adjectives": """
Sofia held up a complex scene to describe.

[bold cyan]"Describe everything! I want the right adjective, the right gender,
the right number. Adjective agreement is where beginners stumble,
but I think you're ready."[/bold cyan]
""",
    "question_words": """
Sofia crossed her arms with a smile.

[bold cyan]"I'll give you answers. You figure out what question was asked!
Working backwards with question words shows true mastery.
Ready to prove you're a Curious Mind?"[/bold cyan]
""",
    "basic_sentences": """
Sofia pushed her notebook aside and leaned forward.

[bold cyan]"Everything comes together here. Sentences with the right gender,
the right verb form, the right word order. This is real Spanish.
Show me everything you've learned!"[/bold cyan]
""",
}
