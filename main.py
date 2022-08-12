
from selenium_driver import BaseClass
from youtube import YouTube


def main():

    base = BaseClass()
    DRIVER = base.driver()

    youtube_ = YouTube(DRIVER, "danilkhorosun@gmail.com", "555gta555")
    youtube_.auth()

    # ToDo: отдельный файл для получения логина и пароля


if __name__ == '__main__':
    main()
