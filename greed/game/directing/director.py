import time
import random
from game.shared.color import Color
from game.shared.point import Point
from game.casting.stone import Stone


#Armando to work on Director
class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service, COLS, ROWS, CELL_SIZE, FONT_SIZE):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._score = 0
        self.COLS = COLS
        self.ROWS = ROWS
        self.CELL_SIZE = CELL_SIZE
        self.FONT_SIZE = FONT_SIZE
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast, self.COLS, self.ROWS, self.CELL_SIZE, self.FONT_SIZE)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the #.
        
        Args:
            cast (Cast): The cast of actors.
        """

        player = cast.get_first_actor("players")
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)

    def _do_updates(self, cast, COLS, ROWS, CELL_SIZE,FONT_SIZE):
        """Updates the player position and resolves any collisions with stones.
        
        Args:
            cast (Cast): The cast of actors.
        """
        # banner = cast.get_first_actor("banners")
        # robot = cast.get_first_actor("robots")
        # gems = cast.get_actors("gems")
        # rocks = cast.get_actors("rocks")

        # banner.set_text("")
        # max_x = self._video_service.get_width()
        # max_y = self._video_service.get_height()
        # robot.move_next(max_x, max_y)
        
        # for rock in rocks:
        #     if robot.get_position().equals(rock.get_position()):
        #         pass
        #         # self._score.decrease() change to actual name of methods
        # for gem in gems:
        #     if robot.get_position().equals(gem.get_position()):
        #         pass
        #         # self._score.increase() change to actual name of methods    
        banner = cast.get_first_actor("banners")
        player = cast.get_first_actor("players")
        stones = cast.get_actors("stones")

        #banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)


        if self._video_service.window_timer() == 1:
          for  stone in stones:
            x = (stone._position.get_x())
            y = (stone._position.get_y() + 5)
            stone._position = Point(x,y)  

          characters = [42, 79] 
          text = chr(random.choice(characters))
         #message = message[n]

          x = random.randint(1, COLS - 1)
          y = random.randint(1, ROWS - 1)
          position = Point(x, 5)
          position = position.scale(CELL_SIZE)

          r = random.randint(0, 255)
          g = random.randint(0, 255)
          b = random.randint(0, 255)
          color = Color(r, g, b)

          # create the stones 
          stone = Stone()
          stone.set_text(text)
          stone.set_font_size(FONT_SIZE)
          stone.set_color(color)
          stone.set_position(position)
          #stone.set_message(message) #may not need
          cast.add_actor("stones", stone) 

        for stone in stones:
            if player.get_position().equals(stone.get_position()):
                stone.set_score()            
                points = stone.get_score()
                self._score += points
                cast.remove_actor("stone", stone)
                message = "Score: " + str(self._score)
                banner.set_text(message)    
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        # add a method in video_service to show the score
        self._video_service.flush_buffer()
        