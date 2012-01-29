import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.vector import Vector
from kivy.factory import Factory
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.properties import ObjectProperty,DictProperty
from kivy.graphics import Line,Color,Rectangle
import math

class KurveApp(App):
    def build(self):
        game = KurveGame()
        x = game.width
        y = game.top
        leftbtn = Button(text="left",pos=(0,y-y/5),size=(x/8,y/5))
        rightbtn = Button(text = "right",pos = (0,0),size=(x/8,y/5))
        leftbtn2 = Button(text="left",pos = (x-x/8,0),size=(x/8,y/5))
        rightbtn2 = Button(text = "right",pos = (x-x/8,y-y/5),size=(x/8,y/5))
        game.add_widget(leftbtn)
        game.add_widget(rightbtn)
        game.add_widget(leftbtn2)
        game.add_widget(rightbtn2)
        game.begin()
        Clock.schedule_interval(game.update,1.0/10.0)
        #Clock.schedule_interval(game.check,.8)
                    
        def turn_left(obj):
            game.snake1.velocity = Vector(*game.snake1.velocity).rotate(90)
        def turn_right(obj):
            game.snake1.velocity = Vector(*game.snake1.velocity).rotate(270)
        def turn_left2(obj):
            game.snake2.velocity = Vector(*game.snake2.velocity).rotate(90)
        def turn_right2(obj):
            game.snake2.velocity = Vector(*game.snake2.velocity).rotate(270)
            
        leftbtn.bind(on_press = turn_left)
        rightbtn.bind(on_release = turn_right)
        leftbtn2.bind(on_press = turn_left2)
        rightbtn2.bind(on_release = turn_right2)
        return game
        
class KurveGame(Widget):
    a = dict()
    a['hello'] = 2 
#These two steps are done just so that the dict is properly initialized.
    data = DictProperty(a)
    '''
    popup1 = Popup(title = "Winner",content = Label(text='Player1 wins',size =(300,300)))
    popup2 = Popup(title = "Winner",content = Label(text='Player2 wins',size = (300,300)))
    ''' 
    snake1 = ObjectProperty(None)
    snake2 = ObjectProperty(None)
    
    def stop(dt):
            exit(1)
            print "hello"
    t = Clock.create_trigger(stop,timeout = 2)
    
    def begin(self):
        y=self.right
        x=self.width
        with self.canvas:
            Rectangle(pos=(0,0),size=(x/60,y))
            Rectangle(pos=(0,0),size=(x,y/60))
            Rectangle(pos=(x-x/60,0),size=(x/60,y))
            Rectangle(pos=(0,y-y/60),size=(x,y/60))
        self.data['div']=(150.0,150.0)
        self.data['pix']=(600.0,600.0)
        divx,divy = int(self.data['div'][0]),int(self.data['div'][1])
        
        self.data['occupied'] = list()
        for i in range(divx*divy):
            self.data['occupied'] += [0]
        for i in range(divx):
            self.data['occupied'][i]=1
            self.data['occupied'][-i-1]=1
        for i in range(divy):
            self.data['occupied'][i*divx]=1
        for i in range(1,divy+1):
            self.data['occupied'][(i*divx)-1]=1

        for i in range(divy):
            for j in range(divx):
                print self.data['occupied'][(i*divx)+j],
            print "\n"

        self.snake1.pos = self.width/6,self.top/6
        self.snake2.pos = self.width*5/6,self.top*5/6
        self.snake1.velocity = (7,0)
        self.snake2.velocity = (-7,0)
        with self.canvas:
            Color(255,255,0)
            self.data["line1"] = Line(points = (self.snake1.center_x,self.snake1.center_y))
            Color(255,0,0)
            self.data["line2"] = Line(points = (self.snake2.center_x,self.snake2.center_y))
        
    def update(self,dt):
        self.snake1.move1(self.data)
        self.snake2.move2(self.data)
    '''              
                
                
        
                print "Player 1 loses"
                self.popup2.open()
                self.t()        
    '''     
        
class Snake(Widget):
    def move1(self,data):
        self.pos = Vector(*self.velocity)+self.pos
        data["line1"].points += (self.center_x,self.center_y)
        n = self.convert(data)
        print n
        data['occupied'][n] = 1
        self.check(data)
        
    def move2(self,data):
        self.pos = Vector(*self.velocity)+self.pos
        data["line2"].points += (self.center_x,self.center_y)
        n = self.convert(data)
        data['occupied'][n] = 1
        print "    ",n
        self.check(data)
        
    def convert(self,data):
        x_pix,y_pix = data['pix']
        divx,divy = data['div']
        x,y = self.pos
        x = math.floor(float(x)/float(x_pix/divx))
        y = math.floor(float(y)/float(y_pix/divy))
        n = (divx-1)*y + x
        if n<divx*divy:
            return int(n)
        else:
            print "large value",n,self.pos,x,y
            return 300
    
    def convert1(self,pos,data):
        x_pix,y_pix = data['pix']
        divx,divy = data['div']
        x,y = pos
        x = math.ceil(float(x)/float(x_pix/divx))
        y = math.floor(float(y)/float(y_pix/divy))
        n = (divx)*y + x
        if n<divx*divy:
            print "check at",int(n)
            print "----------"
            return int(n)
        else:
            print "large value",n,self.pos,x,y
            return 300
       
    def check(self,data):
        pos = Vector(*self.velocity)+self.pos
        if data['occupied'][self.convert1(pos,data)]==1:
            print "Died at",pos,self.convert1(pos,data)
            print "game over"
            exit(1)
            
        
        

    
        
Factory.register("KurveGame",KurveGame)
Factory.register("Snake",Snake)
   
if __name__ in ('__main__'):
    KurveApp().run()     
        
