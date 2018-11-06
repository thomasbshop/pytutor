# A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition.
# Such a docstring becomes the __doc__ special attribute of that object.
# docstrings can be used to document modules, functions, classes and methods.

# NB: rawstring - r"this is a raw string"


class Song:
    """ A class to represent a song

    Artist:
        title(str): the title of the song.
        artist(Artist): an artist object representing the song's creator.
        duration(int): duration of the song in seconds. may be zero
    """

    def __init__(self, title, artist, duration=0):
        """Song init method

        Args:
            title (str): initialises the title attribute
            artist (Artist): At Artist object representing the song's creator.
            duration (Optional[int]: Initial value for the duration attribute.
                Will default to zero if not specified.
        """

        self.title = title
        self.artist = artist
        self.duration = duration


help(Song)
help(Song.__init__)  # Help on function __init__ in module __main__
print(Song.__doc__)
print(Song.__init__.__doc__)

# you can also do this
Song.__init__.__doc__ = """Song init method

        Args:
            title (str): initialises the title attribute
            artist (Artist): At Artist object representing the song's creator.
            duration (Optional[int]: Initial value for the duration attribute.
                Will default to zero if not specified.
        """