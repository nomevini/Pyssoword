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

    def exibirSenha(self):
        self.geradorSenha = Pyssword()
        self.geradorSenha.gerar_senha()
        
class PysswordLayout(GridLayout):
    def __init__(self, **kwargs):    
        super(PysswordLayout, self).__init__(**kwargs)
        self.cols = 1
        #self.rows = 4
        #self.row_force_default=True
        #self.row_default_height=40

        """self.add_widget(Label(text="Pyssord"))
        self.senhaGerada = None
        self.add_widget(Label(text=F"{self.senhaGerada}"))
        self.botaoGerar = Button(text="Gerar")
        self.botaoGerar.bind(on_press=self.exibirSenha)
        self.add_widget(self.botaoGerar)
        self.botaoConfigurar = Button(text="Configurar")
        self.add_widget(self.botaoConfigurar)"""

    def botaoGerarSenha(self, instance):
        pass

    def exibirSenha(self, upperCase:bool = None, lowerCase:bool = True, numbers:bool = True, simbols:bool = True, qtd_numbers:int =8) -> str:
        self.geradorSenha = Pyssword()
        self.senhaGerada =  self.geradorSenha.gerar_senha()
        self.ids.senha.text = self.senhaGerada = self.geradorSenha.gerar_senha()
        

        

class PysswordApp(App):
    def build(self):
        #return MeuLayout()
        return PysswordLayout()


if __name__ == "__main__":
    PysswordApp().run()
