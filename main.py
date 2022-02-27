#!/usr/bin/env python3

TOPICS = ["adjectives", "occupations", "genres", "movies"]

import random


def read(path):
    with open(path, encoding="utf-8") as f_in:
        text = f_in.read()

    return text.splitlines()


def rand(items):
    return random.choice(items)


def main():
    """
    Command-line entry-point.
    """
    vocab = {topic: read(f"{topic}.txt") for topic in TOPICS}

    a = rand(vocab["adjectives"])
    o = rand(vocab["occupations"])

    g1 = rand(vocab["genres"])
    i = vocab["genres"].index(g1)
    vocab["genres"].pop(i)
    g2 = rand(vocab["genres"])

    b1 = rand(vocab["movies"])
    i = vocab["movies"].index(b1)
    vocab["movies"].pop(i)
    b2 = rand(vocab["movies"])

    title = f"The {a.title()} {o.title()}"
    genres = f"A {g1} {g2} story"
    based = f"{b1} meets {b2}"

    print(title)
    print()
    print(genres)
    print()
    print(based)


if __name__ == "__main__":
    main()
