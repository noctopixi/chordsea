from app.chords import CHORDS
from app.generator import generate_chords
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
    count = int(args.count)
    sets = int(args.sets)

    # Check if the desired number of chords is higher than the available count in chords.py
    if count > NUM_AVAILABLE_CHORDS or count <= 0:
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

generate_chords(count, sets, args.export, args.no_tab)
