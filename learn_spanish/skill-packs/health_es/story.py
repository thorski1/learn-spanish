"""
story.py — Narrative for the Health & Body skill pack.

Doctora Elena guides you through a warm Spanish clinic at sunset, teaching
vocabulary for body parts, feelings, doctor visits, pharmacy, and healthy habits.
"""

INTRO_STORY = """
[bold red]LEARN SPANISH[/bold red]
[bold yellow]Chapter: Health & Body[/bold yellow]

Warm amber light streamed through the tall windows
of a clinic perched on a quiet hillside, the sunset
casting long golden shadows across the tiled floor.
The soft hum of a ceiling fan and the faint scent
of lavender filled the waiting room.

[bold cyan]"Bienvenido a la Clínica del Sol,"[/bold cyan] said Doctora Elena,
stepping forward with a calm smile and a stethoscope
draped over her white coat. Her eyes were kind,
the sort that put nervous patients at ease instantly.
[bold cyan]"I've been a doctor in this city for twenty years,
and I'll tell you something -- knowing how to talk
about your body and health in another language
can change everything."[/bold cyan]

She gestured to a poster on the wall showing
the human body, labeled entirely in Spanish.
[bold yellow]"La cabeza, el brazo, la pierna...
Let's start with the basics."[/bold yellow]

[bold cyan]"By the time we're done, you'll know how to
describe symptoms, visit a doctor, get medicine
at the pharmacy, and talk about healthy habits --
all in Spanish. Ready for your check-up?"[/bold cyan]

[bold white]Learn to talk about health and the body in Spanish.[/bold white]
"""

ZONE_INTROS = {
    "body_parts": """
Doctora Elena pointed to the anatomical poster
on the wall, its colors glowing in the sunset light.

[bold cyan]"Every conversation about health starts here,"[/bold cyan]
she said, tracing the outline of the figure.
[bold cyan]"If you can name the parts of the body,
you can tell any doctor exactly where it hurts.
That's power."[/bold cyan]

[bold white]Let's learn the parts of the body in Spanish![/bold white]
""",
    "feelings_emotions": """
Doctora Elena sat down beside you,
her voice gentle as the evening light softened.

[bold cyan]"Health isn't just physical,"[/bold cyan] she said,
folding her hands thoughtfully.
[bold cyan]"How you feel -- happy, sad, tired, worried --
matters just as much. And being able to express
those feelings in another language?
That's real fluency."[/bold cyan]

[bold white]Let's learn to express feelings and emotions in Spanish![/bold white]
""",
    "at_the_doctor": """
Doctora Elena led you into the consultation room,
where the sunset painted the walls a warm copper.

[bold cyan]"This is where it gets real,"[/bold cyan] she said,
pulling up a chair and clicking her pen.
[bold cyan]"Symptoms, pain, fever, duration --
a doctor's visit requires clear communication.
The better you explain, the better the care
you'll receive."[/bold cyan]

[bold white]Let's learn to navigate a doctor's visit in Spanish![/bold white]
""",
    "pharmacy_medicine": """
Doctora Elena handed you a prescription slip
and gestured toward the door.

[bold cyan]"Next stop: la farmacia,"[/bold cyan] she said
with an encouraging nod.
[bold cyan]"Spanish pharmacists are incredibly knowledgeable.
But you need to know how to ask for what you need --
the right medicine, the right dosage,
and the right questions."[/bold cyan]

[bold white]Let's learn pharmacy and medicine vocabulary in Spanish![/bold white]
""",
    "healthy_habits": """
Doctora Elena leaned back as the last rays of sun
streamed through the window, a peaceful glow
settling over the clinic.

[bold cyan]"Prevention is the best medicine,"[/bold cyan] she said,
a warm smile crossing her face.
[bold cyan]"Exercise, sleep, nutrition, water, rest --
these are the habits that keep you out of my office.
Let me teach you how to talk about
living well in Spanish."[/bold cyan]

[bold white]Let's learn about healthy habits in Spanish![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "body_parts": """
[bold green]Doctora Elena tapped the poster proudly![/bold green]

[bold cyan]"Cabeza, brazo, pierna, mano, ojo, oreja --
you've got the whole body covered!
Now when something hurts, you can point
and name it. That's the foundation
of every medical conversation."[/bold cyan]
""",
    "feelings_emotions": """
[bold green]Doctora Elena nodded with genuine warmth![/bold green]

[bold cyan]"Feliz, triste, cansado, enfermo --
you can express how you truly feel now.
Not just 'bien' or 'mal,' but real,
nuanced emotions. That takes courage
and skill. Well done."[/bold cyan]
""",
    "at_the_doctor": """
[bold green]Doctora Elena closed her notebook with a satisfied click![/bold green]

[bold cyan]"Symptoms, duration, pain levels --
you handled the consultation like a pro.
Any doctor in the Spanish-speaking world
will understand you clearly now.
That's not just language -- that's safety."[/bold cyan]
""",
    "pharmacy_medicine": """
[bold green]Doctora Elena smiled as you pocketed the prescription![/bold green]

[bold cyan]"Farmacia, receta, pastilla, efectos secundarios --
you can navigate any pharmacy in Spain
or Latin America with confidence.
You know what to ask and what to watch for.
Your health is in good hands -- yours!"[/bold cyan]
""",
    "healthy_habits": """
[bold green]Doctora Elena stood and shook your hand as the stars appeared![/bold green]

[bold cyan]"Ejercicio, dormir, comer bien, agua, descansar --
you've learned the language of wellness.
From body parts to healthy habits,
you can now talk about every aspect
of health in Spanish.
¡Cuida tu salud -- take care of your health!"[/bold cyan]
""",
}

BOSS_INTROS = {
    "body_parts": """
Doctora Elena pointed to the examination table.

[bold cyan]"Imagine you're at the doctor and need
to explain exactly where it hurts.
Multiple locations, left or right --
can you describe it all clearly?
Show me what you've learned."[/bold cyan]
""",
    "feelings_emotions": """
Doctora Elena leaned forward attentively.

[bold cyan]"A friend asks how you're really feeling --
not just 'fine,' but the full picture.
Tired, sad, but improving?
Can you express that complexity
in Spanish?"[/bold cyan]
""",
    "at_the_doctor": """
Doctora Elena picked up her clipboard.

[bold cyan]"You're sitting in my office with real symptoms.
Fever, headache, two days --
can you give me the complete picture?
Symptoms, duration, extra details.
This is the real test."[/bold cyan]
""",
    "pharmacy_medicine": """
Doctora Elena held up the prescription.

[bold cyan]"You walk into a farmacia feeling unwell.
Can you greet the pharmacist, describe
your symptoms, ask for the right medicine,
and check if you need a prescription?
One smooth interaction. Go."[/bold cyan]
""",
    "healthy_habits": """
Doctora Elena crossed her arms with a smile.

[bold cyan]"A friend asks you for health advice.
Exercise, sleep, water, nutrition --
can you give them a complete wellness plan
in Spanish? Pull it all together.
This is your final check-up."[/bold cyan]
""",
}
