import logging
import random
import string
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    letters = []
    for i in range(4):
        letters.append(random.choice(string.ascii_lowercase))
    return func.HttpResponse(f"{letters}")

