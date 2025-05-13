# ⚠️ Disclaimer:
This tool uses AI to assist in drafting assignment solutions. Please use it responsibly, review all content thoroughly, and comply with your institution’s academic integrity policies.

---

# 📚 Jaarvis - Automated Assignment Submission Assistant

**Jaarvis** is a Python-based automation tool designed to streamline the entire assignment handling process on Google Classroom. It helps you download assignments, generate draft solutions using GPT, edit them in DOCX format, and finally convert and submit the solution PDF — all automatically.

**Note:** This tool is designed to assist in the process, but **always review AI-generated solutions** before submission to ensure accuracy and originality.

---

## 🆕 Recent Updates

- **New**: A user-friendly GUI has been added to the project using **Tkinter**.
- **New**: Now creates an additional PDF which contains the explanation to the response provided by GPT for better understanding and clarity.
- **New**: `classroom.py` now opens the Chrome browser in a half-screen window instead of maximized to avoid UI element click issues.
- Font Requirement: To ensure proper rendering of Unicode characters in the generated PDFs, the script uses the DejaVuSans.ttf font.
  
   📁 Place the `DejaVuSans.ttf` file in the same directory as assignment_gen.py.<br>
   🔗 You can download the font from the official repository:<br>
   https://github.com/dejavu-fonts/dejavu-fonts/blob/master/ttf/DejaVuSans.ttf
- Replace the font path with your font path manually in `assignment_gen.py`
- Example:
  ```python 
   font_path = "C:/Users/spars/OneDrive/Desktop/Python Projects/Jaarvis/DejaVuSans.ttf"
  ```
- Note: Ensure that the window opened by `classsroom.py` stays in a half-screen window to avoid any errors.


## 🚀 Features

- 📥 **Auto-downloads Assignment PDFs** from Google Classroom
- 🤖 **Draft Solution Generation** via ChatGPT API
- 📝 **Editable DOCX File Creation** for user customization
- 📄 **Auto PDF Conversion** after user edits
- 📤 **One-click Assignment Submission** to Classroom
- 🧠 **Ethical Use Reminder**: GPT usage is disclosed with a disclaimer in the PDF

 ## 🖥️ GUI Interface (New)

- It allows the user to:
  - ✅ Enter the **Google Classroom assignment link**
  - ✅ Provide an optional **prompt** for the assignment response
  - ✅ Enter the **Solution File Name**
- Two interactive message prompts are used to **pause the flow** (like `Press ENTER`) so users can:
  - 👀 Read the explanation PDF
  - 📄 Review the draft solution before submission

 📂 **To launch the GUI**, run:

> ```bash
> python gui.py
> ```

### 📸 GUI Preview

![image](https://github.com/user-attachments/assets/86ec1b45-2ff3-4fb2-a33c-e301bbafc99c)

📌 **Note**: The GUI internally triggers the full pipeline (`auto_submit.py`) — make sure all scripts are functional.

---

## 🔁 Workflow

1. **Download Assignment**  
   `assignment_download.py` scrapes the assignment question PDF from Classroom.

2. **Generate Solution**  
   `assignment_gen.py` sends the question text to GPT and generates a DOCX draft.

3. **User Edits**  
   DOCX is opened for manual editing by the user in MS Word or LibreOffice.

4. **Auto-Save and Convert**  
   After editing, the DOCX is automatically saved and converted to PDF.

5. **Submit Assignment**  
   `classroom.py` uploads the final PDF directly to the correct assignment submission portal.

6. **Automation Script**  
   `auto_submit.py` combines all the above steps into one seamless script.

---

## 🛠️ Setup Instructions

### 1. **Clone the Repository**
```bash
git clone https://github.com/sparsh2347/jaarvis.git
cd jaarvis
```

### 2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

**Required Libraries**:
- `selenium`
- `pyautogui`
- `python-docx`
- `docx2pdf`
- `Pypdf2`
- `fpdf`
- `docx2pdf`

### 3. **ChromeDriver Setup**
- Ensure that Google Chrome is installed on your system.
- Download the appropriate version of [ChromeDriver](https://chromedriver.chromium.org/downloads) that is compatible with your installed version of Google Chrome.
  (Recommended version: 136.7103.0.93)
- Place the `chromedriver` executable either in your system's PATH or within your project directory.
- Update the `chrome_driver` path in each of the Selenium scripts accordingly:
  ```python
  service = Service("C:/Users/spars/OneDrive/Desktop/Google Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")

### 4. **Configure Google Classroom Profile**

To automate Google Classroom interactions using Selenium, use an existing Chrome user profile where you're already logged in to Google. This will ensure that the script can access your Google Classroom and ChatGPT without requiring additional authentication steps.

#### Steps:
1. **Use an existing Chrome user profile** with Google login already authenticated. This allows the automation script to interact with Google Classroom without requiring you to log in every time.

2. **Update the profile path** in the Selenium script:
   In the script, find the line where the `options.add_argument` method is used, and provide the path to your Chrome user profile. It should look something like this:
   ```python
   options.add_argument("user-data-dir=path/to/your/chrome/profile")
   options.add_argument("profile-directory=profile_name") 
   ```
3. **Find the Chrome Profile Path**

   To locate the path of your Chrome user profile, follow these steps:
   1. Open Chrome and type the following URL in the address bar:
      ```html
      chrome://version/
      ```
   2.On the resulting page, look for the "Profile Path" entry. This will show the location of       your Chrome profile on your system.

   Example profile path:
      ```profile_path
      C:\Users\YourUser\AppData\Local\Google\Chrome\User Data
      ```


## 🧪 Example Usage

Run the all-in-one automation script:
```bash
python auto_submit.py
```

This will:
- Extract the assignment
- Get GPT draft
- Let you edit
- Convert to PDF
- Submit it

---

## ✅ Ethically Responsible AI Usage


The solution genreated is just a draft solution generated by AI.Please always review and edit GPT-generated content before finalizing.

---

## 📁 Project Structure

```plaintext
jaarvis/
│
├── assignment_download.py    # Downloads assignment PDF
├── assignment_gen.py         # Generates draft solution with GPT
├── auto_submit.py            # Links all components for end-to-end automation
├── classroom.py              # Handles submission to Google Classroom
├── gui.py                    # GUI interface for non technical users
├── DejaVuSans.ttf/.pkl/.ttc  # Fonts and model files used for formatting
├── README.md                 # This file
```

---

## 📌 Future Enhancements

- Add GUI for non-technical users
- Add email notifications on submission
- Enable multi-assignment batch processing

---

## 🧑‍💻 Author

**Sparsh Sinha** – BTech CSE, IIIT Lucknow  
Feel free to contribute, raise issues, or suggest features!

---
