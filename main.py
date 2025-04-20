import random
from chords import CHORDS
import argparse
from exporter import export_tabs

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
parser.add_argument(
    "--export",
    # Export generated tabs to a text file. Filename can be specified.
    nargs="?",
    const="tabs.txt",
    default=None,
    help=f"Create a text file with the generated chord tabs. Default: tabs.txt",
)
args = parser.parse_args()


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


# Validate the --count argument
try:
    # If input cannot be converted to an integer, throws a TypeError
    COUNT = int(args.count)

    # Check if the desired number of chords is higher than the available count in chords.py
    if COUNT > NUM_AVAILABLE_CHORDS or COUNT <= 0:
        raise ValueError(
            f"There are {NUM_AVAILABLE_CHORDS} chords to choose from. Please specify a number within that limit."
        )
    chosen_chords = pick_random_chords(COUNT)

except Exception as e:
    # Catch errors and exit gracefully
    print(f"ERROR: {e}")
    exit(1)

generated_tablatures = []
tablature = assemble_chord_tablature(chosen_chords)
print(str(tablature[0]))  # print chord names
generated_tablatures.append(tablature)

if args.export:
    export_tabs(generated_tablatures, args.export)

# Unless --no-tab is used, always print the ASCII tabs
if not args.no_tab:
    for tablature in generated_tablatures:
        print(*tablature[1:], sep="\n")
