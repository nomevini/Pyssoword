from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout

class MeuLayout(FloatLayout):
    usuario = ObjectProperty(None)
    senha = ObjectProperty(None)

    def fazerLogin(self):
        usuario = self.usuario.text
        senha = self.senha.text
        if usuario == "mauricio" and senha == "senha123":
            print("Entrou!!!")
        else:
            print("Sai fora!!!")

        self.usuario.text = ""
        self.senha.text = ""

class PysswordApp(App):
    def build(self):
        return MeuLayout()

if __name__ == "__main__":
    PysswordApp().run()