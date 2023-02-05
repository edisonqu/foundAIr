## foundAIr

Become a startup founder in just 30 seconds! Create a business plan in minutes!

## Quick Start

Start the React Frontend server by navigating to the `/client`, installing the dependencies with `npm install` and then starting it up with `npm start`



## Examples

* Edison's Small Business Plan
  * [foundAIr Generated Business Plan on Dog Fur Jackets.](dog_jacket_business_plan.pdf)
* Anna's Small Business Plan
  * [foundAIr Generated Business Plan on Real Cat Ears.](real_cat_ears_business_plan.pdf)
* Ian's Small Business Plan
  * [foundAIr Generated Business Plan for Daycares.](daycare_business_plan.pdf)
* Stephen's Small Business Plan
  * [foundAIr Generated Business Plan for Egirls.](daycare_business_plan.pdf)

## Try It Out!

Try it out for yourself. Become a founder in minutes!

**[http://foundair.tech/](requirements.txt)**
## Inspiration

Imagine you have a great idea for a startup (as we're sure you probably don't even need to imagine). You've got a vision, you've got your dream, but when it comes time to execute, suddenly, you feel lost, and you don't know where to even start. Lucky for you, we created foundAIr - an AI-powered business plan writer that will take care of the logistics for you! We felt that uncertainty when we started our own ventures, but after overcoming this challenge, we've put our minds together to help other founders take their ventures to the moon!

## What it does

Introducing the future of business planning: an AI-powered business plan generator! Say goodbye to the stress and frustration of writing a business plan from scratch. All you need is your business idea and a few clicks of a button. Simply enter your idea into the webpage, as well as your name, your budget, and your proposed business name, and the AI will take care of the rest. In no time, you'll have a comprehensive and customized business PDF plan, tailored to your specific needs. Say hello to more time, less stress, and a clearer path to success with foundAIr - the world’s first AI-powered business plan generator.

## How we built it

Starting off with the front end, we used Tailwind CSS and React to create a webpage, consisting of a landing page with a parallax effect and a Typeform, to create an interactive and founder-friendly UI. To integrate this with the back end, we used an AWS Lambda function where we called upon the OpenAI API to generate text for the business plan, using specifically-engineering prompts. We formatted a PDF file using the fPDF library and returned it to the user using the IPFS peer-to-peer networking system.

## Challenges we ran into

Our most prominent challenge was integrating a parallax scrolling effect. It might seem simplistic and swift from the outside, but in reality, it was quite the opposite to integrate. We worked on it since the start of the hackathon period, and it was only in the culminating moments that we were able to finish integrating it into our software. The complexities of the animation and the creation of the landing page in general made front-end development quite a challenge in this short hacking period.

Moreover, using an AWS Lambda function was not easy. Learning how to use the software was quite simple, but adding layers with minimal support required some effort. Through countless debugging efforts, we were able to add layers, and ultimately, by combining our efforts to tackle AWS bugs with our diversified skill sets, we were able to integrate our front end with our back end.

## Accomplishments that we're proud of

__-Two Worlds Collide.__ Our front end was written using Tailwind, and our back end was initially written using Flask. However, to integrate them together, we learned that we needed to use an AWS Lambda function to connect the two, making them interconnected. After overcoming many obstacles along the way, such as working through errors when creating layers and transferring most of our code to AWS, we are proud that we were able to debug our software, even though most solutions required multiple alternative approaches. 

__-What Do I Say?__ Delivering the ideal advice for founders wasn’t easy, especially since we weren’t dishing out tips and tricks ourselves. By digging deep into the semantics of NLP and conducting intensive prompt engineering, we are proud that we are able to construct the perfect prompts to enable the generation of desired responses.

__- Founders helping founders, zero to one.__ As former founders, we’re proud that we were able to combine our diversified skill sets to tackle a prominent dilemma that most entrepreneurs are facing. By utilizing our software, we hope that founders will be able to launch their ventures and pursue their dreams, progressing the prominence of the startup industry around the world.

## What we learned

At an AI-focused hackathon, some of us were working with AI for the first time. However, by working with OpenAI APIs to generate text responses, we were able to create an innovative solution for business plan generation. Now, instead of general templates, you can get a customized solution.

Moreover, we integrated IPFS, a decentralized network for sharing and storing data using a peer-to-peer approach. It is equipped with a protocol, hypermedia, and file-sharing capabilities. IPFS relies on content-addressing to identify every file in a global namespace that links IPFS hosts, and using this methodology, we are able to transfer files from the server side to the client side after the request to generate and receive the PDF was sent on the front-end.

Finally, we wanted to make the website more than just a webpage. By designing our webpage vision on markerboards and then using our web dev skills to create animations, we were able to create engaging content for future entrepreneurs beyond our AI-powered business plan generator.

## What's next for foundAIr

Although we've helped founders overcome the hurdle of deciding how to grow and scale their dream ventures, there are still many obstacles that budding entrepreneurs have to face. How will they decide on a logo? What if they can’t come up with a company name? Perhaps they’ll need more diagrams for further clarification? This, and much more, will be implemented in the next release of foundAIr!

