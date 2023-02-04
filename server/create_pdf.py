from fpdf import FPDF
from api_call import *

title = 'Business Plan'
company_name = "Edison's Dog Store"
author = "Edison Qu"
idea = "dog plushies"

class PDF(FPDF):
    # def header(self):
    #     # Arial bold 15
    #     self.set_font('Arial', 'B', 15)
    #     # Calculate width of title and position
    #     w = self.get_string_width(title) + 6
    #     self.set_x((210 - w) / 2)
    #     # Colors of frame, background and text
    #     self.set_draw_color(0, 80, 180)
    #     self.set_fill_color(230, 230, 0)
    #     self.set_text_color(220, 50, 50)
    #     # Thickness of frame (1 mm)
    #     self.set_line_width(1)
    #     # Title
    #     self.cell(w, 9, title, 1, 1, 'C', 1)
    #     # Line break
    #     self.ln(10)
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self, num, label):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, 'Chapter %d : %s' % (num, label), 0, 1, 'L', 1)
        # Line break
        self.ln(4)

    def chapter_body(self, name):
        # Read text file
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        # Times 12
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(0, 5, txt)
        # Line break
        self.ln()
        # Mention in italics
        self.set_font('', 'I')
        self.cell(0, 5, '(end of excerpt)')

    def print_chapter(self, num, title, name):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(name)

    def title_page(self, company_name):
        self.add_page()
        self.set_font('Arial', "", 36)
        self.cell(0, 50, "Business Plan", 0, 1, 'C', False)
        self.set_font('Arial',"B", 48)
        self.cell(0, 50, "Edison's Dog Store", 0, 1, 'C', False)
        self.set_font('Arial',"", 24)
        self.cell(0,50,'Presented By:',0,1)
        self.cell(0,0,"Edison Qu",0,1)

    def body_page(self, title, output):
        self.add_page()
        self.set_font('Times', "B", 24)
        self.cell(0, 8, title, 0, 1, 'L', False)
        self.set_font('Times', "", 11)
        self.multi_cell(0, 5, output, 0, 1)

pdf = PDF(format="A4")
pdf.set_title(title)
pdf.set_author(author)
pdf.title_page(company_name)
pdf.body_page("Executive Summary", get_executive_summary(company_name, idea, 3000))
# pdf.print_chapter(1, 'A RUNAWAY REEF', '20k_  c1.txt')
# pdf.print_chapter(2, 'THE PROS AND CONS', '20k_c2.txt')
pdf.output('tuto3.pdf', 'F')