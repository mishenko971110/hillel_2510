from track_locators import TrackingCssLocators, TrackingXpathLocators
from base_page import BasePage

class TrackingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def track_package(self, post_id):
        self.enter_text(TrackingCssLocators.track_post_field, post_id)
        self.click_element(TrackingCssLocators.search_button)

    def get_tracking_status(self):
        """Отримує статус посилки або помилку."""
        try:
            # якщо відпрацює валідація
            self.get_text(TrackingXpathLocators.error_msg)
            return 'Ми не знайшли посилку за таким номером.'
        except:
            # якщо дана посилка існує
            self.click_element(TrackingXpathLocators.frame_btn)
            return self.get_text(TrackingXpathLocators.status_text)
