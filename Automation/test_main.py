import pytest
from main import Base
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


# We'll use the Login Page URL to shorten the process
base_url = "https://homme.co.il/wp-login.php"

# Credentials
user_password = "tester123!@#qwe"
user_username = "tester"


# Will be used for image uploading process
image_file_name = "house.jpg"
this_file_path = os.path.dirname(os.path.abspath(__file__))
image_upload_path = os.path.join(this_file_path, image_file_name)


# Setting a fixture to be used for all Pytest-related of the current session (To yield(use obj) and afterwards to quit(end session and obj))
@pytest.fixture(scope= "session")
def driver():
    
    driver = Base()
    driver.navigation(base_url)

    yield driver

    # Remove/Uncomment the line below to close the browser being opened
    # driver.close_driver()




# Test Cases:

# 1. Checking ALL Fields are present and logging in - 
def test_login_exist(driver):
    username_field = driver.get_web_element("ID", "user_login")
    password_field = driver.get_web_element("ID", "user_pass")
    login_btn = driver.get_web_element("ID", "wp-submit")
    driver.insert_text(username_field, user_username)
    driver.insert_text(password_field, user_password)
    driver.click_on(login_btn)
    # time.sleep(1)

    # Closing Terms pop-up
    terms_btn = driver.get_web_element("PARTIAL_LINK_TEXT", "אני מסכים")
    driver.click_on(terms_btn)

    
    assert driver.get_location() == "https://homme.co.il/%D7%94%D7%97%D7%A9%D7%91%D7%95%D7%9F-%D7%A9%D7%9C%D7%99/" # <- Login was successful



# 2. Creating the Ad (part 1) -
def test_ad_publishing_page_one(driver):
    publish_page_btn = driver.get_web_element("PARTIAL_LINK_TEXT", "פרסם מודעה")
    driver.click_on(publish_page_btn)

    # Choosing the options:
    asset_type_list = driver.get_web_element("ID", "ff_8_asset_type")
    driver.click_on(asset_type_list)
    apartment_opt = driver.get_web_element("CSS_SELECTOR", "option[value='דירה']")
    driver.click_on(apartment_opt)

    asset_status_list = driver.get_web_element("ID", "ff_8_asset_status")
    driver.click_on(asset_status_list)
    new_contr = driver.get_web_element("CSS_SELECTOR", "option[value='חדש מקבלן (לא גרו בנכס)']")
    driver.click_on(new_contr)

    cities_list = driver.get_web_element("ID", "ff_8_city")
    driver.click_on(cities_list)
    karmiel = driver.get_web_element("CSS_SELECTOR", "option[value='כרמיאל']")
    driver.click_on(karmiel)


    streets_list = driver.get_web_element("ID", "ff_8_street_1")
    driver.click_on(streets_list)
    street = driver.get_web_element("CSS_SELECTOR", "option[value='אביב']")
    driver.click_on(street)

    street_num_field = driver.get_web_element("ID", "ff_8_street_number")
    driver.insert_text(street_num_field, "5/5")

    next_btn = driver.get_web_element("CSS_SELECTOR", "button[data-action='next']")
    driver.click_on(next_btn)

    # If all went well, should move to the next step (more meaningful Asserts will be used later on the validation part)
    assert 1 == 1 



# 3. Creating the Ad (part 2) -
def test_ad_publishing_page_two(driver):
    floor = driver.get_web_element("ID", "ff_8_floor")
    out_of_floors = driver.get_web_element("ID", "ff_8_floors")
    meters = driver.get_web_element("ID", "ff_8_built_mr")
    driver.insert_text(floor, "1")
    driver.insert_text(out_of_floors, "2")
    driver.insert_text(meters, "140")

    # Had an issue choosing the same "1" options as it refers to the same one.
    # Choose a more specific method using ID and then its Value "#element_id option[value='some_val']"
    rooms_list = driver.get_web_element("ID", "ff_8_room_num")
    driver.click_on(rooms_list)
    room_opt = driver.get_web_element("CSS_SELECTOR", "#ff_8_room_num option[value='1']")
    driver.click_on(room_opt)

    terrace_list = driver.get_web_element("ID", "ff_8_terrace")
    driver.click_on(terrace_list)
    terrace_opt = driver.get_web_element("CSS_SELECTOR", "#ff_8_terrace option[value='1']")
    driver.click_on(terrace_opt)

    parking_list = driver.get_web_element("ID", "ff_8__parking")
    driver.click_on(parking_list)
    parking_opt = driver.get_web_element("CSS_SELECTOR", "#ff_8__parking option[value='1']")
    driver.click_on(parking_opt)

    elevator_list = driver.get_web_element("ID", "ff_8_elevator_1")
    driver.click_on(elevator_list)
    elevator_opt = driver.get_web_element("CSS_SELECTOR", "#ff_8_elevator_1 option[value='ללא']")
    driver.click_on(elevator_opt)

    """
    Since the buttons, using similar attributes exists on all forms throughout the creation, I had to change the usage
    to refer to the Elements by their EXACT CSS Selectors relative to the page's structure
    """
    time.sleep(0.5)
    first_next_btn = driver.get_web_element("CSS_SELECTOR", "div.step-nav:nth-child(5) > button:nth-child(2)")
    driver.click_on(first_next_btn)


    """
    Choosing Handicapped Access for example
    After many tries, the solution I found for the dynamic ID assignment, is to address to the first checkbox/input by listing all classes that lead to it.
    Then, finding the label wrapping it (with a class called "ff-el-form-check-label") <-which is its "ancestor" (XPath axis). 
    And finally, clicking it.
    """
    handicap_opt_input = driver.get_web_element("CSS_SELECTOR", ".ff_el_checkable_photo_holders .ff-el-form-check-input.ff-el-form-check-checkbox:first-of-type")
    handicap_clickable_label = handicap_opt_input.find_element(By.XPATH, "./ancestor::label[contains(@class, 'ff-el-form-check-label')]")
    driver.click_on(handicap_clickable_label)

    time.sleep(0.5)
    second_next_btn = driver.get_web_element("CSS_SELECTOR", "div:nth-child(3) > button:nth-child(2)")
    driver.click_on(second_next_btn)

    assert 1 == 1



# 4. Creating the Ad (part 3) -
def test_ad_publishing_page_three(driver):    
    payments = driver.get_web_element("ID", "ff_8_credits")
    driver.insert_text(payments, "8")
    price = driver.get_web_element("ID", "ff_8_price")
    driver.insert_text(price, "500")
    
    # Triggering the date picker and choosing the first of January available for example
    date_event = driver.get_web_element("ID", "ff_8_date_start")
    driver.click_on(date_event)
    month_list = driver.get_web_element("CSS_SELECTOR", ".flatpickr-monthDropdown-months")
    driver.click_on(month_list)
    selected_month = driver.get_web_element("CSS_SELECTOR", "select.flatpickr-monthDropdown-months option[value='0']")
    driver.click_on(selected_month)
    selected_day = driver.get_web_element("CSS_SELECTOR", "span.flatpickr-day:nth-child(4)")
    driver.click_on(selected_day)

    time.sleep(0.5)
    third_next_btn = driver.get_web_element("CSS_SELECTOR", ".next-form-3 > div:nth-child(3) > button:nth-child(2)")
    driver.click_on(third_next_btn)
    assert 1 == 1


# 5. Creating the Ad (final part) -
def test_ad_publishing_final_page(driver):
    # Since uploading a file uses "Browse", and in other words accepts a PATH -
    # We can simply insert the image's path relative to this file path (on the same directory)
    img_input_field = driver.get_web_element("ID", "ff_8_pictures_1")
    driver.insert_text(img_input_field, image_upload_path)
    time.sleep(2) #<- Waiting to make sure file is uploaded

    fourth_next_btn = driver.get_web_element("CSS_SELECTOR", "div.step-nav:nth-child(2) > button:nth-child(2)")
    driver.click_on(fourth_next_btn)

    time.sleep(1)
    full_name_field = driver.get_web_element("ID", "ff_8_name_full")
    driver.insert_text(full_name_field, "דביר קרילקר")
    phone_num_field = driver.get_web_element("ID", "ff_8_phone_number")
    driver.insert_text(phone_num_field, "0544713295")
    time.sleep(0.5)
    publish_btn = driver.get_web_element("CSS_SELECTOR", ".ff-btn-submit")
    driver.click_on(publish_btn)

    time.sleep(5) #<-Waiting for redirection
    assert driver.get_location() == "https://homme.co.il/appartments/"
    


# 6. Validating Ad's details -
def test_validate_details(driver):
    time.sleep(1)
    listing = driver.get_web_element("CSS_SELECTOR", ".jet-listing-grid__item[data-post-id]")
    driver.click_on(listing)

    time.sleep(2)
    title = driver.get_web_element("CSS_SELECTOR", "h1.elementor-heading-title").text
    assert title == "כרמיאל 5/5"

    asset_stat = driver.get_web_element("CSS_SELECTOR", ".elementor-element-7eac330 > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > span:nth-child(2)").get_attribute("innerHTML")
    assert asset_stat == "<strong>מצב הנכס:</strong> חדש מקבלן (לא גרו בנכס)"

    meter_amoun = driver.get_web_element("CSS_SELECTOR", ".elementor-element-7eac330 > div:nth-child(1) > ul:nth-child(1) > li:nth-child(2) > span:nth-child(2)").get_attribute("innerHTML")
    assert meter_amoun == "<strong> מ\"ר בנוי: </strong> 140"

    terrace_amoun = driver.get_web_element("CSS_SELECTOR", ".elementor-element-7eac330 > div:nth-child(1) > ul:nth-child(1) > li:nth-child(3) > span:nth-child(2)").get_attribute("innerHTML")
    assert terrace_amoun == "<strong> מרפסות: </strong> 1"




    # Additional details assertions......#

    #END OF CODE#