from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
import time


class ImageScreen(Screen):
    pass


class CameraScreen(Screen):

    def start(self):
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None

    def capture(self):
        current_time = time.strftime("%Y%m%d-%H%M%S")
        filepath = f"files/{current_time}.png"
        self.ids.camera.export_to_png(filepath)
        print("Image captured and saved")
        self.manager.current = "image_screen"


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
