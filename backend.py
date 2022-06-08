import requests
from api_util import APIUtil
from recipe import Recipe
from qr_code import QRCode
from quote import Quote
import datetime
from abc import ABC
from file_system import FileSystemHelper


class Backend(ABC):
    api_util = APIUtil()

    @classmethod
    def get_recipe(cls) -> Recipe:

        headers = {
            "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
            "X-RapidAPI-Key": "{}".format(Backend.api_util.rapid_api_key)
        }

        payload = {
            "number": "1"
        }

        try:
            response = requests.request("GET", Backend.api_util.random_recipes_endpoint, headers=headers, params=payload)
            return Recipe.from_dict(data=response.json()["recipes"][0])
        except Exception as e:
            print("Could not fetch Recipe \n")
            print("Error code: {}".format(e))

    @classmethod
    def get_qr_code(cls, recipe: Recipe) -> QRCode:
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Host": "qrcode3.p.rapidapi.com",
            "X-RapidAPI-Key": "{}".format(Backend.api_util.rapid_api_key)
        }

        payload = {
            "data": recipe.url,
            "style": {
                "module": {
                    "color": "black",
                    "shape": "default"
                },
                "inner_eye": {"shape": "default"},
                "outer_eye": {"shape": "default"},
                "background": {
                    "color": "white"
                }
            },
            "size": {
                "width": 100,
                "quiet_zone": 0,
                "error_correction": "M"
            },
            "output": {
                "filename": "Random recipe",
                "format": "png"
            }
        }

        try:
            response = requests.request("POST", Backend.api_util.qr_text_endpoint, json=payload, headers=headers)
            return QRCode.from_bytestring_and_recipe(qr_bytestring=response.content, recipe_ref=recipe)
        except Exception as e:
            print("Could not fetch QR Code \n")
            print("Error code: {}".format(e))


    @classmethod
    def get_quote(cls):

        payload = {
            "topicId": 100,
        }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Host": "quotel-quotes.p.rapidapi.com",
            "X-RapidAPI-Key": "{}".format(Backend.api_util.rapid_api_key)
        }
        try:
            response = requests.request("POST", Backend.api_util.random_quote_endpoint, headers=headers, json=payload)
            return Quote.from_json(data=response.json())
        except Exception as e:
            print("Could not fetch Random Quote \n")
            print("Error code: {}".format(e))

