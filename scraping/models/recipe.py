from pydantic import BaseModel
from typing import Optional

class Recipe(BaseModel):
    recipe_title: str
    recipe_amount: str    
    recipe_image_link: Optional[str]
    making_time: Optional[str]
    recipe_ingredients: str
    recipe_making_steps: str


class RecipeLink(BaseModel):
    url: str