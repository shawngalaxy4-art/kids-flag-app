from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import AsyncImage
from kivy.core.text import LabelBase

class FlagApp(App):
    def build(self):
        layout = GridLayout(cols=2, spacing=10, padding=10)
        # Example for Afghanistan
        btn = Button(background_normal='https://flagcdn.com/w320/af.png', size_hint_y=None, height=200)
        btn.bind(on_press=self.speak_flag)
        layout.add_widget(btn)
        return layout

    def speak_flag(self, instance):
        print("Feature: Trigger Android Text-to-Speech here")

if __name__ == '__main__':
    FlagApp().run()
