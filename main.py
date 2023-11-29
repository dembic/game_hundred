from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
import random

Window.size = (500, 400)

rnd = int(random.randrange(100))
user = int(1)
i = 0


class GameHundred(GridLayout):

    def __init__(self, **kwargs):
        super(GameHundred, self).__init__(**kwargs)
        self.cols = 1
        self.rows = 30
        self.row_default_height = 30
        self.padding = 60

        self.count = 0

        self.add_widget(Label(text='Игра угадай число от 1 до 100', size_hint=(1.0, .05)))
        # self.add_widget(Label(text=str(user), size_hint=(1.0, 0.05)))

        self.user = TextInput(multiline=False, input_filter='int', size_hint=(1.0, .05))
        self.add_widget(self.user)

        self.add_widget(Label(text=str(rnd), size_hint=(1.0, .05)))

        self.userButton = Button(text='Угадай', on_press=self.clsInputText, size_hint=(1.0, .05))
        self.add_widget(self.userButton)

    def clsInputText(self, instance):

        if self.user.text != '':
            self.count += 1

        if self.user.text == '':
            return True

        if int(self.user.text) < rnd:
            ss = 'Я загадал больше'
        elif int(self.user.text) > rnd:
            ss = 'Я загадал меньше'
        else:
            ss = 'Ты угадал c ' + str(self.count) + ' попыток'
            self.userButton = Button(text='С играем еще?', size_hint=(1.0, .05))
            self.add_widget(self.userButton)
            # return
        self.add_widget(Label(text=ss, size_hint=(1.0, 0.05)))
        self.user.text = ''

class MyApp(App):
    def build(self):
        return GameHundred()


if __name__ == '__main__':
    MyApp().run()
