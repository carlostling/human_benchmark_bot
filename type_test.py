
import geckodriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



def start():
    geckodriver_autoinstaller.install()
    driver = webdriver.Firefox()
    driver.get("https://humanbenchmark.com/tests/typing")

    text_box = driver.find_element_by_class_name("letters")
    letters = text_box.find_elements_by_tag_name("span")

    for letter in letters:
        if letter.text == "":
            text_box.send_keys(Keys.SPACE)
        else:
            text_box.send_keys(letter.text)
