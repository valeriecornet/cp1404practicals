"""Miles to km converter"""

from kivy.app import App
from kivy.lang import Builder

CONVERSION = 1.60934


class MilesConverterApp(App):
    """ Converts miles to kilometres """
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """ calculate km """
        value = self.value()
        result = value * CONVERSION
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment):
        """increment miles value"""
        value = self.value() + increment
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def value(self):
        """Return 0 if not correct value"""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0.0


MilesConverterApp().run()
