import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.vector import Vector
from kivy.factory import Factory
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import ObjectProperty,DictProperty
from kivy.graphics import Line

class KurveApp(App):
    def build(self):
        game = KurveGame()
        leftbtn = Button(text="left",pos = (0,500))
        rightbtn = Button(text = "right",pos = (0,0))
        game.add_widget(leftbtn)
        game.add_widget(rightbtn)
        game.begin()
        Clock.schedule_interval(game.update,1.0/6.0)
               
        def turn_left(obj):
            game.snake1.velocity = Vector(*game.snake1.velocity).rotate(10)
        def turn_right(obj):
            game.snake1.velocity = Vector(*game.snake1.velocity).rotate(270)
        leftbtn.bind(on_press = turn_left)
        rightbtn.bind(on_release = turn_right)
        return game
        
class KurveGame(Widget):
    snake1 = ObjectProperty(None)
    snake2 = ObjectProperty(None)
    a = dict()
    a['hello'] = 2 #These two steps are done just so that the dict is properly initialized.
    data = DictProperty(a)
        
            
    def begin(self):
        self.snake1.pos = self.pos[0],self.pos[1]+300
        self.snake2.pos = self.x,self.y+150
        print self.center
        self.snake1.velocity = (25,0)
        self.snake2.velocity = (25,0)
        with self.canvas:
            self.data["line1"] = Line(points = (self.snake1.center_x,self.snake1.center_y))
            self.data["line2"] = Line(points = (self.snake2.center_x,self.snake2.center_y))
        
    def update(self,dt):
        self.snake1.move1(self.data)
        self.snake2.move2(self.data)
        
            
    def on_touch_move(self,touch):
        pass
   
class Snake(Widget):
    def move1(self,data):
        self.pos = Vector(*self.velocity)+self.pos
        data["line1"].points += (self.center_x,self.center_y)
        
    def move2(self,data):
        self.pos = Vector(*self.velocity)+self.pos
        data["line2"].points += (self.center_x,self.center_y)

    
        
Factory.register("KurveGame",KurveGame)
Factory.register("Snake",Snake)
   
if __name__ in ('__main__'):
    KurveApp().run()     
        
