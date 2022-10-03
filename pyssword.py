from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout

class MeuLayout(FloatLayout):
    pass
class PysswordApp(App):
    def build(self):
        return MeuLayout()

if __name__ == "__main__":
    PysswordApp().run()