from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as WDWait


class BasePage:
    def __init__(self, web_drv):
        self.web_drv = web_drv

    @property
    def current_url(self):
        return self.web_drv.current_url

    @property
    def new_window_url(self, timeout=10):
        wait = WDWait(self.web_drv, timeout)
        wait.until(ec.number_of_windows_to_be(2))
        for window_handle in self.web_drv.window_handles:
            if window_handle != self.web_drv.current_window_handle:
                self.web_drv.switch_to.window(window_handle)
                break
            wait.until(ec.title_is("Дзен"))
        return self.web_drv.current_url

    def get_element_text(self, locator, timeout=10):
        return WDWait(self.web_drv, timeout).until(ec.visibility_of_element_located(locator)).text

    def open_page(self, url):
        self.web_drv.get(url)

    def click_by_element(self, locator, timeout=10):
        WDWait(self.web_drv, timeout).until(ec.element_to_be_clickable(locator)).click()

    def scroll_to_element(self, locator, timeout=10):
        target_element = WDWait(self.web_drv, timeout).until(ec.visibility_of_element_located(locator))
        self.web_drv.execute_script("arguments[0].scrollIntoView();", target_element)
