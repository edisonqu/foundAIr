import os
import openai
import dotenv

dotenv.load_dotenv()

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="I want to start a business that is focused on selling water bottle plushies. Can you write me the section, around 250 words, for how I can market my product on the internet using $300. This product is aimed at young adults between the ages of 18 and 34 who are looking for a unique and fun way to express their individual style. Our target audience is comprised of people who are environmentally conscious and are looking for a creative way to reduce their single-use plastic consumption. Our target audience is also composed of people who appreciate unique and creative designs, as well as those who want to make a statement with their purchases.",
  temperature=0.7,
  max_tokens=3500,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response["choices"][0]['text'])