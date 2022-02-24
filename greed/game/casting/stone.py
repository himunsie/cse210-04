from game.casting.actor import Actor

# Diego to work on

class Stone(Actor):
    """
     
    
    The responsibility of an Stone is to provide a point system when a stone (gem or rock) is collected.

    """
    def __init__(self):
        super().__init__()
        self._score = 0
   


    def get_score(self):
        """Gets the artifact's message.
        
        Returns:
            string: The message.
        """
        return self._score
    
    def set_score(self):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        
        """
        if self._text == "*":
            self._score += 10
        else:
            self._score -= 10
