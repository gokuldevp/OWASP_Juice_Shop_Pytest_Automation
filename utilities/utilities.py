import random
import logging
import datetime
import os

def get_current_date_time():
    """ Function to return datetime int YYMMDDHHmmSS format """
    current_datetime = str(datetime.datetime.now())[0:19]
    return datetime.datetime.strptime(current_datetime, '%Y-%m-%d %H:%M:%S').strftime('%Y%m%d%H%M%S')

def get_current_date():
    """ Function to return datetime int YYMMDDHHmmSS format """
    current_date = str(datetime.date.today().strftime("%Y_%m_%d"))
    return current_date

def generate_credit_card_details():
    names = [
        "John", "Jane", "Alex", "Emily", "Chris", "Katie",
        "Michael", "Sarah", "David", "Laura", "Robert", "Jessica",
        "James", "Emma", "Daniel", "Olivia", "Matthew", "Sophia",
        "Joshua", "Isabella", "Andrew", "Mia", "Joseph", "Abigail",
        "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia",
        "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez",
        "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor",
        "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson",
        "White", "Harris"
    ]

    name = random.choice(names) + " " + random.choice(names)
    card_number = random.randrange(1111111111111111,5000000000000000)
    card_exp_month = str(random.randrange(1,13))
    card_exp_year = str(random.randrange(2080,2100))
    return name, card_number, card_exp_month, card_exp_year


def loggen(): 
    log_file = os.path.join(os.path.dirname(os.path.abspath(__file__).replace('utilities\\', '')), 'logs', 'automation.log') 
    log_handler = logging.FileHandler(log_file) 
    log_handler.setFormatter( logging.Formatter("%(asctime)s: %(levelname)s: %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")) 
    logger = logging.getLogger() 
    logger.addHandler(log_handler) 
    logger.setLevel(logging.INFO) 
    return logger

class ScreeShots:
    def __init__(self, driver):
        self.driver = driver
    def take_screenshots_as_png(self,screenshot_name):
        dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__).replace('utilities\\', '')),'Reports\\',datetime.date.today().strftime("%Y_%m_%d"))
        
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)
        
        screenshot_name = "" + datetime.datetime.strptime(get_current_date_time(), '%Y%m%d%H%M%S').strftime('%d_%m_%Y_%H_%M_%S') + f"_{screenshot_name}" + ".png"
        screenshot_file = os.path.join(dir_path, screenshot_name)
        
        self.driver.save_screenshot(screenshot_file)

        re_path = screenshot_file.replace(os.path.dirname(os.path.abspath(__file__).replace('utilities\\', '')),"")
        return re_path
