import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time

# --- 1. Title ---
st.title("🎯 Streamlit Top 20 Functions Demo")

# --- 2. Header ---
st.header("📌 Headers and Text")

# --- 3. Subheader ---
st.subheader("This is a subheader.")

# --- 4. Text ---
st.text("This is plain text.")

# --- 5. Markdown ---
st.markdown("**This text is bold using markdown!**\n\n*And this is italicized.*")

# --- 6. Write ---
st.write("Using `st.write()` to print numbers, text, or even DataFrames:")

# --- 7. Code ---
st.code("print('Hello, World!')", language='python')

# --- 8. LaTeX ---
st.latex(r'E = mc^2')

# --- 9. Text Input ---
name = st.text_input("Enter your name")
if name:
    st.write(f"Hello, {name}!")

# --- 10. Text Area ---
bio = st.text_area("Tell us about yourself")
if bio:
    st.success("Thanks for sharing!")

# --- 11. Number Input ---
age = st.number_input("Enter your age", min_value=0, max_value=120)

# --- 12. Slider ---
value = st.slider("Rate your experience", 0, 10, 5)

# --- 13. Selectbox ---
lang = st.selectbox("Choose a programming language", ["Python", "Java", "C++"])

# --- 14. Multiselect ---
tools = st.multiselect("Select the tools you use", ["VSCode", "PyCharm", "Jupyter", "GitHub"])

# --- 15. Checkbox ---
agree = st.checkbox("I agree to the terms and conditions")

# --- 16. Radio ---
gender = st.radio("Select gender", ["Male", "Female", "Other"])

# --- 17. Button ---
if st.button("Click me"):
    st.balloons()
    st.write("🎉 Button clicked!")

# --- 18. File Uploader ---
uploaded_file = st.file_uploader("Upload a CSV file")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.dataframe(df)

# --- 19. DataFrame Display ---
st.write("Here's a sample DataFrame:")
sample_df = pd.DataFrame(np.random.randn(5, 3), columns=["A", "B", "C"])
st.dataframe(sample_df)

# --- 20. Charts ---
st.write("Here's a line chart:")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['X', 'Y', 'Z'])
st.line_chart(chart_data)

# ------------------------
# 🎁 BONUS FUNCTIONS
# ------------------------

st.header("🎁 Bonus Functions")

# --- Image ---
st.subheader("Image Display")
image = Image.new("RGB", (100, 100), color="purple")
st.image(image, caption="Sample Image")

# --- Audio ---
st.subheader("Audio Player")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

# --- Video ---
st.subheader("Video Player")
st.video("https://www.w3schools.com/html/mov_bbb.mp4")

# --- Sidebar ---
st.sidebar.title("Sidebar Example")
st.sidebar.radio("Choose page", ["Home", "Profile", "Settings"])

# --- Spinner ---
st.subheader("Spinner Example")
with st.spinner("Loading for 3 seconds..."):
    time.sleep(3)
st.success("Done!")

# --- Progress Bar ---
st.subheader("Progress Bar")
progress = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progress.progress(i + 1)

# --- Metric ---
st.subheader("Key Metric")
st.metric(label="Active Users", value=1200, delta="+100")

# --- Session State Example ---
if "counter" not in st.session_state:
    st.session_state.counter = 0
if st.button("Increment Counter"):
    st.session_state.counter += 1
st.write("Counter value:", st.session_state.counter)
