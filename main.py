import requests
import json
from PIL import Image
import io
import datetime

def main():

    def generateQRCode(for_url: str, recipe_id: int, timestamp: datetime):

        url = "https://qrcode3.p.rapidapi.com/qrcode/text"

        filename = "ID_{}_Date_{}.png".format(recipe_id, timestamp)

        payload = {
            "data": for_url,
            "image": {
                "uri": "https://cdn.onlinewebfonts.com/svg/img_509437.png"
                },
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
                "filename": "{}".format(filename),
                "format": "png"
            }
        }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Host": "qrcode3.p.rapidapi.com",
            "X-RapidAPI-Key": "f534f7cd18mshbf4a89d26996e13p1aeab2jsnb452754d62bc"
        }

        response = requests.request("POST", url, json=payload, headers=headers)

        response = response.content

        image = Image.open(io.BytesIO(response))
        image.save('/home/pi/Desktop/Raspberry_Pi/Recipe_QRs/{}'.format(filename))
        #image.show()


    def foodApi():
        api_url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random"

        querystring = {"number":"1"}

        headers = {
            "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
            "X-RapidAPI-Key": "f534f7cd18mshbf4a89d26996e13p1aeab2jsnb452754d62bc"
        }

        response = requests.request("GET", api_url, headers=headers, params=querystring)

        response = response.json()["recipes"][0]
        ready_in_minutes = response["readyInMinutes"]
        servings= response["servings"]
        isVegetarian = response["vegetarian"]
        isVegan = response["vegan"]
        isDairyFree = response["dairyFree"]
        isGlutenFree = response["glutenFree"]
        recipe_id = response["id"]
        title = response["title"]
        url = response["spoonacularSourceUrl"]
        timestamp = datetime.date.today().strftime("%Y_%m_%d")

        return url, recipe_id, timestamp

    url, recipe_id, timestamp = foodApi()

    generateQRCode(url, recipe_id, timestamp)

if __name__ == "__main__":
    main()