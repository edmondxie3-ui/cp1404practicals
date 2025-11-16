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
            miles = float(value)
        except ValueError:
            miles = 0
        kilometers = float(miles) * MILES_TO_KM
        self.message = str(kilometers)

    def handle_increment(self, increment):
        try:
            current = float(self.root.ids.input_miles.text)
        except ValueError:
            current = "0"

        new_value = current + increment
        self.root.ids.input_miles.text = str(new_value)
        self.handle_calculate(self.root.ids.input_miles.text)

ConvertMilesKm().run()
