import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By


def test_presence_of_the_button_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    checkbutton = browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    assert checkbutton is not None, "Element is not found"

