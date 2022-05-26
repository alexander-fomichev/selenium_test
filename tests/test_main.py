import pytest
import pages


def test_yandex_search(browser, yandex_start_page):
    """ Тестовая функция реализует проверку сценария поиска в Яндексе"""
    # 1) на yandex.ru проверяем наличие поля запроса и вводим в него слово:
    search_field_element = yandex_start_page.enter_word("selenium")
    # 2) проверяем что появилась таблица с подсказками
    yandex_start_page.suggest_check()
    # 3) нажимаем "Enter" для старта поиска
    yandex_start_page.start_search(search_field_element)
    search_results_page = pages.SearchPage(browser)
    # 4) проверяем наличие таблицы результатов поиска
    assert search_results_page.check_search_table()
    # 5) проверяем наличие нужной ссылки в первых пяти результатах поиска
    search_results = search_results_page.check_search_results()
    assert any(["selenium.dev" in href for href in search_results[:5]])


def test_yandex_pictures(browser, yandex_start_page):
    """ Тестовая функция реализует проверку сценария поиска картинок в Яндексе"""
    # 1) на yandex.ru проверяем наличие ссылки "Картинки" и кликаем на нее:
    yandex_start_page.open_images()
    images_page = pages.ImagesPage(browser)
    # 2) на yandex.ru проверяем наличие ссылки "Картинки" и кликаем на нее:
    assert images_page.check_title("Картинки")
    # 3) проверяем что перешли на нужный url:
    assert "https://yandex.ru/images/" in images_page.get_url()
    # 4) открываем первую категорию картинок:
    first_cat_text = images_page.go_to_first_category()
    # 5) проверяем что открылась нужная категория:
    assert images_page.check_title(first_cat_text)
    # 6) проверяем что в поле поиска верный текст:
    assert images_page.get_search_text() == first_cat_text
    # 7) открываем первую картинку:
    first_picture_thumb = images_page.open_first_picture()
    # 8) проверяем что открылась нужная картинка:
    first_picture_thumb_opened = images_page.get_image_preview_href()
    assert first_picture_thumb_opened in first_picture_thumb
    first_picture = images_page.get_pic_src()
    # 9) нажимаем на кнопку "Вперед":
    images_page.next_picture()
    # 10) проверяем что картинка изменилась:
    second_picture = images_page.get_pic_src()
    assert first_picture != second_picture
    # 11) нажимаем на кнопку "Назад":
    images_page.prev_picture()
    # 12) проверяем что вернулись к первой картинке:
    first_picture_again = images_page.get_pic_src()
    assert first_picture == first_picture_again


@pytest.fixture(scope="function")
def yandex_start_page(browser):
    """ Фикстура yandex_start_page реализует открытие главной страницы Яндекса"""
    yandex_main_page = pages.MainPage(browser)
    yandex_main_page.go_default_url()
    return yandex_main_page
