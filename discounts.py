# 1. Create a function named calculate_discount
def calculate_discount(price, discount_percent):

  # Check if the discount is 20% or higher
  if discount_percent >= 20:
    # Apply the discount
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price
  else:
    # Return the original price
    return price

# 2. Prompt the user for input and use the function
try:
  # Get user input for original price and discount percentage
  original_price = float(input("Enter the original price of the item: "))
  discount_percentage = float(input("Enter the discount percentage: "))

  # Call the function to calculate the final price
  final_price_result = calculate_discount(original_price, discount_percentage)
  
  # Print the final price based on whether a discount was applied
  if discount_percentage >= 20:
    print(f"The final price after a {discount_percentage:.2f}% discount is: ${final_price_result:.2f}")
  else:
    print(f"No discount was applied. The original price is: ${final_price_result:.2f}")

except ValueError:
  # Handle cases where the user enters non-numeric input
  print("Invalid input. Please enter a valid number for price and discount percentage.")
