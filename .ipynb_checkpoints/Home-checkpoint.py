import streamlit as st
import base64

# Decoding JPG
def get_base64_image(image_path):
    with open(image_path, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Lady Susan Manuscript for Background
img = get_base64_image('Lady_Susan_Manuscript_pg10.jpg')

# Manuscript as Background settings + Background colour
st.markdown(f"""
<style>
.stApp {{
    background-color: #E8DFC8;
}}
.stApp::before {{
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url('data:image/jpeg;base64,{img}');
    background-size: cover;
    background-position: center;
    opacity: 0.15;
    z-index: 0;
}}
</style>
""", unsafe_allow_html=True)

# Text Background Colour
st.markdown("""
<style>
.block-container {
    background-color: rgba(255, 255, 255, 0.5);
    border-radius: 10px;
    padding: 2rem;
}
</style>
""", unsafe_allow_html=True)

st.title("The Austenian Way 📜✍🏼")
st.subheader("Analysing and Comparing Jane Austen's & her Contemporaries' Writing Styles")
st.write("""
Welcome to the Austenian Way!

If you have wondered, like me, why exactly Jane Austen, out of all the writers of the Regency era, stuck out for so many people, and is to this day as popular as she is, well then, my friend, you are exactly in the right place!

We will discover if there is a distinct difference in style between her and her fellow contemporary authors, or rather authoresses to be specific, as I have only chosen to compare her to other female authors of her time.
""")
st.divider()
st.subheader("📋 About the Project")
st.markdown("""
❓ **Research Question:** Is Austen's writing style statistically distinctive enough that a machine can recognise it?

📚 **Dataset:**

Six Austen novels:
- Sense and Sensibility (1811)
- Pride and Prejudice (1813)
- Mansfield Park (1814)
- Emma (1815)
- Northanger Abbey (1817, posthumous)
- Persuasion (1817, posthumous)

Seven Contemporary novels:
- Evelina (1778) by Fanny Burney
- Emmeline (1788) by Charlotte Smith
- A Sicilian Romance (1790) by Ann Radcliffe
- Belinda (1801) by Maria Edgeworth
- The Wild Irish Girl (1806) by Sydney Owenson
- Self-Control (1811) by Mary Brunton
- Frankenstein (1818) by Mary Shelley

🧮 **Methodology:**
- TF-IDF vectorisation (Term Frequency-Inverse Document Frequency)
- Two Models: Logistic Regression & Random Forest
- Two versions: with and without proper nouns
""")
st.divider()
st.subheader("🗺️ What you'll find here")
st.markdown("""
- 📊 **Model Performance** – Confusion matrices and accuracy scores for both versions and models
- 🔡 **Top Features** – The most distinctive words that separate Austen from her contemporaries
- ❌ **Error Analysis** – Which novels fooled the model and why
- ✍🏼 **Interactive Predictor** – Paste any text and see if it reads like Austen!
- 📜 **Conclusion** – The Answer
""")
st.caption("Data sourced from Project Gutenberg. Built with Python, scikit-learn and Streamlit.")