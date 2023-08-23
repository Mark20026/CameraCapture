from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class CameraScreen(Screen):
    pass


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
