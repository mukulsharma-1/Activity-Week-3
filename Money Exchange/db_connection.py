import sqlite3

class DatabaseConnection:
    """Handles the database connection and schema initialization."""
    
    def __init__(self, db_name="money_exchange.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.create_tables()

    def create_tables(self):
        """Creates the three required tables for the system."""
        cursor = self.conn.cursor()
        
        # Using executescript for cleaner multi-table creation
        cursor.executescript('''
            CREATE TABLE IF NOT EXISTS Customers (
                CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                Email TEXT UNIQUE,
                Phone TEXT
            );

            CREATE TABLE IF NOT EXISTS Currencies (
                CurrencyCode TEXT PRIMARY KEY,
                CurrencyName TEXT,
                ExchangeRateToUSD REAL NOT NULL
            );

            CREATE TABLE IF NOT EXISTS Transactions (
                TransactionID INTEGER PRIMARY KEY AUTOINCREMENT,
                CustomerID INTEGER,
                FromCurrency TEXT,
                ToCurrency TEXT,
                AmountIn REAL,
                AmountOut REAL,
                Date TEXT,
                FOREIGN KEY(CustomerID) REFERENCES Customers(CustomerID),
                FOREIGN KEY(FromCurrency) REFERENCES Currencies(CurrencyCode),
                FOREIGN KEY(ToCurrency) REFERENCES Currencies(CurrencyCode)
            );
        ''')
        self.conn.commit()

    def get_connection(self):
        """Returns the active connection for other classes to use."""
        return self.conn

    def close(self):
        """Safely closes the database connection."""
        self.conn.close()