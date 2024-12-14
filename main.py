from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from fileshare import FileSharer
import time
import pyperclip
import webbrowser
from dotenv import load_dotenv
import os




Builder.load_file("design.kv")


class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play = True
        self.ids.startbtn.text = "Stop"
        self.ids.camera.opacity = 1
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.opacity = 0
        self.ids.camera.play = False
        self.ids.camera.texture = None
        self.ids.startbtn.text = "Start"

    def capture(self):
        curent_time = time.strftime("%Y%m%d-%H%M%S")
        filepath = f"captures/{curent_time}.png"
        self.ids.camera.export_to_png(filepath)
        if self.ids.camera.play:
            self.manager.current = "image_screen"
        self.manager.get_screen("image_screen").ids.img.source = filepath


class ImageScreen(Screen):
    load_dotenv()
    public_key = os.getenv("UPLOADCARE_PUBLIC_KEY")
    secret_key = os.getenv("UPLOADCARE_SECRET_KEY")
    def share(self):
        fileshare = FileSharer(
            filepath=self.ids.img.source,
            public_key=self.public_key,
            secret_key=self.secret_key,
        )
        link = fileshare.share()
        self.ids.linklabel.text = link
        return link

    def copylink(self):
        pyperclip.copy(self.ids.linklabel.text)
        self.ids.linklabel.text = "Copied to clipboard"


    def openlink(self):
        if self.ids.linklabel.text == "Copied to clipboard":
            self.ids.linklabel.text = pyperclip.paste()
        webbrowser.open(self.ids.linklabel.text)

    def goback(self):
        self.manager.current = "camera_screen"


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
