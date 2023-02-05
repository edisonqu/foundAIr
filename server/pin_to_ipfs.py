import requests
import dotenv
import os
from pestuary import Pestuary

dotenv.load_dotenv()


def pinToIPFS():

    pestuary = Pestuary(estuary_key=os.getenv("ESTUARY_API_KEY"))

    collectionsApi = pestuary.get_collections_api()
    contentApi = pestuary.get_content_api()

    adding_content = contentApi.content_add_post("tmp/business_plan.pdf", filename="business_plan.pdf")

    return adding_content

pinToIPFS()


