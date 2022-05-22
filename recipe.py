import datetime
import requests
from display_controller import DisplayController

class Recipe():

    def __init__(self,
                 ready_in_minutes=0,
                 servings=0,
                 isVegetarian=False,
                 isVegan=False,
                 isDairyFree=False,
                 isGlutenFree=False,
                 recipe_id=0,
                 title="N/A",
                 url="N/A",
                 timestamp=datetime.date(1990, 1, 1),
                 ):
        self.ready_in_minutes = ready_in_minutes
        self.servings = servings
        self.isVegetarian = isVegetarian
        self.isVegan = isVegan
        self.isDairyFree = isDairyFree
        self.isGlutenFree = isGlutenFree
        self.recipe_id = recipe_id
        self.title = title
        self.url = url
        self.timestamp = timestamp
