#Import necessary libraries
import json
from fpdf import FPDF
import os
import requests
from api_call import *

#Algorithm for generating business plan
def lambda_handler(event, context):
    #Defines constant variables, including user input
    query = event['queryStringParameters']
    title = 'Business Plan'
    company_name = query['company_name']
    author = query['author']
    idea = query['idea']
    budget = query['budget']
    print(event)
    #Creates PDF and defines base parameters
    class PDF(FPDF):
        #Creates footer
        def footer(self):
            # Position at 1.5 cm from bottom
            self.set_y(-15)
            # Arial italic 8
            self.set_font('Arial', 'I', 8)
            # Text color in gray
            self.set_text_color(128)
            # Page number
            self.cell(0, 10, 'Page ' + str(self.page_no()) + " Powered by foundAIr", 0, 0, 'C')
        #Creates title page
        def title_page(self, company_name, author):
            self.add_page()
            self.set_font('Arial', "I", 32)
            self.set_text_color(255, 255, 255)
            self.cell(0, 50, "Business Plan", 0, 1, 'C', True)
            self.set_font('Arial', "B", 30)
            self.cell(0, 150, f"{company_name}", 0, 1, 'C', True)
            self.set_font('Arial', "", 24)
            self.cell(0, 20, 'Presented By:', 0, 1, 'C', True)
            self.cell(0, 20, f"{author}", 0, 1, 'C', True)
            #self.set_font('Arial', "I", 10)
            #self.cell(0, 25, "Powered by foundAIr", 0, 1, 'C', True)
            #self.set_text_color(0, 0, 0)
        #Creates table of contents
        def table_of_contents(self):
            self.add_page()
            self.set_font("Arial", "B", 24)
            self.cell(0, 30, "Table Of Contents", 0, 1, 'C', False)
            self.set_font("Arial", "", 18)
            # topics = ["Executive Summary","Business Overview","Market Analysis","Competitive Advantage","Sales & Market Strategy","Finance","Risk Deduction","Conclusion"]
            #
            # for index in range(len(topics)):
            #     character_number = len(topics[index])
            #     number_of_periods = 90-character_number-1
            #     periods = '.'*number_of_periods
            #     self.cell(0, 18, topics[index]+periods+str(index), 0, 1, '', False)
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
        #Base template for body pages
        def body_page(self, title, output):
            self.add_page()
            self.set_font('Arial', "B", 24)
            self.cell(0, 12, title, 0, 1, 'C', False)
            self.set_font('Arial', "", 14)
            fix_unicode = output.replace("’", "'")
            final_output = fix_unicode.replace("•", '- ')
            self.multi_cell(0, 5, output.replace("’", "'"))
    #Sets constant variables to page values
    pdf = PDF(format="A4")
    pdf.set_title(title)
    pdf.set_author(author)
    pdf.title_page(company_name, author)
    pdf.table_of_contents()
    pdf.set_font('Arial', "", 24)
    #Defines sections of PDF business plan
    topics = ["Executive Summary", "Business Overview", "Market Analysis", "Competitive Advantage",
              "Sales & Market Strategy", "Timeline", "Finance", "Key Metrics and Risk Deduction", "Conclusion"]

    # Removed support for an actual summary

    #Generated body pages
    AI_answers = call_api(company_name, idea, budget)
    for index_number in range(len(topics)):
        pdf.body_page(topics[index_number], AI_answers[index_number]['choices'][0]['message']['content'])
    #PDF is stored a byte
    byte = pdf.output()
    #Defines IPFS specifics
    url = "https://api.nft.storage/upload"
    headers = {
        "Content-Type": "*/*",
        "accept": "application/json",
        "Authorization": f"Bearer {os.getenv('YOUR_STORAGE_API_KEY')}"
    }

    # with open("tmp/business_plan.pdf", 'rb') as f:
    #     file = f.read()

    #Stored to be returned to user, leverages IPFS (Interplanetary File Sharing System)
    response = requests.request("POST", url, headers=headers, data=byte)

    res = response.json()

    print(res)
    #Returns CID for retrieval of PDF of front end
    return {
        'statusCode': 200,
        'body': res['value']['cid']
    }
