# AlienGame
2D Game made in python using pygame based on the project Alien Invasion in the book Python Crash Course by Eric Matthes. The basic game functionalities are the same as given in the book with added functionalities and improvements. Currrently these features or codes are added/modified:

1) Added component class for managing components. This leads to effective refraction of the code and avoidance of the horrific argument passing problem. The structure of code is changed quite a bit due to this.
2) Settings is not modified at all in the whole code instead variables with temporary values are used.
3) Ship speed can be changed using up or down arrow keys for increasing or decreasing speed respectively.
4) Added sleep(temporary solution) so that the components refresh at fixed rate.

Otherwise the game is simple to play, fire the bullets through spacebar and take down the approaching aliens. Use arrow keys for movement of the ship
