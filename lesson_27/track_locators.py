from selenium.webdriver.common.by import By

class TrackingCssLocators:
    track_post_field = (By.CSS_SELECTOR, '.track__form-group-input')
    search_button = (By.CSS_SELECTOR, '#np-number-input-desktop-btn-search-en')

class TrackingXpathLocators:
    frame_btn = (By.XPATH, '//div[@id="chat"]//div[@class="first-visit-helper-wrapper d-flex flex-column tracking-desktop"]//button')
    status_text = (By.XPATH, '//div[@class="header__status-text"]')
    error_msg = (By.XPATH, '//div[@id="np-number-input-desktop-message-error-message"]')
