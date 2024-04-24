from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from PIL import Image as PILImage
import io

def resize_image(img_path, target_size):
    # Load the image using PIL
    img = PILImage.open(img_path)

    # Resize the image while preserving the aspect ratio
    # img.thumbnail(target_size, PILImage.ANTIALIAS)
    img = img.resize(target_size, PILImage.LANCZOS)

    # Return the resized image
    return img

def format_input(key, value, bullet="-"):
    return f"<b>{key}:</b> {bullet} {value}"

def create_resume(output_path):
    # Get image size from the user
    img_width = int(input("Enter the image width (in pixels): "))
    img_height = int(input("Enter the image height (in pixels): "))
    img_size = (img_width, img_height)

    # Resize user image and attach it to the PDF header
    while True:
        try:
            img_path = input("Enter the path to your image: ")
            img = resize_image(img_path, target_size=img_size)
            break
        except FileNotFoundError:
            print("Error: Image file not found. Please provide a valid image path.")

    # Get user contact details
    contact_details = [
        ('Name', input("Enter your name: ")),
        ('Email', input("Enter your email: ")),
        ('Phone', input("Enter your phone number: ")),
        ('Father\'s Name', input("Enter your father's name: ")),
        ('Mother\'s Name', input("Enter your mother's name: ")),
        ('Alternate Mobile', input("Enter your alternate mobile number: ")),
        ('Village', input("Enter your village: ")),
        ('District', input("Enter your district: ")),
        ('Pincode', input("Enter your pincode: ")),
        ('State', input("Enter your state: ")),
        ('Language', input("Enter your language: "))
    ]

    # Create a PDF document
    doc = SimpleDocTemplate(output_path, pagesize=letter)
    flowables = []

    # Create a style for the resume content
    normal_style = getSampleStyleSheet()['Normal']

    # Create a table to hold the image and contact details side by side
    contact_data = [[Paragraph(format_input(key, value, bullet="-"), normal_style)] for key, value in contact_details]
    table_data = [
        [Image(img_path, width=img_width, height=img_height), Spacer(1, 60,260), Table(contact_data, colWidths=[400])]
    ]
    table = Table(table_data, colWidths=[img_width, 60,260, 400])
    table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0, (1, 1, 1)),  # Add grid lines
    ]))

    flowables.append(table)

    # Add the summary to the PDF
    summary = input("Enter your summary: ")
    flowables.append(Spacer(1, 12))  # Add space between summary and other details
    flowables.append(Paragraph("<b>Summary:</b>", normal_style))
    flowables.append(Paragraph(f"- {summary}", normal_style))

    # Educational Details
    flowables.append(Spacer(1, 12))  # Add space between summary and educational details
    flowables.append(Paragraph("<b>Educational Details:</b>", normal_style))
    while True:
        degree = input("Enter your degree: ")
        university = input("Enter the university: ")
        start_date_edu = input("Enter the start date (education): ")
        end_date_edu = input("Enter the end date (education): ")
        edu_details = format_input(degree, f"{university}, {start_date_edu} to {end_date_edu}", bullet=".")
        flowables.append(Paragraph(f"- {edu_details}", normal_style))

        more_edu_details = input("Do you have more educational details? (yes/no): ").lower()
        if more_edu_details != 'yes':
            break

    # Experience
    flowables.append(Spacer(1, 12))  # Add space between educational details and experience
    flowables.append(Paragraph("<b>Experience:</b>", normal_style))
    while True:
        company = input("Enter the company name: ")
        position = input("Enter your position: ")
        start_date_exp = input("Enter the start date (experience): ")
        end_date_exp = input("Enter the end date (experience): ")
        experience_desc = input("Enter the experience description: ")

        flowables.append(Paragraph(f"- <b>{company}, {position}</b>", normal_style))
        exp_details = format_input("Duration", f"{start_date_exp} to {end_date_exp}", bullet=".")
        flowables.append(Paragraph(f"- {exp_details}", normal_style))
        flowables.append(Paragraph(experience_desc, normal_style))

        more_exp_details = input("Do you have more experience details? (yes/no): ").lower()
        if more_exp_details != 'yes':
            break

    # Achievements
    flowables.append(Spacer(1, 12))  # Add space between experience and achievements
    flowables.append(Paragraph("<b>Achievements:</b>", normal_style))
    while True:
        achievement_title = input("Enter the achievement title: ")
        start_date_ach = input("Enter the start date (achievement): ")
        end_date_ach = input("Enter the end date (achievement): ")
        achievement_desc = input("Enter the achievement description: ")

        flowables.append(Paragraph(f"- <b>{achievement_title}</b>", normal_style))
        achievement_details = format_input("Duration", f"{start_date_ach} to {end_date_ach}", bullet=".")
        flowables.append(Paragraph(f"- {achievement_details}", normal_style))
        flowables.append(Paragraph(achievement_desc, normal_style))

        more_achievements = input("Do you have more achievements? (yes/no): ").lower()
        if more_achievements != 'yes':
            break

    # Interests
    flowables.append(Spacer(1, 12))  # Add space between achievements and interests
    flowables.append(Paragraph("<b>Interests:</b>", normal_style))
    while True:
        interest = input("Enter your interest: ")
        flowables.append(Paragraph(f"- {interest}", normal_style))

        more_interests = input("Do you have more interests? (yes/no): ").lower()
        if more_interests != 'yes':
            break

    # Skills
    flowables.append(Spacer(1, 12))  # Add space between interests and skills
    flowables.append(Paragraph("<b>Skills:</b>", normal_style))
    while True:
        skill = input("Enter your skill: ")
        flowables.append(Paragraph(f"- {skill}", normal_style))

        more_skills = input("Do you have more skills? (yes/no): ").lower()
        if more_skills != 'yes':
            break

    # Projects
    flowables.append(Spacer(1, 12))  # Add space between skills and projects
    flowables.append(Paragraph("<b>Projects:</b>", normal_style))
    while True:
        project_title = input("Enter the project title: ")
        start_date_proj = input("Enter the start date (project): ")
        end_date_proj = input("Enter the end date (project): ")
        project_desc = input("Enter the project description: ")

        flowables.append(Paragraph(f"- <b>{project_title}</b>", normal_style))
        proj_details = format_input("Duration", f"{start_date_proj} to {end_date_proj}", bullet=".")
        flowables.append(Paragraph(f"- {proj_details}", normal_style))
        flowables.append(Paragraph(project_desc, normal_style))

        more_projects = input("Do you have more projects? (yes/no): ").lower()
        if more_projects != 'yes':
            break

    # Build the PDF
    doc.build(flowables)

if __name__ == "__main__":
    output_path = "resume.pdf"  # Output PDF file path (you can change this)
    create_resume(output_path)
    print("Resume generated successfully as 'resume.pdf'.")
