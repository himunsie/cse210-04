from game.casting.actor import Actor

# Diego to work on

class Stone(Actor):
    """
     
    
    The responsibility of an Stone is to provide a point system when a stone (gem or rock) is collected.

    """
    def __init__(self):
        super().__init__()
        
        
    def get_message(self): #update and rename method
        """Gets the Stone's value in points
        
        Returns:
            
        """
        return self._message
    
    def set_message(self, message): #update and rename method
        """Updates points based on type of stone collected (gem or rock).
        
        Args:
           
        """
        self._message = message