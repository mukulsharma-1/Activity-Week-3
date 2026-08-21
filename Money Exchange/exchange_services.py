from datetime import datetime

class ExchangeService:
    """Handles logic and CRUD operations for the exchange system."""
    
    def __init__(self, connection):
        # Starts the database connection into the service
        self.conn = connection

    def add_customer(self, name, email, phone):
        cursor = self.conn.cursor()
        cursor.execute('INSERT OR IGNORE INTO Customers (Name, Email, Phone) VALUES (?, ?, ?)', (name, email, phone))
        self.conn.commit()

    def add_currency(self, code, name, rate):
        cursor = self.conn.cursor()
        cursor.execute('INSERT OR IGNORE INTO Currencies VALUES (?, ?, ?)', (code, name, rate))
        self.conn.commit()

    def execute_exchange(self, customer_id, from_code, to_code, amount):
        cursor = self.conn.cursor()
        
        # 1. Fetch exchange rates
        cursor.execute('SELECT ExchangeRateToUSD FROM Currencies WHERE CurrencyCode = ?', (from_code,))
        rate_in = cursor.fetchone()[0]
        
        cursor.execute('SELECT ExchangeRateToUSD FROM Currencies WHERE CurrencyCode = ?', (to_code,))
        rate_out = cursor.fetchone()[0]
        
        # 2. Calculate conversion
        amount_usd = amount * rate_in
        amount_out = round(amount_usd / rate_out, 2)
        date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 3. Log the transaction securely
        cursor.execute('''
            INSERT INTO Transactions (CustomerID, FromCurrency, ToCurrency, AmountIn, AmountOut, Date)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (customer_id, from_code, to_code, amount, amount_out, date_now))
        
        self.conn.commit()
        return amount_out