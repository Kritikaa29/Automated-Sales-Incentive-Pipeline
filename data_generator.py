import pandas as pd
from faker import Faker
import random
import time

fake = Faker()

def generate_sales_data(num_records):
    print(f"Generating {num_records} records...")
    data = []
    
    regions = ['North', 'South', 'East', 'West']
    products = ['Enterprise License', 'Cloud Storage', 'Basic Plan', 'Hardware Setup']
    
    for _ in range(num_records):
        record = {
            'Emp_ID': random.randint(100, 150),
            'Name': fake.name(),
            'Region': random.choice(regions),
            'Sale_Date': fake.date_between(start_date='-1y', end_date='today').isoformat(),
            'Revenue': round(random.uniform(5000, 150000), 2),
            'Product': random.choice(products)
        }
        data.append(record)
        
    df = pd.DataFrame(data)
    return df

# Generate 10,000 rows
sales_df = generate_sales_data(10000)
print(sales_df.head())
# Compress and save the payload
output_file = 'compressed_sales_data.csv.gz'
sales_df.to_csv(output_file, index=False, compression='gzip')
print(f"Data successfully compressed and saved to {output_file}")

from sqlalchemy import create_engine

# Paste your complete Supabase connection string here (with your real password)
DATABASE_URL = "postgresql://postgres:eNqLtBuLNUWbYcQh@db.njhvmueyszlgdoewttxp.supabase.co:5432/postgres"

print("Connecting to Supabase cloud database...")
engine = create_engine(DATABASE_URL)

# Push the 10,000 rows directly into a table named 'sales_data'
print("Uploading data to the cloud...")
sales_df.to_sql('sales_data', con=engine, if_exists='replace', index=False)

print("Success! Your 10,000 rows are now live in the cloud database.")