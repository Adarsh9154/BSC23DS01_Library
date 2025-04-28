import streamlit as st
import pandas as pd

# Initialize an empty ledger as a list of dictionaries
ledger = []

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

# Function to display the ledger using a Pandas DataFrame
def display_ledger():
    st.write("\n--- LIBRARY BOOK LEDGER ---")
    if not ledger:
        st.write("Ledger is currently empty.")
        return

    df = pd.DataFrame(ledger)  # Create DataFrame from ledger
    st.dataframe(df)  # Display DataFrame in Streamlit

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
