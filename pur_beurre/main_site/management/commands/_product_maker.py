class ApiProduct:
    """This class create a product"""

    def __init__(self, json_product):
        self.json_product = json_product

    def name(self):
        """Search for name"""
        try:
            if self.json_product["product_name"] != "":
                return self.json_product["product_name"]
            else:
                return None
        except KeyError:
            print("Name not found")
            return None

    def categories(self):
        """Search for categories"""
        try:
            if self.json_product["categories"] != "":
                return [
                    category.strip()
                    for category in self.json_product["categories"].split(",")
                ]
            else:
                return None
        except KeyError:
            print("Category not found")
            return None

    def nutriscore(self):
        """Search for nutriscore"""
        try:
            if self.json_product["nutrition_grades"] != "":
                return self.json_product["nutrition_grades"].upper()
            else:
                return None
        except KeyError:
            print("Nutriscore not found")
            return None

    def url(self):
        """Search for url"""
        try:
            if self.json_product["url"] != "":
                return self.json_product["url"]
            else:
                return None
        except KeyError:
            print("Url not found")
            return None

    def categories_language(self):
        """Search the language of the product"""
        try:
            if self.json_product["categories_lc"] == "fr":
                return "fr"
            else:
                return None
        except KeyError:
            print("Product language not found")
            return None

    def image_url(self):
        """"Search the image of the product"""
        try:
            if self.json_product["image_url"] != "":
                return self.json_product["image_url"]
            else:
                return None
        except KeyError:
            print("Image's url not found")
            return None

    def kcal(self):
        """"Search the kcal for 100g of the product"""
        try:
            product_kcal = self.json_product["nutriments"]["energy-kcal_100g"]
        except KeyError:
            print("Kcal not found")
            return None
        if product_kcal != "":
            return product_kcal
        else:
            return None

    def fat(self):
        """"Search the fat for 100g of the product"""
        try:
            product_fat = self.json_product["nutriments"]["fat_100g"]
        except KeyError:
            print("Fat not found")
            return None
        if product_fat != "":
            return product_fat
        else:
            return None

    def protein(self):
        """"Search the protein for 100g of the product"""
        try:
            product_protein = self.json_product["nutriments"]["proteins_100g"]
        except KeyError:
            print("Protein not found")
            return None
        if product_protein != "":
            return product_protein
        else:
            return None

    def sugar(self):
        """"Search the sugar for 100g of the product"""
        try:
            product_sugar = self.json_product["nutriments"]["sugars_100g"]
        except KeyError:
            print("Sugar not found")
            return None
        if product_sugar != "":
            return product_sugar
        else:
            return None
