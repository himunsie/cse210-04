#Armando to work on Director
class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._score = 0
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
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

    def _do_updates(self, cast):
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

        banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)
        
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
        