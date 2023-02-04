from fpdf import FPDF

title = 'Business Plan'

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

    def table_of_contents(self):

        self.add_page()
        self.set_font("Times","B",24)
        self.cell(0,30,"Table Of Contents",0,1,'C',False)
        self.set_font("Times","",18)
        # topics = ["Executive Summary","Business Overview","Market Analysis","Competitive Advantage","Sales & Market Strategy","Finance","Risk Deduction","Conclusion"]
        #
        # for index in range(len(topics)):
        #     character_number = len(topics[index])
        #     number_of_periods = 90-character_number-1
        #     periods = '.'*number_of_periods
        #     self.cell(0, 18, topics[index]+periods+str(index), 0, 1, '', False)
        self.cell(0, 18, "Executive Summary................................................................................3", 0, 1, '', False)
        self.cell(0, 18, "Business Overview............ .....................................................................4", 0, 1, '', False)
        self.cell(0, 18, "Market Analysis......................................................................................5", 0, 1, '', False)
        self.cell(0, 18, "Competitive Advantage..........................................................................6", 0, 1, '', False)
        self.cell(0, 18, "Sales & Market Strategy.........................................................................7", 0, 1, '', False)
        self.cell(0, 18, "Timeline...................................................................................................8", 0, 1, '', False)
        self.cell(0, 18, "Finance....................................................................................................9", 0, 1, '', False)
        self.cell(0, 18, "Risk Deduction.......................................................................................10", 0, 1, '', False)
        self.cell(0, 18, "Conclusion..............................................................................................11", 0, 1, '', False)


    def body_page(self):

        return

pdf = PDF(format="A4")
pdf.set_title(title)
pdf.set_author('Edison Qu')
pdf.title_page(company_name=3)
pdf.table_of_contents()
# pdf.print_chapter(1, 'A RUNAWAY REEF', '20k_  c1.txt')
# pdf.print_chapter(2, 'THE PROS AND CONS', '20k_c2.txt')
pdf.output('tuto3.pdf', 'F')