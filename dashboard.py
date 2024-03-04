import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "final_dataset_copy.pkl"
data = pd.read_pickle(file_path)

# Title
st.title('Analisis Data E-Commerce')
st.subheader('Silahkan untuk memilih menu hasil analisis di samping')

# Sidebar title
st.sidebar.title("Dashboard Menu")

# Function to display top 5 product categories by order count
def top_5_product_categories():
    st.header("Top 5 Product Categories by Order Count")
    top_categories = data['product_category_name'].value_counts().head(5)
    st.bar_chart(top_categories)

# Function to display distribution of review scores
def review_score_distribution():
    st.header("Distribution of Review Scores")
    review_distribution = data['review_score'].value_counts().sort_index()
    fig, ax = plt.subplots()
    ax.pie(review_distribution, labels=review_distribution.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

# Button to trigger actions
if st.sidebar.button("Show Top 5 Product Categories"):
    top_5_product_categories()

if st.sidebar.button("Show Review Score Distribution"):
    review_score_distribution()
