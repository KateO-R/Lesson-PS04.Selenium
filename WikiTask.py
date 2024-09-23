from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys  # Setting the encoding for UTF-8
import io

sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

def list_paragraphs():
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)
        time.sleep(1)  # Pause for ease of reading
        if input("Press Enter to continue or type q to quit:") == 'q':
            break


def visit_link():
    time.sleep(3)  # Time to load
    links = browser.find_elements(By.TAG_NAME, "a")
    links_list = [link.get_attribute('href') for link in links if link.get_attribute('href')]

    print(f"Found {len(links_list)} links.")  # Debug info

    if links_list:
        print("\nAvailable links:")
        for index, href in enumerate(links_list):
            print(f"{index}: {href[:50]}...")  # Output shortened URL

        try:
            choice = int(input("Enter the number of the link you want to visit: "))
            if 0 <= choice < len(links_list):
                selected_link = links_list[choice]
                browser.get(selected_link)
                time.sleep(5)
            else:
                print("Invalid choice. Returning to menu.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("No links available.")

def main_menu():
    while True:
        print("\nChoose action:")
        print("1. Scroll through paragraphs of the current article")
        print("2. Go to one of the related pages")
        print("3. Exit the program")
        choice = input("Enter the action number: ")

        if choice == '1':
            list_paragraphs()
        elif choice == '2':
            visit_link()
            sub_menu()
        elif choice == '3':
            break
        else:
            print("Wrong input. Please, print 1, 2 or 3.")

def sub_menu():
    while True:
        print("\nChoose action:")
        print("1. Scroll through paragraphs of the current article")
        print("2. Go to one of the related pages")
        print("3. Return to main menu")
        choice = input("Enter the action number: ")

        if choice == '1':
            list_paragraphs()
        elif choice == '2':
            visit_link()
        elif choice == '3':
            break
        else:
            print("Wrong input. Please, print 1, 2 or 3.")

# Initializing the browser
browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

assert "Википедия" in browser.title
time.sleep(5)
request = input("Hello! What are you interested in today? ")
search_box = browser.find_element(By.ID, "searchInput")
search_box.send_keys(request)
search_box.send_keys(Keys.RETURN)
time.sleep(5)

main_menu()
browser.quit()
