from typing import Optional, Union

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Sel:
    """
    It's a class that simplifies working with the Selenium library.
    """

    def __init__(self, browser: webdriver):
        """
        Initializes a class.

        :param webdriver browser: instance of WebDriver (Ie, Firefox, Chrome or Remote)
        """
        self.browser = browser

    def get_element(self, find_it: str, sec: int = 10, by: str = By.XPATH) -> Optional[WebElement]:
        """
        Explicit waits of an element appearing.

        :param str find_it: a string to search for the element
        :param int sec: the element waiting time (10)
        :param str by: find the element by ... (XPATH)
        :return WebElement: the founded element
        """
        return WebDriverWait(self.browser, sec).until(EC.presence_of_element_located((by, find_it)))

    def get_text(self, find_it: str, sec: int = 10, by: str = By.XPATH) -> Optional[str]:
        """
        Explicit waits of an element appearing and get its text.

        :param str find_it: a string to search for the element
        :param int sec: the element waiting time (10)
        :param str by: find the element by ... (XPATH)
        :return str: the parsed text
        """
        try:
            return self.get_element(find_it, sec, by).text

        except:
            pass

    def wait_for_clickability(self, find_it: str, sec: int = 10, by: str = By.XPATH) -> Optional[WebElement]:
        """
        Waiting for an element to become clickable.

        :param str find_it: a string to search for the element
        :param int sec: the element waiting time (10)
        :param str by: find the element by ... (XPATH)
        :return WebElement: the founded element
        """
        return WebDriverWait(self.browser, sec).until(EC.element_to_be_clickable((by, find_it)))

    def wait_for_visibility(self, find_it: str, sec: int = 10, by: str = By.XPATH) -> Optional[WebElement]:
        """
        Waiting for an element to become visible.

        :param str find_it: a string to search for the element
        :param int sec: the element waiting time (10)
        :param str by: find the element by ... (XPATH)
        :return WebElement: the founded element
        """
        return WebDriverWait(self.browser, sec).until(EC.visibility_of_element_located((by, find_it)))

    def clear(self, find_it: str, sec: int = 10, by: str = By.XPATH) -> Optional[WebElement]:
        """
        Explicit waits of an element appearing and clear its contents.

        :param str find_it: a string to search for the element
        :param int sec: the element waiting time (10)
        :param str by: find the element by ... (XPATH)
        :return WebElement: the founded element
        """
        element = self.get_element(find_it, sec, by)
        element.clear()
        return element

    def write(self, find_it: str, text: str, sec: int = 10, by: str = By.XPATH, clear: bool = True) -> Optional[
        WebElement]:
        """
        Explicit waits of an element appearing and write a text to it.

        :param str find_it: a string to search for the element
        :param str text: a text to write
        :param int sec: the element waiting time (10)
        :param str by: find the element by ... (XPATH)
        :param bool clear: clear the element before writing (True)
        :return WebElement: the founded element
        """
        element = self.get_element(find_it, sec, by)
        if clear:
            element.clear()

        element.send_keys(text)
        return element

    def click(self, find_it: str, sec: int = 10, by: str = By.XPATH) -> Optional[WebElement]:
        """
        Explicit waits of an element appearing and click it.

        :param str find_it: a string to search for the element
        :param int sec: the element waiting time (10)
        :param str by: find the element by ... (XPATH)
        :return WebElement: the founded element
        """
        element = self.get_element(find_it, sec, by)
        element.click()
        return element

    def click_js(self, find_it: str, sec: int = 10, by: str = By.XPATH) -> Optional[WebElement]:
        """
        Explicit waits of an element appearing and click it using JS script. Use it if simple click has no effect.

        :param str find_it: a string to search for the element
        :param int sec: the element waiting time (10)
        :param str by: find the element by ... (XPATH)
        :return WebElement: the founded element
        """
        element = self.wait_for_clickability(find_it, sec, by)
        self.browser.execute_script('arguments[0].click();', element)
        return element

    def click_when_clicable(self, find_it: str, sec: int = 10, by: str = By.XPATH) -> Optional[WebElement]:
        """
        Explicit waits of an element appearing and click it when clickable.

        :param str find_it: a string to search for the element
        :param int sec: the element waiting time (10)
        :param str by: find the element by ... (XPATH)
        :return WebElement: the founded element
        """
        element = self.wait_for_clickability(find_it, sec, by)
        element.click()
        return element

    def click_with_coord(self, find_it: Union[str, WebElement], sec: int = 10, by: str = By.XPATH, x_off: int = 1,
                         y_off: int = 1) -> Optional[WebElement]:
        """
        Explicit waits of an element appearing and click it via coordinates.

        :param str find_it: a string or WebElement to interact
        :param int sec: the element waiting time (10)
        :param str by: find the element by ... (XPATH)
        :param int x_off: x coordinate (1)
        :param int y_off: y coordinate (1)
        :return WebElement: the founded element
        """
        if isinstance(find_it, str):
            element = self.get_element(find_it, sec, by)

        else:
            element = find_it

        ActionChains(self.browser).move_to_element(element).move_by_offset(x_off, y_off).click().perform()
        return element
