# This is the game pong where ball bounces when it hits the edge or inner side of the the rectangle
#Score is incresead when it touches the right or left egde respectively
#first player to 11 wins
import pygame

# User-defined functions
def main():
   # initialize all pygame modules (some need initialization)
   pygame.init()
   # create a pygame display window
   pygame.display.set_mode((500, 400))
   # set the title of the display window
   pygame.display.set_caption('Pong Version 1')   
   # get the display surface
   w_surface = pygame.display.get_surface() 
   # create a game object
   game = Game(w_surface)
   # start the main game loop by calling the play method on the game object
   game.play() 
   # quit pygame and clean up the pygame window
   pygame.quit()
class Game:
   # An object in this class represents a complete game.
   def __init__(self, surface): 
      # Initialize a Game.
      # - self is the Game to initialize
      # - surface is the display window surface object      
      self.surface = surface
      self.bg_color = pygame.Color('black')      
      self.FPS = 150
      self.game_Clock = pygame.time.Clock()
      self.close_clicked = False
      
      
      # game specific object
      self.ball = Ball('white', 5, [250, 200], [4, 2], self.surface)
      self.screen_width = 500
      self.screen_height = 400
      self.rect_color = pygame.Color('white')
              
         
      self.left_paddle = pygame.Rect(100,self.screen_height/2-35,10,40)
      self.right_paddle = pygame.Rect(350,self.screen_height/2-35,10,40)
      self.max_frames = 150
      self.frame_counter = 0
      
   def play(self):
      # Play the game until the player presses the close box.
      # - self is the Game that should be continued or not.

      while not self.close_clicked:  # until player clicks close box
         # play frame
         self.handle_events()
         self.draw()            
         
         self.update()
         self.game_Clock.tick(self.FPS) # run at most with FPS Frames Per Second 

   def handle_events(self):
      # Handle each user event by changing the game state appropriately.
      # - self is the Game whose events will be handled

      events = pygame.event.get()
      for event in events:
         if event.type == pygame.QUIT:
            self.close_clicked = True

   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      self.surface.fill(self.bg_color) # clear the display surface first
      self.ball.draw()
      pygame.draw.rect(self.surface,self.rect_color,self.left_paddle)
      pygame.draw.rect(self.surface,self.rect_color,self.right_paddle)
      pygame.display.update() # make the updated surface appear on the display

   def update(self):
      # Update the game objects for the next frame.
      # - self is the Game to update
      
      self.ball.move()
   

  
      

class Ball:
   def __init__(self, ball_color, ball_radius, ball_center, ball_velocity, surface):
      # Initialize a Ball.
      # - self is the Dot to initialize
      # - color is the pygame.Color of the dot
      # - center is a list containing the x and y int
      #   coords of the center of the dot
      # - radius is the int pixel radius of the dot
      # - velocity is a list containing the x and y components
      # - surface is the window's pygame.Surface object

      self.color = pygame.Color(ball_color)
      self.radius = ball_radius
      self.center = ball_center
      self.velocity = ball_velocity
      self.surface = surface  
      self.screen_width = 500
      self.screen_height = 400
      self.screen_size = (self.screen_width,self.screen_height)
      
   def move(self):
      # Change the location of the Dot by adding the corresponding 
      # speed values to the x and y coordinate of its center
      # - self is the Dot
      
      for i in range(0,2):
                     self.center[i] = (self.center[i] + self.velocity[i])
                     if (self.center[i] <= 0 + self.radius or self.center[i] >= self.screen_size[i] - self.radius):
                        self.velocity[i] = - self.velocity[i]
                     
                     
                     
   def draw(self):
      # Draw the dot on the surface
      # - self is the Dot
      
      pygame.draw.circle(self.surface, self.color, self.center, self.radius)      
   


main()
