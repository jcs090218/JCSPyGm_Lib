#  ========================================================================
#  $File: JCSPyGm_Collider.py $
#  $Date: 2016-10-31 22:42:29 $
#  $Revision: $
#  $Creator: Jen-Chieh Shen $
#  $Notice: See LICENSE.txt for modification and distribution information
#                     Copyright (c) 2016 by Shen, Jen-Chieh $
#  ========================================================================



class JCSPyGm_Collider(object):

    """Collider base type."""

    # --------------------------------------------
    # Public Variables
    # --------------------------------------------

    # --------------------------------------------
    # Private Variables
    # --------------------------------------------

    # --------------------------------------------
    # Protected Variables
    # --------------------------------------------

    # --------------------------------------------
    # Constructor
    # --------------------------------------------
    def __init__(self, gmObj):
        """Constructor."""
        
        self.active = True
        
        self.gameObject = gmObj
        
        # collider position.
        self.x = 0
        self.y = 0
        
        self.pivotX = 0
        self.pivotY = 0
        
        self._name = ""
        self._type = ""
        self._tag = ""
        
    # --------------------------------------------
    # Public Methods
    # --------------------------------------------
    def update(self, deltaTime):
        """Update game logics."""
        
    def draw(self, windowInfo):
        """Update game graphics."""
        
        self.x = self.gameObject.camX - self.pivotX
        self.y = self.gameObject.camY - self.pivotY
        
    def auto_pivot(self):
        """Auto pivot the collider."""
        
    def is_name(self, cmpName):
        """Check the same name."""
        return self._name is cmpName

    def is_tag(self, cmpTag):
        """Check the same tag."""
        return self._tag is cmpTag
    
    def is_type(self, cmpType):
        """Check the same type."""
        return self._type is cmpType

    # --------------------------------------------
    # Protected Methods
    # --------------------------------------------

    # --------------------------------------------
    # Private Methods
    # --------------------------------------------

    # --------------------------------------------
    # setter / getter
    # --------------------------------------------
    def set_name(self, newId):
        """Identity of the collider name,"""
        self._name = newId
    
    def get_name(self):
        """Return the identity of the collider name."""
        return self._name
    
    def set_type(self, newType):
        """Identity of the collider type,"""
        self._type = newType
    
    def get_type(self):
        """Return the identity of the collider type."""
        return self._type
    
    def set_tag(self, newTag):
        """Identity of the collider tag,"""
        self._tag = newTag
    
    def get_tag(self):
        """Return the identity of the collider tag."""
        return self._tag
