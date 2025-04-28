import streamlit as st
import pandas as pd
import json

# Initialize an empty ledger as a list of dictionaries
ledger = []

# Load data from GitHub if available, otherwise use an empty ledger.
try:
    import requests
    url = "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPOSITORY/main/ledger.json"  # Replace with your GitHub repo details
    response = requests.get(url)
    response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
    ledger = json.loads(response.text)
except (requests.exceptions.RequestException, json.JSONDecodeError, FileNotFoundError):
    st.warning("Could not load ledger from GitHub. Starting with an empty ledger.")

# Function to add a book to the ledger with additional columns
def add_book(book_name, price, author, isbn, issued_to):
    ledger.append({
        "book_name": book_name,
        "price": price,
        "author": author,
        "isbn": isbn,
        "issued_to": issued_to
    })
    st.success(f"Book '{book_name}' added successfully.")
    # Save updated ledger to GitHub
    save_ledger_to_github()

# Function to display the ledger using a Pandas DataFrame
def display_ledger():
    st.write("\n--- LIBRARY BOOK LEDGER ---")
    if not ledger:
        st.write("Ledger is currently empty.")
        return
    df = pd.DataFrame(ledger)  # Create DataFrame from ledger
    st.dataframe(df)  # Display DataFrame in Streamlit

# Function to save the ledger to a JSON file in GitHub
def save_ledger_to_github():
    try:
        import requests
        from github import Github

        # Replace with your GitHub personal access token
        github_token = "YOUR_GITHUB_TOKEN"
        g = Github(github_token)
        repo = g.get_user().get_repo("YOUR_REPOSITORY") # Replace with your repository name
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
