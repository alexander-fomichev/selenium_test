from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Класс BasePage реализует основной функционал Selenium для работы с веб-страницей

        Аттрибуты:
        driver: драйвер selenium.webdriver;
        default_url(str): адрес веб-страницы по умолчанию.
    """
    def __init__(self, driver, default_url: str = "https://yandex.ru/"):
        """
            driver: драйвер selenium.webdriver;
            default_url(str): адрес веб-страницы по умолчанию.
        """
        self.driver = driver
        self.default_url = default_url

    def find_element(self, locator, time=10):
        """Метод возвращает элемент с заданным локатором,в случае неудачи возвращет сообщение об ошибке

               Аттрибуты:
               locator(selenium.webdriver.common.by.By, str): драйвер selenium.webdriver;
               time(int): таймаут, по умолчанию 10.
           """
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        """Метод возвращает список элементов с заданным локатором,в случае неудачи возвращет сообщение об ошибке

               Аттрибуты:
               locator(selenium.webdriver.common.by.By, str): драйвер selenium.webdriver;
               time(int): таймаут, по умолчанию 10.
           """
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_default_url(self):
        """Метод реализует переход на страницу по умолчанию
        """
        return self.driver.get(self.default_url)

    def check_title(self, title: str, time=10):
        """Метод проверяет содержится ли строка в заголовке веб-страницы, в случае неудачи возвращет сообщение об ошибке

               Аттрибуты:
               title(str): строка для проверки;
               time(int): таймаут, по умолчанию 10.
        """
        return WebDriverWait(self.driver, time).until(EC.title_contains(title),
                                                      message=f"Can't find title {title}")

    def get_url(self):
        """Метод возвращает текущий url
        """
        current_url = self.driver.current_url
        return current_url
