from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.units import inch

class ResumeBuilder:
    def __init__(self):
        self.resume_data = {
            "Name": "",
            "Email": "",
            "Phone": "",
            "Address": "",
            "Summary": "",
            "Work Experience": [],  # Changed to a list of dictionaries
            "Education": [],  # Changed to a list of dictionaries
            "Skills": [],
        }

    def update_information(self, field, value):
        if field in self.resume_data:
            self.resume_data[field] = value
            print(f"Updated {field} successfully.")
        else:
            print("Invalid field name.")

    def add_work_experience(self, position, company, start_date, end_date, description):
        experience = {
            "Position": position,
            "Company": company,
            "Start Date": start_date,
            "End Date": end_date,
            "Description": description,
        }
        self.resume_data["Work Experience"].append(experience)
        print("Work experience added successfully.")

    def add_education(self, degree, university, start_date, end_date):
        education = {
            "Degree": degree,
            "University": university,
            "Start Date": start_date,
            "End Date": end_date,
        }
        self.resume_data["Education"].append(education)
        print("Education added successfully.")

    # ... Rest of the code remains the same ...

    def add_skill(self, skill_name, proficiency):
        skill = {
            "Skill Name": skill_name,
            "Proficiency": proficiency,
        }
        self.resume_data["Skills"].append(skill)
        print("Skill added successfully.")
    
    

    # ... Rest of the code remains the same ...

if __name__ == "__main__":
    builder = ResumeBuilder()

    # Ask user for resume data
    print("Please enter your resume data:")
    builder.update_information("Name", input("Name: "))
    builder.update_information("Email", input("Email: "))
    builder.update_information("Phone", input("Phone: "))
    builder.update_information("Address", input("Address: "))
    builder.update_information("Summary", input("Summary: "))

    while True:
        print("\nOptions:")
        print("1. Update information")
        print("2. Add work experience")
        print("3. Add education")
        print("4. Add skill")
        print("5. Generate resume")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            field_name = input("Enter the field name to update: ")
            field_value = input("Enter the new value: ")
            builder.update_information(field_name, field_value)
        elif choice == "2":
            position = input("Position: ")
            company = input("Company: ")
            start_date = input("Start Date: ")
            end_date = input("End Date: ")
            description = input("Description: ")
            builder.add_work_experience(position, company, start_date, end_date, description)
        elif choice == "3":
            degree = input("Degree: ")
            university = input("University: ")
            start_date = input("Start Date: ")
            end_date = input("End Date: ")
            builder.add_education(degree, university, start_date, end_date)
        elif choice == "4":
            skill_name = input("Skill Name: ")
            proficiency = input("Proficiency: ")
            builder.add_skill(skill_name, proficiency)
        elif choice == "5":
            builder.generate_resume()
            print("Resume generated successfully as 'resume.pdf'.")
        elif choice == "6":
            print("Exiting the Resume Builder.")
            break
        else:
            print("Invalid choice. Please try again.")
