# TASK 2: Stock Portfolio Tracker

# Step 1: Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "AMZN": 3300,
    "MSFT": 300
}

# Step 2: Initialize portfolio dictionary
portfolio = {}

print("📈 Welcome to Stock Portfolio Tracker!")
print("Available stocks and their prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

# Step 3: User input
while True:
    stock_name = input("\nEnter stock symbol (or 'done' to finish): ").upper()
    if stock_name == "DONE":
        break
    if stock_name not in stock_prices:
        print("⚠️ Stock not available. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
        if quantity < 0:
            print("⚠️ Quantity cannot be negative.")
            continue
    except ValueError:
        print("⚠️ Enter a valid number.")
        continue

    # Save in portfolio
    if stock_name in portfolio:
        portfolio[stock_name] += quantity
    else:
        portfolio[stock_name] = quantity

# Step 4: Calculate total investment
total_investment = 0
print("\n💹 Your Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total_investment += investment
    print(f"{stock}: {qty} shares x ${price} = ${investment}")

print(f"\nTotal Investment Value: ${total_investment}")

# Step 5: Optional - Save to a text file
save_option = input("\nDo you want to save this summary to a file? (yes/no): ").lower()
if save_option == "yes":
    with open("portfolio_summary.txt", "w") as f:
        f.write("Stock Portfolio Summary\n")
        f.write("======================\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            investment = price * qty
            f.write(f"{stock}: {qty} shares x ${price} = ${investment}\n")
        f.write(f"\nTotal Investment Value: ${total_investment}\n")
    print("✅ Portfolio summary saved as portfolio_summary.txt")