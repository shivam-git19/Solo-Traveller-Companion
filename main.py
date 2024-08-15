import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set the Google API key
os.environ['GOOGLE_API_KEY'] = "AIzaSyAtd2CJjGr-Uf41z2tcej4vImDEdIeWVLM"

# Configure the generative AI model
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-1.5-flash')


accommodation_options = [
    {
        "name": "Manali Backpackers Hostel",
        "type": "hostel",
        "location": "Manali",
        "safety_ratings": "high",
        "amenities": ["Wi-Fi", "24/7 reception", "mountain view dorms"],
        "proximity_to_attractions": "central"
    },
    {
        "name": "Shimla Homestay",
        "type": "homestay",
        "location": "Shimla",
        "safety_ratings": "high",
        "amenities": ["Wi-Fi", "local cuisine meals", "guided tours"],
        "proximity_to_attractions": "near The Ridge"
    },
    {
        "name": "Zostel Leh",
        "type": "hostel",
        "location": "Leh",
        "safety_ratings": "high",
        "amenities": ["Wi-Fi", "common room", "mountain view dorms"],
        "proximity_to_attractions": "central"
    },
    {
        "name": "Nubra Organic Retreat",
        "type": "retreat",
        "location": "Nubra Valley",
        "safety_ratings": "high",
        "amenities": ["organic meals", "guided tours", "campfire evenings"],
        "proximity_to_attractions": "near Nubra River"
    },
    {
        "name": "Fort Kochi Hostel",
        "type": "hostel",
        "location": "Fort Kochi",
        "safety_ratings": "high",
        "amenities": ["Wi-Fi", "community kitchen", "city tours"],
        "proximity_to_attractions": "central"
    },
    {
        "name": "Munnar Homestay",
        "type": "homestay",
        "location": "Munnar",
        "safety_ratings": "high",
        "amenities": ["Wi-Fi", "home-cooked meals", "tea plantation tours"],
        "proximity_to_attractions": "near tea plantations"
    }
]

activities_and_attractions = [
    {
        "name": "Rohtang Pass",
        "type": "outdoor",
        "location": "Near Manali",
        "safety_considerations": "cold, ensure proper clothing, safe with guides",
        "best_time_to_visit": "morning"
    },
    {
        "name": "Mall Road",
        "type": "cultural",
        "location": "Shimla",
        "safety_considerations": "crowded, keep belongings secure",
        "best_time_to_visit": "evening"
    },
    {
        "name": "Great Himalayan National Park",
        "type": "nature",
        "location": "Kullu",
        "safety_considerations": "guided hikes recommended, safe",
        "best_time_to_visit": "early morning"
    },
{
            "name": "Pangong Lake",
            "type": "nature",
            "location": "Pangong Tso",
            "safety_considerations": "high altitude, carry enough water, safe with guides",
            "best_time_to_visit": "early morning"
        },
        {
            "name": "Thiksey Monastery",
            "type": "cultural",
            "location": "Leh",
            "safety_considerations": "well-maintained, safe for solo travelers",
            "best_time_to_visit": "morning"
        },
        {
            "name": "Khardung La Pass",
            "type": "adventure",
            "location": "Near Leh",
            "safety_considerations": "extreme cold, high altitude, travel with a guide",
            "best_time_to_visit": "afternoon"
        },
    {
        "name": "Backwaters of Alleppey",
        "type": "nature",
        "location": "Alleppey",
        "safety_considerations": "safe with guides, avoid monsoon season",
        "best_time_to_visit": "morning"
    },
    {
        "name": "Munnar Tea Plantations",
        "type": "nature",
        "location": "Munnar",
        "safety_considerations": "safe, guided tours available",
        "best_time_to_visit": "early morning"
    },
    {
        "name": "Fort Kochi",
        "type": "cultural",
        "location": "Kochi",
        "safety_considerations": "crowded during festivals, safe",
        "best_time_to_visit": "afternoon"
    }
]

food_and_dining = [
    {
        "name": "Johnson's Café",
        "type": "restaurant",
        "location": "Manali",
        "safety_considerations": "popular, solo-friendly",
        "cuisine": "Himachali, continental",
        "dietary_options": ["vegetarian options available"]
    },
    {
        "name": "Café Simla Times",
        "type": "café",
        "location": "Shimla",
        "safety_considerations": "well-reviewed, family-friendly",
        "cuisine": "Indian, global fusion"
    },
{
            "name": "The Tibetan Kitchen",
            "type": "restaurant",
            "location": "Leh",
            "safety_considerations": "highly recommended, solo-friendly",
            "cuisine": "Tibetan, Ladakhi",
            "dietary_options": ["vegetarian options available"]
        },
        {
            "name": "Gesmo Restaurant",
            "type": "café",
            "location": "Leh",
            "safety_considerations": "popular with tourists, safe",
            "cuisine": "Indian, continental"
        },
{
            "name": "Dhe Puttu",
            "type": "restaurant",
            "location": "Kochi",
            "safety_considerations": "highly reviewed, family-friendly",
            "cuisine": "Kerala, South Indian",
            "dietary_options": ["vegetarian options available"]
        },
        {
            "name": "Sree Krishna Inn",
            "type": "restaurant",
            "location": "Kochi",
            "safety_considerations": "safe, popular with locals",
            "cuisine": "South Indian, vegetarian"
        }
]

# Streamlit UI

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-color: #30317F;
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Solo Traveller Companion")

checkin_date = st.date_input("Enter Travel date from")
checkout_date = st.date_input("Enter date To")
enter_city = st.text_input("Enter City")

if st.button("Generate Itinerary"):
    context = f"""
        You are a travel agent who makes itineraries for travelers.The city is {enter_city}. The check-in date is {checkin_date} and the check-out date is {checkout_date}.
        The traveler is visiting Himachal or Leh or Kerala. Below are the accommodation options, activities and attractions, and food and dining options available:
        
        City Entered: {enter_city}
        Accommodation options: {accommodation_options}
        Activities and attractions: {activities_and_attractions}
        Food and dining options: {food_and_dining}

        Please generate a travel itinerary for city entered, that takes into account the traveler's preferences and schedule activities appropriately during their stay. 
        Make sure to include recommendations for safe areas and dining options that cater to dietary restrictions.
    """

    pred = model.generate_content(context)
    st.text(pred.text.replace("**", ""))

