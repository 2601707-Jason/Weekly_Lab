from product import Product

class Inventory:
    def __init__(self, products: list[Product]):
        self.__products = products
    
    def add_product(self, product: Product):
        if self.has_product(product.product_id):
            raise ValueError("Product ID already exists")
        self.__products.append(product)
        
    def search_product(self, product_id: int) -> Product | None:
        for product in self.__products:
            if product.product_id == product_id:
                return product
        return None
    
    def has_product(self, product_id: int) -> bool:
        return self.search_product(product_id) is not None
    
    def display_all_products(self):
        for product in self.__products:
            product.display_information()
    
    def to_dict(self) -> list[dict]:
        return [p.to_dict() for p in self.__products]

