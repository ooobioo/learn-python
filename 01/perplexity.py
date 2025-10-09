import random

print("Willkommen bei der magischen Python-Kugel!")
name = input("Wie heißt du? ")

fragen = [
    "Werde ich heute Glück haben?",
    "Soll ich mehr Python lernen?",
    "Wird das Wetter morgen gut?",
    "Gibt es bald Kuchen?",
    "Werde ich reich?"
]

antworten = [
    "Definitiv ja!",
    "Frag später nochmal.",
    "Das sieht nicht gut aus.",
    "Super Idee!",
    "Das ist ein großes Geheimnis.",
    "Vielleicht...",
    "Nur, wenn du lächelst!",
    "Klar doch!"
]

frage = random.choice(fragen)
input(f"{name}, stelle eine Frage: '{frage}' (drücke Enter) ")

print("Die magische Kugel sagt:", random.choice(antworten))
