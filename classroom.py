def upload_solution(assignment_link,file_path):
    ## STEP 1 -> Importing dependencies

    #selenium is  use dto interact with the web browser
    from selenium import webdriver
    #By is used to locate elements(buttons/divs/inputs)
    from selenium.webdriver.common.by import By

    #for accesing differnet services,waiting conditions
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    #to conifgure chrome
    from selenium.webdriver.chrome.options import Options
    #used for delays
    import time
    #executes system commands
    import os

    ## STEP 2 -> Opening Chrome Browser

    #forcefully closed any already running chrome.exe or chromedriver.exe processes to avoid conflicts such as anothe ropen session
    os.system("taskkill /f /im chrome.exe")
    os.system("taskkill /f /im chromedriver.exe")

    #sets up chromes browser instance that selenium will automate
    #you are already logged in to google accounts, if not then it will open a fresh blank browser
    chrome_options = Options()
    #here you need to enter the profile path of the profile you need to enter
    #you can see the profile path by writing chrome://version
    chrome_options.add_argument("--user-data-dir=C:/selenium_profiles/myprofile")
    chrome_options.add_argument("profile-directory=Profile 1")  # Exactly as
    # Use your chromedriver path
    #chromedriver acts as a bridge between selenium code and actual browser
    service = Service("C:/Users/spars/OneDrive/Desktop/Google Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")

    #starts the chrome browser with the desired profile
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()

    # time.sleep(1)  

    # Helper: Wait object
    wait = WebDriverWait(driver, 20)

    ## STEP 3: Opens Google Classroom and the respective assignemnt page
    # assignment_link = input("Paste your Google Classroom assignment link: ").strip()
    driver.get(assignment_link)

    #When the page is opened press ENTER
    input("Press ENTER after the page is opened...")

    ## STEP 4: Clicking 'Add or create' Button
    #waits for the add or create button to be clickable and then clicks it and handle errors if any
    try:
        #waits until a span button containing text "Add or create" is clickable
        #wait is a WebDriverWait object
        add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Add or create')]")))
        #js to scroll the page until add button is visible
        driver.execute_script("arguments[0].scrollIntoView(true);", add_button)
        #clicks on the button 
        driver.execute_script("arguments[0].click();",add_button)
        print("✅ Clicked 'Add or create'")
    #handle any errors
    except Exception as e:
        print("❌ Error clicking 'Add or create' button:", e)

    ## STEP 5:  Click 'File'
    #Locates and waits for the “File” upload option then scrolls to and checks if it’s visible then clicks it using JS and handles errors.
    try:
        # Now, use the new XPath to locate the file upload option from the list and wist until it is clickable 
        file_option = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[10]/div/ul/li[3]"))) 
        driver.execute_script("arguments[0].scrollIntoView(true);", file_option)  # Scroll into view

        # Debug: Check if the element is visible
        if file_option.is_displayed():
            print("✅ File upload button is visible, attempting click.")
        else:
            print("❌ File upload button is not visible")

        # JavaScript click
        driver.execute_script("arguments[0].click();", file_option)
        print("✅ Clicked 'File upload' button inside iframe")

    #handles errors if any
    except Exception as e:
        print("❌ Error clicking 'File' option inside iframe:", e)

    ## STEP 6: Upload file using input
    #First take the file path you need to upload as input from the user and then after normalizing it sending to the input field directly as this is how the UI basically works , when we click on the browse button it trigeers the input filed and uploads the file through that

    # --- Enter the file path ---
    files=[]
    # num=int(input("Enter no of files you want to enter: "))
    num=1
    for i in range(num):
        # file_path = input("Enter full path of the file to upload: ").strip()
        #converts windows \ to / so as to make it safe for selenium and strip('"') removes any surrounding quotes
        file_path = file_path.replace("\\", "/").strip('"')
        #check if the file path exists in teh os
        if not os.path.exists(file_path):
            print("❌ File does not exist. Please check the path:", file_path)
            exit()
        else:
            print("✅ File exists")
            files.append(file_path)

    #delay of 2 seconds giving the page time to process
    time.sleep(2)

    # --- Switch to iframe with input[type='file'] ---
    #looping through all iframes to find the iframe having element having input type="file" field
    #selenium can interact with an element in an iframe only if you explicityly switch to that iframe

    #finding all iframes
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    target_iframe = None
    #lopping through all iframes
    for iframe in iframes:
        try:
            #switching and seraching
            driver.switch_to.frame(iframe)
            file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
            target_iframe = iframe
            #if target iframe is found then break
            print("✅ Found the iframe containing file input.")
            break
        except:
            driver.switch_to.default_content()
    if target_iframe is None:
        raise Exception("❌ Could not find iframe with file input.")

    # --- Make input field visible ---
    #changing the styles of the input field to make it visible and interactable
    driver.execute_script("""
        arguments[0].style.display = 'block';
        arguments[0].style.visibility = 'visible';
        arguments[0].style.opacity = 1;
        arguments[0].style.height = 'auto';
        arguments[0].style.width = 'auto';
    """, file_input)

    # --- Upload the file --- 
    #This line simulates typing the file path into the file input field (<input type="file">).
    #It triggers the upload just as if you selected the file manually in the dialog box.

    # Join with \n and send to the file input
    file_input.send_keys("\n".join(files))


    # Switch back to main content
    driver.switch_to.default_content()

    ## STEP 7: Clicking on the turn in buttons after uploading the file confirming the submission
    try:
        # First "Turn in"
        #looks for span element with Turn in text and waits untill clickable
        turn_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Turn in')]")))
        #scrolls the bring the button to view and clicks it after a short delay  
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", turn_in_button)
        time.sleep(1.2)
        driver.execute_script("arguments[0].click();", turn_in_button)
        print("✅ Clicked first 'Turn in' button")
        #cliks the first turn in button and opens the confirmation modal

        # Wait for confirmation modal
        #role='dialog' ensures its a popup
        confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='dialog']//span[normalize-space()='Turn in']")))
        # Scroll and JS-click the second Turn In
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", confirm_button)
        time.sleep(1)  # Let animation settle
        driver.execute_script("arguments[0].click();", confirm_button)
        print("✅ Clicked confirm 'Turn in' via JS")
    except Exception as e:
        print("❌ Error during 'Turn in' process:", e)

    # Done
    print("🎯 All Done! You may close the browser manually.")
