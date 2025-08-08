from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen


class LandingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.window = GridLayout()
        self.window.cols = 1    
        self.window.size_hint = (0.6,0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

        self.window.add_widget(Image(source='Assets/ctr_alt_delete.png',  size_hint=(2, 2)))
        self.greeting = Label(text = "Welcome!",
                              font_size = 30)
        self.window.add_widget(self.greeting)
        
        # using anchor layout wrap to center the button, otherwise its left aligned
        button_container = AnchorLayout(anchor_x='center', anchor_y='center')
        self.getStarted = Button(text="Get Started",
                             size_hint=(None, 0.6),
                             width=300,
                             background_color = "#00bf63",
                             background_normal = "") # background color will be darker than normal without this
        self.getStarted.bind(on_press=self.go_to_home) # go to home is a function def go_to_home found below
        button_container.add_widget(self.getStarted)
        self.window.add_widget(button_container)
        self.add_widget(self.window)
    
    def go_to_home(self, instance):
        self.manager.current = 'home'