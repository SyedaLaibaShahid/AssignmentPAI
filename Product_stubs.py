#SP23-BAI-052 SYEDA LAIBA SHAHID ,
#SP23-BAI-022 KHADIJA SAJID
class Product:
  def _init_(self, name, amount, price):
      self.name = name
      self.amount = amount
      self.price = price

def get_price(self, quantity):
        try:
            if quantity <= 0:
                raise ValueError("Quantity must be a positive integer.")

            total_price = self.price * quantity

            if quantity < 10:
                discount = 0
            elif 10 <= quantity <= 99:
                discount = 0.1
            else:
                discount = 0.2

            final_price = total_price * (1 - discount)
            return final_price

        except ValueError as error:
            # Handle the error and return None
            print(f"Error: {error}")
            return None
        

  def make_purchase(self, quantity):
        try:
            if quantity < 0:
                raise ValueError("Quantity cannot be negative.")
            elif quantity > self.amount:
                raise ValueError("Not enough items in stock.")

            total_cost = self.get_price(quantity)
            self.amount -= quantity
            print(f"Purchased {quantity} items of {self.name}")
            print(f"Total cost: ${total_cost:.2f}")
            print(f"Remaining stock: {self.amount}")

        except ValueError as e:
            print(e)

# Example usage
product = Product("Widget", 150, 10.00)  
product.make_purchase(5)
product.make_purchase(50)
product.make_purchase(150)
