from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

'''
Justin Victoria
Dan Huang
Neural Magic - JupyterLab Selenium
'''


def testJupyter():
    driver = webdriver.Chrome()
    driver.maximize_window()
    print("Navigating to the jupyter notebook")
    driver.get("https://jupyter.org/try")

    try:
        print("Clicking \"Try JupyterLab\" link")
        JupyterLab = driver.find_element_by_css_selector('a.try-link:nth-child(2) div.card-heading')
        JupyterLab.click()
        JupyterLabReference = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.jp-Activity:nth-child(6) div.fvaq30"))
        )
        ActionChains(driver).pause(1).click(JupyterLabReference).perform()
        print("Navigating to and clicking on 'File'")
        File = driver.find_element_by_css_selector('#jp-MainMenu li:first-child')
        File.click()
        New = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "li.lm-Menu-item.p-Menu-item:nth-child(2)"))
        )
        print("New was found")
        print("Moving mouse to 'New' submenu and clicking 'Notepad'")
        ActionChains(driver).move_to_element_with_offset(New, 20, 0).pause(1).move_by_offset(350, 30).click().perform()
        print("Clicking 'Select' with 'Python 3' selected in the drop down")
        Select = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div:nth-child(11) div:nth-child(3) button:nth-child(2)"))
        )
        Select.click()
        print("Selecting text area and writing Python code")
        InputArea = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[class$=editMode] textarea"))
        )
        InputArea.send_keys('print("Hello World")')
        print("Running python code")
        Run = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "li.p-MenuBar-item:nth-child(4)"))
        )
        Run.click()
        RunAllCells = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "li.p-Menu-item:nth-child(17)"))
        )
        ActionChains(driver).move_to_element(RunAllCells).pause(1).click().pause(5).perform()
        driver.close()
        print("Operation successful")
    except NoSuchElementException:
        print("Error: An element was not found")
        driver.close()
    except TimeoutException:
        print("Error: The driver timed out")
        driver.close()


def main():
    testJupyter()


if __name__ == '__main__':
    main()
