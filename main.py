import random
from chords import CHORDS
import argparse

NUM_AVAILABLE_CHORDS = len(CHORDS.keys())

# Set and load user arguments. By default, the script generates 2 random chords with ASCII tabs.
parser = argparse.ArgumentParser(
    description="Generate random chord progressions and accompanying tabs"
)
parser.add_argument(
    "--no-tab",
    action="store_true",
    default=False,
    help="Do NOT generate an ASCII tab for the chords.",
)
parser.add_argument(
    "--count",
    default=2,
    help=f"Number of chords to generate. Default: 2. Max: {NUM_AVAILABLE_CHORDS}",
)
args = parser.parse_args()

# Validate the --count argument
try:
    # If input cannot be converted to an integer, throws a TypeError
    COUNT = int(args.count)

    # Check if the desired number of chords is within range
    if COUNT > NUM_AVAILABLE_CHORDS:
        raise ValueError(
            f"There are {NUM_AVAILABLE_CHORDS} chords to choose from. Please specify a number within that limit."
        )
except Exception as e:
    # Catch errors and exit gracefully
    print(f"ERROR: {e}")
    exit(1)


def pick_random_chords(count=2):
    # Convert chords to a sequence that random.sample can go through
    iterable_chords = list(CHORDS.values())
    random_chords = random.sample(iterable_chords, count)
    return random_chords


def create_tablature(chosen_chords):
    STRINGS = ["e", "B", "G", "D", "A", "E"]
    diagram = []
    # Create tablature by going over the 6 strings and adding each chord's fingering
    for string_num, string_name in enumerate(STRINGS):
        separated_fingerings = ""
        for chord in chosen_chords:
            # Fingerings are in tab notation, starting from string 1 (high 'e')
            fret = chord["tab_fingering"][string_num]
            separated_fingerings += f"---{fret}"
        # Start each line w/ string name; end with --- to match separators
        diagram.append(f"{string_name}|{separated_fingerings}---")
    return diagram


# Error and exit gracefully if the user requested a chord count higher than the currently known count
try:
    chosen_chords = pick_random_chords(COUNT)
except ValueError as e:
    print(f"ERROR: {e}")
    exit(1)

chord_names = [chord["short_name"] for chord in chosen_chords]
print(", ".join(chord_names))

# Unless --no-tab is used, always print an ASCII tab
if not args.no_tab:
    tablature = create_tablature(chosen_chords)
    print(*tablature, sep="\n")
