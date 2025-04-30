import logging
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)


def create_driver() -> webdriver.Chrome:
    options = Options()
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-blink-features=AutomationControlled")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    return driver


def test_purchase_flow():
    driver = create_driver()
    wait = WebDriverWait(driver, 15)

    try:
        driver.get("https://www.saucedemo.com/")
        logger.info("Открываем saucedemo.com и логинимся")
        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
        wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

        logger.info("Добавляем Sauce Labs Backpack в корзину")
        wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-backpack']")
            )
        ).click()

        logger.info("Переходим в корзину")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.shopping_cart_link"))).click()

        logger.info("Начинаем оформление заказа")
        wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

        logger.info("Заполняем информацию о покупателе")
        wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Test")
        wait.until(EC.visibility_of_element_located((By.ID, "last-name"))).send_keys("User")
        wait.until(EC.visibility_of_element_located((By.ID, "postal-code"))).send_keys("12345")
        wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()

        logger.info("Завершаем покупку")
        wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

        logger.info("Проверяем, что покупка завершена успешно")
        completion = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h2.complete-header"))
        ).text
        assert completion == "Thank you for your order!", \
            f"Ожидали сообщение об успешном заказе, получили: {completion}"
        logger.info("E2E тест прошёл успешно")

    except Exception as e:
        logger.error("Ошибка во время выполнения теста: %s", e)
        raise

    finally:
        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    test_purchase_flow()