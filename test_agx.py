from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
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
    time.sleep(5)


def testMarketBuy(orderType = "market", stock = "UKOIL", volume = "100", StopLossPoint = "50", TakeProfitPoint = "50"):
    driver.get("https://aqxtrader.aquariux.com/web ")
    time.sleep(3)
    # Search Stock
    elemSearch = driver.find_element(By.XPATH, '//input[@placeholder="Search symbol/name"]')
    elemSearch.send_keys(stock)
    time.sleep(3)
    elemSearchFirst = driver.find_element(By.XPATH, f'//div[@data-testid="symbol-input-search-items"]//div//div[contains(text(),{stock})]')
    elemSearchFirst.click()
    time.sleep(1)

    # orderType
    elemOrderTypeMain = driver.find_element(By.XPATH, '//div[@data-testid="trade-dropdown-order-type"]//div[1]//div[2]')
    elemOrderTypeMain.click()
    time.sleep(1)
    elemOrderType = driver.find_element(By.XPATH, f'//div[@data-testid="trade-dropdown-order-type-{orderType}"]')
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


def testOrderValidation():
    # Notification tab
    elemNotificationTab = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/div[6]/div')
    elemNotificationTab.click()
    time.sleep(1)

    #Get All Order Text
    elemFirstOrder = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/div[6]/div[2]/div/div[3]/div[1]/div[1]/div')
    orderInfo_raw = elemFirstOrder.text
    print(orderInfo_raw)

    #Get Order#
    noti_order_number = orderInfo_raw.split("#")[1].split(",")[0]
    print(noti_order_number)

    #Get Volume
    noti_volume = orderInfo_raw.split("Size ")[1].split(" /")[0]
    print(noti_volume)

    # Get Unit
    noti_units = orderInfo_raw.split("Units ")[1].split(" @")[0]
    print(noti_units)

    #Get OrderStatus
    noti_orderStatus = orderInfo_raw.split("n ")[1].split(":")[0]
    print(noti_orderStatus)

    #Close Notification Tab
    elemNotificationTab.click()
    time.sleep(1)

    #Position Table
    #Asset Tab
    driver.get("https://aqxtrader.aquariux.com/web/assets ")
    time.sleep(3)

    #PositionHistory Tab
    elemPositionHistoryTab = driver.find_element(By.CSS_SELECTOR, 'div[data-testid="tab-asset-order-type-history"]')
    elemPositionHistoryTab.click()
    time.sleep(1)

    #Table History Position Get All Data
    table = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div/table')
    rows = table.find_elements(By.TAG_NAME, "tr")
    # for row in rows:
    #     cells = row.find_elements(By.TAG_NAME, "th")
    #     for cell in cells:
    #         cell_value = cell.text
    #         print(cell_value)

    # #Get Table OrderNumber 1st row
    table_orderNumber = rows[1].find_elements(By.TAG_NAME, "th")[1].text
    print(table_orderNumber)

    # Det Table Volume for 1st row
    table_volume = rows[1].find_elements(By.TAG_NAME, "td")[4].text
    print(table_volume)

    # Det Table Unit for 1st row
    table_units = rows[1].find_elements(By.TAG_NAME, "td")[5].text
    print(table_units)

    # Validate 1st order in Notification vs History Position
    assert noti_order_number == table_orderNumber
    assert noti_volume == table_volume
    assert noti_units == table_units


















