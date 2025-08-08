from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) 
        with self.canvas.before:
            Color(1, 1, 1, 1)  # RGB + Alpha (white)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)


        self.window = GridLayout()
        self.window.cols = 1    
        self.window.size_hint = (0.6,0.9)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

        self.window.add_widget(Image(source='Assets/CAD_black.png',  size_hint=(2, 2)))
        self.greeting = Label(text = "time for some girl math!",
                              font_size = 30,
                              color = '#000000')
        self.window.add_widget(self.greeting)
        self.add_widget(self.window)
    
    
    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
 

