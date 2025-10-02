#!/usr/bin/env python3
"""
SD5913 Assignment 3 - Starter script.

Usage examples:
  python main.py
  python main.py --name Alice
"""

from __future__ import annotations

import argparse
from typing import Optional

def greet(name: Optional[str] = None) -> str:
    """Return a greeting message for the provided name (defaults to 'world')."""
    person = name or "world"
    return f"Hello, {person}!"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Assignment 3 starter CLI.")
    parser.add_argument("--name", "-n", help="Name to greet")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    name = args.name
    if not name:
        name = input("Please enter your name: ")
        name = input("Please enter your name: ")
        print(f"Hello, {name}!")


if __name__ == "__main__":
    main()
