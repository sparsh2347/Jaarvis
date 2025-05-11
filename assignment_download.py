def download_assignment(assignment_link):
    #selenium imports from web automation
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    #used for adding delays, interacting with operating system, regex matching and file search
    import time, os
    import re
    import glob

    # STEP 1: Set download folder
    #use the path where the downloaded file will be saved eg Downloads
    download_dir = "C:/Users/spars/OneDrive/Desktop/Google Downloads"
    #forcefully closed any already runinig chrome.exe or chromedriver.exe processes to avoid conflicts such as anothe ropen session
    os.system("taskkill /f /im chrome.exe")
    os.system("taskkill /f /im chromedriver.exe")

    # STEP 2: Setup Chrome
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True
    })

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

    driver = webdriver.Chrome(service=service, options=chrome_options)
    wait = WebDriverWait(driver, 20)

    ## STEP 3: Opens Google Classroom and the respective assignemnt page
    # assignment_link = input("Paste your Google Classroom assignment link: ").strip()
    driver.get(assignment_link)

    # STEP 4: Click the PDF attachment
    try:
        # Look for any anchor with 'drive.google.com' and a 'pdf' in title/text
        pdf_link = wait.until(EC.presence_of_element_located((
            By.XPATH, "//a[contains(@href, 'drive.google.com') and (contains(@title, '.pdf') or contains(@aria-label, '.pdf'))]"
        )))
        #retreives teh url of teh pdf file 
        pdf_url = pdf_link.get_attribute("href")
        print("📄 Found PDF URL:", pdf_url)

    except Exception as e:
        print("❌ Failed to click PDF link:", e)
        driver.quit()
        exit()

    #extracting the file id from the url
    #captures everything that follows /d/ and stpos at next /
    match = re.search(r"/d/([^/]+)", pdf_url)
    if not match:
        raise ValueError("Could not extract file ID from URL")
    #first captured group
    file_id = match.group(1)

    # Direct download URL:
    download_url = f"https://drive.google.com/uc?export=download&id={file_id}"
    print("Direct download URL:", download_url)
    # Open the direct download link in a new tab which will automatically download the assignment qs poth
    driver.execute_script(f"window.open('{download_url}', '_blank');")
    print("✅ Download link opened in new tab. File should download automatically.")
    time.sleep(10)

    # Find the most recently downloaded PDF in the specified download folder
    list_of_files = glob.glob(os.path.join(download_dir, '*.pdf'))
    if not list_of_files:
        print("❌ No PDF found in download directory.")
        driver.quit()
        exit()
    latest_file = max(list_of_files, key=os.path.getctime)

    #Asking for the input file name from the user
    new_filename = "assignment_qs.pdf"
    new_filename = os.path.join(download_dir, new_filename)

    # Rename the file
    try:
        os.rename(latest_file, new_filename)
        print(f"✅ Renamed file to: {new_filename}")
    except Exception as e:
        print(f"❌ Failed to rename file: {e}")

    #returns the path to the downloaded file
    return new_filename
    
