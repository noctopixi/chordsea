from pathlib import Path
from datetime import datetime


def export_tabs(tabs, output_file="tabs.txt"):
    # Generate a Big endian timestamp (YYYY.mm.dd)
    timestamp = datetime.now().strftime("%Y.%m.%d")
    output_str = f"{timestamp}\n"
    for i, t in enumerate(tabs):
        # Each tab is a list of 7 strings: the chord names, and fingerings for the 6 guitar strings
        # Join all strings items in a tab with a newline
        output_str += f"\nSet {i+1}\n" + "\n".join(t)

    Path(output_file).write_text(output_str, encoding="utf-8")
    return output_str
