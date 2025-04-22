import random
from app.chords import CHORDS
from app.exporter import export_tabs


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


def generate_chords(count=2, sets=3, export=None, no_tab=False):
    generated_tablatures = []

    for i in range(sets):
        chosen_chords = pick_random_chords(count)
        tablature = assemble_chord_tablature(chosen_chords)
        print(f"Set {i+1}")
        print(str(tablature[0]))  # print chord names
        generated_tablatures.append(tablature)
        # Unless --no-tab is used, always print each set's ASCII tab and a separator
        if not no_tab:
            print(*tablature[1:], sep="\n")
            print("")

    if export:
        export_tabs(generated_tablatures, export)
