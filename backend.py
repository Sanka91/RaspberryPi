import requests
from api_util import APIUtil
from recipe import Recipe
from qr_code import QRCode
import datetime
from abc import ABC


class Backend(ABC):
    api_util = APIUtil()

    @classmethod
    def get_recipe(cls) -> Recipe:
        print("in Get recipe")

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
            ready_in_minutes = data["readyInMinutes"],
            servings = data["servings"],
            isVegetarian = data["vegetarian"],
            isVegan = data["vegan"],
            isDairyFree = data["dairyFree"],
            isGlutenFree = data["glutenFree"],
            recipe_id = data["id"],
            title = data["title"],
            url = data["spoonacularSourceUrl"],
            timestamp = datetime.date.today().strftime("%Y_%m_%d")
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

        response = requests.request("POST", Backend.api_util.qr_text_endpoint, json=payload, headers=headers)
        return Backend.serialize_qr_code(qr_bytestring= response.content, recipe= recipe)

    @classmethod
    def serialize_qr_code(cls, qr_bytestring: bytes, recipe: Recipe) -> QRCode:
        filename = "ID_{}_Date_{}.png".format(recipe.recipe_id, recipe.timestamp)

        # image = Image.open(io.BytesIO(qr_bytestring))
        # image.save('/home/pi/Desktop/Raspberry_Pi/Recipe_QRs/{}'.format(filename))
        return QRCode(
            filename=filename,
            recipe_id_ref = recipe.recipe_id,
            timestamp=recipe.timestamp
        )