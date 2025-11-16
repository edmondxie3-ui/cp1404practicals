from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

class ConvertMilesKm(App):
    message = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        try:
            result = float(value) * 1.609
            self.message = str(result)
        except ValueError:
            pass

ConvertMilesKm().run()
