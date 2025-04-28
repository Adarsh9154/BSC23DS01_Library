import streamlit as st

# Initialize an empty ledger
ledger = []

# Function to add a book to the ledger
def add_book(book_name, price):
    ledger.append({"book_name": book_name, "price": price})
    st.success(f"Book '{book_name}' added successfully.")

# Function to display the ledger
def display_ledger():
    st.write("\n--- LIBRARY BOOK LEDGER ---")
    if not ledger:
        st.write("Ledger is currently empty.")  # Handle empty ledger case
        return
    for item in ledger:
        st.write(f"Book Name: {item['book_name']}, Price: {item['price']}")


# Streamlit app
st.title("Library Book Issuing Ledger")

# Input fields for adding a book
book_name = st.text_input("Book Name:")
price = st.number_input("Price:", min_value=0, step=1)

# Button to add the book to the ledger
if st.button("Add Book"):
    if book_name and price:  # Check if both inputs are provided
      add_book(book_name, price)
    else:
      st.error("Please fill in both book name and price.")

# Display the ledger
display_ledger()
