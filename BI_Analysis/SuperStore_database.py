import pandas as pd
import sqlite3

# Load the CSV
csv = pd.read_csv("/Users/enzowurtele/Desktop/DATABASES/Sample-Superstore.csv", encoding='latin1')

# Create DataFrames
customer = csv[['Customer ID', 'Customer Name', 'City', 'State', 'Postal Code', 'Region', 'Segment']]
orders = csv[['Order ID', 'Order Date', 'Ship Date', 'Ship Mode']]
products = csv[['Product ID', 'Category', 'Sub-Category', 'Product Name']]
order_details = csv[['Order ID', 'Product ID', 'Sales', 'Quantity', 'Discount', 'Profit']]

# Connect to SQLite database
conn = sqlite3.connect('superstore.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Customer (
CustomerID TEXT PRIMARY KEY,
CustomerName TEXT,
City TEXT,
State TEXT,
PostalCode TEXT,
Region TEXT,
Segment TEXT
)
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
ProductID TEXT PRIMARY KEY,
Category TEXT,
SubCategory TEXT,
ProductName TEXT
)
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Orders (
OrderID TEXT PRIMARY KEY,
OrderDate TEXT,
ShipDate TEXT,
ShipMode TEXT
)
''')




