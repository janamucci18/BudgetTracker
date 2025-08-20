from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) 
        with self.canvas.before: 
            Color(1, 1, 1, 1)  # RGB + Alpha (white)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        self.window = GridLayout()
        self.window.spacing = 20
        self.window.cols = 1    
        self.window.size_hint = (0.6,0.9)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

        self.window.add_widget(Image(source='Assets/CAD_black.png',  size_hint=(2, 2)))
        self.greeting = Label(
            text="Lets break down your last bank statement, please upload it below!",
            font_size=30,
            color='#000000'
        )
        self.window.add_widget(self.greeting)

        # Add PDF Upload Button
        self.upload_button = Button(text="Upload PDF", size_hint=(1, 0.2), background_color = "#00bf63",
                             background_normal = "")
        self.upload_button.bind(on_release=self.open_file_popup)
        self.window.add_widget(self.upload_button)

        # PDF RUN Button
        self.run_stat = Button(text="Run Statement", size_hint=(1, 0.2), background_color = "#00bf63",
                             background_normal = "")
       # self.run_stat.bind(on_release=self.open_file_popup)
        self.window.add_widget(self.run_stat)



        # Label to show selected file
        self.selected_file_label = Label(text="", font_size=20, color='#000000')
        self.window.add_widget(self.selected_file_label)

        self.add_widget(self.window)



    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def open_file_popup(self, instance):
        # Layout for Popup
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        filechooser = FileChooserListView(filters=["*.pdf"], size_hint=(1, 0.8))
        layout.add_widget(filechooser)

        # Buttons at bottom of popup
        btn_layout = BoxLayout(size_hint=(1, 0.2), spacing=10)
        select_btn = Button(text="Select")
        cancel_btn = Button(text="Cancel")
        btn_layout.add_widget(select_btn)
        btn_layout.add_widget(cancel_btn)
        layout.add_widget(btn_layout)

        # Create popup
        popup = Popup(title="Select a PDF", content=layout, size_hint=(0.9, 0.9))

        # Bind buttons
        select_btn.bind(on_release=lambda x: self.select_file(filechooser.selection, popup))
        cancel_btn.bind(on_release=popup.dismiss)

        popup.open()

    def select_file(self, selection, popup):
        if selection:
            self.selected_file_label.text = f"Selected file: {selection[0]}"
            print(f"PDF selected: {selection[0]}")
        popup.dismiss()


