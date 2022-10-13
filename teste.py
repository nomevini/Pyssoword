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
from kivy.uix.slider import Slider


class GerenciadorTelas(ScreenManager):
    pass


class Pyssword:
    def __init__(self):
        self.letters_lower_case = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
                                   "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.letters_upper_case = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
                                   "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.listNumbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        self.listSimbols = ["!", "@", "#", "$", "%", "&", "*", "_"]
        self.upperCase = True
        self.lowerCase = True
        self.numbers = True
        self.simbols = True
        self.qtd_numbers = 10

    def gerar_senha(self):
        senha = ''
        if self.upperCase or self.lowerCase or self.numbers or self.simbols:
            print(f"Quantidade de numeros: {self.qtd_numbers}")
            while len(senha) < self.qtd_numbers:
                if self.upperCase:
                    senha += choice(self.letters_upper_case)
                if self.lowerCase:
                    senha += choice(self.letters_lower_case)
                if self.numbers:
                    senha += choice(self.listNumbers)
                if self.simbols:
                    senha += choice(self.listSimbols)
            senha = list(senha)
            shuffle(senha)
            senha = ''.join(senha)
            if len(senha) > self.qtd_numbers:
                return senha[0:self.qtd_numbers]
            else:
                return senha
        else:
            # nenhum campo foi escolhido, impossivel gerar senha
            return False


passwordGenerator = Pyssword()


class TelaPrincipal(GridLayout, Screen):
    def __init__(self, **kwargs):    
        super(TelaPrincipal, self).__init__(**kwargs)
        self.cols = 1
    
    def exibirSenha(self, upperCase:bool = None, lowerCase:bool = True, numbers:bool = True, simbols:bool = True, qtd_numbers:int =8) -> str:
        #self.geradorSenha = Pyssword()
        self.senhaGerada = passwordGenerator.gerar_senha()
        self.ids.senha.text = self.senhaGerada


class TelaConfiguracao(GridLayout, Screen):
    def __init__(self, **kwargs):    
        super(TelaConfiguracao, self).__init__(**kwargs)
        self.cols = 1

    # , sLetrasMinusculas.active, sNumeros.active, sSimbolos.active, sQntCaracteres.value
    def switch_click(self, switchObject, switchValue, configuração):
        print(switchValue, configuração)

    # objetivo desssa funcao e definir os atributos
    def defineTypePassword(self):
        passwordGenerator.upperCase = self.ids.sLetrasMaiusculas.active
        passwordGenerator.lowerCase = self.ids.sLetrasMinusculas.active
        passwordGenerator.numbers = self.ids.sNumeros.active
        passwordGenerator.simbols = self.ids.sSimbolos.active
        passwordGenerator.qtd_numbers = int(self.ids.sQntCaracteres.value)


class SimpleSwitch(GridLayout): 
    def __init__(self, **kwargs): 
        super(SimpleSwitch, self).__init__(**kwargs) 
        self.cols = 2
        self.add_widget(Label(text ="Switch")) 
        self.settings_sample = Switch(active=False)
        self.add_widget(self.settings_sample)


class TesteApp(App):
    """def build(self):
        #return MeuLayout()
        return TelaPrincipal()"""
    pass


if __name__ == "__main__":
    TesteApp().run()
