#!/usr/bin/env python2

from pprint import pprint

def part_1(data, tsv_path):
    """
    Save the given dictionary to the given file using the tab-separated value 
    (TSV) format.

    You can think of TSV files like Excel spreadsheets because they organize 
    data into rows and columns.  The columns are separated by tabs ('\t') and 
    the rows are separated by newlines ('\n').  A nice feature of the TSV 
    format is that Excel understands it, so you can look at your saved data in 
    Excel to make sure it looks right.
    
    Make one row in your TSV file for each entry in the given dictionary.  Save 
    the keys in the first column and the values in the second.
    """
    pass

def part_2(tsv_path):
    """
    Load a dictionary from the given TSV file and return it.

    This function is exactly the opposite of part_1().  If the TSV file given 
    to this function was created by part_1(), the dictionary returned by this 
    function should be identical to the one passed to part_1().

    Note that you get strings when you read data from a file, even if the data 
    are numeric.  Use the ``int()`` function to convert a string to a integer 
    and the ``float()` function to convert a string to a real number.
    """
    pass

def part_3(data, pkl_path):
    """
    Save the given dictionary to the given pickle (*.pkl) file.

    The pickle module can save almost any python object (dicts, lists, dicts of 
    lists, lists of dicts, tuples, sets, custom classes, etc.) to a file so it 
    can be loaded back into python later.  It's usually much easier to pickle 
    data than to write your own code to read and write a file.
    
    Read this page to learn how to use the pickle module:
    https://docs.python.org/2/library/pickle.html
    """
    pass

def part_4(pkl_path):
    """
    Load a dictionary from the given pickle file and return it.
    """
    pass


word_lens = {
        'already': 7,
        'audacity': 8,
        'crunch': 6,
        'formula': 7,
        'grieving': 8,
        'heartless': 9,
        'marble': 6,
}

print "Writing a TSV file..."
part_1(word_lens, 'word_lens.tsv')

print "Reading a TSV file..."
pprint(part_2('word_lens.tsv'))

print "Writing a pickle file..."
part_3(word_lens, 'word_lens.pkl')

print "Reading a TSV file..."
pprint(part_4('word_lens.pkl'))

