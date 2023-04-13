#Import libraries
import asyncio
import aiohttp
import os
import openai

#Define api key to be stored in .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

#Used to retrieve next tasks
def get_tasks(session,company_name, idea,budget):
    tasks = []
    #Defines all of the prompts used when API is called
    prompts = [
        f"the business name is {company_name}. i am writing a business plan with the idea of {idea}. write an executive summary for my business. "
        f"minimum 500 words. business idea: {idea}. topics to cover: problem, solution, customer segments, "
        f"financials on a {budget} budget, marketing channels both online and in-person, sales methods both online "
        f"and in-person, key metrics, risk reduction, and competitive advantage. section paragraphs by topic. no "
        f"headings and no jot notes.",
        f"the business name is {company_name}. i am writing a business plan. business idea: {idea}. minimum 600 words. describe the problem faced by people without my business idea, the pain points my business idea targets, and explain my idea. no headings, no jot notes.",
        f"the business name is {company_name}. i am writing a business plan. business idea: {idea}. minimum 500 words. write me a market analysis, explaining the target market, the customer segments, explain how the consumers will take advantage of this, and explain the competition from other business i will face. no headings and no jot notes.",
        f"the business name is {company_name}. i am writing a business plan. business idea: {idea}. minimum 500 words. write me the unique value proposition of my idea and the competitive advantage of my idea. no headings and no jot notes.",
        f"the business name is {company_name}. i am writing a business plan. business idea: {idea}. minimum 550 words. explain the marketing channels i can take advantage of to promote my idea and interact with my consumers, both online and in person. explain how i can sell my idea in person and online. no headings and no jot notes.",
        f"the business name is {company_name}. i am writing a business plan. write a timeline to launch my business with numbers. minimum 500 words. business idea: {idea}. no headings and no jot notes.",
        f"the business name is {company_name}. i am writing a business plan. business idea: {idea}. my budget is only {budget}. write a short preamble without a preamble heading. give me a budget for my business and include subcategories and long descriptions for each cost. include numbers and jot form with subcategories for each cost.",
        f"the business name is {company_name}. i am writing a business plan. business idea: {idea}. minimum 500 words. explain the key metrics with specific numbers in jot form. describe methods to reduce risk. explain how we will reassess and reevaluate our progress. no headings.",
        f"i am writing a business plan. write a conclusion on a company called {company_name} which has the idea of {idea}."]
    for prompt in prompts:
        #Print tracker used for debugging and to keep track of progress
        print(f"Currently Computing: {prompt}")

        headers = {
            # Grant authorization
            # Already added when you pass json=
            # 'Content-Type': 'application/json',
            'Authorization': f'Bearer {os.getenv("OPENAI_API_KEY")}',
        }

        #Define GPT model to be used, as well as max tokens per request and variance
        json_data = {
            'model': 'gpt-3.5-turbo',
            'messages': [
                {
                    'role': 'user',
                    'content': f'{prompt} write around 400 words',
                },
            ],
        }
        url = "https://api.openai.com/v1/chat/completions"
        tasks.append(asyncio.create_task(session.post(url,headers=headers,json=json_data,ssl=False)))
    return tasks

#Gets the data to be used for the API call
async def get_data(company_name,idea,budget):
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session,company_name,idea,budget)
        responses = await asyncio.gather(*tasks)
        results = []
        for response in responses:
            results.append(await response.json())
    return results

#Calls the API
def call_api(company_name,idea,budget):
  data = asyncio.run(get_data(company_name,idea,budget))
  # Returns as a list
  return data
