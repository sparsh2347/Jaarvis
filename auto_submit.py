# master_automation.py
from docx2pdf import convert
from assignment_download import download_assignment
from assignment_gen import generate_solution
from classroom import upload_solution
import subprocess
def main():
    assignment_link = input("Paste your Google Classroom assignment link: ").strip()
    print("\n🚀 STEP 1: Downloading assignment...")
    downloaded_pdf = download_assignment(assignment_link)  # Should return path like "assignment_question.pdf"
    
    if not downloaded_pdf:
        print("❌ Assignment download failed. Exiting...")
        return

    print("\n🧠 STEP 2: Generating solution using ChatGPT...")
    solution_doc = generate_solution(downloaded_pdf)  # Should return path like "solution_output.pdf"
    subprocess.Popen(['start', '', solution_doc], shell=True)
    input("📝 Press Enter after reviewing and saving your changes in Word...")

    solution_pdf = solution_doc.replace(".docx", ".pdf")
    convert(solution_doc, solution_pdf)
    print(f"📄 Converted DOCX to PDF: {solution_pdf}")

    if not solution_pdf:
        print("❌ Solution generation failed. Exiting...")
        return

    print("\n📤 STEP 3: Uploading solution to Google Classroom...")
    upload_solution(assignment_link,solution_pdf)

    print("\n✅ All Done! The solution is submitted successfully.")

if __name__ == "__main__":
    main()
