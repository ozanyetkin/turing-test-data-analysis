import pandas as pd

listings = pd.read_csv("https://storage.googleapis.com/public-data-337819/listings%202%20reduced.csv",low_memory=False)
reviews = pd.read_csv("https://storage.googleapis.com/public-data-337819/reviews%202%20reduced.csv",low_memory=False)

print(listings.head().to_markdown())
print(reviews.head().to_markdown())

print(listings.head())

