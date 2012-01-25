import kivy
kivy.require('1.0.9')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
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
        parent = Widget()
        painter = MyPaintWidget()
        clrbtn = Button(text="clear")
        parent.add_widget(painter)
        parent.add_widget(clrbtn)

        def clear_canvas(obj):
            painter.canvas.clear()

        clrbtn.bind(on_release = clear_canvas)

        return parent

if __name__ in ('__android__','__main__'):
    MyApp().run()



