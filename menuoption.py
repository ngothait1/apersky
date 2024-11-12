from enum import Enum, auto

class MenuOption(Enum):
    SAVE_NEW_ENTRY = auto()
    SEARCH_BY_ID = auto()
    PRINT_AGES_AVERAGE = auto()
    PRINT_ALL_NAMES = auto()
    PRINT_ALL_IDS = auto()
    PRINT_ALL_ENTRIES = auto()
    PRINT_ENTRY_BY_INDEX = auto()
    SAVE_ALL_DATA = auto()
    EXIT = auto()

# Tests
if __name__ == "__main__":
    print("Notice: This file is meant to be used by the main program only.")