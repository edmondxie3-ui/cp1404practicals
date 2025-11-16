from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["John", "Greg", "Ted"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        container = self.root.ids.main

        for name in self.names:
            lbl = Label(text=name)
            container.add_widget(lbl)
        return self.root


DynamicLabelsApp().run()