import streamlit as st
import pandas as pd
import json
import requests
from github import Github

# Initialize an empty ledger as a list of dictionaries
ledger = []

# Load data from GitHub if available, otherwise use an empty ledger.
try:
    url = "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPOSITORY/main/ledger.json"  # Update with your details
    response = requests.get(url)
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    ledger = json.loads(response.text)
except (requests.exceptions.RequestException, json.JSONDecodeError, FileNotFoundError):
    st.warning("Could not load ledger from GitHub. Starting with an empty ledger.")

# Function to add a book to the ledger
def add_book(book_name, price, author, isbn, issued_to):
    ledger.append({
        "book_name": book_name,
        "price": price,
        "author": author,
        "isbn": isbn,
        "issued_to": issued_to
    })
    st.success(f"Book '{book_name}' added successfully.")
    save_ledger_to_github()

# Function to save the ledger to a JSON file in GitHub
def save_ledger_to_github():
    try:
        github_token = "YOUR_GITHUB_TOKEN"  # Replace with your GitHub token
        g = Github(github_token)
        repo = g.get_user().get_repo("YOUR_REPOSITORY")  # Replace with your repository name
        contents = repo.get_contents("ledger.json", ref="main")  # Get file content
        repo.update_file(contents.path, "Update ledger", json.dumps(ledger, indent=2), contents.sha, branch="main")
        st.success("Ledger saved to GitHub successfully.")
    except Exception as e:
        st.error(f"Error saving ledger to GitHub: {e}")

# Streamlit app
st.title("Library Book Issuing Ledger")

# Input fields for adding a book
book_name = st.text_input("Book Name:")
price = st.number_input("Price:", min_value=0, step=1)
author = st.text_input("Author:")
isbn = st.text_input("ISBN:")
issued_to = st.text_input("Issued To:")

# Button to add the book to the ledger
if st.button("Add Book"):
    if book_name and price and author and isbn and issued_to:
        add_book(book_name, price, author, isbn, issued_to)
    else:
        st.error("Please fill in all the fields.")

# Display the ledger
display_ledger()
