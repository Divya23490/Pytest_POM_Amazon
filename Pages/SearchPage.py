from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData
import time

class SearchPage(BasePage):
    SEARCH_BUTTON = (By.XPATH, "//input[@id='twotabsearchtextbox']")
    RESULT_SEARCH = (By.XPATH, "//span[contains(text(),'Classic-fit Soft-Touch Long-Sleeve Crewnec')]")
    SELECT_SIZE   = (By.XPATH,"//span[@id='dropdown_selected_size_name']//span[@class='a-button-text a-declarative']")
    SELECTED_SIZE_VALUE=(By.XPATH,"(//a[normalize-space()='Medium'])[1]")
    SELECTED_PRODUCT_COLOR=(By.XPATH,"//img[@alt='Dark Red']")
    ADD_TO_CART_BUTTON = (By.XPATH, "//input[@id='add-to-cart-button']")
    CART_BUTTON=(By.XPATH,"//span[normalize-space()='Cart']")
    SHOPPINGCART_SELECTEDPRODUCT=(By.XPATH,"//span[@class='a-truncate-cut']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def do_search(self, searchvalue):
        self.do_send_keys(self.SEARCH_BUTTON, searchvalue)
        self.do_send_keys_enter(self.SEARCH_BUTTON)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.do_click(self.RESULT_SEARCH)
        self.is_visible(self.SELECT_SIZE)
        self.do_click(self.SELECT_SIZE)
        self.do_click(self.SELECTED_SIZE_VALUE)
        self.is_visible(self.SELECTED_PRODUCT_COLOR)
        self.do_click(self.SELECTED_PRODUCT_COLOR)
        time.sleep(5)
        self.is_enabled(self.ADD_TO_CART_BUTTON)
        self.do_click(self.ADD_TO_CART_BUTTON)
        time.sleep(10)
        self.do_click(self.CART_BUTTON)

    def addedproduct_text(self):
        return self.get_element_text(self.SHOPPINGCART_SELECTEDPRODUCT)








