import unittest
from selenium import webdriver

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)


def download_pdf(lnk):

    from selenium import webdriver
    from time import sleep

    options = webdriver.ChromeOptions()

    download_folder = "/Users/ruiliu/Desktop/"

    profile = {"plugins.plugins_list": [{"enabled": False,
                                         "name": "Chrome PDF Viewer"}],
               "download.default_directory": download_folder,
               "download.extensions_to_open": ""}

    options.add_experimental_option("prefs", profile)

    print("Downloading file from link: {}".format(lnk))

    driver = webdriver.Chrome(chrome_options = options)
    driver.get(lnk)

    filename = lnk.split("/")[4].split(".cfm")[0]
    print("File: {}".format(filename))

    print("Status: Download Complete.")
    print("Folder: {}".format(download_folder))

    driver.close()

download_pdf("https://www.linkedin.com/in/rui-liu-rachel/")