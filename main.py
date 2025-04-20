import random
from chords import CHORDS
import argparse
from exporter import export_tabs

NUM_AVAILABLE_CHORDS = len(CHORDS.keys())


def pick_random_chords(count=2):
    # Convert chords to a sequence that random.sample can go through
    iterable_chords = list(CHORDS.values())
    random_chords = random.sample(iterable_chords, count)
    return random_chords


def create_string_tabs(chosen_chords):
    STRINGS = ["e", "B", "G", "D", "A", "E"]
    tablature = []
    # Create tablature by going over the 6 strings and adding each chord's fingering
    for string_num, string_name in enumerate(STRINGS):
        separated_fingerings = ""
        for chord in chosen_chords:
            # Fingerings are in tab notation, starting from string 1 (high 'e')
            fret = chord["tab_fingering"][string_num]
            separated_fingerings += f"---{fret}"
        # Start each line w/ string name; end with --- to match separators
        tablature.append(f"{string_name}|{separated_fingerings}---")
    return tablature


# Assemble a full tab for chosen chords
def assemble_chord_tablature(chosen_chords):
    chord_names = [chord["short_name"] for chord in chosen_chords]
    string_tabs = create_string_tabs(chosen_chords)
    tablature = [", ".join(chord_names)]
    tablature.extend(string_tabs)
    return tablature


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
    help=f"Number of chords to generate per set. Default: 2. Max: {NUM_AVAILABLE_CHORDS}",
)
parser.add_argument(
    "--export",
    # Export generated tabs to a text file. Filename can be specified.
    nargs="?",
    const="tabs.txt",
    default=None,
    help=f"Create a text file with the generated chord tabs. Default: tabs.txt",
)
parser.add_argument(
    "--sets",
    default=3,
    help=f"Number of chord sets to generate. Default: 3 (a typical practice lasts 15m, 5m per set)",
)
args = parser.parse_args()


# Validate arguments: --count, --sets
try:
    # If input cannot be converted to an integer, throws a TypeError
    COUNT = int(args.count)
    sets = int(args.sets)

    # Check if the desired number of chords is higher than the available count in chords.py
    if COUNT > NUM_AVAILABLE_CHORDS or COUNT <= 0:
        raise ValueError(
            f"There are {NUM_AVAILABLE_CHORDS} chords to choose from. Please specify a number within that limit."
        )

    if sets <= 0:
        raise ValueError(
            f"At least 1 set of chords must be generated. Please specify a number equal or higher than 1."
        )

except Exception as e:
    # Catch errors and exit gracefully
    print(f"ERROR: {e}")
    exit(1)

generated_tablatures = []

for i, s in enumerate(range(sets)):
    chosen_chords = pick_random_chords(COUNT)
    tablature = assemble_chord_tablature(chosen_chords)
    print(f"Set {i+1}")
    print(str(tablature[0]))  # print chord names
    generated_tablatures.append(tablature)
    # Unless --no-tab is used, always print each set's ASCII tab and a separator
    if not args.no_tab:
        print(*tablature[1:], sep="\n")
        print("")

if args.export:
    export_tabs(generated_tablatures, args.export)
