import pandas as pd
import sqlite3

# Load the CSV
csv = pd.read_csv("/Users/enzowurtele/Desktop/DATABASES/Sample-Superstore.csv", encoding='latin1')

# Create DataFrames
customer = csv[['Customer ID', 'Customer Name', 'City', 'State', 'Postal Code', 'Region', 'Segment']]

orders = csv[['Order ID','Customer ID', 'Order Date', 'Ship Date', 'Ship Mode']]

products = csv[['Product ID', 'Category', 'Sub-Category', 'Product Name']]

order_details = csv[['Order ID', 'Product ID', 'Sales', 'Quantity', 'Discount', 'Profit']]

customer_clean = customer.drop_duplicates()

# Connect to SQLite database
conn = sqlite3.connect('SuperStore.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Customer (
CustomerID TEXT PRIMARY KEY,
CustomerName TEXT,
City TEXT,
State TEXT,
PostalCode TEXT,
Region TEXT,
Segment TEXT
);
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Orders (
CustomerID TEXT,
OrderID TEXT PRIMARY KEY,
OrderDate TEXT,
ShipDate TEXT,
ShipMode TEXT,
FOREIGN KEY (CustomerID) REFERENCES customer (CustomerID)
);
''')

cursor.execute(''' CREATE TABLE IF NOT EXISTS Products (
ProductID TEXT PRIMARY KEY,
Category TEXT,
SubCategory TEXT,
ProductName TEXT
);
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Order_details (
OrderID TEXT,
ProductID TEXT,
Sales REAL,
Quantity INTEGER,
Discount REAL,
Profit REAL,
FOREIGN KEY (OrderID) REFERENCES orders (OrderID),
FOREIGN KEY (ProductID) REFERENCES products (ProductID)
);
''')

customer_clean.to_sql('Customer', conn, if_exists='replace', index=False)

orders.to_sql('Orders', conn, if_exists='replace', index=False)

products.to_sql('Products', conn, if_exists='replace', index=False)

order_details.to_sql('Order_details', conn, if_exists='replace', index=False)

