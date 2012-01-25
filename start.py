import kivy
kivy.require('1.0.9')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color,Ellipse,Line

class MyPaintWidget(Widget):
    def on_touch_down(self,touch):
        userdata = touch.ud
        with self.canvas:
            Color(1,1,0)
            d = 30.0
            Ellipse(pos = (touch.x - d/2,touch.y - d/2),size = (d,d))
            userdata['line'] = Line(points = (touch.x,touch.y))
    
    def on_touch_move(self,touch):
        touch.ud['line'].points += [touch.x,touch.y]

class MyApp(App):
    def build(self):
        return MyPaintWidget()

if __name__ in ('__android__','__main__'):
    MyApp().run()



