import random
from chords import CHORDS
import argparse

parser = argparse.ArgumentParser(
    description="Generate random chord progressions and accompanying tabs"
)

parser.add_argument(
    "--no-tab",
    action="store_true",
    default=False,
    help="Do NOT generate an ASCII tab for the chords.",
)

args = parser.parse_args()


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
print("Chords:", ", ".join(chord_names))

if not args.no_tab:
    tablature = create_tablature(chosen_chords)
    print(*tablature, sep="\n")
