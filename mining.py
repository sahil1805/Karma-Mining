# Importing all the modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random
import datetime
from colors import bcolors
import getpass
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

desc = """This is a Free Version It will comment between 50-100 comments For paid version contact on 
our gmail. As we all know on reddit our account got suspended and again and again. Gaining Karma on 
reddit is easy but commenting manual is just taking your precious time. This is the solution.\nThank You"""
print(bcolors.OKCYAN + desc.center(len(desc)))

print(bcolors.OKGREEN + """
88""88  888888  88 88    88 88    88  888888
88__88  88__    88   88  88   88  88    88  
88"88   88""    88   88  88   88  88    88  
88  88  888888  88 88    88 88    88    88                               BY ASAP Contact : asapofficialsite@gmail.com                                                                                                  
""" + bcolors.ENDC)

# Creating option from over to make it hide from detection
option = Options()
option.add_argument("--headless")
option.add_argument('--no-sandbox')
option.add_argument('--start-maximized')
option.add_argument('--disable-dev-shm-usage')
option.add_argument("--incognito")
option.add_argument('--disable-blink-features=AutomationControlled')
option.add_argument("--disable-infobars")
option.add_argument("--disable-notifications")
option.add_argument("--disable-extensions")
option.add_argument("--log-level=3")
option.add_experimental_option('useAutomationExtension', False)
option.add_experimental_option("prefs",
                               {"profile.default_content_setting_values.notifications": 2})
option.add_experimental_option(
    "excludeSwitches", ["enable-logging", "disable-popup-blocking", 'enable-automation'])


def link_grab(more_filtered):
    # For filessssss
    with open('sample.txt') as f:
        lines = f.readlines()

    new = []
    post_link = []

    for i in range(len(lines)):
        new.append(lines[i].replace("\n", ""))

    for i in range(len(more_filtered)):
        if more_filtered[i] not in new:
            new.append(more_filtered[i])
            post_link.append(more_filtered[i])
        else:
            pass

    with open("sample.txt", "a") as f:
        for i in range(len(post_link)):
            f.write(f"{post_link[i]}\n")

    return post_link


def spamming(username, password):
    c = 0
    # path for the driver
    driver = webdriver.Chrome(options=option)

    driver.get("https://www.reddit.com")

    driver.get(
        "https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2F")

    # Maximize the Window for better view
    driver.maximize_window()
    time.sleep(2)

    # Entering Credentials
    driver.find_element(By.ID, "loginUsername").send_keys(username)
    driver.find_element(By.ID, "loginPassword").send_keys(password)

    driver.find_element(
        By.XPATH, """/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button""").click()
    time.sleep(10)
    print("Login Completed!!")

    url = "https://www.reddit.com/"
    community = ["r/FreeKarma4U", "r/FreeKarma4You"]
    new = "/new/"

    comment_list = ["Upvote my comment I need karma for post!", "Please upvote my comment I am new on reddit, I have upvoted your post.", "Looking for some comment karma!! I just upvoted you. Could you please return?", "I have just upvoted you :) Could you please return the favor by upvoting my comment?", "I am looking to trade some upvotes, just gave one your way. Can you please return on my post?", "Here is an upvote from me to you! Please return it on some posts of mine?",
                    "Hope you are enjoying the rest of your day! Just upvoted you, can you return on a post or two?", "Hello - upvoted would you help me out on a upvote as well please", "Could you please upvote a post or two of mine? I have upvoted you!!", "Hit you with an upvote just now. Please return on one or two of my posts?", "Please Upvote me I am new On reddit Please help me", "Hi I am new here Please upvote my comment I need comment Karma"]

    # Community selection loop
    for i in range(len(community)):

        link = url+community[i]+new
        driver.get(link)

        # Only used for 18+ communities
        try:
            driver.find_element(
                By.XPATH, """//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div[1]/div/div/div[2]/button""").click()
        except:
            pass
        time.sleep(2)

        # Scraping all the links from the current page
        all_link = []
        elems = driver.find_elements(By.XPATH, "//a[@href]")
        for elem in elems:
            all_link.append(elem.get_attribute("href"))

        filtered = list(set(all_link))

        more_filtered = []
        for k in range(len(filtered)):
            if f"https://www.reddit.com/{community[i]}/comments/" in filtered[k]:
                more_filtered.append(filtered[k])

        post_link = link_grab(more_filtered)
        # Post Selecting loop
        for j in range(0, len(post_link)-1):
            # Opening the link for Commenting
            driver.get(post_link[j])
            time.sleep(5)

            try:
                comment_index = random.randint(0, len(comment_list)-1)
                # Send Message or link in comment section
                driver.find_element(By.XPATH, """//*[@id="AppRouter-main-content"]/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[2]/div/div/div[2]/div/div[1]/div/div/div""").send_keys(comment_list[comment_index])
                time.sleep(2)

                comment_button = driver.find_element(By.XPATH, """//*[@id="AppRouter-main-content"]/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[2]/div/div/div[3]/div[1]/button""")
                desired_y = (
                    comment_button.size['height']/2) + comment_button.location['y']
                current_y = (driver.execute_script('return window.innerHeight') /
                             2) + driver.execute_script('return window.pageYOffset')
                scroll_y_by = desired_y - current_y
                driver.execute_script(
                    "window.scrollBy(0, arguments[0]);", scroll_y_by)
                comment_button.click()
                time.sleep(10)
                c += 1
                print(f"{c} - Comment Done", end="\r", flush=True)

            except:
                pass

    driver.quit()
    return c


u1 = str(input(bcolors.OKBLUE + "\nPlease Enter your Reddit Username: " + bcolors.BOLD))

p1 = getpass.getpass(prompt=bcolors.WARNING + "\nPlease Enter your Reddit Password:: " + bcolors.BOLD)

k = int(input(bcolors.OKBLUE + "\nPlease Enter Number of comments: " + bcolors.BOLD))

print(bcolors.OKGREEN + "\nLOADING .....\n")

x = 20

count = 0

karma = k

date_t = str(datetime.date.today()).split("-")

with open("detail.txt", "r+") as f:
    pre = f.read()

if str(int(pre[-3:-1])) < date_t[-1]:
    with open("sample.txt", "w") as f:
        f.write("")

with open("detail.txt", "w") as f:
    f.write(f"{str(datetime.date.today())}")

while count < karma:
    count += spamming(u1, p1)
    now = datetime.datetime.now()
    current = now.strftime("%H:%M:%S")
    print(f"Till now comments done : {count}\nCurrent time - {current}... All new comments are done.It will start again after {x} min")
    time.sleep(x*60)

print(f"Total comments done : {count}")
choice = str(input("Press Any Key for Quit: "))
quit()