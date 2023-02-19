from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
import time


#@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_e2e(self):

        self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        cards = self.driver.find_elements(By.CSS_SELECTOR, ".card-title a")
        for i, card in enumerate(cards, start=-1):
            if card.text == "Blackberry":
                self.driver.find_elements(By.CSS_SELECTOR, ".card-footer button")[i].click()
