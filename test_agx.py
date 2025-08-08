from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)



def testAqxSite():
    driver.maximize_window()
    driver.get("https://aqxtrader.aquariux.com ")
    time.sleep(1)
    elemAcctID = driver.find_element(By.XPATH, '//input[@data-testid="login-user-id"]')
    elemAcctID.send_keys("999041")
    elemPw = driver.find_element(By.XPATH, '//input[@type="password"]')
    elemPw.send_keys("Ygq9!EK!fF87")
    loginSubmitBtn = driver.find_element(By.CSS_SELECTOR, 'button[type = "submit"]')
    loginSubmitBtn.click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.title_contains("Aquariux"))
    assert "Aquariux " in driver.title
    time.sleep(1)


def testMarketBuy(orderType = "market", stock = "UKOIL", volume = "100", StopLossPoint = "50", TakeProfitPoint = "50"):
    driver.get("https://aqxtrader.aquariux.com/web ")
    time.sleep(3)
    # Search Stock
    elemSearch = driver.find_element(By.XPATH, '//input[@placeholder="Search symbol/name"]')
    elemSearch.send_keys(stock)
    time.sleep(3)
    elemSearchFirst = driver.find_element(By.XPATH, f'//div[@data-testid="symbol-input-search-items"]//div//div[contains(text(),{stock})]')
    # elemSearchFirst = driver.find_element(By.XPATH, '//div[@data-testid="symbol-input-search-items"]//div//div[contains(text(),"UKOIL")]')
    elemSearchFirst.click()
    time.sleep(1)

    # orderType
    elemOrderTypeMain = driver.find_element(By.XPATH, '//div[@data-testid="trade-dropdown-order-type"]//div[1]//div[2]')
    elemOrderTypeMain.click()
    time.sleep(1)
    elemOrderType = driver.find_element(By.XPATH, f'//div[@data-testid="trade-dropdown-order-type-{orderType}"]')
    # elemOrderType = driver.find_element(By.XPATH, '//div[@data-testid="trade-dropdown-order-type-market"]')
    elemOrderType.click()

    # Volume Input
    elemVolume = driver.find_element(By.XPATH, '//input[@placeholder="Min: 0.1"]')
    elemVolume.clear()
    elemVolume.send_keys(volume)

    # Stop Loss
    elemStopLoss = driver.find_element(By.XPATH, '//input[@data-testid="trade-input-stoploss-points"]')
    elemStopLoss.send_keys(StopLossPoint)
    time.sleep(1)

    # Take Profit
    elemTakeProfit = driver.find_element(By.XPATH, '//input[@data-testid="trade-input-takeprofit-points"]')
    elemTakeProfit.send_keys(TakeProfitPoint)
    time.sleep(1)

    # Submit Order
    elemSubmitOrder = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="trade-button-order"]')
    elemSubmitOrder.click()
    time.sleep(1)

    # Confirm Order
    elemSubmitOrder = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="trade-confirmation-button-confirm"]')
    elemSubmitOrder.click()
    time.sleep(1)







