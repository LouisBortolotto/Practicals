from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

from kivy.app import StringProperty

__author__ = 'Louis Bortolotto'


class MilesConverter(App):

    kilometres = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (600, 250)
        self.title = "Miles to Kilometres Converter"
        self.root = Builder.load_file('miles_to_kilometres.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        result = value ** 1.61
        self.kilometres = str(result)

    def handle_increment(self, text, change):
        value = value + change
        self.root.ids.input_number = str(value)


MilesConverter().run()
