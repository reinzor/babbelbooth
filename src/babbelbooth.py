#!/usr/bin/env python

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.config import Config

# Set the raspberry pi size 
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '1280')
Config.set('graphics', 'height', '1024')

class Babbelbooth(App):

    def build(self):
        return FloatLayout()

if __name__ == "__main__":
    Babbelbooth().run()