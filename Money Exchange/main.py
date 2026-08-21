# importing the functions
from db_connection import DatabaseConnection
from exchange_services import ExchangeService

def main():
    print("Initializing Money Exchange System...\n")
    
    db = DatabaseConnection()
    services = ExchangeService(db.get_connection())

    # Setting-up currencies
    services.add_currency('USD', 'US Dollar', 1.00)
    services.add_currency('EUR', 'Euro', 1.08)
    services.add_currency('NZD', 'New Zealand Dollar', 0.60)

    # Setting up a customer for the manual transaction
    services.add_customer('Manual User', 'manual@email.com', '555-0000')

    print("--- Welcome to the Currency Exchange ---")
    print("Available Currencies: USD, EUR, NZD")
    
    try:
        # Getting manual input from the terminal
        from_code = input("Enter the currency you are converting FROM (e.g., NZD): ").strip().upper()
        to_code = input("Enter the currency you are converting TO (e.g., EUR): ").strip().upper()
        amount = float(input(f"Enter the amount of {from_code} to convert: "))

        print("\nProcessing...")
        # Passing the manual inputs into your existing OOP function
        result = services.execute_exchange(customer_id=1, from_code=from_code, to_code=to_code, amount=amount)
        
        print(f"Success! {amount} {from_code} was converted to {result} {to_code}.")
        
    except Exception as error:
        print("\nError: Please ensure you entered valid currencies and a numerical amount.")
        print(f"Developer details: {error}")

    finally:
        # Closing the DB connection
        db.close()
        print("\nSystem closed safely.")

# Running the script
if __name__ == "__main__":
    main() 