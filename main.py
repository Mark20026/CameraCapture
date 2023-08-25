from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class CameraScreen(Screen):

    def start(self):
        pass

    def stop(self):
        pass

    def capture(self):
        pass



class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
