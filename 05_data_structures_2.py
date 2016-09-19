#!/usr/bin/env python2

def morse_code(text):
    """
    Convert the given text to morse code (i.e. dots and dashes).  You can find 
    the morse code alphabet here:

    https://en.wikipedia.org/wiki/Morse_code

    Represent each morse code character using '.' and '-', and use a space to 
    separate each letter.  For example, "ucsf" would become:

    ..- -.-. ... ..-.
    """
    pass

def braille(text):
    """
    Convert the given text to english braille (also called grade-2 braille).  
    There are many different braille alphabets in use, but english braille is
    an interesting one because it includes abbreviations for commonly used 
    words (e.g. "and", "of", the") and digraphs (e.g. "sh", "er", "th").  You 
    can find a full description of the alphabet here:

    https://en.wikipedia.org/wiki/English_Braille#Alphabet

    Represent each braille character using up to six dots spanning up to three 
    lines, and use a space to each letter.  For example, "ucsf" would become:

    .  ..  . ..
          .  . 
    ..    .    

    Think about the data structure you want to use the store the translation 
    between print and morse letters.  You will have to convert everything in 
    the top row before you can jump to the next line and start converting the 
    middle row, and your data structure should help make this easy to do.  Also 
    think about what you would need to do to convert abbreviations (e.g. words 
    and digraphs) when they appear, and how your data structure could make this 
    easier or harder.
    """
    pass


# Part 1: Convert the following text to morse code:
print morse_code("purple haze")

# Part 2: Convert the following text to braille:
print braille("rocket man")

# Part 3: Add support for numbers to your braille converter:
print braille("8675309")

# Part 4: Add support for common words and digraphs to you braille converter:
print braille("twist and shout")

# Part 5: Add support for upper-casing to your braille converter:
print braille("Hey Jude")

