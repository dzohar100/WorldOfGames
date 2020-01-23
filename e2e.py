from selenium import webdriver


# The method gets a URL, opens it with Chromedriver, check if the score number is between 0-1000 and return true or
# false.
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


# The method calls localhost on port 8777, test it with test_scores_service and return 0 if the test success and -1
# if not.
def main_function():
    call = test_scores_service("http://localhost:8777")
    errornum = 0
    if call:
        return errornum
    else:
        errornum = -1
        if errornum == -1:
            return "Error"


main_function()
