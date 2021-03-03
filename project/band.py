from project.album import Album
from project.song import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            res = f"Band {self.name} already has {album.name} in their library."
        else:
            res = f"Band {self.name} has added their newest album {album.name}."
            self.albums.append(album)
        return res

    def remove_album(self, name: str):
        if self.albums:
            current_album = [a for a in self.albums if a.name == name][0]
            res = ""
            if current_album:
                if current_album.published:
                    res = "Album has been published. It cannot be removed."
                else:
                    res = f"Album {name} has been removed."
                    self.albums.remove(current_album)
            else:
                res = f"Album {name} is not found."
            return res
        else:
            return f"Album {name} is not found."

    def details(self):
        res = f"Band {self.name}\n"
        for current_album in self.albums:
            res += f"{current_album.details()}\n"
        return res

#song = Song("Running in the 90s", 3.45, False)
#print(song.get_info())
#album = Album("Initial D", song)
#second_song = Song("Around the World", 2.34, False)
#print(album.add_song(second_song))
#print(album.details())
#print(album.publish())
#band = Band("Manuel")
#print(band.add_album(album))
#print(band.remove_album("Initial D"))
#print(band.details())
