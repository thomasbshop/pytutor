# circular references
# NB: download albums.zip file


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


class Album:
    """ Class to represent an album, using it's track list

    Attributes:
        name (str): The name of the album.
        year (int): The year the album was released.
        artist: (Artist): The artist responsible for the album. If not specified,
        the artist will default to an artist with te name 'Various Artists'.
        tracks (List[Song]): A list of the songs on the album.

    Methods:
        addSong: Used to add a new song to the album's track list.
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """Adds a song to the track-list

        Args:
            song (Song): A song to add.
            position (Optional[int]): If specified, the song will be added to that position
                in the track list - inserting it between other songs if necessary.
                Otherwise, the song will be added to the end of the list.
            """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """Basic class to store artist details.

    Attributes:
    name (str): The name of the artist.
    albums (List[Album]): A list of the albums by this artist.
        The list includes only those albums in this collection, it is
        not an exhaustive list of the artist's published albums.

    Methods:
        add_album: use to add a new album to the artist's albums list.
     """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list.

        Args:
            album (Album): Album object to add to the list.
                If the album is already present, it will not be added again (although this is yet to be implemented.
        """

        self.albums.append(album)


def find_object(field, object_list):
    """Check object_list to see if an object with a 'name' attribute equal to 'field' exists, return it if so."""
    # this is brute force - there are faster ways to search items in a list(require the list tobe sorted would make
    #  the code less efficient. An approach would be to sort the data in a file).
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            # data row should consist of (track_number,	track,	artist,	album,	time)
            track_field, song_field, artist_field, album_field, length_field = tuple(line.strip('\n').split('\t'))
            track_field = int(track_field)
            print("{}:{}:{}:{}:{}".format(track_field, song_field, artist_field, album_field, length_field))

            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            elif new_artist.name != artist_field:
                # We've just read details for a new artist
                # retrieve the artist object if there is one,
                # otherwise create a new artist object and add it to the artist list.
                new_artist = find_object(artist_field, artist_list)
                if new_artist is None:
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, album_field, new_artist)
                new_artist.add_album(new_album)
            elif new_album.name != album_field:
                # We'eve just read a new album for the current artist
                # Retrieve the album object if there is one,
                # otherwise create a new album object and store it in the artist's collection.
                new_album = find_object(album_field, new_artist.albums)
                if new_album is None:
                    new_album = Album(album_field, album_field, new_artist)
                    new_artist.add_album(new_album)

            # create a new song object and add it to the current album's collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

    return artist_list


def create_checkfile(artist_list):
    """create a check file from the object data for comparison with the original file"""
    with open("check_file.txt", 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.name}\t{2.title}".format(new_artist, new_album, new_song),
                          file=checkfile)


if __name__ == "__main__":  # run if the program is executed as a script.
    artists = load_data()
    print("There are {} artists.".format(len(artists)))
    create_checkfile(artists)
