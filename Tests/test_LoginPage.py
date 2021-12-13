import pytest
from Pages.SearchPage import SearchPage
from Pages.BasePage import BasePage
from Tests.test_base import BaseTest
from Config.config import TestData

class Test_Login(BaseTest):

    def test_login_page_title(self):
        self.SearchPage=SearchPage(self.driver)
        title=self.SearchPage.get_login_page_title(TestData.LOGIN_PAGE_TITLE)
        assert title==TestData.LOGIN_PAGE_TITLE

    def test_search(self):
        self.SearchPage=SearchPage(self.driver)
        self.SearchPage.do_search(TestData.SEARCH_VALUE)
        shoppingcart_product=self.SearchPage.addedproduct_text()
        assert TestData.EXPECTED_PRODUCT_VALUE in shoppingcart_product, "Text not found %s" % TestData.EXPECTED_PRODUCT_VALUE


