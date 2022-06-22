import constants

from game.casting.cast import Cast
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point
from game.casting.snake import Snake
from game.scripting.control_actors_snake2 import ControlActorsAction_player2
from game.casting.score import Score

def main():

    # create the cast
    cast = Cast()

    # This is for create the label of the score in the top of the screen.
    cast.add_actor("score", Score())

    # This is the second label for the score of the other gamer
    score2 = Score()
    score2.set_position(Point(800, 0))
    cast.add_actor("score", score2)
    
    # create player 1
    player_1 = Snake()
    player_1.set_color(constants.YELLOW)
    player_1.set_segment_color(constants.GREEN)
    player_1.set_buttons(["w", "a", "s", "d"])
    cast.add_actor("snakes", player_1)

    # create player 2
    player_2 = Snake()
    player_2.set_color(constants.RED)
    player_2.set_segment_color(constants.PURPLE)
    player_2.set_buttons(["i", "j", "k", "l"])
    cast.add_actor("snakes", player_2)

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("input", ControlActorsAction_player2(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))

    director = Director(video_service)
    director.start_game(cast, script)

if __name__ == "__main__":
    main()
