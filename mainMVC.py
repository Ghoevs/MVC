class ShoeModel:
    def __init__(self, shoe_type, gender, kind, color, price, manufacturer, size):
        self.shoe_type = shoe_type
        self.gender = gender
        self.kind = kind
        self.color = color
        self.price = price
        self.manufacturer = manufacturer
        self.size = size

    def get_info(self):
        return {
            "shoe_type": self.shoe_type,
            "gender": self.gender,
            "kind": self.kind,
            "color": self.color,
            "price": self.price,
            "manufacturer": self.manufacturer,
            "size": self.size
        }

    def update_info(self, shoe_type=None, gender=None, kind=None, color=None, price=None, manufacturer=None, size=None):
        if shoe_type is not None:
            self.shoe_type = shoe_type
        if gender is not None:
            self.gender = gender
        if kind is not None:
            self.kind = kind
        if color is not None:
            self.color = color
        if price is not None:
            self.price = price
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if size is not None:
            self.size = size


class RecipeModel:
    def __init__(self, name, author, recipe_type, description, ingredients, cuisine):
        self.name = name
        self.author = author
        self.recipe_type = recipe_type
        self.description = description
        self.ingredients = ingredients
        self.cuisine = cuisine

    def get_info(self):
        return {
            "name": self.name,
            "author": self.author,
            "recipe_type": self.recipe_type,
            "description": self.description,
            "ingredients": self.ingredients,
            "cuisine": self.cuisine
        }

    def update_info(self, name=None, author=None, recipe_type=None, description=None, ingredients=None, cuisine=None):
        if name is not None:
            self.name = name
        if author is not None:
            self.author = author
        if recipe_type is not None:
            self.recipe_type = recipe_type
        if description is not None:
            self.description = description
        if ingredients is not None:
            self.ingredients = ingredients
        if cuisine is not None:
            self.cuisine = cuisine


class ShoeView:
    def display(self, data):
        print("Shoe info:")
        for key, value in data.items():
            print(f"{key}: {value}")


class RecipeView:
    def display(self, data):
        print("Recipe info:")
        for key, value in data.items():
            print(f"{key}: {value}")


class ShoeController:
    def __init__(self):
        self.model = None
        self.view = ShoeView()

    def create_shoe(self, shoe_type, gender, kind, color, price, manufacturer, size):
        self.model = ShoeModel(shoe_type, gender, kind, color, price, manufacturer, size)

    def show_shoe(self):
        if self.model:
            data = self.model.get_info()
            self.view.display(data)

    def update_shoe(self, shoe_type=None, gender=None, kind=None, color=None, price=None, manufacturer=None, size=None):
        if self.model:
            self.model.update_info(shoe_type, gender, kind, color, price, manufacturer, size)


class RecipeController:
    def __init__(self):
        self.model = None
        self.view = RecipeView()

    def create_recipe(self, name, author, recipe_type, description, ingredients, cuisine):
        self.model = RecipeModel(name, author, recipe_type, description, ingredients, cuisine)

    def show_recipe(self):
        if self.model:
            data = self.model.get_info()
            self.view.display(data)

    def update_recipe(self, name=None, author=None, recipe_type=None, description=None, ingredients=None, cuisine=None):
        if self.model:
            self.model.update_info(name, author, recipe_type, description, ingredients, cuisine)


if __name__ == "__main__":
    # Задание 1
    shoe_ctrl = ShoeController()
    shoe_ctrl.create_shoe("мужская", "мужская", "кроссовки", "черный", 5000, "Nike", 42)
    shoe_ctrl.show_shoe()
    shoe_ctrl.update_shoe(price=4500)
    shoe_ctrl.show_shoe()

    print("---")

    # Задание 2
    recipe_ctrl = RecipeController()
    recipe_ctrl.create_recipe("Борщ", "Иванов", "первое", "Варить 2 часа", ["свекла", "капуста", "мясо"], "украинская")
    recipe_ctrl.show_recipe()
    recipe_ctrl.update_recipe(author="Петров")
    recipe_ctrl.show_recipe()