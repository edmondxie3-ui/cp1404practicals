from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.609

class ConvertMilesKm(App):
    message = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        try:
            kilometers = float(value) * MILES_TO_KM
            self.message = str(kilometers)
        except ValueError:
            pass

    def handle_increment(self, increment):
        try:
            current = float(self.root.ids.input_miles.text)
            self.root.ids.input_miles.text = str(current + increment)
        except ValueError:
            self.root.ids.input_miles.text = "0"

ConvertMilesKm().run()
