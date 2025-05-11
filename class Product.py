class Product:

 def __init__(self, name: str, price: float, quantity: int):
     if not isinstance(name, str) or not name.strip():
      raise ValueError("Product name must be a non-empty string.")
 if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number.")
                 if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")

        self.name = name
     self.price = float(price)
    self.quantity = quantity

   def add_inventory(self, amount: int):
       """Add inventory to the product."""
      if not isinstance(amount, int) or amount <= 0:
           raise ValueError("Amount to add must be a positive integer.")
         self.quantity += amount

    def remove_inventory(self, amount: int):
         
        if not isinstance(amount, int) or amount <= 0:
           raise ValueError("Amount to remove must be a positive integer.")
            if amount > self.quantity:
                 raise ValueError("Cannot remove more than available quantity.")
        self.quantity -= amount

      def total_value(self) -> float:
         
       return self.price * self.quantity

     def display_info(self):
    
     print(f"Product: {self.name}")
       print(f"Price: ${self.price:.2f}")
        print(f"Quantity: {self.quantity}")
        print(f"Total Value: ${self.total_value():.2f}")

# Example usage
if __name__ == "__main__":
  try:
      p = Product("Laptop", 899.99, 10)
      p.display_info()
      p.add_inventory(5)
      p.remove_inventory(3)
      p.display_info()
     except ValueError as e:
     print(f"Error: {e}")a