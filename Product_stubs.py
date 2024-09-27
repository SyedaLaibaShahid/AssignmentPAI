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
        

