def validate_ingredients(ingredients: str) -> str:
    valid_ingredients = ["fire", "water", "earth", "air"]
    is_valid = (
        any(ingr in valid_ingredients for ingr in ingredients.lower())
    )
    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
