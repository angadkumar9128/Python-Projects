from fpdf import FPDF
from PIL import Image
import os

class ResumeBuilder(FPDF):
    def __init__(self):
        super().__init__()
        self.WIDTH = 210
        self.HEIGHT = 297
        self.IMG_SIZE = (10, 10)

    def add_page(self):
        super().add_page()
        self.set_font('Arial', 'B', 16)

    def header(self):
        # Customize header (optional)
        pass

    def footer(self):
        # Customize footer (optional)
        pass

    def add_photo(self, img_path):
        if not os.path.exists(img_path):
            print("Invalid image file path. Please provide a valid path.")
            return

        try:
            img = Image.open(img_path)
            img = img.resize(self.IMG_SIZE)
            x_offset = (self.WIDTH - self.IMG_SIZE[0]) / 2
            y_offset = 20

            self.image(img_path, x_offset, y_offset, self.IMG_SIZE[0], self.IMG_SIZE[1])
        except Exception as e:
            print(f"Error while processing the image: {e}")

    def add_personal_info(self, name, email, phone, address):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, name, ln=True)
        self.set_font('Arial', '', 12)
        self.cell(0, 10, f"Email: {email}", ln=True)
        self.cell(0, 10, f"Phone: {phone}", ln=True)
        self.cell(0, 10, f"Address: {address}", ln=True)
        self.ln(20)

    def wrap_content(self, content, line_height, available_width):
        words = content.split()
        wrapped_content = ""
        current_line = ""

        for word in words:
            if self.get_string_width(current_line + word) <= available_width:
                current_line += word + " "
            else:
                wrapped_content += current_line + "\n"
                current_line = word + " "

        wrapped_content += current_line
        self.multi_cell(available_width, line_height, wrapped_content)

    def generate_data_table(self, data):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, data["title"], ln=True)
        self.set_font('Arial', '', 12)

        available_width = (self.WIDTH - (self.l_margin + self.r_margin)) / 2 - 10
        for key, value in data["entries"].items():
            self.cell(available_width, 10, key, ln=True)
            self.wrap_content(value, 8, available_width)
            self.ln(5)

    def generate_resume(self, filename):
        self.output(filename)


def validate_email(email):
    # Implement email validation logic here
    return True


if __name__ == "__main__":
    print("Welcome to the Online Resume Builder")

    # Get user input for personal information
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")

    # Validate email address
    while not validate_email(email):
        print("Invalid email address. Please enter a valid email.")
        email = input("Enter your email: ")

    # Get user input for image path
    img_path = input("Enter the path to your photo: ")

    # Validate image path
    while not os.path.exists(img_path):
        print("Invalid image file path. Please provide a valid path.")
        img_path = input("Enter the path to your photo: ")

    # Get user input for summary
    print("\nEnter a summary about yourself:")
    summary = input()
    summary = summary.strip()

    # Get user input for education details
    print("\nEnter your educational details:")
    education_data = {}
    while True:
        degree = input("Enter your degree: ")
        institution = input("Enter the institution: ")
        duration = input("Enter the duration: ")

        education_data[degree] = f"{institution}\n{duration}"

        another = input("Do you want to add another education entry? (yes/no): ")
        if another.lower() != 'yes':
            break

    # Get user input for experience details
    print("\nEnter your work experience:")
    experience_data = {}
    while True:
        title = input("Enter your job title: ")
        company = input("Enter the company: ")
        duration = input("Enter the duration: ")
        description = input("Enter the job description: ")

        experience_data[title] = f"{company}\n{duration}\n{description}"

        another = input("Do you want to add another experience entry? (yes/no): ")
        if another.lower() != 'yes':
            break

    # Get user input for skills
    print("\nEnter your skills (comma-separated):")
    skills_input = input()
    skills_data = [skill.strip() for skill in skills_input.split(',')]

    # Create an instance of the ResumeBuilder class
    resume_builder = ResumeBuilder()

    # Generate the resume PDF
    output_filename = "resume.pdf"
    resume_builder.add_page()
    resume_builder.add_photo(img_path)
    resume_builder.add_personal_info(name, email, phone, address)
    resume_builder.generate_data_table({"title": "Summary", "entries": {"Summary": summary}})
    resume_builder.generate_data_table({"title": "Education", "entries": education_data})
    resume_builder.generate_data_table({"title": "Experience", "entries": experience_data})
    resume_builder.generate_data_table({"title": "Skills", "entries": {"Skills": ", ".join(skills_data)}})

    resume_builder.generate_resume(output_filename)

    print("Professional resume generated successfully!")
