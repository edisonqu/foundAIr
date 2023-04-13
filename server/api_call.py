import time

import dotenv
import asyncio
import aiohttp
import os
import openai

# Load your environment file with your OPENAI API Key
dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_tasks(session, company_name, idea, budget):
    """
    :param session: AIOHTTP Client Session
    :param company_name: Pass in the Company Name for AI to read in the prompts
    :param idea: Pass in the Idea for AI to read in the prompts
    :param budget: Pass in the Idea Name for AI to read in the prompts
    :return: List of all the coroutines from the requests
    """
    tasks = []
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
        f"the business name is {company_name}.i am writing a business plan. business idea: {idea}. my budget is only {budget}. give me a budget for my business and include descriptions for each cost. include numbers and jot form.",
        f"the business name is {company_name}. i am writing a business plan. business idea: {idea}. minimum 500 words. explain the key metrics with specific numbers in jot form. describe methods to reduce risk. explain how we will reassess and reevaluate our progress. no headings.",
        f"i am writing a business plan. write a conclusion on a company called {company_name} which has the idea of {idea}."]
    for prompt in prompts:
        print(f"Currently Computing: {prompt}")
        headers = {
            'Authorization': f'Bearer {os.getenv("OPENAI_API_KEY")}',
        }

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

        response = asyncio.create_task(session.post(url, headers=headers, json=json_data, ssl=False))
        print(response)
        tasks.append(response)
    return tasks


async def get_data(company_name, idea, budget):
    """
    The function gets all the request coroutines from get_tasks and awaits them to be put inside a list.

    :param company_name: Pass in the Company Name for the get_tasks function
    :param idea: Pass in the Idea for the get_tasks function
    :param budget: Pass in the Company Name for the get_tasks function
    :return: A list of all the responses from the API
    """
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session, company_name, idea, budget)
        responses = await asyncio.gather(*tasks)
        results = []
        for response in responses:
            results.append(await response.json())
            print(response)
    print(results)
    return results


def call_api(company_name, idea, budget):
    """
    Calls the APIs using Asyncio
    :return: A list of all the responses
    """
    data = asyncio.run(get_data(company_name, idea, budget))
    # Returns as a list
    return data
