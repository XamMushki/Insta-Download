
__version__ = '1.0.0'

from instaloader import Instaloader, Profile
import instaloader
from kivymd.app import MDApp
from kivy.base import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.properties import ObjectProperty

Window.size = (320, 600)

'''Please use instaloader instead of instalooter'''


# # post_code = input('Post Code> ')
# # looter = PostLooter(post_code)
# # looter.download('download/', media_count=10)
#
# u_name = input('Username> ')
# l = ProfileLooter(u_name)
# path = 'downloads/' + u_name
# l.download(path, media_count=10)
#
class WindowManager(ScreenManager):
    pass


class MainWindow(Screen):
    u_name = ObjectProperty(None)

    def download(self):
        try:
            username = self.u_name.text
            # L = Instaloader(save_metadata=True, compress_json=False, download_video_thumbnails=False)
            L = Instaloader(download_video_thumbnails=False, download_comments=False, compress_json=False)
            USER = username
            PROFILE = USER
            profile = Profile.from_username(L.context, PROFILE)
            post_list = profile.get_posts()
            for post in post_list:
                L.download_post(post, PROFILE)
            L.close()

            return 0
            #     self.u_name.text='Error! Private User or Something else'
        except instaloader.exceptions.ProfileNotExistsException:
            username = self.u_name.text
            # L = Instaloader(save_metadata=True, compress_json=False, download_video_thumbnails=False)
            L = Instaloader(download_video_thumbnails=False, download_comments=False,
                            compress_json=False)
            post_url = username
            # PROFILE = USER
            post_code = username
            post = instaloader.Post.from_shortcode(L.context, post_code)
            L.download_post(post, 'Downloads')
            L.close()
            # profile = Profile.from_username(L.context, PROFILE)
            # post_list = profile.get_posts()


class MainApp(MDApp):
    title = "Insta-Download"

    def build(self):
        kv = Builder.load_file('main.kv')
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return kv


if __name__ == '__main__':
    app = MainApp()
    app.run()
