from logger import Logger
from flashcard import Flashcards
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Description how to use this Flashcards')
    parser.add_argument('--import_from')
    parser.add_argument('--export_to')
    args = parser.parse_args()
    flashcards = Flashcards(Logger(), args).start()
