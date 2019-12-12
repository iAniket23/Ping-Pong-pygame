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
   pygame.display.set_caption('Pong Version 3')   
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
      pygame.key.set_repeat(20, 20) 
      self.surface = surface
      self.bg_color = pygame.Color('black')      
      self.FPS = 50
      self.game_Clock = pygame.time.Clock()
      self.close_clicked = False
      
      
      # game specific object
      self.ball = Ball('white', 5, [250, 200], [4, 2], self.surface)
      self.screen_width = 500
      self.screen_height = 400
      self.rect_color = pygame.Color('white')
              
         
      self.left_paddle = pygame.Rect(100,self.screen_height/2-30,10,40)
      self.right_paddle = pygame.Rect(390,self.screen_height/2-30,10,40)
      self.max_frames = 150
      self.frame_counter = 0
      self.score_left=0
      self.score_right=0
      self.max_score=11
      self.left_paddle_velocity=0
      self.right_paddle_velocity=0
      
   def play(self):
      # Play the game until the player presses the close box.
      # - self is the Game that should be continued or not.

      while not self.close_clicked:  # until player clicks close box
         # play frame
         self.handle_events()
         self.draw()
         self.collide()
         
         self.update()
         self.game_Clock.tick(self.FPS) # run at most with FPS Frames Per Second 

   def handle_events(self):
      # Handle each user event by changing the game state appropriately.
      # - self is the Game whose events will be handled
      
      pygame.display.update()

      events = pygame.event.get()
      for event in events:
         if event.type == pygame.QUIT:
            self.close_clicked = True
         if not(self.score_left== self.max_score or self.score_right== self.max_score):
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_q:
                  if self.left_paddle.top > 0:
                     self.left_paddle_velocity=-10
               if event.key == pygame.K_a:
                  if self.left_paddle.bottom<400:
                     self.left_paddle_velocity=10
               if event.key == pygame.K_p:
                  if self.right_paddle.top>0: 
                     self.right_paddle_velocity=-10
               if event.key == pygame.K_l:
                  if self.right_paddle.bottom<400:
                     self.right_paddle_velocity=10
            if event.type == pygame.KEYUP:
               if event.key == pygame.K_q:
                  self.left_paddle_velocity=0
               if event.key == pygame.K_a:
                  self.left_paddle_velocity=0
               if event.key == pygame.K_p:
                  self.right_paddle_velocity=0
               if event.key == pygame.K_l:
                  self.right_paddle_velocity=0                  
                     
               

   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      self.surface.fill(self.bg_color) # clear the display surface first
      self.ball.draw()
      pygame.draw.rect(self.surface,self.rect_color,self.left_paddle)
      pygame.draw.rect(self.surface,self.rect_color,self.right_paddle)
      # make the updated surface appear on the display
      self.draw_score()
      pygame.display.update()
   def draw_score(self):
      # 1. Set the color
      fg_color = pygame.Color('white')
      # 2.create the font object
      font = pygame.font.SysFont('',50)
      # 3 Create a text box by rendering the font
      text_string_left = str(self.score_left)
      text_box_left = font.render(text_string_left,True,fg_color,self.bg_color)
      text_string_right = str(self.score_right)
      text_box_right = font.render(text_string_right,True,fg_color,self.bg_color)      
      # 4 Compute the location of the text box
      location_left = (10,10)
      location_right = (460,10)
      # 5 Blit or pin the text box on the surface
      self.surface.blit(text_box_left,location_left)
      self.surface.blit(text_box_right,location_right)
           

   def update(self):
      # Update the game objects for the next frame.
      # - self is the Game to update
      if not (self.score_left>=self.max_score or self.score_right>=self.max_score):
         self.ball.move()
         if (self.ball.center[0] <= 0 + self.ball.radius):
            self.score_left = self.score_left+1
         
         if (self.ball.center[0] >= self.ball.screen_size[0] - self.ball.radius):
            self.score_right = self.score_right+1
   def collide(self):
      for i in range(0,2):
         if self.right_paddle.collidepoint(self.ball.center[0],self.ball.center[1]):
            if self.ball.velocity[0]>0:
               self.ball.velocity[i] = - self.ball.velocity[i]
         if self.left_paddle.collidepoint(self.ball.center[0],self.ball.center[1]):
            if self.ball.velocity[0]<0:
               self.ball.velocity[i] = - self.ball.velocity[i]
      if self.left_paddle.top<0:
         self.left_paddle.top=0
      if self.left_paddle.bottom>400:
         self.left_paddle.bottom=400 
      if self.right_paddle.top<0:
         self.right_paddle.top=0
      if self.right_paddle.bottom>400:
         self.right_paddle.bottom=400
         
         
      if self.left_paddle.top>=0 and self.left_paddle.bottom<=400:
         self.left_paddle.top=self.left_paddle.top+self.left_paddle_velocity
   
      if self.right_paddle.top>=0 and self.right_paddle.bottom<=400:
         self.right_paddle.top=self.right_paddle.top+self.right_paddle_velocity
      
      

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

