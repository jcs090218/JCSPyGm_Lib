#  ========================================================================
#  $File: JCSPyGm_SceneManager.py $
#  $Date: 2016-10-27 21:59:41 $
#  $Revision: $
#  $Creator: Jen-Chieh Shen $
#  $Notice: See LICENSE.txt for modification and distribution information
#                     Copyright (c) 2016 by Shen, Jen-Chieh $
#  ========================================================================

from jcspygm import JCSPyGm
from jcspygm.core.JCSPyGm_Camera import JCSPyGm_Camera
from jcspygm.core.JCSPyGm_GameObject import JCSPyGm_GameObject
from jcspygm.core.JCSPyGm_Sprite import JCSPyGm_Sprite
from jcspygm.managers.JCSPyGm_SoundManager import JCSPyGm_SoundManager
from jcspygm.util.JCSPyGm_Debug import JCSPyGm_Debug


class JCSPyGm_SceneManager(object):

    """Manager class take care of the scene 
    and switch scene.
    """

    # --------------------------------------------
    # Public Variables
    # --------------------------------------------
    instance = None
    
    # default fade in and out time.
    BGM_SOUND_FADEIN_TIME = 1000 * 1    # (ms)
    BGM_SOUND_FADEOUT_TIME = 1000 * 1   # (ms)
    
    # default fade scene time.
    SCENE_FADEIN_TIME = 1.5     # (seconds)
    SCENE_FADEOUT_TIME = 1.5    # (seconds)
    
    # path for game fading.
    WHITE_SCREEN_PATH = "../../data/white_screen_3840x2160"
    BLACK_SCREEN_PATH = "../../data/black_screen_3840_2160"
    
    SCREEN_EXTENSION = ".png"
    
    # --------------------------------------------
    # Private Variables
    # --------------------------------------------

    # --------------------------------------------
    # Protected Variables
    # --------------------------------------------

    # --------------------------------------------
    # Constructor
    # --------------------------------------------
    def __init__(self):
        """Private Constructor."""
        
        # current scene in game.
        self.currentScene = None
        self.currentBgmFilePath = ""
        self.currentBgmExt = ""
        
        # use for fading the scene.
        self.__nextScene = None
        self.__nextBgmFilePath = ""
        self.__nextBgmExt = ""
        
        # get the sound manager.
        self.soundManager = JCSPyGm_SoundManager.get_instance()
        
        # get the camera.
        self.camera = JCSPyGm_Camera.get_instance()
        
        # create black and white screen.
        self.__init_black_white_screen()
        
        # trigger to check is switching the scene.
        self.__switchingScene = False
        
        self.__fadingBackIntheScene = False
        
        
    @staticmethod
    def get_instance():
        """Singleton Pattern"""
        
        if JCSPyGm_SceneManager.instance is None:
            JCSPyGm_SceneManager.instance = JCSPyGm_SceneManager()
            
        return JCSPyGm_SceneManager.instance

    # --------------------------------------------
    # Public Methods
    # --------------------------------------------
    def update(self, deltaTime):
        """Update scene object's game logic."""
        
        # check if scene null references.
        if self.currentScene is None:
            return;
        
        # update logic. 
        self.currentScene.update(deltaTime)
        
        # update position to camera position.
        self.get_black_screen().x = self.camera.x
        self.get_black_screen().y = self.camera.y
        self.get_whithe_screen().x = self.camera.x
        self.get_whithe_screen().y = self.camera.y
        
        # IMPORTATN(jenchieh): this should always be the last 
        # thing to be render or update.
        self.get_whithe_screen().update(deltaTime)
        self.get_black_screen().update(deltaTime)
        
        # do stuff when switching the scene
        self.__during_switching_scene()
        
    def draw(self, windowInfo):
        """Update scene object's graphics."""
        
        # check if scene null references.
        if self.currentScene is None:
            return;
        
        # draw it
        self.currentScene.draw(windowInfo)
        
        
        # IMPORTATN(jenchieh): this should always be the last 
        # thing to be render or update.
        self.__white_screen.draw(windowInfo)
        self.__black_screen.draw(windowInfo)
    
    def switch_scene(self, newScene):
        """"Switch to the new scene."""
        self.switch_scene_with_bgm(newScene, None, None)
        
    def switch_scene_with_bgm(self, newScene, newBgmFilePath, newBgmExt):
        """"Switch to the new scene with background music."""
        
        # check if new scene good memory space.
        if newScene is None:
            JCSPyGm_Debug.Error("Scene u trying to switch is null references...")
            return
        
        # check if still switching the scene.
        if self.__switchingScene or self.__fadingBackIntheScene:
            JCSPyGm_Debug.Log("Still switching the scene, plz wait...")
            return
        
        # -----------------------------------------
        # IMPORTANT(jenchieh): first assign
        if self.currentScene is None:
            self.currentScene = newScene
            
            # call initialize for the scene.
            self.currentScene.on_enable_scene()
            
            self.currentBgmFilePath = newBgmFilePath
            self.currentBgmExt = newBgmExt
            self.get_black_screen().fade_out(
                JCSPyGm_SceneManager.SCENE_FADEOUT_TIME)
            
            # enable the switching scene trigger.
            self.__fadingBackIntheScene = True
            return
        # -----------------------------------------
        
        # save the next scene
        self.__nextScene = newScene
        self.__nextBgmFilePath = newBgmFilePath
        self.__nextBgmExt = newBgmExt
        
        # initialize the next scene.
        self.__nextScene.on_enable_scene()
        
        # fade out the background music.
        self.soundManager.stop_bgm(
            JCSPyGm_SceneManager.BGM_SOUND_FADEOUT_TIME)
        
        # start fading in the black screen
        self.get_black_screen().fade_in(
            JCSPyGm_SceneManager.SCENE_FADEIN_TIME)
        
        # enable the switching scene trigger.
        self.__switchingScene = True
        
    # --------------------------------------------
    # Protected Methods
    # --------------------------------------------

    # --------------------------------------------
    # Private Methods
    # --------------------------------------------
    def __init_black_white_screen(self):
        """Initialize black and white screen."""
        
        self.__black_screen = JCSPyGm_GameObject()
        self.__white_screen = JCSPyGm_GameObject()
        
        self.__black_screen.active = False
        self.__white_screen.active = False
        
        self.__black_screen.load_sprite(
            JCSPyGm_SceneManager.BLACK_SCREEN_PATH, 
            JCSPyGm_SceneManager.SCREEN_EXTENSION)
        self.__white_screen.load_sprite(
            JCSPyGm_SceneManager.WHITE_SCREEN_PATH, 
            JCSPyGm_SceneManager.SCREEN_EXTENSION)
        
        self.__black_screen.auto_pivot()
        self.__white_screen.auto_pivot()
        
    def __during_switching_scene(self):
        """Do stuff during switching the scene."""
        
        if self.__switchingScene:
        
            if self.get_black_screen().is_fade_in():
                
                # first clean up the scene before switch to 
                # the next scene.
                self.currentScene.on_disable_scene()
                
                # assign current scene to next scene.
                self.currentScene = self.__nextScene
                self.currentBgmFilePath = self.__nextBgmFilePath
                self.currentBgmExt = self.__nextBgmExt
                
                # fade out the black screen
                self.get_black_screen().fade_out(JCSPyGm_SceneManager.SCENE_FADEOUT_TIME)
                
                # fade in the background music.
                self.soundManager.play_bgm(
                    self.currentBgmFilePath, 
                    self.currentBgmExt, 
                    JCSPyGm_SceneManager.BGM_SOUND_FADEIN_TIME)
                
                self.__fadingBackIntheScene = True
            
        if self.__fadingBackIntheScene:
            if self.get_black_screen().is_fade_out():
                # end switching scene.
                self.__switchingScene = False
                self.__fadingBackIntheScene = False
        
    
    # --------------------------------------------
    # setter / getter
    # --------------------------------------------
    def get_current_scene(self):
        """"Return current scene."""
        return self.currentScene
    
    def get_black_screen(self):
        """Return the black screen."""
        return self.__black_screen
    
    def get_whithe_screen(self):
        """Return the white screen."""
        return self.__white_screen
