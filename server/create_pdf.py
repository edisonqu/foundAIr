from fpdf import FPDF
from api_call import *

title = 'Business Plan'
company_name = "Edison's Dog Store"
author = "Edison Qu"
idea = "dog plushies"
budget = 3000

class PDF(FPDF):
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def title_page(self, company_name):
        self.add_page()
        self.set_font('Arial', "", 36)
        self.cell(0, 50, "Business Plan", 0, 1, 'C', False)
        self.set_font('Arial',"B", 48)
        self.cell(0, 50, f"{company_name}", 0, 1, 'C', False)
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
        self.cell(0, 18, "Business Overview..................................................................................4", 0, 1, '', False)
        self.cell(0, 18, "Market Analysis......................................................................................5", 0, 1, '', False)
        self.cell(0, 18, "Competitive Advantage..........................................................................6", 0, 1, '', False)
        self.cell(0, 18, "Sales & Market Strategy.........................................................................7", 0, 1, '', False)
        self.cell(0, 18, "Timeline...................................................................................................8", 0, 1, '', False)
        self.cell(0, 18, "Finance....................................................................................................9", 0, 1, '', False)
        self.cell(0, 18, "Key Metrics & Risk Reduction..............................................................10", 0, 1, '', False)
        self.cell(0, 18, "Conclusion..............................................................................................11", 0, 1, '', False)


    def body_page(self, title, output):
        self.add_page()
        self.set_font('Times', "B", 24)
        self.cell(0, 8, title, 0, 1, 'C', False)
        self.set_font('Times', "", 14)
        self.multi_cell(0, 5, output, 0, 1)

pdf = PDF(format="A4")
pdf.set_title(title)
pdf.set_author(author)
pdf.title_page(company_name)
pdf.table_of_contents()
pdf.set_font('Times',"",24)
topics = ["Business Overview","Market Analysis","Competitive Advantage","Sales & Market Strategy","Timeline","Finance","Key Metrics and Risk Deduction","Conclusion"]
pdf.body_page("Executive Summary", get_executive_summary(company_name, idea, budget))
for index_number in range(len(topics)):
    pdf.body_page(topics[index_number],call_api(company_name,idea,budget,topics[index_number]))
# pdf.print_chapter(1, 'A RUNAWAY REEF', '20k_  c1.txt')
# pdf.print_chapter(2, 'THE PROS AND CONS', '20k_c2.txt')
pdf.output('tuto3.pdf', 'F')