from flask import Flask
from create_pdf import *

app = Flask(__name__)  # notice that the app instance is called `app`, this is very important.

@app.route("/")
def hello():
    return "hi"
@app.route("/create")
def plan():
    title = 'Business Plan'
    company_name = "Stephen's Light Bulb Store"
    author = "Edison Qu"
    idea = "light bulb retailer"
    budget = 3000
    bytes = create_pdf(title, company_name, author, idea, budget)
    with open("business_plan.pdf", "wb") as binary_file:
        # Write bytes to file
        binary_file.write(bytes)
    return 'hi'
    # return pinToIPFS("tmp/business_plan.pdf")
