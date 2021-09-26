"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Sam Messer
Started 26/09/2021
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class SquareNumberApp(App):

    def build(self):
        Window.size = (200, 100)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        try:
            result = int(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = ""


SquareNumberApp().run()
