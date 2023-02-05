from fpdf import FPDF
from api_call import *

title = 'Business Plan'
company_name = "Edison's Dog Store"
author = "Edison Qu"
idea = "dog plushies"
budget = 3000
# prompts = [f"the business name is {company_name}. i am writing a business plan. business idea: {idea}. minimum 600 words. describe the problem faced by people without my business idea, the pain points my business idea targets, and explain my idea. no headings, no jot notes.", f"the business name is {company_name}. i am writing a business plan. business idea: {idea}. minimum 500 words. write me a market analysis, explaining the target market, the customer segments, explain how the consumers will take advantage of this, and explain the competition from other business i will face. no headings and no jot notes.", f"the business name is {company_name}. i am writing a business plan. business idea: {idea}. minimum 500 words. write me the unique value proposition of my idea and the competitive advantage of my idea. no headings and no jot notes.", f"the business name is {company_name}. i am writing a business plan. business idea: {idea}. minimum 550 words. explain the marketing channels i can take advantage of to promote my idea and interact with my consumers, both online and in person. explain how i can sell my idea in person and online. no headings and no jot notes.", f"the business name is {company_name}. i am writing a business plan. write a timeline to launch my business with numbers. minimum 500 words. business idea: {idea}. no headings and no jot notes.", f"the business name is {company_name}.i am writing a business plan. business idea: {idea}. my budget is only {budget}. give me a budget for my business and include descriptions for each cost. include numbers and jot form.", f"the business name is {company_name}. i am writing a business plan. business idea: {idea}. minimum 500 words. explain the key metrics with specific numbers in jot form. describe methods to reduce risk. explain how we will reassess and reevaluate our progress. no headings.", f"summarize the following text in 150 words. {summary}"]

def create_pdf(title,company_name,author,idea,budget):
    class PDF(FPDF):
        def footer(self):
            # Position at 1.5 cm from bottom
            self.set_y(-15)
            # Arial italic 8

            self.set_font('Arial', 'I', 8)
            # Text color in gray
            self.set_text_color(128)
            # Page number
            self.cell(0, 10, 'Page ' + str(self.page_no()) + " Powered by foundAIr",align='C')

        def title_page(self, company_name,author):
            self.add_page()
            self.set_font('Arial', "I", 32)
            self.set_text_color(255, 255, 255)
            self.cell(0, 50, "Business Plan", 0, 1, 'C', True)
            self.set_font('Arial', "B", 30)
            self.cell(0, 150, f"{company_name}", 0, 1, 'C', True)
            self.set_font('Arial', "", 24)
            self.cell(0, 20, 'Presented By:', 0, 1, 'C', True)
            self.cell(0, 20, f"{author}", 0, 1, 'C', True)
            self.set_font('Arial', "I", 10)
            self.cell(0, 25, "Powered by foundAIr", 0, 1, 'C', True)
            self.set_text_color(0, 0, 0)

        def table_of_contents(self):

            self.add_page()
            self.set_font("Arial","B",24)
            self.cell(0,30,"Table Of Contents",0,1,align='C')
            self.set_font("Arial","",18)
            # topics = ["Executive Summary","Business Overview","Market Analysis","Competitive Advantage","Sales & Market Strategy","Finance","Risk Deduction","Conclusion"]
            #
            # for index in range(len(topics)):
            #     character_number = len(topics[index])
            #     number_of_periods = 90-character_number-1
            #     periods = '.'*number_of_periods
            #     self.cell(0, 18, topics[index]+periods+str(index), 0, 1, '', False)
            self.cell(0, 18, "Executive Summary........................................................................3", 0, 1, '', False)
            self.cell(0, 18, "Business Overview..........................................................................4", 0, 1, '', False)
            self.cell(0, 18, "Market Analysis...............................................................................5", 0, 1, '', False)
            self.cell(0, 18, "Competitive Advantage...................................................................6", 0, 1, '', False)
            self.cell(0, 18, "Sales & Market Strategy..................................................................7", 0, 1, '', False)
            self.cell(0, 18, "Timeline...........................................................................................8", 0, 1, '', False)
            self.cell(0, 18, "Finance............................................................................................9", 0, 1, '', False)
            self.cell(0, 18, "Key Metrics & Risk Reduction........................................................10", 0, 1, '', False)
            self.cell(0, 18, "Conclusion......................................................................................11", 0, 1, '', False)


        def body_page(self, title, output):
            self.add_page()
            self.set_font('Arial', "B", 24)
            self.cell(0, 12, title, 0, 1, 'C', False)
            self.set_font('Arial', "", 14)
            self.multi_cell(0, 5, output.replace("’","'"))

    pdf = PDF(format="A4")
    pdf.set_title(title)
    pdf.set_author(author)
    pdf.title_page(company_name,author)
    pdf.table_of_contents()
    pdf.set_font('Arial',"",24)
    # topics = ["Business Overview","Market Analysis","Competitive Advantage","Sales & Market Strategy","Timeline","Finance","Key Metrics and Risk Deduction","Conclusion"]
    # summary = get_executive_summary(company_name,idea,budget)
    # pdf.body_page("Executive Summary",summary)
    # prompts = [f"the business name is {company_name}. i am writing a business plan. business idea: {idea}. minimum 600 words. describe the problem faced by people without my business idea, the pain points my business idea targets, and explain my idea. no headings, no jot notes.", f"the business name is {company_name}. i am writing a business plan. business idea: {idea}. minimum 500 words. write me a market analysis, explaining the target market, the customer segments, explain how the consumers will take advantage of this, and explain the competition from other business i will face. no headings and no jot notes.", f"the business name is {company_name}. i am writing a business plan. business idea: {idea}. minimum 500 words. write me the unique value proposition of my idea and the competitive advantage of my idea. no headings and no jot notes.", f"the business name is {company_name}. i am writing a business plan. business idea: {idea}. minimum 550 words. explain the marketing channels i can take advantage of to promote my idea and interact with my consumers, both online and in person. explain how i can sell my idea in person and online. no headings and no jot notes.", f"the business name is {company_name}. i am writing a business plan. write a timeline to launch my business with numbers. minimum 500 words. business idea: {idea}. no headings and no jot notes.", f"the business name is {company_name}.i am writing a business plan. business idea: {idea}. my budget is only {budget}. give me a budget for my business and include descriptions for each cost. include numbers and jot form.", f"the business name is {company_name}. i am writing a business plan. business idea: {idea}. minimum 500 words. explain the key metrics with specific numbers in jot form. describe methods to reduce risk. explain how we will reassess and reevaluate our progress. no headings.", f"summarize the following text in 150 words. Make it a conclusion for a business plan. {summary}"]
    # #
    # summaries = ''
    # for index_number in range(len(topics)):
    #     if "summarize the following text in 150 words" in prompts[index_number]:
    #         print('used')
    #         pdf.body_page(topics[index_number],call_api(prompts[index_number],summary))
    #     else:
    #         pdf.body_page(topics[index_number], call_api(prompts[index_number], summaries))
    pdf.output('tmp/business_plan.pdf', 'F')
    return "solid"


title = 'Business Plan'
company_name = "SmartChan's Edison"
author = "Edison Qu"
idea = "Cannabis Shop that sells shoes"
budget = 3000
print(create_pdf(title, company_name, author, idea, budget))