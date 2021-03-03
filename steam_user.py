class SteamUser:
    """"
    Create a class called SteamUser. Upon initialization it should receive username (string), games (list). It should also have an attribute called played_hours (0 by default). Add three methods to the class:
-	play(game, hours)
o	If the game is in the user games increase the played_hours by the given hours and return "{username} is playing {game}"
o	Otherwise, return "{game} is not in library"
-	buy_game(game)
o	If the game is not already in the user's games, add it and return "{username} bought {game}"
o	Otherwise return "{game} is already in your library"
-	stats() - returns "{username} has {games_count} games. Total play time: {played_hours}"
    """
    def __init__(self, username, games):
        self.username = username
        self.games = games
        self.played_hours = 0

    def play(self, game, hours):
        if game not in self.games:
            return f"{game} is not in library"
        self.played_hours += hours
        return f"{self.username} is playing {game}"

    def buy_game(self, game):
        if game not in self.games:
            self.games.append(game)
            return f"{self.username} bought {game}"
        else:
            return f"{game} is already in your library"

    def stats(self):
        return f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"


#user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
#print(user.play("Fortnite", 3))
#print(user.play("Oxygen Not Included", 5))
#print(user.buy_game("CS:GO"))
#print(user.buy_game("Oxygen Not Included"))
#print(user.play("Oxygen Not Included", 6))
#print(user.stats())
