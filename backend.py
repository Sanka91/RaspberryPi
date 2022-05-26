import requests
from api_util import APIUtil
from recipe import Recipe
from qr_code import QRCode
import datetime
from abc import ABC
from file_system import FileSystemHelper

class Backend(ABC):
    api_util = APIUtil()
    file_system = FileSystemHelper()

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
            test = response.json()["recipes"][0]
            return Backend.serialize_recipe(data=response.json()["recipes"][0])
        except Exception as e:
            print("Could not fetch Recipe \n")
            print("Error code: {}".format(e))

    @classmethod
    def serialize_recipe(cls, data: dict) -> Recipe:
        return Recipe(
            ready_in_minutes = "{}".format(data["readyInMinutes"]),
            servings = "{}".format(data["servings"]),
            isVegetarian = "{}".format(data["vegetarian"]),
            isVegan = "{}".format(data["vegan"]),
            isDairyFree = "{}".format(data["dairyFree"]),
            isGlutenFree = "{}".format(data["glutenFree"]),
            recipe_id = "{}".format(data["id"]),
            full_title="{}".format(data["title"]),
            url = data["spoonacularSourceUrl"],
            timestamp = "{}".format(datetime.date.today().strftime("%Y_%m_%d"))
        )

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
                    "shape": "vertical_lines"
                },
                "inner_eye": {"shape": "leaf"},
                "outer_eye": {"shape": "heavyround"},
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
            return Backend.serialize_qr_code(qr_bytestring=response.content, recipe_ref=recipe)
        except Exception as e:
            print("Could not fetch QR Code \n")
            print("Error code: {}".format(e))

    @classmethod
    def serialize_qr_code(cls, qr_bytestring: bytes, recipe_ref: Recipe) -> QRCode:
        filename = "ID_{}_Date_{}.png".format(recipe_ref.recipe_id, recipe_ref.timestamp)

        qr_path = Backend.file_system.save_image(filename=filename, bytestring=qr_bytestring)

        qr_code = QRCode(
            bytestring=qr_bytestring,
            filename=filename,
            recipe_id_ref=recipe_ref.recipe_id,
            timestamp=recipe_ref.timestamp,
            qr_code_location=qr_path
        )
        return qr_code
