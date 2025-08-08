from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from landing_screen import LandingScreen    
from home import HomeScreen

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LandingScreen(name='landing'))
        sm.add_widget(HomeScreen(name='home'))
        return sm


MyApp().run()