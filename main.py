from kivy.app import App 
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class Interface(FloatLayout):

    def Display_information(self):
        data = self.ids.textinput.text
        self.ids.label.text = data


class myApp(App):
    pass

myApp().run()
