import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point


class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.

    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._growing_trail(cast)
            self._handle_opponent_collision(cast)
            self._handle_segment_collision(cast)

            self._handle_game_over(cast)

    def _growing_trail(self, cast):
        """While the game is not over, the trails of the both snakes are growing.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snake = cast.get_first_actor("snakes")
        snake.grow_tail(1)
        snake2 = cast.get_second_actor("snakes")
        snake2.grow_tail(1)

    def _handle_opponent_collision(self, cast):
        """The game is over when the snake collides with the opponent, the other gamer.

        Args:
            cast (Cast): The cast of Actors in the game.
        """

        snake = cast.get_first_actor("snakes")
        segments = snake.get_segments()[1:]
        head = snake.get_head()
        score01 = cast.get_first_actor("score")

        snake2 = cast.get_second_actor("snakes")
        segments_S2 = snake2.get_segments()[1:]
        head_S2 = snake2.get_head()
        score02 = cast.get_second_actor("score")

        for segment_S2 in segments_S2:
            if head.get_position().equals(segment_S2.get_position()):
                self._is_game_over = True
                score02.add_points(1)

        for segment in segments:
            if head_S2.get_position().equals(segment.get_position()):
                self._is_game_over = True
                score01.add_points(1)

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snake = cast.get_first_actor("snakes")
        head = snake.get_segments()[0]
        segments = snake.get_segments()[1:]
        score01 = cast.get_first_actor("score")

        snake2 = cast.get_second_actor("snakes")
        head_S2 = snake2.get_segments()[0]
        segments_S2 = snake2.get_segments()[1:]
        score02 = cast.get_second_actor("score")

        for segment in segments:
            if head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                score02.add_points(1)

        for segment_S2 in segments_S2:
            if head_S2.get_position().equals(segment_S2.get_position()):
                self._is_game_over = True
                score01.add_points(1)

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            snake = cast.get_first_actor("snakes")
            segments = snake.get_segments()

            snake2 = cast.get_second_actor("snakes")
            segments_S2 = snake2.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)

            for segment_02 in segments_S2:
                segment_02.set_color(constants.WHITE)
