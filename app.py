import streamlit as st
import pandas as pd

# Function to add a row to the DataFrame
def add_row(first_name, last_name, age):
    new_row = {'First Name': first_name, 'Last Name': last_name, 'Age': age}
    return new_row

# Main Streamlit app
def main():
    st.title('Table Creation and Query App')

    # Initialize an empty DataFrame to store the data
    data = pd.DataFrame(columns=['First Name', 'Last Name', 'Age'])

    # Sidebar for adding rows
    st.sidebar.header('Add a Row')
    first_name = st.sidebar.text_input('First Name')
    last_name = st.sidebar.text_input('Last Name')
    age = st.sidebar.number_input('Age', min_value=0, max_value=150)

    if st.sidebar.button('Add'):
        new_row = add_row(first_name, last_name, age)
        data = data.append(new_row, ignore_index=True)
        st.sidebar.success('Row added successfully!')

    # Sidebar for querying data
    st.sidebar.header('Query Data')
    query_first_name = st.sidebar.text_input('First Name for Query')
    query_last_name = st.sidebar.text_input('Last Name for Query')
    min_age = st.sidebar.number_input('Minimum Age for Query', min_value=0, max_value=150)
    max_age = st.sidebar.number_input('Maximum Age for Query', min_value=0, max_value=150)

    if st.sidebar.button('Query'):
        query_result = data[(data['First Name'] == query_first_name) & (data['Last Name'] == query_last_name) & (data['Age'] >= min_age) & (data['Age'] <= max_age)]
        st.write(query_result)

    # Display the current table
    st.header('Current Table')
    st.write(data)

if __name__ == "__main__":
    main()
