from game.casting.actor import Actor


class Score(Actor):
    """
    A record of points made. 

    The responsibility of Score is to keep track of the points the player has earned by make the opponent lost.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _nameGamer (str): this is for the label score at the top of the screen.
        _points (int): The points earned in the game.
    """

    def __init__(self):
        self._nameGamer = ""

        super().__init__()
        self._points = 0
        self.add_points(0)

    def add_points(self, points):
        """Adds the given points to the score's total points.

        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"{self._nameGamer}: {self._points}")

    def label_name_player(self, namePlayer):
        """Adds the label name of the score of both players.

        Args:
            namePlayer (string): The name of the gamer.
        """
        self._nameGamer = namePlayer
