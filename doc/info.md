## class AudioSource(Undrawable.Undrawable):
###     def __init__(self, filename, pos, isGlobal, radius=10, baseVolume=1):
    Inherits: Undrawable

    An undrawable pgxObject that tracks the location of a sound and it's properties.
    ...

    Attributes
    ----------
    _global:    (private) bool: 
        Whether or not the sound plays regardless of distance to the focus
    _sound:     (private) pygame.mixer.sound: 
        The sound object this audiosource plays
    radius:     (public) int: 
        The minimum distance the focus must be for this sound to be audible
    baseVolume: (public) float:
        The base volume of the sound

    Methods
    -------
    Play(); 
        plays the _sound file.
    
###     def PlayOnce(self):
        
        Plays contained sound file one time.
        
###     def Play(self):
        
        Plays contained sound file on loop.
        
A module that controls all aspects of viewing the world using the pgx library.
## class Camera(Undrawable.Undrawable):
The pgx camera is incredibly versatile. Given any group of pgx based objects, it can draw them if told to. Multiple cameras can draw the same objects, originating at different positions. This allows for something like split screens and combined UIs to be not only possible, but much easier.
Each camera acts as a drawing surface. While not necessarily controllimg the objects they view themselves, the methods it contains allow for easy translation between the screen and the global positioned object world. 
Cameras can move, zoom, and translate viewport space to world space.
###     def __init__(self, pos, viewport, origin, camSurface):

    Inherits

    PGX: A class to control how a user views any instantiated pgx object types.

    pos:
        Vector2 position of the camera
    viewport:
        Width and height of cam
    origin:
        Where on the display the topleft of this cameras surface will be displayed
    camSurface:
        the surface to give to the camera initially
    ...

    Attributes
    ----------
    viewport:   (private) tuple: 
        Describes the height and width of the viewport 
    origin:     (private) tuple: 
        Describes the origin of this camera
    camSurface: (public) Surface: 
        The surface that acts as this cameras view frustrum onto
    zoom:       (private) Vector2: 
        The current camera zoom multiplier.

    Methods
    -------
    SetCamPos(absolutePos): absolutePos(Vector2);
        Sets the cameras global position, absolutely.

    MoveCam(relativePos): relativePos(Vector2);
        Sets the cameras global position, relatively.

    SetCamZoom(self, absoluteMultiplier, pygameDisplaySurface): absoluteMultiplier(float) pygameDisplaySurface(Surface)
        Zooms in or out on the cameras viewport.

    ScreenPosToGlobalPos(self,MousePos): MousePos(tuple);
        Returns: A pygame.math.Vector2 object representing the x and y coordinates of the adjusted mouse in units of
        global position measurement.
    
###     def SetCamPos(self, absolutePos):
        
        Sets the cameras global position, absolutely

        absolutePos:    pygame.math.Vector2 object representing the new absolute position
        
###     def MoveCam(self, relativePos):
        
        Sets the cameras global position, relatively

        relativePos:    pygame.math.Vector2 object representing the change in relative position
        
###     def SetCamZoom(self, absoluteMultiplier, pygameDisplaySurface):
        
        Transform scale the screen.
        Used to set the scale factor of the camera. Will zoom in and out based on topleft.
        Must be called every frame that the cameras zoom is not 1.

        abosluteMultiplier:     The absolute multiplier of the camera zoom.
        pygameDisplaySurface:   The pygame.display surface object representing the window.
        
###     def ScreenPosToGlobalPos(self,MousePos):
        
        Returns: A pygame.math.Vector2 object representing the x and y coordinates of the adjusted mouse in units of
        global position measurement.
        For example: If there is an object whose topleft = (0,0), moving the camera around and hovering mouse over
        this top left area will return a value of (0,0), as that is the converted screen position to global position.

        MousePos:   Should just be the return value of pygame.mouse.get_pos(). Essentially, just a screen mouse position tuple.
        
###     def Clear(self,color,colorKey=None):
        
        Clears the camera feed with a solid color;

        If colorKey is set, it will fill the screen with a color which is the same color as the color key,
        effectively laying a transparent mask fill. This is useful for things like UI elements.

        color:      pygame.color.Color object or triple set (,,)
        colorKey:   pygame.color.Color object or triple set (,,)
        
## class Drawable(pgxObject.pgxObject, pygame.sprite.Sprite):
### 	def __init__(self, pos, image, group=None, layer=0):
	Inherits pgxObject, pygame.Sprite

 	The most base class for all drawn objects. Controls drawing and updating.
	...

	Attributes
	----------
	localLayer:	(public) int:
		Drawing layer of this object. Objects in the same layer will be drawn in order.
		layer order is not designed to be global, but can be if desired. Idea is that certain types of objects have their own
		general layers (i.e. UI, background, foreground, etc) and the local layer decides layering based on those groupings.
		In pygame, however, there are no layers, and layering is determined by draw order only.

	image:		(public) pygame.Surface: 
		the image to render in the Draw() method. if group is not none, it will be used by the sprite init 
		to add object to a group automatically.

	rect:		(public) pygame.Rect: 
		The image rect to allow functionality for collisions.

	Methods
	-------
	Draw(cam):a cam(pgx.Camera);
		draws image to camera surface
	
### 	def Draw(self,cam):
		
		Draws an image onto the cam.camSurface using the blit method.
		The destination param of blit is pgxObject -> GetCamAlignPos.

		cam: a Camera object
		
### 	def Update(self,cam):
		
		Generic update method. Override as needed

		cam: a Camera object
		
### 	def update(self,*args,**kwargs):
		
		This is the method inherited from pygame.sprite.Sprite()

		it does nothing by default, so I just made it be a wrapper for 
		the pgx Update() method. If you want to use sprite.update (like in a group)
		then you should pass the cam as args[0]
		
## class Dynamic(Transformable.Transformable):
###     def __init__(self,pos,image, group=None,layer=0):
## class Particle(Physical.Physical):
###     def __init__(self, pos, image, group=None,layer=0):
## class Physical(Transformable.Transformable):
###     def __init__(self,pos,image,group=None,layer=0):
## class PhysicsBody(Physical.Physical):
###     def __init__(self, pos, image,group=None,layer=0):
## class Static(Transformable.Transformable):
###     def __init__(self,pos, image, group=None, layer=0):
## class Transformable(Drawable.Drawable):
	
	Inherits Drawable

 	The main parent class to all functional subtype drawn objects. Contains functionality for scaling, rotating, and moving
	drawn objects.

	pos:	s.e;
	image:	pygame.Surface object; any surface.
	group:	(OPTIONAL) pygame.sprite.Group object to belong to.
	layer:	(OPTIONAL) local draw layer.
	...

	Attributes
	----------
	name: (intended protection) type:
	    tabbed in description
	scale: (private) float:
		the current scale of this transformable object
	rotation: (private) float:
		the current rotation of this transformable object
	baseSize: (private) Vector2:
		used to keep track of the base size of this object to be used with scaling.

	Methods
	-------
	MethodName(param1, param2="foobar"): param1(int) param2(string);
	    short desc of method
	
### 	def __init__(self,pos,image, group=None, layer=0):
### 	def MoveAbsolute(self, vec2Pos):
		
		Changes the global position, absolutely.

		vec2Change: pygame.math.Vector2 object representing new position
		
### 	def MoveRelative(self, vec2Change):
		
		Changes the global position, relatively.

		vec2Change: pygame.math.Vector2 object representing position change
		
### 	def ScaleTo(self, floatScale):
		
		scale the object with a pygame transform, absolutely

		floatScale: float amount to scale
		
### 	def RotateTo(self, floatRotation):
		
		rotate object with pygame transform, absolutely
		Positive values are counter clockwise.

		floatRotation: float amount of rotation to set for this object.
		
### 	def Rotate(self, deltaRotation):
		
		Use pygame.transform.rotate to additively rotate the surface.
		keeps track of current rotation.
		positive values are counter clockwise.

		deltaRotation: float amount to rotate
		
### 	def Update(self, cam):
		
		Makes sure that the rect object is updated for 'collision' purposes.
		Can be overridden.

		cam: vestigial at this point.

		
### 	def GetRotation(self):
		Returns the value of the protected rotation member
### 	def GetScale(self):
		Returns the value of the protected scale member
### 	def GetBaseSize(self):
		Returns the value of the protected base size member
## class UI(Transformable.Transformable):
#### Inherit this class to make your own buttons with overridden OnClick methods.
    
    Inherits Transformable

    A purely abstract subclass of Transformable. Inherit and overload  for your needs; maintains properties of other pgxObjects.

    pos:    Position of object in global space.
    image:  s.e;
    group:  (OPTIONAL) input a pygame.sprite.Group object to make this object a part of that group.
    layer:  Local layer for whatever camera object is being drawn on. Determines draw order
    ...

    Attributes
    ----------
    gPosition: (public) pygame.math.Vector2:
        see readme for more info on the PGX GPS.

    Methods
    -------
    OnClick();
        A method to call when button is clicked.
    
###     def __init__(self,pos, image, group=None, layer=0):
###     def OnClick(self):
        
        Overload this method with custom functionality. Future delegate-like system in the works.
        
## class Undrawable(pgxObject.pgxObject):
### 	def __init__(self, pos):
A wrapper module for pygame that makes all aspects of drawing and viewing much, much easier by compiling the boilerplate you would have used into a library.
## class pgxObject():
	
	Parent object of all objects in PGX. Introduces the global positioning system.

	...

	Attributes
	---------
	gPosition: (public) Vector2: 
		the global position, in worldspace. This is the literal location of the object, regardless of cam view.

	Methods
	-------
	GetCamAlignPos(self, cam): cam(Camera);
		Returns a position to draw an object at.
	InCamRange(self, cam): cam(Camera);
		Returns if object is in range of Camera cam

	
### 	def __init__(self, pos_vector):
### 	def GetCamAlignPos(self, cam):
		
		Returns a position to draw an object at.

		Inherited:
		cam: cam.gPosition (Vector2) - the camera's "global position"
		
### 	def InCamRange(self, cam):
		
		Returns whether or not the other object is in range of this camera based on camera view.

        self: A pgxObject
        cam: A Camera
		
## class Text(Transformable.Transformable):
###     def __init__(self,pos,fontName,text,size,group = None, layer = 0,color=color.Color(1,1,1),antiAlias=False,bold=False,italic=False):
    
    Store pygame font rendering information and functionality
    ...

    The constructor is a doozy. Controls everything about the font and text

    pos (Vector2): Vector2 topleft position

    fontName (str, union sys.path): name of the font to look for. Will look for a custom font first, then default to sys file, then to pygame default.
    
    text (str): text you want it to display

    size (int): size in pixels, the height of the letters.

    group (pygame.sprite.Group): (OPTIONAL) a python sprite group.

    layer (int): (OPTIONAL) default = 0. Order to draw.

    color (pygame.color.Color): (OPTIONAL) default = black.

    antiAlias (bool): (OPTIONAL) default = false. Anti alias text rendering.

    bold (bool): (OPTIONAL) default = false. s.e;
    
    italic (bool): (OPTIONAL) default = false. s.e;

    Attributes
    ----------
    self._font: (private) pygame.font.Font:
        A pygame font/sysfont object used for text rendering functionality.

    Methods
    -------
    ChangeText(text, antiAlias,color): text(string) antiAlias(bool) color(pygame.color.Color);
        Changes text string on text object.

###     def ChangeText(self,text,antiAlias=False,color=color.Color(1,1,1)):
        
        Re-Render the font with different text.

        text: a string
        antiAlias: (OPTIONAL) bool whether or not text is AA'd
        color: (OPTIONAL) a pygame.Color or triple set describing a text color
        
