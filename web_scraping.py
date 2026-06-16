import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# TASK 1: WEB SCRAPING
# ==========================

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

titles = []
prices = []

for book in soup.find_all("article", class_="product_pod"):
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text.replace("£", "")

    titles.append(title)
    prices.append(float(price))

# Create DataFrame
df = pd.DataFrame({
    "Book_Title": titles,
    "Price": prices
})

# Save dataset
df.to_csv("books_data.csv", index=False)

print("Web Scraping Completed Successfully!")
print("\nFirst 5 Records:")
print(df.head())

# ==========================
# TASK 2: EDA
# ==========================

print("\n----- Exploratory Data Analysis -----")

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nHighest Priced Book:")
print(df.loc[df['Price'].idxmax()])

print("\nLowest Priced Book:")
print(df.loc[df['Price'].idxmin()])

print("\nAverage Price:", round(df['Price'].mean(), 2))

# ==========================
# TASK 3: DATA VISUALIZATION
# ==========================

# Top 10 expensive books
top_books = df.nlargest(10, "Price")

plt.figure(figsize=(10, 5))
plt.bar(top_books["Book_Title"], top_books["Price"])
plt.title("Top 10 Most Expensive Books")
plt.xlabel("Book Title")
plt.ylabel("Price (£)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Price Distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Price"], bins=10)
plt.title("Book Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

print("\nData Visualization Completed!")
