import random
from chords import CHORDS


def pick_random_chords(num=2):
    iterable_chords = list(CHORDS.values())
    random_chords = random.sample(iterable_chords, num)
    return random_chords


def create_tablature(chosen_chords):
    STRINGS = ["e", "B", "G", "D", "A", "E"]
    diagram = []
    for string_num, string_name in enumerate(STRINGS):
        separated_fingerings = ""
        for chord in chosen_chords:
            # Fingerings are in tab notation, starting from string 1 (high 'e')
            fret = chord["tab_fingering"][string_num]
            separated_fingerings += f"---{fret}"
        # Start each line w/ string name; end with --- to match separators
        diagram.append(f"{string_name}|{separated_fingerings}---")
    return diagram


chosen_chords = pick_random_chords()
chord_names = [chord["short_name"] for chord in chosen_chords]
tablature = create_tablature(chosen_chords)


print("Chord pair:", ", ".join(chord_names))
print(*tablature, sep="\n")
