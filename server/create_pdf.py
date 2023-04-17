from fpdf import FPDF
from api_call import *
from create_watermark import *


def create_pdf(title, company_name, author, idea, budget):
    class PDF(FPDF):
        def footer(self):
            # Position at 1.5 cm from bottom
            self.set_y(-15)
            # Arial italic 8
            self.set_font('Arial', 'I', 8)
            # Text color in gray
            self.set_text_color(255)
            # Page number
            self.cell(0, 10, 'Page ' + str(self.page_no()) + " Powered by foundair.tech", align='C')

        def title_page(self, company_name, author):
            self.add_page()
            self.set_font('Arial', "I", 32)
            self.set_text_color(0)
            self.cell(0, 50, "Business Plan", 0, 1, 'C', False)
            self.set_font('Arial', "B", 30)
            self.cell(0, 150, f"{company_name}", 0, 1, 'C', False)
            self.set_font('Arial', "", 24)
            self.cell(0, 20, 'Presented By:', 0, 1, 'C', False)
            self.cell(0, 20, f"{author}", 0, 1, 'C', False)
            self.set_font('Arial', "I", 10)
            self.cell(0, 25, "Powered by foundAIr", 0, 1, 'C', False)
            self.set_text_color(0, 0, 0)

        def table_of_contents(self):
            self.add_page()
            self.set_font("Arial", "B", 24)
            self.cell(0, 30, "Table Of Contents", 0, 1, align='C')
            self.set_font("Arial", "", 18)
            self.cell(0, 18,
                      "Executive Summary........................................................................3", 0,
                      1, '', False)
            self.cell(0, 18,
                      "Business Overview..........................................................................4", 0,
                      1, '', False)
            self.cell(0, 18,
                      "Market Analysis...............................................................................5",
                      0, 1, '', False)
            self.cell(0, 18,
                      "Competitive Advantage...................................................................6", 0, 1,
                      '', False)
            self.cell(0, 18,
                      "Sales & Market Strategy..................................................................7", 0,
                      1, '', False)
            self.cell(0, 18,
                      "Timeline...........................................................................................8",
                      0, 1, '', False)
            self.cell(0, 18,
                      "Finance............................................................................................9",
                      0, 1, '', False)
            self.cell(0, 18, "Key Metrics & Risk Reduction........................................................10",
                      0, 1, '', False)
            self.cell(0, 18,
                      "Conclusion......................................................................................11",
                      0, 1, '', False)

        def body_page(self, title, output):
            self.add_page()
            self.set_font('Arial', "B", 24)
            self.cell(0, 12, title, 0, 1, 'C', False)
            self.set_font('Arial', "", 14)
            fix_unicode = output.replace("’", "'")
            final_output = fix_unicode.replace("•", '- ')
            self.multi_cell(0, 5, final_output.replace("’", "'").replace("“","'").replace("–",'-'))

    pdf = PDF(format="A4")
    pdf.set_title(title)
    pdf.set_author(author)
    pdf.title_page(company_name, author)
    pdf.table_of_contents()
    pdf.set_font('Arial', "", 24)
    topics = ["Executive Summary", "Business Overview", "Market Analysis", "Competitive Advantage",
              "Sales & Market Strategy", "Timeline", "Finance", "Key Metrics and Risk Deduction", "Conclusion"]

    # Calls the function
    AI_answers = call_api(company_name, idea, budget)
    for index_number in range(len(topics)):
        try:
            print(AI_answers[index_number])
            # response.json()['choices'][0]['message']['content']
            pdf.body_page(topics[index_number], AI_answers[index_number]['choices'][0]['message']['content'])
        except Exception as err:
            print(f"An Error has occurred! {err}")
            print(AI_answers[index_number])
            pdf.body_page(topics[index_number], f"{err}")
    pdf.output('server/tmp/business_plan.pdf', 'F')
    watermark()
    return "Finished"

create_pdf(title="beef",company_name="beef it up",author="edison q.",idea="making beef from artificial chemicals",budget=50000)