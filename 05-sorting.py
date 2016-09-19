# Python Sorting Exercise

# Metadata about your lovely bootcamp TAs.
tas_dict = {"Erin Poss": {"year": 3, "lab": "Fraser", "program": "CCB"},
            "Seth Axen": {"year": 3, "lab": "Sali", "program": "iPQB"},
            "Charlotte Nelson": {"year": 2, "lab": "Baranzini/Butte",
                                 "program": "iPQB"},
            "Kale Kundert": {"year": 5, "lab": "Kortemme", "program": "iPQB"}}


# Examples #

def sort_by_name(d, decreasing=False):
    """Print names of TAs sorted by name. Sorting is by default always
       alphanumerically increasing. If we want them in decreasing order, we
       can reverse the sort."""
    for name in sorted(tas_dict.keys(), reverse=decreasing):
        print(name)


def _year_from_dict(x):
    """From a tuple containing a TA's name and info, get the year."""
    name, info = x
    return info["year"]


def sort_by_decreasing_year(d):
    """Let's find the most sagely TA by sorting by year in decreasing order.
       Now we need to specify a "key" argument. This is just a function that
       takes one argument (an item) and returns a list, tuple, string, or
       number that reflects how the items should be alphanumerically sorted.
       dict.items() is a simple way to get the (key, value) pairs in a dict.
    """
    for name, info in sorted(tas_dict.items(), key=_year_from_dict,
                             reverse=True):
        print(name + ": " + str(info["year"]) + " year")


# Functions to be completed #

def sort_by_lastname(d):
    """Print TA names sorted by last name."""
    pass


def sort_by_lab_lastname(d):
    """Print TA names sorted by lab then last name."""
    pass


def sort_by_year_program_lastname(d):
    """Print TA names sorted by year, then program, then last name."""
    pass


def sort_by_vowel_count(d):
    """Print TA names sorted by number of vowels in name."""
    pass


# part 1: print TA names sorted by last name
sort_by_lastname(tas_dict)

# part 2: print TA names sorted by lab then last name
sort_by_lab_lastname(tas_dict)

# part 3: print TA names sorted by lab then last name
sort_by_year_program_lastname(tas_dict)

# part 4: print TA names sorted by vowel count
sort_by_vowel_count(tas_dict)
