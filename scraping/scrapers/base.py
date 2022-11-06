from scraping.models.recipe import RecipeLink, Recipe
from typing import List, Optional
from abc import ABC, abstractmethod
import math

# abstrakti klase - ja inicializuoti nera logiska, tik paveldeti
class BaseScraper(ABC):
    __items_per_page__: int = 0

    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def _retrieve_items_list(self, pages_count: int, keyword: str) -> List[RecipeLink]:
        # keywordas, tai kad galetume naudoti paieska, nu pvz paduosim "ledu tortas"
        pass

    def _retrieve_recipe_info(self, link: RecipeLink) -> Optional[Recipe]:
        pass

    def scrape(self, recipes_count: int, keyword: str) -> List[Recipe]:
        pages_count = math.ceil(recipes_count / self.__items_per_page__)
        recipe_links = self._retrieve_items_list(pages_count, keyword)
        scraped_recipes: List[Recipe] = []
        for recipe_link in recipe_links:
            scraped_recipe = self._retrieve_recipe_info(recipe_link)
            if scraped_recipe is not None:
                scraped_recipes.append(scraped_recipe)