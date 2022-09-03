
from selenium_driver import BaseClass
from youtube_api import YouTube


def main():

    base = BaseClass()
    DRIVER = base.driver()

    youtube_ = YouTube(DRIVER)
    youtube_.auth("your_account@gmail.com", "Your password")
    youtube_.upload_video(r"C:\Users\Username\Downloads\upload.mp4", 'Name video', '#mine_first_video #hastags_for_the_video')

    DRIVER.close()
    DRIVER.quit()

if __name__ == '__main__':
    main()
