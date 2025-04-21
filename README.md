# Chordmuse 🎶

## Overview

This Python script selects random guitar chords and creates practice sets with ASCII tabs.

It's perfect for practicing guitar chord changes or simply generating chord progressions to explore new sounds.

## Features

- Creates sets of chords to practice guitar chord changes (by default, 3 sets of 2 chords each).
- Generates ASCII tablatures for each chord set in standard E tuning (EADGBe).
- Allows exporting chords to a text file (by default, tabs.txt)

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/noctopixi/chord-selector.git
    ```

2. **Navigate to the project directory**:

    ```bash
    cd chord-selector
    ```

## Usage

1. **Run the script**:

    ```bash
    python main.py
    ```

2. **Customize chord generation with command line arguments**:
   The following arguments are available:

    ```bash
    --no-tab           Do NOT generate an ASCII tab for the chords.
    --count COUNT      Number of chords to generate per set. Default: 2. Max: 16
    --export [EXPORT]  Create a text file with the generated chord tabs. Default: tabs.txt
    --sets SETS        Number of chord sets to generate. Default: 3 (a typical practice lasts 15m, 5m per set)
    ```

## Example Output

```bash
$ python main.py
Chord pair: Am, Cadd9
e|---0---0---
B|---1---3---
G|---2---0---
D|---2---2---
A|---0---3---
E|---x---x---
```

## License

You may view the LICENSE in which this software is provided to you [here](LICENSE).
