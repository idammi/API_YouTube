
from selenium_driver import BaseClass
from youtube_api import YouTube


def main():

    base = BaseClass()
    DRIVER = base.driver()

    youtube_ = YouTube(DRIVER)
    youtube_.auth("e56333180@gmail.com", "Jesus8800")
    # youtube_.auth("danilkhorosun@gmail.com", "555gta555")
    # youtube_.auth("e48320035@gmail.com", "Jesus8800")
    youtube_.upload_video(r"C:\Users\Username\Downloads\download.mp4", 'Name video is None', '#rap #mine_first_video')

    # ToDo: отдельный файл для получения логина и

    DRIVER.close()
    DRIVER.quit()

if __name__ == '__main__':
    main()
