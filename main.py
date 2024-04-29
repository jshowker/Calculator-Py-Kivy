from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
import re

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)

class CalculatorApp(App):

    def update_label(self):
        self.lbl.text = self.formula

    def add_number(self, instance):
        if self.formula == '0':
            self.formula = ''
        self.formula += str(instance.text)
        self.update_label()

    def add_operation(self, instance):
        operation = instance.text
        if operation == 'x':
            operation = '*'
        if self.formula and (self.formula[-1] not in '+-*/'):
            self.formula += operation
        self.update_label()

    def calc_result(self, instance):
        try:
            # Обработка выражения с использованием безопасной функции eval
            self.formula = str(eval(self.formula))
            self.update_label()
        except Exception as e:
            self.formula = 'Error'
            self.update_label()

    def clear(self):
        # Сброс к начальному состоянию
        self.formula = '0'
        self.update_label()

    def build(self):
        self.formula = '0'
        bl = BoxLayout(orientation='vertical', padding=25)
        gl = GridLayout(cols=4, spacing=3, size_hint=(1, .6))

        self.lbl = Label(text='0', font_size=40, halign='right', valign='center', size_hint=(1, .4), text_size=(400-50, 500*.4-50))
        bl.add_widget(self.lbl)

        numbers = ['7', '8', '9', 'x', '4', '5', '6', '-', '1', '2', '3', '+']
        for number in numbers:
            btn = Button(text=number)
            if number in '1234567890.':
                btn.on_press = lambda btn=btn: self.add_number(btn)
            else:
                btn.on_press = lambda btn=btn: self.add_operation(btn)
            gl.add_widget(btn)

        gl.add_widget(Button(text='C', on_press=lambda btn=Button(text='C'): self.clear()))
        gl.add_widget(Button(text='0', on_press=lambda btn=Button(text='0'): self.add_number(btn)))
        gl.add_widget(Button(text='.', on_press=lambda btn=Button(text='.'): self.add_number(btn)))
        gl.add_widget(Button(text='=', on_press=lambda btn=Button(text='='): self.calc_result(btn)))

        bl.add_widget(gl)
        return bl

if __name__ == '__main__':
    CalculatorApp().run()
