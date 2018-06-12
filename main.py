from kivy.app import App
from kivy.uix.widget import Widget
from random import choice


class MyWidget(Widget):

    membros = ['PÉ DIREITO', 'PÉ ESQUERDO', 'MÃO DIREITA', 'MÃO ESQUERDA']
    cores = [0, 1, 2, 11]

    def jogada(self, bt):
        instrucao = choice(self.membros)
        cor = choice(self.cores)
        cor_padrao = [0, 0, 0, .7]
        try:
            cor_padrao[cor] = 1
        except IndexError:
            cor_padrao = [1, 1, 0, .85]

        if instrucao == self.membros[0] or instrucao == self.membros[1]:
            self.ids['img'].source = 'data/pe2.png'
        else:
            self.ids['img'].source = 'data/mao3.png'
        bt.background_color = cor_padrao
        bt.text = instrucao


class TwisterApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    TwisterApp().run()
