import logging
import random
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    numbers = []
    for x in range(4):
        numbers.append(str(random.randint(0,9)))
    return func.HttpResponse(f"{numbers}")