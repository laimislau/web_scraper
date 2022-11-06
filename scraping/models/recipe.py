from pydantic import BaseModel

class Recipe(BaseModel):
    recipe_title: str
    recipe_link: str
    recipe_image_link: str
    making_time: str
    recipe_ingredients: str
    recipe_making_steps: str


class RecipeLink(BaseModel):
    url: str