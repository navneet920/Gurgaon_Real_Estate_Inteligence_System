import streamlit as st
from price_prediction import run_prediction
from Analytics_app import Analysis
from recomendation_system import recommended_system

# Set Streamlit page configuration
st.set_page_config(page_title="Home - Gurgaon Housing Project", layout="centered")

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Sidebar buttons for page navigation
st.sidebar.title("Navigation")
if st.sidebar.button("Home"):
    st.session_state.page = "Home"
if st.sidebar.button("Prediction"):
    st.session_state.page = "Prediction"
if st.sidebar.button("Analytics"):
    st.session_state.page = "Analytics"
if st.sidebar.button("Recommendation"):
    st.session_state.page = "Recommendation"
if st.sidebar.button("Insights"):
    st.session_state.page = "Insights"
if st.sidebar.button("About"):
    st.session_state.page = "About"

# Define each page as a function
def show_home_page():
    st.title("🏡 Gurgaon Housing Intelligence")
    st.subheader("An AI-Powered Real Estate Analysis & Prediction Platform")
    st.markdown("""
    Welcome to the homepage of our **Gurgaon House and Flat Prediction** project!  
    This application empowers users with intelligent tools to explore, analyze, and predict property trends in Gurgaon.

    ---

    ### 📌 Project Overview

    Our platform is designed to assist home buyers, investors, and real estate professionals with:

    - 💡 **Accurate Price Prediction**
    - 📊 **Data Analytics**
    - 🤝 **Property Recommendation System**
    - 📍 **Actionable Insights**

    ---

    ### 🔍 Key Features
    - 📈 Data Visualization  
    - 🤖 AI/ML Predictions  
    - 🧠 Interactive Dashboards  
    - 📁 Data Upload & Download  
    - 📌 Location-wise Market Insights  
    - 🏷️ Filter-based Property Recommendations

    ---
    """)

def show_prediction_page():
    run_prediction()

def show_analytics_page():
    Analysis()

def show_recommendation_page():
    recommended_system()

def show_insights_page():
    st.title("📍 Market Insights")
    st.write("**Insights Dashboard** coming soon...")

def show_about_page():
    st.title("ℹ️ About the Project")
    st.write("**About the Project** coming soon...")

# Display the current page
if st.session_state.page == "Home":
    show_home_page()
elif st.session_state.page == "Prediction":
    show_prediction_page()
elif st.session_state.page == "Analytics":
    show_analytics_page()
elif st.session_state.page == "Recommendation":
    show_recommendation_page()
elif st.session_state.page == "Insights":
    show_insights_page()
elif st.session_state.page == "About":
    show_about_page()

# Footer
st.markdown("---")
st.markdown("Created with ❤️ using Streamlit | Powered by AI & Data Science")
