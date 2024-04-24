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
            "Work Experience": [],
            "Education": [],
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

    def add_skill(self, skill_name, proficiency):
        skill = {
            "Skill Name": skill_name,
            "Proficiency": proficiency,
        }
        self.resume_data["Skills"].append(skill)
        print("Skill added successfully.")

    def generate_resume(self):
        doc = SimpleDocTemplate("resume.pdf", pagesize=letter)
        styles = getSampleStyleSheet()
        story = []

        # Add a title
        title_style = styles["Title"]
        story.append(Paragraph("Resume", title_style))
        story.append(Paragraph("", title_style))

        # Add personal information as a table
        personal_info = []
        for key, value in self.resume_data.items():
            personal_info.append([key, value])
        personal_info_table = Table(personal_info, colWidths=[3*inch, 3*inch])
        personal_info_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (0, -1), colors.lightgrey),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
        ]))
        story.append(personal_info_table)
        story.append(Paragraph("", styles["Normal"]))

        # Add work experience as a table
        work_experience = [["Work Experience"]]
        for exp in self.resume_data["Work Experience"]:
            work_experience.append([f"{exp['Position']} at {exp['Company']}"])
            work_experience.append([f"{exp['Start Date']} - {exp['End Date']}"])
            work_experience.append([f"Description: {exp['Description']}"])
        work_experience_table = Table(work_experience, colWidths=[6*inch])
        work_experience_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ]))
        story.append(work_experience_table)
        story.append(Paragraph("", styles["Normal"]))

        # Add education as a table
        education = [["Education"]]
        for edu in self.resume_data["Education"]:
            education.append([f"{edu['Degree']} at {edu['University']}"])
            education.append([f"{edu['Start Date']} - {edu['End Date']}"])
        education_table = Table(education, colWidths=[6*inch])
        education_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ]))
        story.append(education_table)
        story.append(Paragraph("", styles["Normal"]))

        # Add skills as a table
        skills = [["Skills"]]
        for skill in self.resume_data["Skills"]:
            skills.append([f"{skill['Skill Name']} - Proficiency: {skill['Proficiency']}"])
        skills_table = Table(skills, colWidths=[6*inch])
        skills_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ]))
        story.append(skills_table)

        # Build the PDF
        doc.build(story)

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
