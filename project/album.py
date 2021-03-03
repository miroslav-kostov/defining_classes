from project.song import Song


class Album:
    def __init__(self, name: str, songs=[]):
        self.name = name
        self.songs = [songs]
        self.published = False

    def add_song(self, song: Song):
        res = f""
        if song.single == True:
            res = f"Cannot add {song.name}. It's a single"
        elif self.published == True:
            res = f"Cannot add songs. Album is published."
        elif song in self.songs:
            res = f"Song is already in the album."
        else:
            self.songs.append(song)
            res = f"Song {song.name} has been added to the album {self.name}."
        return res

    def remove_song(self, song_name: str):
        res = ""
        if self.published == True:
            return f"Cannot remove songs. Album is published."
        current_song = [song for song in self.songs if song.name == song_name][0]
        if current_song:
            self.songs.remove(current_song[0])
            res = f"Removed song {song_name} from album {self.name}."
        else:
            res = "Song is not in the album."
        return res

    def details(self):
        res = f"Album {self.name}\n"
        for current_song in self.songs:
            res += f"== {current_song.get_info()}\n"
        return res

    def publish(self):
        if self.published == True:
            return f"Album {self.name} is already published."
        else:
            self.published = True
            return f"Album {self.name} has been published."