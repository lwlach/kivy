from kivy.app import App
from kivy.uix.widget import Widget
from math import ceil

# __version__ = '1.0'


class MyWidget(Widget):
    c = 0
    s = 1

    def count(self, bt):
        self.ids['lb1'].text = str(self.s)
        self.c += 1
        aux = ceil(self.c / self.s)
        if aux == 1:
            bt.text = str(self.s)
        elif aux == 2:
            bt.text = 'Patinho'
        elif aux == 3:
            bt.text = 'Quac'
            if self.s * aux == self.c:
                self.c = 0
                self.s += 1

    def reset(self):
        self.c = 0
        self.s = 1
        self.ids['bt1'].text = 'Start!'
        self.ids['lb1'].text = str(0)


class PatinhoApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    PatinhoApp().run()

