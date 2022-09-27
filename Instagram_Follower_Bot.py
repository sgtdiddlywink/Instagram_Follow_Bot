"""
IMPORTANT WARNING: THERE IS A HIGH POSSIBILITY THAT INSTAGRAM WILL DETECT THIS AS A BOT AND BAN YOUR ACCOUNT.  THIS IS
                    YOUR WARNING.  I WOULDN'T FOLLOW MORE THAN 50 PEOPLE FOR A PERIOD OF TIME TO REDUCE THIS CHANCE.
                    I DON'T KNOW WHAT THIS PERIOD OF TIME SHOULD BE BUT IT'S A GOOD CHANCE YOU CAN GET BANNED IF YOU
                    ABUSE THIS.

IMPORTANT NOTE: Do not have 2FA for Instagram.  This script will not work if it is turned on.
IMPORTANT NOTE: Some target accounts do not let you view all of their followers and therefore this script will only grab
                a select few before it ends.

This script will log into your Instagram account and go to the specified link of the account you want to mass follow.
You can change this link to another Instagram account to mass follow who they follow.

A random timer is set up for following to look less like a bot.  However, Instagram may still flag your account as a bot
and ban it so here is your forewarning.

"""

"""Import and install appropriate modules below."""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
import random

# Put your own credentials here.  Ensure there is no 2FA turned on for your Instagram account.
INSTAGRAM_LOGIN = "YOUR INSTAGRAM LOGIN"
INSTAGRAM_PW = "YOUR INSTAGRAM PASSWORD"

# URL for front page of Instagram.
URL = "https://www.instagram.com/accounts/login/"

# Specify the account name that you want to mass follow.
INSTAGRAM_ACCOUNT_TARGET = "YOUR TARGETS INSTAGRAM NAME"

# Specify how many follows you want it to go click.  Keep in mind it needs to be less than the amount of followers
# your target has.  I would recommend not going above 50 or Instagram will detect it.
FOLLOWER_COUNT = 50

"""Need to install the appropriate browser driver and place .exe in accessible file."""
# Chrome driver path should reference the .exe browser driver.
chrome_driver_path = "THE PATH TO YOUR BROWSER'S DRIVER"


# Create a class to break up the parts of the bot.
class InstaFollower:

    # Initialize basic features of the class objects.
    def __init__(self, driver_path):
        # Access the driver.
        self.driver = webdriver.Chrome(executable_path=driver_path)

    # Method to log in to Instagram.
    def login(self, url, login, password):
        # Open the website.
        self.driver.get(url)

        # Sleep for random amount of time.
        time.sleep(random.randint(2, 5))

        # Fill in the username input box with the Instagram Login provided above.
        self.driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(login)

        # Sleep for random amount of time.
        time.sleep(random.randint(2, 5))

        # Fill in the password input box with the Instagram Password provided above.  Ensure 2FA is turned off.
        self.driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(password)

        # Sleep for random amount of time.
        time.sleep(random.randint(2, 5))

        # Click the "Log in" button.
        self.driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button/div").click()

        # Sleep for random amount of time.
        time.sleep(random.randint(4, 6))

        # Click the "Save Info" button that appears in the popup if you have not already initialized it.
        try:
            self.driver.find_element(
                By.XPATH,
                "//button[@type='button' and text()='Save Info']"
            ).click()

            # Sleep for random amount of time.
            time.sleep(random.randint(3, 6))

        except NoSuchElementException:
            pass

    # Click the "Turn On" button that appears in the popup if you have not already initialized it.

        self.driver.find_element(
            By.CSS_SELECTOR,
            "button._a9--._a9_1"
        ).click()

        # Sleep for random amount of time.
        time.sleep(random.randint(2, 5))

    # Method to find followers of the specified account on Instagram.
    def find_followers(self, target_account):
        # Search for target account and open followers list.
        self.driver.get(f"https://www.instagram.com/{target_account}/followers/")

        # Sleep for random amount of time.
        time.sleep(random.randint(3, 6))

    # Method to follow each of the followers in the target account.
    def follow(self):
        # For loop to run through each available follow button.  Only one variable changes for each one.
        for num in range(1, FOLLOWER_COUNT):
            follow_button = self.driver.find_element(
                By.XPATH,
                f"/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div"
                f"/div/div[2]/div[1]/div/div[{num}]/div[3]/button"
            )
            # If statement to determine whether you have already followed them.
            if follow_button.text == "Follow":
                follow_button.click()
            else:
                pass

            # Sleep for random amount of time.
            time.sleep(random.randint(2, 5))


# Initialize an object with the class.
insta_bot = InstaFollower(driver_path=chrome_driver_path)

# Initialize the login method of the bot.
insta_bot.login(url=URL, login=INSTAGRAM_LOGIN, password=INSTAGRAM_PW)

# Initialize the find_followers method of the bot.
insta_bot.find_followers(target_account=INSTAGRAM_ACCOUNT_TARGET)

# Initialize the follow method of the bot.
insta_bot.follow()


