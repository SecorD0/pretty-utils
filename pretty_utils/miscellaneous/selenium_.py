from typing import Optional

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Sel:
    def get_element(self, browser: webdriver, find_it: str, sec: int = 10, by: str = By.XPATH) -> Optional[WebElement]:
        """
        Explicit waits of an element appearing.

        :param browser: a Selenium webdriver
        :param find_it: a string to search for the element
        :param sec: the element waiting time (10)
        :param by: find the element by ... (XPATH)
        :return: the founded element
        """
        return WebDriverWait(browser, sec).until(EC.presence_of_element_located((by, find_it)))

    def get_text(self, browser: webdriver, find_it: str, sec: int = 10, by: str = By.XPATH) -> Optional[str]:
        """
        Explicit waits of an element appearing and get its text.

        :param browser: a Selenium webdriver
        :param find_it: a string to search for the element
        :param sec: the element waiting time (10)
        :param by: find the element by ... (XPATH)
        :return: the parsed text
        """
        try:
            return self.get_element(browser, find_it, sec, by).text
        except:
            pass

    def clear(self, browser: webdriver, find_it: str, sec: int = 10, by: str = By.XPATH) -> Optional[WebElement]:
        """
        Explicit waits of an element appearing and clear its contents.

        :param browser: a Selenium webdriver
        :param find_it: a string to search for the element
        :param sec: the element waiting time (10)
        :param by: find the element by ... (XPATH)
        :return: the founded element
        """
        element = self.get_element(browser, find_it, sec, by)
        element.clear()
        return element

    def write(self, browser, find_it, text, sec: int = 10, by: str = By.XPATH, clear: bool = True) -> Optional[
        WebElement]:
        """
        Explicit waits of an element appearing and write a text to it.

        :param browser: a Selenium webdriver
        :param find_it: a string to search for the element
        :param text: a text to write
        :param sec: the element waiting time (10)
        :param by: find the element by ... (XPATH)
        :param clear: clear the element before writing (True)
        :return: the founded element
        """
        element = self.get_element(browser, find_it, sec, by)
        if clear:
            element.clear()
        element.send_keys(text)
        return element

    def click(self, browser: webdriver, find_it: str, sec: int = 10, by: str = By.XPATH) -> Optional[WebElement]:
        """
        Explicit waits of an element appearing and click it.

        :param browser: a Selenium webdriver
        :param find_it: a string to search for the element
        :param sec: the element waiting time (10)
        :param by: find the element by ... (XPATH)
        :return: the founded element
        """
        element = self.get_element(browser, find_it, sec, by)
        element.click()
        return element

    def click_js(self, browser: webdriver, find_it: str, sec: int = 10, by: str = By.XPATH) -> Optional[WebElement]:
        """
        Explicit waits of an element appearing and click it using JS script (use it if simple click has no effect).

        :param browser: a Selenium webdriver
        :param find_it: a string to search for the element
        :param sec: the element waiting time (10)
        :param by: find the element by ... (XPATH)
        :return: the founded element
        """
        element = webdriver.support.ui.WebDriverWait(browser, sec).until(EC.element_to_be_clickable((by, find_it)))
        browser.execute_script("arguments[0].click();", element)
        return element

    def click_when_clicable(self, browser: webdriver, find_it: str, sec: int = 10, by: str = By.XPATH) -> Optional[
        WebElement]:
        """
        Explicit waits of an element appearing and click it when clickable.

        :param browser: a Selenium webdriver
        :param find_it: a string to search for the element
        :param sec: the element waiting time (10)
        :param by: find the element by ... (XPATH)
        :return: the founded element
        """
        element = WebDriverWait(browser, sec).until(EC.element_to_be_clickable((by, find_it)))
        element.click()
        return element

    def click_with_coord(self, browser: webdriver, find_it: str or WebElement, sec: int = 10, by: str = By.XPATH,
                         x_off: int = 1, y_off: int = 1) -> Optional[WebElement]:
        """
        Explicit waits of an element appearing and click it via coordinates.

        :param browser: a Selenium webdriver
        :param find_it: a string or WebElement to interact
        :param sec: the element waiting time (10)
        :param by: find the element by ... (XPATH)
        :param x_off: x coordinate (1)
        :param y_off: y coordinate (1)
        :return: the founded element
        """
        if isinstance(find_it, str):
            element = self.get_element(browser, find_it, sec, by)
        else:
            element = find_it

        ActionChains(browser).move_to_element(element).move_by_offset(x_off, y_off).click().perform()
        return element


sel = Sel()
