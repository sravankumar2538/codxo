exchange_rates = {
    "USD": 1.0,     
    "EUR": 0.85,    
    "GBP": 0.75,    
    "INR": 74.5,    
    "JPY": 110.0,   
    "CAD": 1.25,    
}

def currency_converter():
    print("Available currencies:")
    for currency in exchange_rates:
        print(currency)
    
    try:
        amount = float(input("Enter the amount: "))
        from_currency = input("From currency : ").upper()
        to_currency = input("To currency : ").upper()
        
        if from_currency not in exchange_rates or to_currency not in exchange_rates:
            print("Error: Unsupported currency")
            return

        converted_amount = amount * (exchange_rates[to_currency] / exchange_rates[from_currency])
        
        print(f"{amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    except ValueError:
        print("Error: Invalid input. Please enter a valid number for the amount.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    currency_converter()
