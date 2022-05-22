import datetime


class Recipe:

    def __init__(self,
                 ready_in_minutes,
                 servings,
                 isVegetarian,
                 isVegan,
                 isDairyFree,
                 isGlutenFree,
                 recipe_id,
                 full_title,
                 url,
                 timestamp=datetime.date(1990, 1, 1),
                 ):
        self.ready_in_minutes = ready_in_minutes
        self.servings = servings
        self.isVegetarian = isVegetarian
        self.isVegan = isVegan
        self.isDairyFree = isDairyFree
        self.isGlutenFree = isGlutenFree
        self.recipe_id = recipe_id
        self.full_title = full_title
        self.url = url
        self.timestamp = timestamp
        if len(self.full_title) > 25:
            self.display_title = "{}...".format(self.full_title[:25])
        else:
            self.display_title = self.full_title

