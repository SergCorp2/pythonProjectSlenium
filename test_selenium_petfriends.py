# import time
# from selenium.webdriver.common.by import By
#
# def test_petfriends(selenium):
#
#     selenium.get('https://petfriends.skillfactory.ru/')
#
#     time.sleep(3)
#
#
#     btn_newuser = selenium.find_element(By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]")
#     btn_newuser.click()
#
#     btn_exit_acc = selenium.find_element(By.LINK_TEXT, 'у меня уже есть аккаунт')
#     btn_exit_acc.click()
#
#     field_email = selenium.find_element(By.ID, 'email')
#     field_email.clear()
#     field_email.send_keys('5555@mail.com')
#
#     field_pass = selenium.find_element(By.ID, 'pass')
#     field_pass.clear()
#     field_pass.send_keys('5555')
#
#     btn_submit = selenium.find_element(By.XPATH, "//button[@type='submit']")
#     btn_submit.click()
#
#     time.sleep(3)
#     if selenium.curent_url ==  'https://petfriends.skillfactory.ru/all_pets':
#         selenium.save_screenshot('result_petfriends.png')
#     else:
#         raise Exception('login error')

# import time
#
# import pytest
# from selenium.webdriver.common.by import By


# def test_petfriends(selenium):
#     """ Search some phrase in google and make a screenshot of the page. """
#
#     # Open PetFriends base page:
#     selenium.get("https://petfriends.skillfactory.ru/")
#
#     time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!
#
#     # Find the field for search text input:
#     btn_newuser = selenium.find_element(By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]")
#
#     btn_newuser.click()
#
#     btn_exist_acc = selenium.find_element(By.LINK_TEXT, u"У меня уже есть аккаунт")
#     btn_exist_acc.click()
#
#     field_email = selenium.find_element(By.ID, "email")
#     field_email.click()
#     field_email.clear()
#     field_email.send_keys("5555@mail.com")
#
#     field_pass = selenium.find_element(By.ID, "pass")
#     field_pass.click()
#     field_pass.clear()
#     field_pass.send_keys("5555")
#
#     btn_submit = selenium.find_element(By.XPATH, "//button[@type='submit']")
#     btn_submit.click()
#
#     # Save cookies of the browser after the login
#     # with open('my_cookies.txt', 'wb') as cookies:
#     #     pickle.dump(selenium.get_cookies(), cookies)
#
#     time.sleep(3)
#     if selenium.current_url == 'https://petfriends.skillfactory.ru/all_pets':
#             selenium.save_screenshot('result_petfriends.png')
#     else:
#         raise Exception('login error')
#     # Make the screenshot of browser window:
#     selenium.save_screenshot('result_petfriends.png')
#

# import time
#
# def test_petfriends(web_browser):
#    # Open PetFriends base page:
#    web_browser.get("https://petfriends.skillfactory.ru/")
#
#    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!
#
#    # click on the new user button
#    btn_newuser = web_browser.find_element_by_xpath("//button[@onclick=\"document.location='/new_user';\"]")
#    btn_newuser.click()
#
#    # click existing user button
#    btn_exist_acc = web_browser.find_element_by_link_text(u"У меня уже есть аккаунт")
#    btn_exist_acc.click()
#
#    # add email
#    field_email = web_browser.find_element_by_id("email")
#    field_email.clear()
#    field_email.send_keys("<your_email>")
#
#    # add password
#    field_pass = web_browser.find_element_by_id("pass")
#    field_pass.clear()
#    field_pass.send_keys("<your_pass>")
#
#    # click submit button
#    btn_submit = web_browser.find_element_by_xpath("//button[@type='submit']")
#    btn_submit.click()
#
#    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!
#
#    assert  web_browser.current_url == 'https://petfriends.skillfactory.ru/all_pets',"login error"


import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('D:\Scillfactory\pythonProjectSlenium\chromedriver_win32\chromedriver.exe')
    pytest.driver.get('http://petfriends.skillfactory.ru/login')
    #WebDriverWait(pytest.driver, 2).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/login']")))
    yield

    pytest.driver.quit()



def test_show_my_pets():

    pytest.driver.find_element(By.ID, 'email').send_keys('5555@mail.com')
    pytest.driver.find_element(By.ID, 'pass').send_keys("5555")
    time.sleep(1)
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    time.sleep(2)
    pytest.driver.find_element(By.CSS_SELECTOR, 'body > nav > button > span').click()
    time.sleep(2)
    pytest.driver.find_element(By.CSS_SELECTOR, '#navbarNav > ul > li:nth-child(1) > a').click()

    assert pytest.driver.find_element(By.TAG_NAME, 'h2').text == 'qwert1234'
    time.sleep(2)

    # pytest.driver.implicitly_wait(3)

    images = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr[i]/th/img')
    names = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr[i]/td[1]')
    breed = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr[i]/td[2]')
    ages = pytest.driver.find_element(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr[1]/td[3]')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert breed[i].text != ''
        assert ages[i].ini != ''


