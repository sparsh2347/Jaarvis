# master_automation.py
from tkinter import messagebox
#a gui interface to show system messages
#used to convert final word to pdf
from docx2pdf import convert
#importing the cutsom modules required to automate the task
from assignment_download import download_assignment
from assignment_gen import generate_solution
from classroom import upload_solution
#used to open the solution file for editing
import subprocess
def main():
    # master_script.py
    with open("user_input.txt", "r", encoding="utf-8") as f:
        assignment_link = f.readline().strip()
        custom_prompt = f.readline().strip()
        sol_file_name=f.readline().strip()

    # Step 1: Ask user for Google Classroom assignment link
    print("\n🚀 STEP 1: Downloading assignment...")
    # Download the assignment file from the link
    downloaded_pdf = download_assignment(assignment_link) 
    # Should return path like "assignment_question.pdf"
    if not downloaded_pdf:
        print("❌ Assignment download failed. Exiting...")
        return

    #STEP 2: Generate solution for the downloaded assignment using ChatGPT
    print("\n🧠 STEP 2: Generating solution using ChatGPT...")
    solution_doc = generate_solution(downloaded_pdf,custom_prompt,sol_file_name)  # Should return path like "solution_output.pdf"
    # Automatically open the generated Word document for user to review/edit
    subprocess.Popen(['start', '', solution_doc], shell=True)
    #When the word doc is reviewed press OK
    messagebox.showinfo("Word Doc Opened", "Press OK after reviewing and saving your changes in Word...")

    # Convert the final DOCX file into PDF format
    solution_pdf = solution_doc.replace(".docx", ".pdf")
    convert(solution_doc, solution_pdf)
    print(f"📄 Converted DOCX to PDF: {solution_pdf}")

    if not solution_pdf:
        print("❌ Solution generation failed. Exiting...")
        return

    # Upload the solution PDF back to the Google Classroom assignment
    print("\n📤 STEP 3: Uploading solution to Google Classroom...")
    upload_solution(assignment_link,solution_pdf)

    print("\n✅ All Done! The solution is submitted successfully.")

#script execution
if __name__ == "__main__":
    main()
