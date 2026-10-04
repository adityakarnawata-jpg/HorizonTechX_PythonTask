"""Task 2: Stock Portfolio Tracker - Horizon TechX Python Internship"""
import csv

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 125,
}


def get_portfolio():
    portfolio = {}
    print("Available stocks:", ", ".join(STOCK_PRICES))
    print("Type 'done' when finished.\n")

    while True:
        name = input("Enter stock name: ").strip().upper()
        if name == "DONE":
            break
        if name not in STOCK_PRICES:
            print("Stock not found. Try again.\n")
            continue
        try:
            qty = int(input(f"Enter quantity of {name}: "))
            if qty <= 0:
                raise ValueError
        except ValueError:
            print("Please enter a valid positive number.\n")
            continue
        portfolio[name] = portfolio.get(name, 0) + qty
        print(f"Added {qty} x {name}\n")
    return portfolio


def calculate_total(portfolio):
    rows = []
    total = 0
    for name, qty in portfolio.items():
        value = STOCK_PRICES[name] * qty
        rows.append((name, qty, STOCK_PRICES[name], value))
        total += value
    return rows, total


def save_to_csv(rows, total, filename="portfolio.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])
        writer.writerows(rows)
        writer.writerow(["TOTAL", "", "", total])
    print(f"Results saved to {filename}")


def main():
    print("=== STOCK PORTFOLIO TRACKER ===\n")
    portfolio = get_portfolio()

    if not portfolio:
        print("No stocks entered.")
        return

    rows, total = calculate_total(portfolio)

    print("\n--- Portfolio Summary ---")
    print(f"{'Stock':<8}{'Qty':<6}{'Price':<8}{'Value':<8}")
    for name, qty, price, value in rows:
        print(f"{name:<8}{qty:<6}{price:<8}{value:<8}")
    print(f"\nTotal investment value: ${total}")

    if input("\nSave results to file? (y/n): ").strip().lower() == "y":
        save_to_csv(rows, total)


if __name__ == "__main__":
    main()
