from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge import service
import time

quarters = ['01', '04', '07', '10']

download_quarters = []

with open('quarter.txt', 'r') as file:
    for quarter in file:
        quarter = quarter.split('-')

        year = quarter[0]
        month = int(quarter[1])
        download_quarter = year + quarters[month - 1]
        download_quarters.append(download_quarter)

# 옵션 설정
options = webdriver.EdgeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
options.use_chromium = True
options.add_experimental_option("detach", True)

# Edge 파일 위치 설정
options.binary_location = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
s = service.Service(r"msedgedriver.exe")

# Edge 드라이버 생성
driver = webdriver.Edge(options=options, service = s)
driver.get('https://www.aniplustv.com/')

driver.implicitly_wait(3)

# 로그인창 으로 이동
driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/ul/li[4]').click()

# 로그인
driver.find_element(By.NAME, 'userid').send_keys('newmri')
driver.find_element(By.NAME, 'password').send_keys('!alsk5168')
driver.find_element(By.CLASS_NAME, 'login_btn').click()

# VOD
driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/ul/li[2]').click()

for quarter in download_quarters:
    # 분기 선택
    driver.execute_script("arguments[0].click();", driver.find_element(By.ID, 'checkbox_' + quarter))

time.sleep(5)

count = driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/div/div[2]/div[1]/h1')
count = count.text.split(')')[0].split('(')[1]
print(count)

#driver.quit()