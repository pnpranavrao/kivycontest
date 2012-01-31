import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.vector import Vector
from kivy.factory import Factory
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.properties import ObjectProperty,DictProperty,NumericProperty
from kivy.graphics import Line,Color,Rectangle
from kivy.config import Config
import math
import sys
#android audio. Comment the next line
from kivy.core.audio import SoundLoader

class KurveApp(App):
    def build(self):
        #game = KurveGame()
        self.root = FloatLayout()
        #android audio. Comment next 2 lines to use on android
        self.sound = SoundLoader.load(filename = 'assets/song.mp3')
        self.sound.play()
        loadscreen = Image(source='assets/intro.png')
        x,y = 1280,736
        
        
        start = Button(text = "PLAY! ",font_size = 30,pos = (x-x*3/8,y/10),size=(x/4,y/8))
        help1 = Button(text = "Help",font_size = 20,pos = (x/8,y/10),size=(x/8,y/8))
        start.bind(on_press = self.startgame)
        help1.bind(on_press = self.loadhelp)
        loadscreen.add_widget(start)
        loadscreen.add_widget(help1)
        self.root.add_widget(loadscreen)
        return self.root

    def loadhelp(self,obj):
        app = self
        x,y = 1280,736
        self.root.clear_widgets()
        helpimg = Image(source = 'assets/help.jpg')
        back = Button(text = "Got it. Lets Play!",font_size = 25,pos = (x-x*3/8,y/10),size=(x/4,y/8))
        helpimg.add_widget(back)
        self.root.add_widget(helpimg)
        def backfn(obj):
            self.startgame(app)
        back.bind(on_press = backfn)
        return self.root
    

    def startgame(self,obj):
        self.root.clear_widgets()
        game = KurveGame()
        x = game.width
        y = game.top
        leftbtn = Button(text = "left",pos = (0,y-y/6),size=(x/12,y/6))
        rightbtn = Button(text = "right",pos = (0,0),size=(x/12,y/6))
        leftbtn2 = Button(text="left",pos = (x-x/12,0),size=(x/12,y/6))
        rightbtn2 = Button(text = "right",pos = (x-x/12,y-y/6),size=(x/12,y/6))
        game.add_widget(leftbtn)
        game.add_widget(rightbtn)
        game.add_widget(leftbtn2)
        game.add_widget(rightbtn2)
        game.begin(self,self.root)
        Clock.schedule_interval(game.update,1.0/15.0)
                    
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
        self.root.add_widget(game)
        
        return self.root
        
        
class KurveGame(Widget):
    a = dict()
    a['hello'] = 2 
#These two steps are done just so that the dict is properly initialized.
    data = DictProperty(a)
    snake1 = ObjectProperty(None)
    snake2 = ObjectProperty(None)
    def begin(self,app,root):
        self.app = app
        self.root = root
        y=self.top
        x=self.width
        with self.canvas:
            Rectangle(pos=(0,0),size=(x/126,y))
            Rectangle(pos=(0,0),size=(x,y/80))
            Rectangle(pos=(x-x/126,0),size=(x/126,y))
            Rectangle(pos=(0,y-y/80),size=(x,y/80))
        self.data['div']=(160.0,92.0)
        self.data['pix']=(1280.0,736.0)
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
       
        #Uncomment following to check if initial matrix is generated properly
        '''
        for i in range(divy):
            for j in range(divx):
                print self.data['occupied'][(i*divx)+j],
            print "\n"
        '''

        self.snake1.pos = self.width/6,self.top/6
        self.snake2.pos = self.width*5/6,self.top*5/6
        self.snake1.velocity = (8,0)
        self.snake2.velocity = (-8,0)
        with self.canvas:
            Color(255,255,0)
            self.data["line1"] = Line(points = (self.snake1.center_x,self.snake1.center_y))
            Color(0,191,255)
            self.data["line2"] = Line(points = (self.snake2.center_x,self.snake2.center_y))
    #Change these images
    winner1 = Image(source = 'assets/bluewins.jpg')
    winner2 = Image(source = 'assets/yellowwins.jpg')
   
    def update(self,dt):
        a = self.snake1.move1(self.data)
        b = self.snake2.move2(self.data)
        if (a&b)!=True:
            root = self.root
            app = self.app
            root.clear_widgets()
            if a == False:
                root.add_widget(self.winner1)
                
            if b == False:
                root.add_widget(self.winner2)
            return False
        
class Snake(Widget):
   
    def stop(self):
            exit(1)
    t = Clock.create_trigger(stop,timeout = 4)

    def move1(self,data):
        if self.check(data):
            return False
        self.pos = Vector(*self.velocity)+self.pos
        data["line1"].points += (self.center_x,self.center_y)
        n = self.convert(data)
        #print n
        data['occupied'][n] = 1
        return True
        
    def move2(self,data):
        if self.check(data):
            return False
        self.pos = Vector(*self.velocity)+self.pos
        data["line2"].points += (self.center_x,self.center_y)
        n = self.convert(data)
        #print "    ",n
        data['occupied'][n] = 1
        return True
        
        
    def convert(self,data):
        x_pix,y_pix = data['pix']
        divx,divy = data['div']
        x,y = self.pos
        x = math.floor(float(x)/float(x_pix/divx))
        y = math.floor(float(y)/float(y_pix/divy))
        n = (divx)*y + x
        if n<divx*divy:
            return int(n)
        else:
            print "large value",n,self.pos,x,y
            return 300
    
    def convert1(self,pos,data):
        x_pix,y_pix = data['pix']
        divx,divy = data['div']
        x,y = pos
        x = math.floor(float(x)/float(x_pix/divx))
        y = math.floor(float(y)/float(y_pix/divy))
        n = (divx)*y + x
        if n<divx*divy:
            #Uncomment folowwing to debug
            '''
            print "----------"
            print "check at",pos,int(n)
            '''
            return int(n)
        else:
            print "large value",n,self.pos,x,y
            return 300
       
    def check(self,data):
        pos = Vector(*self.velocity)+self.pos
        if data['occupied'][self.convert1(pos,data)]==1:
            #Uncomment the following to debug
            '''
            print self.uid,"Died at",pos,self.convert1(pos,data)
            print "game over"
            divx,divy = int(data['div'][0]),int(data['div'][1])
            m = dict()
            string = ""
            for i in range(divy):
                string = ""
                for j in range(divx):
                    string  += str(data['occupied'][(i*divx)+j])
                    #sys.stdout.write(str(data['occupied'][(i*divx)+j]))
                #print "\n
                m[str(i)]=str(string)
            for i in range(divy-1,-1,-1):
                print m[str(i)]
            '''  
            return(1)
            
Factory.register("KurveGame",KurveGame)
Factory.register("Snake",Snake)
   
if __name__ in ('__main__'):
    #Config.set('kivy','fullscreen','1')
    #Config.write()
    KurveApp().run()     
        
