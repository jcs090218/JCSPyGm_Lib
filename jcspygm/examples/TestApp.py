#  ========================================================================
#  $File: TestApp.py $
#  $Date: 2016-10-14 20:41:55 $
#  $Revision: $
#  $Creator: Jen-Chieh Shen $
#  $Notice: See LICENSE.txt for modification and distribution information
#                     Copyright (c) 2016 by Shen, Jen-Chieh $
#  ========================================================================

from jcspygm.core.JCSPyGm_Application import JCSPyGm_Application
from jcspygm.examples.Game import Game


class TestApp(JCSPyGm_Application):

    """Test application
    """

    __testGame = None
    __appTitle = "Example Game - JCSPyGm Lib"

    def __init__(self):
        """Constructor."""

        # call the base constructor
        super(TestApp, self).__init__()

        self.__testGame = Game()

        # NOTE(jenchieh): here is how u set the title.
        self.get_window().set_window_title(self.__appTitle)
        
        self.get_window().update_window_title()
        
        # here is how u decide to show the window info.
        self.set_show_frame_rate(True)

    def _run_app(self, deltaTime, windowInfo):
        """Run the application."""

        self.get_game().run(deltaTime, windowInfo)

    def get_game(self):
        """Return the game itself."""
        return self.__testGame
