from element import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class MainPageLocators:
    """Класс MainPageLocators содержит локаторы страницы yandex.ru

        Аттрибуты:
        LOCATOR_SEARCH_FIELD (selenium.webdriver.common.by.By.ID, str): локатор поля поиска;
        LOCATOR_SUGGEST = (selenium.webdriver.common.by.By.CLASS_NAME, str): локатор подсказки поиска;
        LOCATOR_IMAGES = (selenium.webdriver.common.by.By.XPATH, str): локатор ссылки на страницу "Картинки".
    """
    LOCATOR_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_SUGGEST = (By.CLASS_NAME, "mini-suggest__popup-content")
    LOCATOR_IMAGES = (By.XPATH, "//a[@data-id='images']")


class SearchPageLocators:
    """Класс SearchPageLocators содержит локаторы страницы yandex.ru/search

        Аттрибуты:
        LOCATOR_SEARCH_HREF (selenium.webdriver.common.by.By.XPATH, str): локатор ссылок результатов поиска;
        LOCATOR_SEARCH_TABLE = (selenium.webdriver.common.by.By.XPATH, str): локатор результатов поиска.
    """
    LOCATOR_SEARCH_HREF = (By.XPATH, "//*[@id='search-result']/li/div/div/div/a")
    LOCATOR_SEARCH_TABLE = (By.XPATH, "//*[@id='search-result']")


class ImagesPageLocators:
    """Класс ImagesPageLocators содержит локаторы страницы yandex.ru/search

        Аттрибуты:
        LOCATOR_FIRST_CAT_TEXT (selenium.webdriver.common.by.By.XPATH, str): локатор названия категории 1;
        LOCATOR_SEARCH_TEXT = (selenium.webdriver.common.by.By.XPATH, str): локатор поля поиска;
        LOCATOR_FIRST_PICTURE = (selenium.webdriver.common.by.By.XPATH, str): локатор первой картинки поиска;
        LOCATOR_IMAGE_HREF = (selenium.webdriver.common.by.By.XPATH, str): локатор ссылки на открытую картинку;
        LOCATOR_THUMB_IMAGE = (selenium.webdriver.common.by.By.XPATH, str): локатор ссылки на превью картинки;
        LOCATOR_THUMB_IMAGE_OPENED = (selenium.webdriver.common.by.By.XPATH, str): локатор ссылки на превью открытой
                                                                                    картинки;
        LOCATOR_NEXT_IMAGE = (selenium.webdriver.common.by.By.XPATH, str): локатор кнопки "Вперед";
        LOCATOR_PREV_IMAGE = (selenium.webdriver.common.by.By.XPATH, str): локатор кнопки "Назад".
    """
    LOCATOR_FIRST_CAT_TEXT = (By.XPATH, "//div[@class='PopularRequestList']/div[1]/a/"
                                        "div[@class='PopularRequestList-SearchText']")
    LOCATOR_SEARCH_TEXT = (By.XPATH, "//input[@name='text']")
    LOCATOR_FIRST_PICTURE = (By.XPATH, "//div[@class='serp-controller__content']/div/div[1]/div")
    LOCATOR_IMAGE_HREF = (By.XPATH, "//img[@class='MMImage-Preview']")
    LOCATOR_THUMB_IMAGE = (By.XPATH, "//div[@class='serp-controller__content']/div/div[1]/div/a/img")
    LOCATOR_THUMB_IMAGE_OPENED = (By.XPATH, "//div[@class='MMGallery-Item MMGallery-Item_selected']/div/div/div")
    LOCATOR_NEXT_IMAGE = (By.XPATH, "//div[contains(@class, 'ButtonNext')]")
    LOCATOR_PREV_IMAGE = (By.XPATH, "//div[contains(@class, 'ButtonPrev')]")


class MainPage(BasePage):
    """Класс MainPage реализует функционал для работы с веб-страницей yandex.ru
    """
    def enter_word(self, word: str):
        """Метод отправляет "word" в поле поиска, возвращает ссылку на поле поиска
            Аттрибуты:
               word(str): строка для поиска.
        """
        search_field = self.find_element(MainPageLocators.LOCATOR_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def suggest_check(self):
        """Метод возвращает ссылку на таблицу с подсказками поиска
        """
        suggest = self.find_element(MainPageLocators.LOCATOR_SUGGEST)
        return suggest

    def start_search(self, search_field_element):
        """Метод отправляет "Enter" в поле поиска
        """
        search_field_element.click()
        return search_field_element.send_keys(Keys.RETURN)

    def open_images(self):
        """Метод открывает вкладку "Картинки" и переключает браузер на нее
        """
        windows_before = self.driver.window_handles
        self.find_element(MainPageLocators.LOCATOR_IMAGES).click()
        windows_after = self.driver.window_handles
        for window_handle in windows_after:
            if window_handle not in windows_before:
                self.driver.switch_to.window(window_handle)
                break
        return windows_after


class ImagesPage(BasePage):
    """Класс MainPage реализует функционал для работы с веб-страницей yandex.ru/search
    """

    def go_to_first_category(self):
        """Метод открывает картинки категории 1, возвращает строку с ее названием
        """
        first_category = self.find_element(ImagesPageLocators.LOCATOR_FIRST_CAT_TEXT)
        first_category_text = first_category.text
        first_category.click()
        return first_category_text

    def get_search_text(self):
        """Метод возвращает строку с текстом в поле поиска
        """
        search_text = self.find_element(ImagesPageLocators.LOCATOR_SEARCH_TEXT).get_attribute("value")
        return search_text

    def open_first_picture(self):
        """Метод открывает первую картинку, возвращает строку с ссылкой на превью картинки
        """
        first_pic = self.find_element(ImagesPageLocators.LOCATOR_FIRST_PICTURE)
        first_pic.click()
        first_pic_href = self.find_element(ImagesPageLocators.LOCATOR_THUMB_IMAGE)
        return str(first_pic_href.get_attribute("src"))

    def get_image_preview_href(self):
        """Метод возвращает строку с ссылкой на превью открытой картинки
        """
        image_preview = self.find_element(ImagesPageLocators.LOCATOR_THUMB_IMAGE_OPENED)
        background_image = image_preview.get_attribute("style")
        return background_image[background_image.find("\"") + 1: -3]

    def next_picture(self):
        """Метод нажимает на кнопку "Вперед" для переключения картинки
        """
        next_picture = self.find_element(ImagesPageLocators.LOCATOR_NEXT_IMAGE)
        return next_picture.click()

    def prev_picture(self):
        """Метод нажимает на кнопку "Назад" для переключения картинки
        """
        prev_picture = self.find_element(ImagesPageLocators.LOCATOR_PREV_IMAGE)
        return prev_picture.click()

    def get_pic_src(self):
        """Метод возвращает источник картинки
        """
        pic_src = self.find_element(ImagesPageLocators.LOCATOR_IMAGE_HREF)
        return pic_src.get_attribute("src")


class SearchPage(BasePage):
    """Класс MainPage реализует функционал для работы с веб-страницей yandex.ru/images
    """
    def check_search_results(self):
        """Метод возвращает список ссылок результатов поиска
        """
        results_list = self.find_elements(SearchPageLocators.LOCATOR_SEARCH_HREF)
        search_href_list = [x.get_attribute("href") for x in results_list]
        return search_href_list

    def check_search_table(self):
        """Метод возвращает таблицу с результатами поиска
        """
        results_table = self.find_element(SearchPageLocators.LOCATOR_SEARCH_TABLE)
        return results_table
