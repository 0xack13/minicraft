'''
May 2017
@author: Burkhard A. Meier
'''

import pyglet
from pyglet.gl import *
from pyglet.window import key
import time
from pyglet import clock
import copy

# from OpenGL.GLUT import *

WINDOW = 800
INCREMENT = 5

SPACE=-70

class Window(pyglet.window.Window):

    # Cube 3D start rotation
    xRotation = yRotation = 0
    vertical = horizontal = 0
    draw_cubes = 1
    space = SPACE
    
    snake_length = 3
    direction = "up"
    
    #1
    x_white = [25]
    y_white = [25]
    x_yellow = [25]
    y_yellow = [-25]
    x_blue = [-25]
    y_blue = [25]
    x_black = [-25]
    y_black = [-25]
    x_green = [25]
    y_green = [-25]
    x_cyan = [25]
    y_cyan = [25]
    x_magenta = [-25]
    y_magenta = [25]
    x_red = [-25]
    y_red = [-25]

    #2
    x_cyan2 = [25]
    y_cyan2 = [25]
    x_white2 = [25]
    y_white2 = [25]
    x_magenta2 = [-25]
    y_magenta2 = [25]
    x_blue2 = [-25]
    y_blue2 = [25]
    x_green2 = [25]
    y_green2 = [-25]
    x_yellow2 = [25]
    y_yellow2 = [-25]
    x_red2 = [-25]
    y_red2 = [-25]
    x_black2 = [-25]
    y_black2 = [-25]
    
    #3
    x_white3 = [25]
    y_white3 = [25]
    x_cyan3 = [25]
    y_cyan3 = [25]
    x_green3 = [25]
    y_green3 = [-25]
    x_yellow3 = [25]
    y_yellow3 = [-25]
    x_magenta3 = [-25]
    y_magenta3 = [25]
    x_blue3 = [-25]
    y_blue3 = [25]
    x_black3 = [-25]
    y_black3 = [-25]
    x_red3 = [-25]
    y_red3 = [-25]
    
    single_cube = [
        x_white,
        y_white, 
        x_yellow,
        y_yellow,
        x_red,
        y_red,
        x_magenta, 
        y_magenta,
        x_cyan,
        y_cyan,
        x_green, 
        y_green, 
        x_black, 
        y_black, 
        x_blue,
        y_blue,
        x_white2,
        y_white2, 
        x_yellow2,
        y_yellow2,
        x_red2,
        y_red2,
        x_magenta2, 
        y_magenta2,
        x_cyan2,
        y_cyan2,
        x_green2, 
        y_green2, 
        x_black2, 
        y_black2, 
        x_blue2,
        y_blue2,
        x_white3,
        y_white3, 
        x_yellow3,
        y_yellow3,
        x_red3,
        y_red3,
        x_magenta3, 
        y_magenta3,
        x_cyan3,
        y_cyan3,
        x_green3, 
        y_green3, 
        x_black3, 
        y_black3, 
        x_blue3,
        y_blue3,
        ]
    
    all_cubes = []
    for i in range(snake_length):
        l = single_cube
        all_cubes.append(copy.deepcopy(l))
    print(all_cubes)
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.set_minimum_size(300,200)
        glClearColor(0, 0, 0, 1)
        glEnable(GL_DEPTH_TEST)
        for c in range(len(self.all_cubes)):   
            for i in range(len(self.all_cubes[c])):
                if i % 2 == 0:
                    self.all_cubes[c][i][0] += c*SPACE
        clock.schedule_interval(self.callback, 0.2)
    
    # each call represent a cube
    def draw_cube2(self, CI):
        INX=0
        glColor3ub(255, 255, 255)
        glVertex3f(self.all_cubes[CI][0][INX], self.all_cubes[CI][1][INX], 25)

        # Yellow
        glColor3ub(255, 255, 0)
        glVertex3f(self.all_cubes[CI][2][INX], self.all_cubes[CI][3][INX], 25)

        # Red
        glColor3ub(255, 0, 0)
        glVertex3f(self.all_cubes[CI][4][INX], self.all_cubes[CI][5][INX], 25)

        # Magenta
        glColor3ub(255, 0, 255)
        glVertex3f(self.all_cubes[CI][6][INX], self.all_cubes[CI][7][INX], 25)

        # Cyan
        glColor3f(0, 1, 1)
        glVertex3f(self.all_cubes[CI][8][INX], self.all_cubes[CI][9][INX], -25)

        # Green
        glColor3f(0, 1, 0)
        glVertex3f(self.all_cubes[CI][10][INX], self.all_cubes[CI][11][INX], -25)
        
        # Black
        glColor3f(0, 0, 0)
        glVertex3f(self.all_cubes[CI][12][INX], self.all_cubes[CI][13][INX], -25)

        # Blue
        glColor3f(0, 0, 1)
        glVertex3f(self.all_cubes[CI][14][INX], self.all_cubes[CI][15][INX], -25)
        
        # Cyan 2
        glColor3f(0, 1, 1)
        glVertex3f(self.all_cubes[CI][24][INX], self.all_cubes[CI][25][INX], -25)
    
        # White 2
        glColor3f(1, 1, 1)
        glVertex3f(self.all_cubes[CI][16][INX], self.all_cubes[CI][17][INX], 25)
        
        # Magenta 2
        glColor3f(1, 0, 1)
        glVertex3f(self.all_cubes[CI][22][INX], self.all_cubes[CI][23][INX], 25)
        
        # Blue 2
        glColor3f(0, 0, 1)
        glVertex3f(self.all_cubes[CI][30][INX], self.all_cubes[CI][31][INX], -25)

        # Green 2
        glColor3f(0, 1, 0)
        glVertex3f(self.all_cubes[CI][26][INX], self.all_cubes[CI][27][INX], -25)

        # Yellow 2
        glColor3f(1, 1, 0)
        glVertex3f(self.all_cubes[CI][18][INX], self.all_cubes[CI][19][INX], 25)

        # Red 2
        glColor3f(1, 0, 0)
        glVertex3f(self.all_cubes[CI][20][INX], self.all_cubes[CI][21][INX], 25)
        
        # Black 2
        glColor3f(0, 0, 0)
        glVertex3f(self.all_cubes[CI][28][INX], self.all_cubes[CI][29][INX], -25)
        
        # White 3
        glColor3f(1, 1, 1)
        glVertex3f(self.all_cubes[CI][32][INX], self.all_cubes[CI][33][INX], 25)
        
        # Cyan 3
        glColor3f(0, 1, 1)
        glVertex3f(self.all_cubes[CI][40][INX], self.all_cubes[CI][41][INX], -25)

        # Green 3
        glColor3f(0, 1, 0)
        glVertex3f(self.all_cubes[CI][42][INX], self.all_cubes[CI][43][INX], -25)
        
        # Yellow 3
        glColor3f(1, 1, 0)
        glVertex3f(self.all_cubes[CI][34][INX], self.all_cubes[CI][35][INX], 25)
        
        # Red 3
        glColor3f(1, 0, 0)
        glVertex3f(self.all_cubes[CI][36][INX], self.all_cubes[CI][37][INX], 25)
        
        # Magenta 3
        glColor3f(1, 0, 1)
        glVertex3f(self.all_cubes[CI][38][INX], self.all_cubes[CI][39][INX], 25)
        
        # Blue
        glColor3f(0, 0, 1)
        glVertex3f(self.all_cubes[CI][46][INX], self.all_cubes[CI][47][INX], -25)        
    
        # Black
        glColor3f(0, 0, 0)
        glVertex3f(self.all_cubes[CI][44][INX], self.all_cubes[CI][45][INX], -25)
        

    def draw_cube(self, INC=0):
        # White
        glColor3ub(255, 255, 255)
        glVertex3f(50+self.horizontal, 50+self.vertical+INC, 25)

        # Yellow
        glColor3ub(255, 255, 0)
        glVertex3f(50+self.horizontal, -50+self.vertical+INC, 25)

        # Red
        glColor3ub(255, 0, 0)
        glVertex3f(-50+self.horizontal, -50+self.vertical+INC, 25)

        # Magenta
        glColor3ub(255, 0, 255)
        glVertex3f(-50+self.horizontal, 50+self.vertical+INC, 25)

        # Cyan
        glColor3f(0, 1, 1)
        glVertex3f(50+self.horizontal, 50+self.vertical+INC, -25)

        # Green
        glColor3f(0, 1, 0)
        glVertex3f(50+self.horizontal, -50+self.vertical+INC, -25)
        
        # Black
        glColor3f(0, 0, 0)
        glVertex3f(-50+self.horizontal, -50+self.vertical+INC, -25)

        # Blue
        glColor3f(0, 0, 1)
        glVertex3f(-50+self.horizontal, 50+self.vertical+INC, -25)
    
        # Cyan 2
        glColor3f(0, 1, 1)
        glVertex3f(50+self.horizontal, 50+self.vertical+INC, -25)

        # White
        glColor3f(1, 1, 1)
        glVertex3f(50+self.horizontal, 50+self.vertical+INC, 25)

        # Magenta
        glColor3f(1, 0, 1)
        glVertex3f(-50+self.horizontal, 50+self.vertical+INC, 25)

        # Blue
        glColor3f(0, 0, 1)
        glVertex3f(-50+self.horizontal, 50+self.vertical+INC, -25)

        # Green
        glColor3f(0, 1, 0)
        glVertex3f(50+self.horizontal, -50+self.vertical+INC, -25)

        # Yellow
        glColor3f(1, 1, 0)
        glVertex3f(50+self.horizontal, -50+self.vertical+INC, 25)

        # Red
        glColor3f(1, 0, 0)
        glVertex3f(-50+self.horizontal, -50+self.vertical+INC, 25)

        # Black 2
        glColor3f(0, 0, 0)
        glVertex3f(-50+self.horizontal, -50+self.vertical+INC, -25)

        # White 3
        glColor3f(1, 1, 1)
        glVertex3f(50+self.horizontal, 50+self.vertical+INC, 25)

        # Cyan 3
        glColor3f(0, 1, 1)
        glVertex3f(50+self.horizontal, 50+self.vertical+INC, -25)

        # Green
        glColor3f(0, 1, 0)
        glVertex3f(50+self.horizontal, -50+self.vertical+INC, -25)

        # Yellow
        glColor3f(1, 1, 0)
        glVertex3f(50+self.horizontal, -50+self.vertical+INC, 25)
    
        # Magenta
        glColor3f(1, 0, 1)
        glVertex3f(-50+self.horizontal, 50+self.vertical+INC, 25)

        # Blue
        glColor3f(0, 0, 1)
        glVertex3f(-50+self.horizontal, 50+self.vertical+INC, -25)

        # Black
        glColor3f(0, 0, 0)
        glVertex3f(-50+self.horizontal, -50+self.vertical+INC, -25)

        # Red
        glColor3f(1, 0, 0)
        glVertex3f(-50+self.horizontal, -50+self.vertical+INC, 25)

    def on_draw(self):
        # Clear the current GL Window
        self.clear()
        
        # Push Matrix onto stack
        glPushMatrix()

        glRotatef(self.xRotation, 1, 0, 0)
        glRotatef(self.yRotation, 0, 1, 0)

        # Draw the six sides of the cube
        glBegin(GL_QUADS)
        
        for ci in range(self.snake_length):
            for i in range(len(self.all_cubes[ci])):
                self.draw_cube2(ci)
        
        glEnd()
        # Pop Matrix off stack
        glPopMatrix()


    def on_resize(self, width, height):
        # set the Viewport
        # glViewport(0, 0, width, height)

        # using Projection mode
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        aspectRatio = width / height
        gluPerspective(95, aspectRatio, 2, 1000)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0, 0, -725)
    
    def callback(self, dt):
        # print("called:" + str(dt))
        # self.vertical += 10
        for ci in range(len(self.all_cubes)-1,0,-1):
            # for i in range(len(self.all_cubes[ci])):
            #         if self.direction == "up":
            #             self.all_cubes[ci][i][0] -= SPACE
            #         else:
            #             print("got down..")
            #             self.all_cubes[ci][i][0] += SPACE
            #         for ci in range(len(self.all_cubes)):
            for i in range(len(self.all_cubes[ci])):
                self.all_cubes[ci][i][0] = self.all_cubes[ci-1][i][0]
        if self.direction == "up":
            for i in range(len(self.all_cubes[ci])):
                if i % 2 == 1:
                    self.all_cubes[0][i][0] -= SPACE
        elif self.direction == "right":
            for i in range(len(self.all_cubes[ci])):
                if i % 2 == 0:
                    self.all_cubes[0][i][0] -= SPACE
        elif self.direction == "left":
            for i in range(len(self.all_cubes[ci])):
                if i % 2 == 0:
                    self.all_cubes[0][i][0] += SPACE
        else:
            for i in range(len(self.all_cubes[ci])):
                if i % 2 == 1:
                    self.all_cubes[0][i][0] += SPACE
        # collision detection
        for ci in range(len(self.all_cubes)-1,0,-1):
            for i in range(len(self.all_cubes[ci])):
                if self.all_cubes[0] == self.all_cubes[ci]:
                    print("collision detection")
                
        

    
    def on_key_press(self, symbol, modifiers):
        # Symbolic names:
        if symbol == key.ENTER:
            l = self.single_cube
            self.snake_length += 1
            print("Enter..")
            self.all_cubes.append(copy.deepcopy(l))
            for i in range(len(self.all_cubes[-1])):
            #     print(i)
            #     # print(self.all_cubes[c][i][0])
                if i % 2 == 0:
                    self.all_cubes[-1][i][0] = self.all_cubes[-2][i][0]+SPACE
                else:
                    self.all_cubes[-1][i][0] = self.all_cubes[-2][i][0]
                # self.all_cubes[-1][i][0] = self.all_cubes[-2][i][0]+SPACE
            # print(self.all_cubes[-1][i][0])
            # print(self.all_cubes[-2][i][0])

    def on_text_motion(self, motion): 
        if motion == key.UP:
            # self.xRotation -= INCREMENT
            # self.vertical += 60
            # self.draw_cubes += 1
            # clock.schedule_interval(self.callback, 1, self.direction)
            self.direction = "up"
            # for ci in range(len(self.all_cubes)):
            #     for i in range(len(self.all_cubes[ci])):
            #         # for ii in range(len(self.all_cubes[ci][i])):
            #             if self.direction == "up":
            #                 self.all_cubes[ci][i][0] -= SPACE
            #             else:
            #                 self.all_cubes[ci][i][0] += SPACE
        elif motion == key.DOWN:
            # self.xRotation += INCREMENT
            # self.vertical -= 10
            # clock.schedule_interval(self.callback, 1, "down")
            self.direction = "down"
        elif motion == key.P:
            # TODO : ADD NEW BLOCK RELEVANT TO THE LAST BLOCK POSITION
            l = self.single_cube
            self.all_cubes.append(copy.deepcopy(l))
            self.all_cubes[-1] = self.all_cubes[0]
            self.snake_length += 1
            # for i in range(len(self.all_cubes[-1])):
            #     print(i)
            #     # print(self.all_cubes[c][i][0])
                # if i % 2 == 0:
                # self.all_cubes[-1][i][0] = self.all_cubes[-2][i][0]
        elif motion == key.LEFT:
            self.yRotation -= INCREMENT
            self.direction = "left"
        elif motion == key.RIGHT:
            self.direction = "right"
            # self.horizontal -= 10
            self.yRotation += INCREMENT
            

if __name__ == '__main__':
    # Window(WINDOW, WINDOW, 'Pyglet Colored Cube')
    m = Window(width=800, height=600, caption='Minicraft',resizable=True)
    pyglet.app.run()