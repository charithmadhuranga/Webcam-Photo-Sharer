from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from fileshare import FileSharer
import time
Builder.load_file('design.kv')


class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play = True
        self.ids.startbtn.text = 'Stop'
    def stop(self):
        self.ids.camera.play = False
        self.ids.camera.texture = None
        self.ids.startbtn.text = 'Start'
    def capture(self):
        curent_time = time.strftime('%Y%m%d-%H%M%S')
        filepath = f"captures/{curent_time}.png"
        self.ids.camera.export_to_png(filepath)
    pass

class ImageScreen(Screen):
    pass

class RootWidget(Screen):
    pass



class MainApp(App):
    def build(self):
        return RootWidget()

MainApp().run()