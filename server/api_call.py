import dotenv

dotenv.load_dotenv()

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

summary = ""

bname =''
idea = ''
budget =0
prompts = [
  f"the business name is {bname}. i am writing a business plan. business idea: {idea}. minimum 600 words. describe the problem faced by people without my business idea, the pain points my business idea targets, and explain my idea. no headings, no jot notes.",
  f"the business name is {bname}. i am writing a business plan. business idea: {idea}. minimum 500 words. write me a market analysis, explaining the target market, the customer segments, explain how the consumers will take advantage of this, and explain the competition from other business i will face. no headings and no jot notes.",
  f"the business name is {bname}. i am writing a business plan. business idea: {idea}. minimum 500 words. write me the unique value proposition of my idea and the competitive advantage of my idea. no headings and no jot notes.",
  f"the business name is {bname}. i am writing a business plan. business idea: {idea}. minimum 550 words. explain the marketing channels i can take advantage of to promote my idea and interact with my consumers, both online and in person. explain how i can sell my idea in person and online. no headings and no jot notes.",
  f"the business name is {bname}. i am writing a business plan. write a timeline to launch my business with numbers. minimum 500 words. business idea: {idea}. no headings and no jot notes.",
  f"the business name is {bname}.i am writing a business plan. business idea: {idea}. my budget is only {budget}. give me a budget for my business and include descriptions for each cost. include numbers and jot form.",
  f"the business name is {bname}. i am writing a business plan. business idea: {idea}. minimum 500 words. explain the key metrics with specific numbers in jot form. describe methods to reduce risk. explain how we will reassess and reevaluate our progress. no headings.",
  f"summarize the following text in 150 words."]

def call_api(prompts):

  print(prompts)
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompts + f" {summary}",
    temperature=0.1,
    max_tokens=3500,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  return response["choices"][0]['text']

def get_executive_summary(bname, idea, budget):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"the business name is {bname}. i am writing a business plan. write an executive summary for my business. "
           f"minimum 500 words. business idea: {idea}. topics to cover: problem, solution, customer segments, "
           f"financials on a {budget} budget, marketing channels both online and in-person, sales methods both online "
           f"and in-person, key metrics, risk reduction, and competitive advantage. section paragraphs by topic. no "
           f"headings and no jot notes.",
    temperature=0.1,
    max_tokens=3500,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  summary = response["choices"][0]['text']
  return summary




print(summary)
get_executive_summary("ian cookie store","cookie retailer", 3000)
print(summary)
print(call_api("summarize the following text in 150 words."))