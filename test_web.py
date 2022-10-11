from selenium import webdriver
browser = webdriver.Chrome("c:\\webdrivers\\chromedriver.exe")
# Откываем веб-страницу и проверяем на функциональсноть кнопки в правом верхнем углу
browser.get("https://www.ecosia.org")
search_form = browser.find_element_by_xpath("/html/body/div/div/div/header/div[2]/button").click()
search_form = browser.find_element_by_xpath("/html/body/div/div/div/header/div[1]/button").click()
# Проверяем работает ли поиск
search_form = browser.find_element_by_xpath("/html/body/div/div/div/section[1]/div[1]/form/div[1]/input")
search_form.send_keys('вконтакте')
search_form.submit()
# Проверяем можно лои открыть другие варианты поиска
search_form = browser.find_element_by_xpath("/html/body/div[1]/div/nav[2]/div/div/div/div/ul/li[2]/a").click()
search_form = browser.find_element_by_xpath("/html/body/div/div/div/div[1]/header/div[1]/div[3]/div/button").click()
search_form = browser.find_element_by_xpath("/html/body/div/div/div/div[1]/header/div[1]/div[3]/div/div/nav/div[1]/ul/li[1]/a").click()

# Проверяем надпись на странице
message = browser.find_element_by_xpath("/html/body/main/div[1]/div/h1").text
assert message == "Plant trees while you search the web"

# Проверяем функциональность
search_form = browser.find_element_by_xpath("/html/body/nav[1]/div[2]/div[2]/div/a").click()
search_form = browser.find_element_by_xpath("/html/body/nav[1]/div[2]/div[2]/div/nav/div[2]/div/div[3]/a").click()
search_form = browser.find_element_by_xpath("/html/body/div[2]/header/div[1]/div[2]/div[1]/div[2]/div/nav/ul/li[2]/a").click()
search_form = browser.find_element_by_xpath("/html/body/div[2]/header/div[1]/div[2]/div[1]/div[2]/div/nav/ul/li[6]/a").click()
search_form = browser.find_element_by_xpath("/html/body/div/div/div/div[3]/div[1]/div/div[1]/div/a[1]").click()
search_form = browser.find_element_by_xpath("/html/body/div/div/div/div[3]/div[1]/div/a[4]").click()
browser.close()

