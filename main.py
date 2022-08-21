
from selenium_driver import BaseClass
from youtube_api import YouTube


def main():

    base = BaseClass()
    DRIVER = base.driver()

    youtube_ = YouTube(DRIVER)
    youtube_.auth("danilkhorosun@gmail.com", "555gta555")
    youtube_.upload_video(r"C:\Users\Username\Downloads\download.mp4", 'lol_name', '#kek #my_video')

    # ToDo: отдельный файл для получения логина и пароля


if __name__ == '__main__':
    main()
