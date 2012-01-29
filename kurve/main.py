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
from kivy.graphics import Line,Color

class KurveApp(App):
    def build(self):
        game = KurveGame()
        x = game.width
        y = game.top
        leftbtn = Button(text="left",pos=(0,y),size=(x/8,y/5))
        rightbtn = Button(text = "right",pos = (0,0),size=(x/8,y/5))
        leftbtn2 = Button(text="left",pos = (x,0),size=(x/8,y/5))
        rightbtn2 = Button(text = "right",pos = (x,y),size=(x/8,y/5))
        game.add_widget(leftbtn)
        game.add_widget(rightbtn)
        game.add_widget(leftbtn2)
        game.add_widget(rightbtn2)
        game.begin()
        Clock.schedule_interval(game.update,1.0/6.0)
        Clock.schedule_interval(game.check,.8)
        
                     
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
    a['hello'] = 2 #These two steps are done just so that the dict is properly initialized.
    data = DictProperty(a)
    
    popup1 = Popup(title = "Winner",content = Label(text='Player1 wins'),size = (300,300))
    popup2 = Popup(title = "Winner",content = Label(text='Player2 wins'),size = (300,300))
    
    snake1 = ObjectProperty(None)
    snake2 = ObjectProperty(None)
    
    def stop(dt):
            exit(1)
            print "hello"
    t = Clock.create_trigger(stop,timeout = 2)
    
    def begin(self):
        self.snake1.pos = self.x,self.y
        self.data["line1_x"] = [self.snake1.pos[0]]
        self.data["line1_y"] = [self.snake1.pos[1]]
        self.data['current1'] = [(self.snake1.pos[0],self.snake1.pos[1]),(self.snake1.pos[0],self.snake1.pos[1])]
        
        self.snake2.pos = self.width,self.top
        self.data["line2_x"] = [self.snake2.pos[0]]
        self.data["line2_y"] = [self.snake2.pos[1]]
        self.data['current2'] = [(self.snake2.pos[0],self.snake2.pos[1]),(self.snake2.pos[0],self.snake2.pos[1])]
        
        self.snake1.velocity = (10,0)
        self.snake2.velocity = (-10,0)
        with self.canvas:
            Color(255,255,0)
            self.data["line1"] = Line(points = (self.snake1.center_x,self.snake1.center_y))
            Color(255,0,0)
            self.data["line2"] = Line(points = (self.snake2.center_x,self.snake2.center_y))
        
    def update(self,dt):
        self.snake1.move1(self.data)
        self.snake1.current1(self.data)
        self.snake2.move2(self.data)
        self.snake2.current2(self.data)
        
    def check(self,dt):
        val = self.data
        cur1 = self.data['current2'][0]
        cur2 = self.data['current2'][1]
        x1 = max(cur1[0],cur2[0])
        x2 = min(cur1[0],cur2[0])
        y1 = max(cur1[1],cur2[1])
        y2 = min(cur1[1],cur2[1])
        v = 10
        for i in range(len(val['line1_x'])):
            if (val['line1_x'][i] > x2-v)&(val['line1_x'][i] < x1+v)&(val['line1_y'][i] > y2-v)&(val['line1_y'][i] < y1+v):
                print "Player 2 loses"
                self.popup1.open()
                self.t()
                
                
                
        cur1 = self.data['current1'][0]
        cur2 = self.data['current1'][1]
        x1 = max(cur1[0],cur2[0])
        x2 = min(cur1[0],cur2[0])
        y1 = max(cur1[1],cur2[1])
        y2 = min(cur1[1],cur2[1])
        for i in range(len(val['line2_x'])):
            if (val['line2_x'][i] > x2-v)&(val['line2_x'][i] < x1+v)&(val['line2_y'][i] > y2-v)&(val['line2_y'][i] < y1+v):
                print "Player 1 loses"
                self.popup2.open()
                self.t()        
         
        
class Snake(Widget):
    def move1(self,data):
        self.pos = Vector(*self.velocity)+self.pos
        data["line1_x"] += [self.pos[0]]
        data["line1_y"] += [self.pos[1]]
        data["line1"].points += (self.center_x,self.center_y)
    def current1(self,data):
        data['current1'][1] = data['current1'][0]
        data['current1'][0] = (self.pos[0],self.pos[1])
        
    def current2(self,data):
        data['current2'][1] = data['current2'][0]
        data['current2'][0] = (self.pos[0],self.pos[1])
        
    def move2(self,data):
        self.pos = Vector(*self.velocity)+self.pos
        data["line2_x"] += [self.pos[0]]
        data["line2_y"] += [self.pos[1]] 
        #print data['line2_x']
        data["line2"].points += (self.center_x,self.center_y)

    
        
Factory.register("KurveGame",KurveGame)
Factory.register("Snake",Snake)
   
if __name__ in ('__main__'):
    KurveApp().run()     
        
