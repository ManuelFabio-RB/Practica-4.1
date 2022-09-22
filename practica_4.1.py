from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(
    executable_path = "C:/Users\manub\Documents/7mo Semestre\PACS\chromedriver_win32/chromedriver.exe")

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html%22")
time.sleep(2)

driver.maximize_window()
time.sleep(2)

actions = ActionChains(driver)
time.sleep(2)

oslo = driver.find_element(By.ID,"box1")
norway= driver.find_element(By.ID,"box101")
actions.drag_and_drop(oslo, norway).perform()
time.sleep(2)

rome = driver.find_element(By.ID,"box6")
italy = driver.find_element(By.ID,"box106")
actions.drag_and_drop(rome, italy).perform()
time.sleep(2)

madrid = driver.find_element(By.ID,"box7")
spain = driver.find_element(By.ID,"box107")
actions.drag_and_drop(madrid, spain).perform()
time.sleep(2)

copenhague = driver.find_element(By.ID,"box4")
denmark = driver.find_element(By.ID,"box104")
actions.drag_and_drop(copenhague, denmark).perform()
time.sleep(2)

seul = driver.find_element(By.ID,"box5")
korea = driver.find_element(By.ID,"box105")
actions.drag_and_drop(seul, korea).perform()
time.sleep(2)

estocolmo = driver.find_element(By.ID,"box2")
sweden = driver.find_element(By.ID,"box102")
actions.drag_and_drop(estocolmo, sweden).perform()
time.sleep(2)

washington = driver.find_element(By.ID,"box3")
usa = driver.find_element(By.ID,"box103")
actions.drag_and_drop(washington, usa).perform()