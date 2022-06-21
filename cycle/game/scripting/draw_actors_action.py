from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.

    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.

        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        snake = cast.get_first_actor("snakes")
        segments = snake.get_segments()

        snake2 = cast.get_second_actor("snakes")
        segments_2snake = snake2.get_segments()

        self._video_service.draw_actors(segments_2snake)
        self._video_service.draw_actors(segments)
        self._video_service.clear_buffer()

        self._video_service.flush_buffer()
