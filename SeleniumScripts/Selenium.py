__author__ = "Mahesh"

from selenium import webdriver

'''
Simple gmail login using selenium with python
'''
driver=webdriver.Chrome("D:\selenium-java-2.53.0\selenium-2.53.0\ThirdPartyDrivers\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(1000)
# Enter google home page
driver.get("https://www.google.com/?gws_rd=ssl")
driver.get_screenshot_as_file("D:\\workspace_python\\Python_Selenium\\Screenshots\\googlehomepage.png")
# click on gmail button
driver.find_element_by_class_name("gb_P").click()
driver.get_screenshot_as_file("D:\\workspace_python\\Python_Selenium\\Screenshots\\gmailbutton.png")
# click on gmail email box
driver.find_element_by_xpath("//A[@class='gmail-nav__nav-link gmail-nav__nav-link__sign-in'][text()='Sign In']").click()
driver.get_screenshot_as_file("D:\\workspace_python\\Python_Selenium\\Screenshots\\sign-in.png")
# driver.find_element_by_xpath("//INPUT[@id='Email']")
# Enter emailid
driver.find_element_by_xpath("//INPUT[@id='Email']").send_keys("selenium")
driver.get_screenshot_as_file("D:\\workspace_python\\Python_Selenium\\Screenshots\\email.png")
#click on next button
driver.find_element_by_xpath("//INPUT[@id='next']").click()
# enter password
driver.find_element_by_id("Passwd").send_keys("python")
driver.get_screenshot_as_file("D:\\workspace_python\\Python_Selenium\\Screenshots\\password.png")
# click on signin button
driver.find_element_by_id("signIn").click()
driver.get_screenshot_as_file("D:\\workspace_python\\Python_Selenium\\Screenshots\\click.png")
driver.quit()






#driver.quit()
