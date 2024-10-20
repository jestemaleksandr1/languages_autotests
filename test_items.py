import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

class TestProductPage:
    
    def test_button_add_to_basket_is_visible(self, browser):
        browser.get(link)
        
        time.sleep(30)
        
        add_to_cart_button = browser.find_element("css selector", ".btn-add-to-basket")
        
        assert add_to_cart_button.is_displayed(), "Кнопка добавления в корзину не найдена"

