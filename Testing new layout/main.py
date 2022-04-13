# TEST
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from pytube import YouTube
import os

Builder.load_file("styles.kv")

class MyLayout(Widget):
    def clear(self):
        self.ids.textinp.text = ""


class application(App):
    def build(self):
        MyLayout.build()
        Window.clearcolor = (1, 1, 1, 1) #Hintergrund Window
        return MyLayout()

application().run()