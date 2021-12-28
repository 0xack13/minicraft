import pyglet
from pyglet.gl import *
from pyglet.graphics import vertex_list
from pyglet.window import key
import math
import sys

if sys.version_info[0] >= 3:
    xrange = range
def cube_vertices(x, y, z, n):
    return [
        x-n,y+n,z-n, x-n,y+n,z+n, x+n,y+n,z+n, x+n,y+n,z-n,  # top
        x-n,y-n,z-n, x+n,y-n,z-n, x+n,y-n,z+n, x-n,y-n,z+n,  # bottom
        x-n,y-n,z-n, x-n,y-n,z+n, x-n,y+n,z+n, x-n,y+n,z-n,  # left
        x+n,y-n,z+n, x+n,y-n,z-n, x+n,y+n,z-n, x+n,y+n,z+n,  # right
        x-n,y-n,z+n, x+n,y-n,z+n, x+n,y+n,z+n, x-n,y+n,z+n,  # front
        x+n,y-n,z-n, x-n,y-n,z-n, x-n,y+n,z-n, x+n,y+n,z-n,  # back
    ]
def tex_coord(x, y, n=4):
    m = 1.0 / n
    dx = x * m
    dy = y * m
    return dx, dy, dx + m, dy, dx + m, dy + m, dx, dy + m

def tex_coords(top, bottom, side):
    top = tex_coord(*top)
    bottom = tex_coord(*bottom)
    side = tex_coord(*side)
    result = []
    result.extend(top)
    result.extend(bottom)
    result.extend(side * 4)
    return result
    
class Model:
    def get_text(self, file):
        tex = pyglet.image.load(file).get_texture()
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        return pyglet.graphics.TextureGroup(tex)
    
    def __init__(self):
        self.top = self.get_text("grass_top.png")
        self.side = self.get_text("grass_side.png")
        self.bottom = self.get_text("dirt.png")
        self.batch = pyglet.graphics.Batch()
        n = 20  # 1/2 width and height of world
        s = 1  # step size
        y = 0  # initial y height
        x= n
        z = n
        GRASS = tex_coords((1, 0), (0, 1), (0, 0))
        x,y,z = 0,0,-1
        vertex_data = cube_vertices(x, y, z, 0.5)
        n = 80  # 1/2 width and height of world
        s = 1  # step size
        y = 0  # initial y height
        for x in xrange(-n, n + 1, s):
            for z in xrange(-n, n + 1, s):
                vertex_data = cube_vertices(x, y, z, 0.5)
                self.batch.add(24, GL_QUADS, self.top,('v3f/static', vertex_data),('t2f',GRASS))
        n = 80  # 1/2 width and height of world
        s = 1  # step size
        y = 0  # initial y height
        for _ in range(20):
            for x in xrange(1,2):
                for y in xrange(1,14):
                    # create a layer stone an grass everywhere.
                    vertex_data = cube_vertices(x, y, 1, 0.5)
                    self.batch.add(24, GL_QUADS, self.bottom,('v3f/static', vertex_data),('t2f',GRASS))
        X,Y,Z = x+1, y+1, z+1

    def draw(self):
        self.batch.draw()

class Player:
    def __init__(self, pos=(0, 0, 0), rot=(0, 0)):
        self.pos = list(pos)
        self.rot = list(rot)

    def mouse_motion(self, dx, dy):
        dx/= 8
        dy/= 8
        self.rot[0] += dy
        self.rot[1] -= dx
        # if self.rot[0]>90:
        #     self.rot[0] = 90
        # elif self.rot[0] < -90:
        #     self.rot[0] = -90

    def update(self,dt,keys):
        sens = 0.1
        s = dt*10
        rotY = -self.rot[1]/180*math.pi
        dx, dz = s*math.sin(rotY), math.cos(rotY)
        if keys[key.W]:
            self.pos[0] += dx*sens
            self.pos[2] -= dz*sens
        if keys[key.S]:
            self.pos[0] -= dx*sens
            self.pos[2] += dz*sens
        if keys[key.A]:
            self.pos[0] -= dz*sens
            self.pos[2] -= dx*sens
        if keys[key.D]:
            self.pos[0] += dz*sens
            self.pos[2] += dx*sens
        if keys[key.SPACE]:
            self.pos[1] += s
        if keys[key.LSHIFT]:
            self.pos[1] -= s

class Window(pyglet.window.Window):
    def set3d(self):
        self.Projection()
        gluPerspective(70, self.width/self.height, 0.05, 1000)
    
    def Projection(self): glMatrixMode(GL_PROJECTION); glLoadIdentity()
    def Model(self): glMatrixMode(GL_MODELVIEW); glLoadIdentity()
    
    def setLock(self, state):
        self.lock = state
        self.set_exclusive_mouse(state)
    
    lock = False
    mouse_lock = property(lambda self:self.lock, setLock)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_minimum_size(300,200)
        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)
        
        self.player = Player()
        self.model = Model()
        pyglet.clock.schedule(self.update)
        self.label = pyglet.text.Label('mew 123', font_name='Arial', font_size=18, x=10, y=self.height - 10, anchor_x='left', anchor_y='top', color=(10, 20, 20, 255))
    
    def on_key_press(self, KEY, _MOD):
        if KEY == key.ESCAPE:
            self.close()
        elif KEY == key.E:
            self.mouse_lock = not self.mouse_lock
    
    def update(self, dt):
        self.player.update(dt, self.keys)
    
    def on_mouse_motion(self,x,y,dx,dy):
        if self.mouse_lock: self.player.mouse_motion(dx,dy)
    
    def set_2d(self):
        """ Configure OpenGL to draw in 2d.

        """
        width, height = self.get_size()
        glDisable(GL_DEPTH_TEST)
        viewport = self.get_viewport_size()
        glViewport(0, 0, max(1, viewport[0]), max(1, viewport[1]))
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, max(1, width), 0, max(1, height), -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
    
    def draw_label(self):
        self.label.text = "test 1234"
        self.label.draw()

    def on_draw(self):
        self.clear()
        self.set3d()
        glColor3d(1, 1, 1)
        x,y,z = self.player.pos
        glTranslatef(-x,-y,-z)
        rot = self.player.rot
        glRotatef(-rot[0],1,0,0)
        glRotatef(-rot[1],0,1,0)
        self.model.draw()
        self.set_2d()
        self.draw_label()
        

    
if __name__ == '__main__':
    window = Window(width=800, height=600, caption='Minicraft',resizable=True)
    glClearColor(0.5,0.7,1,1)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_CULL_FACE)
    pyglet.app.run()