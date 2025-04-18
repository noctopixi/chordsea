# Chordmuse 🎶

## Overview

This Python script selects random guitar chords and generates tabs.

It's perfect for practicing guitar or simply generating chord progressions to explore new sounds.

## Features

- Selects a specified number of random guitar chords (default is 2).
- Generates a simple ASCII tablature for the selected chords in standard E tuning (EADGBE).

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

2. **Customize the number of chords**:
   You can change the default number of chords by modifying the `num` parameter in the `pick_random_chords` function.
   NOTE: support for command line arguments coming soon!

## Example Output

```
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
