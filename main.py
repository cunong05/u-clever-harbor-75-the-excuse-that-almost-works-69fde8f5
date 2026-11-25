#!/usr/bin/env python3
"""Writes the entry line to /output/entry.txt."""

import os

ENTRY = "sorry boss my keycard died in the update, security says new ones friday, locked out till then"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
