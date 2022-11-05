from pydantic import BaseModel

class Recipe(BaseModel):
    recipe_title: str
    recipe_link: str
    recipe_image_link: str
    making_time: str
    ingredients: str
    making_steps: str