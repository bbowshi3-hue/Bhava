import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load API key from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Page settings
st.set_page_config(
    page_title="FitBuddy",
    page_icon="💪",
    layout="centered"
)

# Title
st.title("💪 FitBuddy")
st.subheader("AI Fitness Plan Generator")

st.write("Create a personalized fitness plan using Gemini AI.")

# User inputs
name = st.text_input("👤 Your Name")

age = st.number_input(
    "🎂 Age",
    min_value=13,
    max_value=100,
    value=20
)

goal = st.selectbox(
    "🎯 Fitness Goal",
    [
        "Weight Loss",
        "Muscle Gain",
        "Build Strength",
        "Improve Fitness",
        "General Health"
    ]
)

level = st.selectbox(
    "🏋️ Fitness Level",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

days = st.slider(
    "📅 Workout Days per Week",
    min_value=1,
    max_value=7,
    value=3
)

duration = st.slider(
    "⏱️ Workout Duration (minutes)",
    min_value=15,
    max_value=120,
    value=30,
    step=5
)

equipment = st.selectbox(
    "🏠 Available Equipment",
    [
        "No Equipment",
        "Dumbbells",
        "Resistance Bands",
        "Home Gym",
        "Full Gym"
    ]
)

diet = st.selectbox(
    "🥗 Diet Preference",
    [
        "No Preference",
        "Vegetarian",
        "Non-Vegetarian",
        "Vegan"
    ]
)

# Generate button
if st.button("✨ Generate My Fitness Plan"):

    if not name:
        st.warning("Please enter your name.")
    else:

        prompt = f"""
        Create a simple and practical fitness plan for the following person:

        Name: {name}
        Age: {age}
        Fitness Goal: {goal}
        Fitness Level: {level}
        Workout Days per Week: {days}
        Workout Duration: {duration} minutes
        Available Equipment: {equipment}
        Diet Preference: {diet}

        Provide:

        1. Weekly workout schedule
        2. Exercises for each workout day
        3. Sets and repetitions
        4. Rest recommendations
        5. Simple nutrition suggestions
        6. Recovery and sleep tips

        Keep the plan beginner-friendly and clearly organized.

        Do not diagnose medical conditions or provide medical treatment.
        Mention that the user should consult a qualified professional
        if they have injuries, medical conditions, or concerns.
        """

        try:
            with st.spinner("🤖 FitBuddy is creating your plan..."):

                response = client.models.generate_content(
                    model="gemini-3.5-flash",
                    contents=prompt
                )

            st.success("🎉 Your personalized fitness plan is ready!")

            st.markdown("## 🏆 Your FitBuddy Plan")
            st.markdown(response.text)

        except Exception as e:
            st.error("Something went wrong while connecting to Gemini.")
            st.write(str(e))
