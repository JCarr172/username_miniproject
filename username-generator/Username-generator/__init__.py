import logging
import random, requests
import azure.functions as func
from azure.cosmos import exceptions, CosmosClient, PartitionKey


endpoint = ""
key = ""

client = CosmosClient(endpoint, key)

database = client.create_database_if_not_exists(id="RandomUserName")
container = database.create_container_if_not_exists(
    id = "UsernameContainer"
    partition_key=PartitionKey(path="/username")
    offer_throughput=400
)


def main(req: func.HttpRequest) -> func.HttpResponse:
    letters = requests.get('https://username-maker.azurewebsites.net/api/letter-generator?code=gc1iyfY27ZP241cX2JrAj9Jo6Cu1ZNYSa3MK3vMKe6HK0DctO4NMhQ==')
    numbers = requests.get('https://username-maker.azurewebsites.net/api/number-generator?code=u6oEpyHNIOd7mvUSNwP8F1axdpo691W5tZELkZq53Nj90RF/a2YfaQ==')
    name = ''
    for i in [2,7,12,17]:
        name = name + letters.text[i]
        name= name + numbers.text[i]

    container.create_item(body=(
        "id": '1',
        "username":name
        ))
    return func.HttpResponse(f"{name}")