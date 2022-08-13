from square.client import Client
import os

client = Client(
    access_token=os.environ['SQUARE_ACCESS_TOKEN'],
    environment='sandbox')