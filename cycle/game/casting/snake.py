from tkinter.tix import MAX
import constants
import random
from game.casting.actor import Actor
from game.shared.point import Point


class Snake(Actor):
    """
    A long limbless reptile.

    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """

    def __init__(self):
        super().__init__()
        self._segments = []
        self._prepare_body()
        self._segment_color = constants.GREEN
        self._buttons = []

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(self._segment_color)
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)

    def get_segment_color(self):
        """Gets the actor's segment color as a tuple of three ints (r, g, b).

        Returns:
            Color: The actor's text color.
        """
        return self._segment_color

    def set_segment_color(self, color):
        """Updates the segment color to the given one.

        Args:
            color (Color): The given color.
        """
        self._segment_color = color

    def get_buttons(self):
        """Gets the snake's button list and returns it.
        Returns:
            Color: The actor's text color.
        """
        return self._buttons

    def set_buttons(self, buttons):
        """Updates the button list with the new given buttons.

        Args:
            buttons: The given buttons.
        """
        self._buttons = buttons

    def _prepare_body(self):
        x = constants.CELL_SIZE * 4 + \
            random.randrange(0, 30) * constants.CELL_SIZE
        #x = int(random.randrange(100, 801))
        y = int(constants.MAX_Y / 2)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE,
                             y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = self._color if i == 0 else self._segment_color

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)
