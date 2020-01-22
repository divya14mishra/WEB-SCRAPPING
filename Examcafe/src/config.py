from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome("/home/cool_vicky/Python Workspace/chromedriver", options=chrome_options)
