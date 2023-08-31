from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
import time
from filesharer import Filesharer
from kivy.core.clipboard import Clipboard
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import webbrowser


class ImageScreen(Screen):
    create_a_link = "Create a link"

    def create_link(self):
        file_path = App.get_running_app().root.ids.camera_screen.filepath
        fileshare = Filesharer(filepath=file_path)
        self.url = fileshare.share()
        self.ids.link.text = self.url

    def copy_link(self):
        try:
            Clipboard.copy(self.url)
            self.show_popup()
        except:
            self.ids.link.text = self.create_a_link

    def open_link(self):
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text = self.create_a_link

    @staticmethod
    def show_popup():
        content = Label(text="Link copied to clipboard!")
        popup = Popup(content=content, size_hint=(None, None), size=(400, 200))
        popup.open()


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
        self.filepath = f"files/{current_time}.png"
        self.ids.camera.export_to_png(self.filepath)
        print("Image captured and saved")
        self.manager.current = "image_screen"
        self.manager.current_screen.ids.img.source = self.filepath


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
