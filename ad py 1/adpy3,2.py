import pygame
import random

pygame.init()
pygame.font.init()
pygame.display.set_caption("ponggame version 2")


class Menu():
    def __init__(self):
        self.showing = False
        self.start_button = pygame.Rect(50, 100, 200, 50)
        self.button_color = (255,0,0)

        self.BG_COLOR = (245, 66, 66)
        self.SIZE = (600, 600)
        self.canvas = pygame.display.set_mode(self.SIZE)
        self.clock = pygame.time.Clock()
    def show(self):
        self.showing = True
        while self.showing:
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    self.hide()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if e.button == 1:
                        click = True
            # self.update()
            self.render()
            self.clock.tick(60)

    def hide(self):
        self.showing = False
    def render(self):
        self.canvas.fill(self.BG_COLOR)
        pygame.display.flip()
        # pygame.draw.rect(self.canvas, self.button_color, self.start_button)
            
    # def update(self):


class Object():
    def __init__(self, x, y, image_path):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)
        self.image_width = self.image.get_rect().size[0]
        self.image_height = self.image.get_rect().size[1]
    
class Paddle(Object):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, "paddle.png")
        self.velocity = velocity
    def move_up(self, screen_height):
        self.y -= self.velocity
    def move_down(self, screen_height):
        self.y += self.velocity

class Ball(Object):
    def __init__(self, x, y, velocity_x, velocity_y):
        super().__init__(x, y, "ball.png")
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
    def move_horizontal(self, screen_width):
        self.x += self.velocity_x
        if self.x <= 0 or self.x >= screen_width - self.image_width:
            self.velocity_x = - self.velocity_x
    def move_vertical(self, screen_height):
        self.y += self.velocity_x
        if self.y <= 0 or self.y >= screen_height - self.image_height:
            self.velocity_y = - self.velocity_y
    def handle_paddle_collision(self):
        self.velocity_x = - self.velocity_x
        self.velocity_y = random.uniform(1.5, 5)
        # print(self.velocity_y)
        # if self.velocity_y >= 0:
            
        # else:
        #     self.velocity_y =  - random.uniform(1.5, 5)

class Player():
    def __init__(self):
        self.point = 0
    def add_point(self):
        self.point += 1
        
class Game():
    def __init__(self):
        self.running = False

        self.player_1 = Player()
        self.player_2 = Player()

        self.paddle_1 = Paddle(x=0, y=250, velocity=5)
        self.paddle_2 = Paddle(x=570, y=250, velocity=5)
        self.ball = Ball(x=285, y=300, velocity_x=3.5, velocity_y=1.5)

        self.w_pressed = False
        self.s_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        self.SIZE = (600, 600)
        self.canvas = pygame.display.set_mode(self.SIZE)
        self.BG_COLOR = (245, 66, 66)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    def run(self):
        self.running = True
        while self.running:
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    self.stop()
                    
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_w:
                        self.w_pressed = True
                    elif e.key == pygame.K_s:
                        self.s_pressed = True
                    elif e.key == pygame.K_UP:
                        self.up_pressed = True
                    elif e.key == pygame.K_DOWN:
                        self.down_pressed = True

                elif e.type == pygame.KEYUP:
                    if  e.key == pygame.K_w:
                        self.w_pressed = False
                    elif e.key == pygame.K_s:
                        self.s_pressed = False
                    elif e.key == pygame.K_DOWN:
                        self.down_pressed = False
                    elif e.key == pygame.K_UP:
                        self.up_pressed = False
            self.update()
            self.render()
            self.clock.tick(60)
    def update(self):
        self.ball.move_horizontal(self.SIZE[0])
        self.ball.move_vertical(self.SIZE[1])

        if self.paddle_1.y <= self.ball.y <= (self.paddle_1.y + self.paddle_1.image_height) and self.ball.x <=  (self.paddle_1.x + self.paddle_1.image_width):
            self.ball.handle_paddle_collision()
        if self.paddle_2.y <= self.ball.y <= (self.paddle_2.y + self.paddle_2.image_height) and self.ball.x >= (self.paddle_2.x - self.ball.image_width):
            self.ball.handle_paddle_collision()
        if self.ball.x <= 0:
            self.player_2.add_point()
            self.reset()
        if self.ball.x >=580:
            self.player_1.add_point()
            self.reset()

        if self.ball.y <= 0 or self.ball.y >= 580:
            self.ball.velocity_y = -self.ball.velocity_y

        if self.paddle_1.y <= 0:
            self.w_pressed = False
        if self.paddle_2.y <= 0:
            self.up_pressed = False
        if self.paddle_1.y >= self.SIZE[1] - self.paddle_1.image_height:
            self.s_pressed = False
        if self.paddle_2.y >= self.SIZE[1] - self.paddle_2.image_height:
            self.down_pressed = False

        if self.w_pressed:
            self.paddle_1.move_up(self.SIZE[0])
        if self.s_pressed:
            self.paddle_1.move_down(self.SIZE[0])
        if self.up_pressed:
            self.paddle_2.move_up(self.SIZE[0])
        if self.down_pressed:
            self.paddle_2.move_down(self.SIZE[0])

    def reset(self):
        self.paddle_1 = Paddle(x=0, y=250, velocity=5)
        self.paddle_2 = Paddle(x=570, y=250, velocity=5)
        self.ball = Ball(x=285, y=300, velocity_x=1.5, velocity_y=3.5)
        
        
    def render(self):
        self.canvas.fill(self.BG_COLOR)
        self.canvas.blit(self.paddle_1.image, (self.paddle_1.x, self.paddle_1.y))
        self.canvas.blit(self.paddle_2.image, (self.paddle_2.x, self.paddle_2.y))
        self.canvas.blit(self.ball.image, (self.ball.x, self.ball.y))
        self.show_showpoint()

        pygame.display.flip()

    def show_showpoint(self):
        point_string = str(self.player_1.point) + " - " + str(self.player_2.point)
        text = self.font.render(point_string, False, (255, 255, 255))
        self.canvas.blit(text,(self.SIZE[0] / 2 - 40,0))
    def stop(self):
        self.running = False

# game = Game()
# game.run()

menu = Menu()
menu.show()