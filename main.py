from random import choice, shuffle
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.switch import Switch
from kivy.uix.slider import Slider
from kivy.core.clipboard import Clipboard as Cb
#import pyperclip
from kivy.core.window import Window
Window.clearcolor = (186/255,35/255,246/255,1)

class GerenciadorTelas(ScreenManager):
    def irParaTela(self, screen):
        self.current = screen


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


class TelaPrincipal(Screen):
    def exibirSenha(self):
        self.senhaGerada = passwordGenerator.gerar_senha()
        if self.senhaGerada:
            self.manager.ids.senha.text = self.senhaGerada
        else:
            self.manager.ids.senha.text = "Opções para geração de senha inválidas"

    def copiarParaAreaTransferencia(self):
        #pyperclip.copy(self.manager.ids.senha.text)
        Cb.copy(self.manager.ids.senha.text)

class TelaConfiguracao(Screen):
    # objetivo desssa funcao e definir os atributos
    def defineTypePassword(self, upperCase, lowerCase, numbers, simbols, qtd_numbers):
        passwordGenerator.upperCase = upperCase
        passwordGenerator.lowerCase = lowerCase
        passwordGenerator.numbers = numbers
        passwordGenerator.simbols = simbols
        passwordGenerator.qtd_numbers = int(qtd_numbers)

class MainApp(App):
    def build(self):
        return GerenciadorTelas()
    pass


if __name__ == "__main__":
    MainApp().run()
