from pyglet.shapes import ShapeBase,Line,Circle,Polygon,Arc
import math


class FourierCircle:
    def __init__(self,parent,batch=None,x=0,y=0,*args,**kwargs):
        super().__init__()
        self.batch = batch
        self.line : Line = None
        self.circle : Circle = None
        self.theta = 0
        self.freq = 0
        self.parent = parent
        self.radius = 100
        self.save = self.completed = False
        self.transverses = []
        self.position = complex(0)
        self.x = x if parent == None else (parent.position.real + parent.x)
        self.y = y if parent == None else (parent.position.imag + parent.x)

    def setDefaults(self):
        self.position: complex = self.radius*math.e**(self.theta*1j)
        self.circle = Arc(self.x,self.y,self.radius,angle=math.pi*2, color=(255,255,255,10),batch=self.batch)
        self.line = Line(self.x,self.y,self.x + self.position.real,self.y + self.position.imag,batch=self.batch)

    def update(self,dt):
        self.theta += 2*math.pi*self.freq*dt
        self.x = self.x if self.parent == None else (self.parent.position.real + self.parent.x)
        self.y = self.y if self.parent == None else (self.parent.position.imag + self.parent.y)
        self.position = self.radius*math.e**(self.theta*1j)
        self.line.x = self.circle.x = self.x
        self.line.y = self.circle.y = self.y
        self.circle.radius = self.radius
        self.line.x2 = self.position.real + self.line.x
        self.line.y2 = self.position.imag + self.line.y
        if self.save and not self.completed:
            self.transverses.append((self.position.real + self.line.x , self.position.imag + self.line.y))
            if len(self.transverses) > 2 and self.transverses[0] == self.transverses[-1]:
                self.completed = True
                print(self.completed)
            print(self.transverses)
    