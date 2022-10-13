from random import choice, shuffle
from turtle import width
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.switch import Switch

class GerenciadorTelas(ScreenManager):
    pass

class TelaPrincipal(GridLayout,Screen):
    def __init__(self, **kwargs):    
        super(TelaPrincipal, self).__init__(**kwargs)
        self.cols = 1
    
    def exibirSenha(self, upperCase:bool = None, lowerCase:bool = True, numbers:bool = True, simbols:bool = True, qtd_numbers:int =8) -> str:
        self.geradorSenha = Pyssword()
        self.senhaGerada =  self.geradorSenha.gerar_senha()
        self.ids.senha.text = self.senhaGerada = self.geradorSenha.gerar_senha()

class TelaConfiguracao(GridLayout,Screen):
    def __init__(self, **kwargs):    
        super(TelaConfiguracao, self).__init__(**kwargs)
        self.cols = 1

    def switch_click(self, switchObject, switchValue,configuração):
        print(switchValue,configuração)
        
class Pyssword:
    def __init__(self):
        self.letters_lower_case = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
                                   "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.letters_upper_case = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
                                   "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        self.simbols = ["!", "@", "#", "$", "%", "&", "*", "_"]

    def gerar_senha(self, upperCase=True, lowerCase=True, numbers=True, simbols=True, qtd_numbers=8):
        senha = ''
        if upperCase or lowerCase or numbers or simbols:
            while len(senha) < qtd_numbers:
                if upperCase:
                    senha += choice(self.letters_upper_case)
                if lowerCase:
                    senha += choice(self.letters_lower_case)
                if numbers:
                    senha += choice(self.numbers)
                if simbols:
                    senha += choice(self.simbols)
            senha = list(senha)
            shuffle(senha)
            senha = ''.join(senha)
            if len(senha) > 12:
                return senha[0:13]
            else:
                return senha
        else:
            # nenhum campo foi escolhido, impossivel gerar senha
            return False

class SimpleSwitch(GridLayout): 
    def __init__(self, **kwargs): 
        super(SimpleSwitch, self).__init__(**kwargs) 
        self.cols = 2
        self.add_widget(Label(text ="Switch")) 
        self.settings_sample = Switch(active = False) 
        self.add_widget(self.settings_sample)

class TesteApp(App):
    """def build(self):
        #return MeuLayout()
        return TelaPrincipal()"""
    pass

if __name__ == "__main__":
    TesteApp().run()
