import selenium_driver

base = selenium_driver.BaseClass()
DRIVER = base.driver()

DRIVER.get('https://accounts.google.com/signin/chrome/sync/identifier?ssp=1&continue=https%3A%2F%2Fwww.google.com%2F&flowName=GlifDesktopChromeSync')

DRIVER.close()
DRIVER.quite()