from selenium import webdriver


def test_scores_service(app_url):
    try:
        driver = webdriver.Chrome(executable_path="/Users/DorZohar 1/Desktop/Softwares/Chrome/chromedriver")
        driver.implicitly_wait(3)
        driver.get(app_url)

        score_text = driver.find_element_by_id("score").text
        score_id = int(score_text)
        if 0 < score_id < 1000:
            return True
        else:
            return False

    except IOError:
        print("Could not find a driver or could not open Chrome browser.")

    finally:
        driver.close()


def main_function():
    call = test_scores_service("http://localhost:8777")
    if call:
        return 0
    elif not call:
        return -1
    else:
        return "Error"


main_function()
