# Author: Kriston Jomari
# Admin No: 231165R

inventory_info = {
  '1': {
    'Product Name': 'Apple',
    'prices': [1.2, 1.5, 1.3]},
  '2': {
    'Product Name': 'Banana',
    'prices': [0.8, 0.9, 0.7, 0.6, 0.6]},
  '3': {
    'Product Name': 'Orange',
    'prices': [1.0, 1.2, 0.9, 1.1]},
}

def prod_info(inventory):
  """
  This function iterates through a product inventory dictionary and displays information
  for each product, including highest price, average price, and product name.
  """
  print("Product Information:", len(inventory))  # Total products
  for product_id, product_details in inventory.items():
    product_name = product_details["Product Name"]
    prices = product_details["prices"]
    highest_price = max(prices)
    average_price = sum(prices) / len(prices)

    print(f"\nP{product_id}.{product_name}")
    print(f"\tHighest Price: {highest_price}")
    print(f"\tAverage Price: {average_price:.2f}")  # Format average to 2 decimal places

prod_info(inventory_info)

def prod_info(inventory):
    print(f"Product Information: {len(inventory)}")

    for product_id, product_details in inventory.items():