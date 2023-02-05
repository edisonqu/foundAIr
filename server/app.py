from flask import Flask
from create_pdf import *
from pin_to_ipfs import *

app = Flask(__name__)  # notice that the app instance is called `app`, this is very important.

@app.route("/create")
def plan():
    title = 'Business Plan'
    company_name = "Stephen's Light Bulb Store"
    author = "Edison Qu"
    idea = "light bulb retailer"
    budget = 3000
    create_pdf(title,company_name,author,idea,budget)
    return pinToIPFS("tmp/business_plan.pdf")