import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestOrders():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def login(self):
        self.driver.get("https://organicafoods.odoo.com/web/login")
        self.driver.find_element(
            By.ID, "login").send_keys("gm070797@gmail.com")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("Organicafoods")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, ".o_app:nth-child(2) > .o_app_icon")))
        self.driver.find_element(
            By.CSS_SELECTOR, ".o_app:nth-child(2) > .o_app_icon").click()

    def test_vieworders(self):
        self.login()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, "Orders")))
        self.driver.find_element(By.LINK_TEXT, "Orders").click()
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, ".show > .dropdown-item:nth-child(1) > span")))
        self.driver.find_element(
            By.CSS_SELECTOR, ".show > .dropdown-item:nth-child(1) > span").click()

    def test_orderdetails(self):
        self.test_vieworders()
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, ".o_data_row:nth-child(3) > .o_data_cell:nth-child(2)")))
        self.driver.find_element(
            By.CSS_SELECTOR, ".o_data_row:nth-child(3) > .o_data_cell:nth-child(2)").click()

    def test_returnproduct(self):
        self.test_vieworders()

        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, ".o_data_row:nth-child(8) > .o_data_cell:nth-child(2)")))
        self.driver.find_element(
            By.CSS_SELECTOR, ".o_data_row:nth-child(8) > .o_data_cell:nth-child(2)").click()

        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, ".btn:nth-child(3) > span")))
        self.driver.find_element(
            By.CSS_SELECTOR, ".btn:nth-child(3) > span").click()

        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, ".btn-primary > span")))
        self.driver.find_element(
            By.CSS_SELECTOR, ".btn-primary > span").click()

        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, "footer > .btn-primary > span")))
        self.driver.find_element(
            By.CSS_SELECTOR, "footer > .btn-primary > span").click()
       # self.driver.find_element(By.CSS_SELECTOR, "#modal_245 .modal-footer span").click()

    def test_viewbankpayments(self):
        self.login()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, "Orders")))
        self.driver.find_element(By.LINK_TEXT, "Orders").click()
        # WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".show > .dropdown-item:nth-child(3) > span")))
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, ".show > .dropdown-item:nth-child(3) > span")))
        self.driver.find_element(
            By.CSS_SELECTOR, ".show > .dropdown-item:nth-child(3) > span").click()

        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, ".o_group_header:nth-child(1) > .o_group_name")))
        self.driver.find_element(
            By.CSS_SELECTOR, ".o_group_header:nth-child(1) > .o_group_name").click()

        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, ".o_data_row:nth-child(4) > .o_data_cell:nth-child(3)")))
        self.driver.find_element(
            By.CSS_SELECTOR, ".o_data_row:nth-child(4) > .o_data_cell:nth-child(3)").click()

    def test_viewcustomerdetails(self):
        self.login()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, "Orders")))
        self.driver.find_element(By.LINK_TEXT, "Orders").click()

        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, ".dropdown-item:nth-child(4) > span")))
        self.driver.find_element(
            By.CSS_SELECTOR, ".dropdown-item:nth-child(4) > span").click()

        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, ".oe_kanban_global_click:nth-child(2) .o_text_overflow > span")))
        self.driver.find_element(
            By.CSS_SELECTOR, ".oe_kanban_global_click:nth-child(2) .o_text_overflow > span").click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, "Sales & Purchase")))
        self.driver.find_element(By.LINK_TEXT, "Sales & Purchase").click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, "Invoicing")))
        self.driver.find_element(By.LINK_TEXT, "Invoicing").click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, "Internal Notes")))
        self.driver.find_element(By.LINK_TEXT, "Internal Notes").click()

        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.LINK_TEXT, "Contacts & Addresses")))
        self.driver.find_element(By.LINK_TEXT, "Contacts & Addresses").click()
