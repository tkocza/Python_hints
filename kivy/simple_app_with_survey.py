from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager


class WelcomeScreen(Screen):
    pass

class SurveyScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("simple_app_with_survey_layout.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()

