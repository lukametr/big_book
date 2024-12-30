from fpdf import FPDF

# Create PDF instance
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font and size for all sections
pdf.set_font('Arial', '', 12)

# Title (centered)
pdf.cell(200, 10, txt="Luka Metreveli", ln=True, align="C")

# Contact Information (centered)
pdf.ln(10)
pdf.cell(200, 10, txt="Email: lukametr@gmail.com", ln=True, align="C")
pdf.cell(200, 10, txt="Phone: +995 599 956 675", ln=True, align="C")
pdf.ln(10)

# Sections (using raw strings for clarity and newline preservation)
sections = {
    "Summary": r"""Highly motivated and results-oriented individual with a strong passion for software development. Eager to contribute to a dynamic team as a Junior Python Developer. 
    Possesses a solid foundation in Python programming acquired through independent study, online courses, and personal projects. Proficient in core Python concepts 
    and familiar with HTML, CSS, and JavaScript. Seeking a challenging role to gain practical experience and further develop coding skills.""",

    "Skills": r"""Programming Languages: Python
    Frontend Technologies: HTML, CSS, JavaScript (Basic)
    Version Control: Git (GitHub)
    IDEs: VS Code, Sublime Text, IDLE, PyCharm
    Other: English, Russian, Georgian""",

    "Education": r"""Python-Мастер. Полное руководство
    Platform/Institution: [Insert Platform Name, if applicable]
    Status: Ongoing/Completion Date: [Insert Date]""",

    "Projects": r"""1. [Project Name 1]
    Description: Briefly describe the project and its purpose. Highlight key skills and technologies used.

    2. [Project Name 2]
    Description: Briefly describe the project and its purpose. Highlight key skills and technologies used.""",

    "Books Read": r"""Python Crash Course, 2nd Edition - Eric Matthes
    Python Head First, 2nd Edition"""
}

# Add sections with justified alignment and spacing
pdf.ln(10)  # Additional spacing before sections
for section_name, section_text in sections.items():
    pdf.cell(200, 10, txt=section_name, ln=True)  # Add section title cell
    pdf.multi_cell(0, 10, txt=section_text, align='J')  # Use section_text directly (no encoding)
    pdf.ln(5)  # Spacing between sections



# Save PDF to file (specify UTF-8 encoding)
file_path = "Luka_Metreveli_CV.pdf"
pdf.output(file_path, 'UTF-8')

print(f"CV has been saved to {file_path}")