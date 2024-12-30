#Common/models.py
from typing import List
from datetime import datetime

class Recipe:
    def __init__(self, gallons: float, lbsOfHoney: float, honeyType: str, otherIngredients: List[str], surgarContent: List[str]) -> None:
        self.gallons = gallons
        self. lbsOfHoney = lbsOfHoney
        self.honeyType = honeyType
        self.otherIngredients = otherIngredients
        self.surgarContent = surgarContent

class Brew:
    def __init__(self, name: str, recipe: Recipe, originalGravity: float, stagaredNutrient: bool, startDate: datetime, notes: str = "") -> None:
        self.name = name
        self. recipe = recipe
        self.originalGravity = originalGravity
        self.stagaredNutrient = stagaredNutrient
        self.startDate = startDate
        self.notes = notes


