import kivy
kivy.require('1.0.9')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color,Ellipse

class MyPaintWidget(Widget):
    def on_touch_down(self,touch):
        with self.canvas:
            Color(1,1,0)
            d = 30.0
            Ellipse(pos = (touch.x - d/2,touch.y - d/2),size = (d,d))

class MyApp(App):
    def build(self):
        return MyPaintWidget()

if __name__ in ('__android__','__main__'):
    MyApp().run()



