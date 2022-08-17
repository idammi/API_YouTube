
from selenium_driver import BaseClass
from youtube_api import YouTube


def main():

    base = BaseClass()
    DRIVER = base.driver()

    youtube_ = YouTube(DRIVER)
    youtube_.auth("danilkhorosun@gmail.com", "555gta555")
    youtube_.upload_video(r"C:\Users\Admin\Downloads\ssstik.io_1660218161909.mp4", 'lol', '#kek')

    # ToDo: отдельный файл для получения логина и пароля


if __name__ == '__main__':
    main()
