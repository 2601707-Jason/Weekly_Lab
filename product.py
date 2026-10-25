class Product:
    def __init__(self, product_id: int, name: str, price: float, stock: int):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        
    def update_stock(self, quantity: int):
        new_stock = self.__stock + quantity
        if new_stock < 0:
            raise ValueError(f"Not enough stock! Only {self.__stock} left")
        self.__stock = new_stock
    
    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: {self.__price} | Stock: {self.__stock}")
    
    @property
    def product_id(self):
        return self.__product_id
    
    def to_dict(self) -> dict:
        return {
            "product_id": self.product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }
        
    @classmethod
    def from_dict(cls, data: dict) -> "Product":
        return cls(data["product_id"], data["name"], data["price"], data["stock"])