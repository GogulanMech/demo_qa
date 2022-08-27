from selenium.webdriver.common.by import By


class Text:
    ### Text data###
    link_elements_xpath = '//div[@class="category-cards"]/div[1]'
    list_text_xpath = '//div[@class="element-list collapse show"]/ul/li[1]'
    txt_fullname_xpath = '//div[@id="userName-wrapper"]/div/input'
    txt_email_xpath = '//div[@id="userEmail-wrapper"]/div/input'
    txt_currentaddress_xpath = '// div[ @ id = "currentAddress-wrapper"] / div / textarea'
    txt_permanentaddress_xpath = '//div[@id="permanentAddress-wrapper"]/div/textarea'
    btn_submit_xpath = "//button[text()='Submit']"
    #### checkbox data###
    list_checkbox_xpath = '//div[@class="element-list collapse show"]/ul/li[2]'
    btn_toggle_xpath = "//*[name()='path' and contains(@d,'M10 6L8.59')]"
    btn_toggle2_xpath = "//li[@class='rct-node rct-node-parent rct-node-expanded']//li[1]//span[1]//button[1]" \
                        "//*[name()='svg']//*[name()='path' and contains(@d,'M10 6L8.59')]"
    btn_toggle3_xpath = "//li[2]//span[1]//button[1]//*[name()='svg']"
    btn_toggle4_xpath = "//li[3]//span[1]//button[1]//*[name()='svg']"
    def __init__(self,driver):
        self.driver = driver

    def click_element(self):
        self.driver.find_element(By.XPATH, self.link_elements_xpath).click()

    def click_text(self):
        self.driver.find_element(By.XPATH, self.list_text_xpath).click()

    def set_fullname(self, fullname):
        self.driver.find_element(By.XPATH, self.txt_fullname_xpath).send_keys(fullname)

    def set_email(self, email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)

    def set_currentaddress(self, currentaddress):
        self.driver.find_element(By.XPATH, self.txt_currentaddress_xpath).send_keys(currentaddress)

    def set_permanentaddress(self, permanentaddress):
        self.driver.find_element(By.XPATH, self.txt_permanentaddress_xpath).send_keys(permanentaddress)

    def click_submit(self):
        button = self.driver.find_element(By.XPATH, self.btn_submit_xpath)
        self.driver.execute_script("arguments[0].click();", button)

