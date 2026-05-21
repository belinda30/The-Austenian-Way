import streamlit as st
import pickle
import seaborn as sns
import matplotlib.pyplot as plt

# Background Colour
st.markdown("""
<style>
.stApp {
    background-color: #E8DFC8;
}
</style>
""", unsafe_allow_html=True)

# Text Background Colour
st.markdown("""
<style>
.block-container {
    background-color: rgba(255, 255, 255, 0.3);
    border-radius: 10px;
    padding: 2rem;
}
</style>
""", unsafe_allow_html=True)

# Load pickled V2 objects
with open('pickles/v2_ea_df.pkl', 'rb') as f:
    v2_ea_df = pickle.load(f)

# Load pickled V1 objects
with open('pickles/v1_ea_df.pkl', 'rb') as f:
    v1_ea_df = pickle.load(f)

st.title("❌ Error Analysis")

tab1, tab2 = st.tabs(["V2 – Without Proper Nouns", "V1 – With Proper Nouns"])

with tab1:
    title_counts = v2_ea_df['title'].value_counts().reset_index()
    title_counts.columns = ['title', 'count']
    
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.barplot(data=title_counts,
                x='count',
                y='title',
                color='darkseagreen',
                ax=ax)
    ax.set_title('Misclassified Chunks per Novel (without Proper Nouns)')
    ax.set_xlabel('Number of Misclassified Chunks')
    ax.set_ylabel('Novel')
    st.pyplot(fig)
    st.divider()
    st.subheader("Most and Least Misclassified Novels:")
    st.markdown("""
The bar chart above shows the number of misclassified chunks per novel in **V2 (without proper nouns)**. 
Notably, all 13 novels appear — meaning every novel had at least some misclassified chunks, suggesting the model struggles more consistently without proper nouns to rely on.
    
**Most misclassified:**
- **Belinda** (Maria Edgeworth) — 50 chunks — unsurprising given Edgeworth was a direct influence on Austen, and their domestic social fiction shares many stylistic features
- **Persuasion** (Jane Austen) — 48 chunks — one of Austen's most atypical novels, with a more melancholic and lyrical tone than her others
    
**Least misclassified:**
- **A Sicilian Romance** (Ann Radcliffe) — 32 chunks — its Gothic vocabulary is distinctive enough to separate it clearly from Austen
    """)
    st.divider()
    st.subheader("Interactive Table")
    st.dataframe(v2_ea_df[['title', 'true_label', 'predicted_label', 'chunk']])


with tab2:
    title_counts = v1_ea_df['title'].value_counts().reset_index()
    title_counts.columns = ['title', 'count']
    
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.barplot(data=title_counts,
                x='count',
                y='title',
                color='thistle',
                ax=ax)
    ax.set_title('Misclassified Chunks per Novel (with Proper Nouns)')
    ax.set_xlabel('Number of Misclassified Chunks')
    ax.set_ylabel('Novel')
    st.pyplot(fig)
    st.divider()
    st.subheader("Most and Least Misclassified Novels:")
    st.markdown("""
The bar chart above shows the number of misclassified chunks per novel in **V1 (with proper nouns)**.
The overall range is tighter (35–47 chunks), suggesting proper nouns help the model more consistently.
    
**Most misclassified:**
- **Persuasion** (Jane Austen) — 47 chunks — consistently the hardest Austen novel for the model across both versions
- **Sense and Sensibility** & **Belinda** — tied at ~44 chunks each
    
**Least misclassified:**
- **Northanger Abbey** (Jane Austen) — 35 chunks — its Gothic parody vocabulary is distinctive enough to be reliably identified
- **Mansfield Park** & **A Sicilian Romance** — ~36 chunks each
    
**Notable finding:** Persuasion appears at the top of both V1 and V2 — making it consistently the most difficult novel for the model to classify correctly!
    """)
    st.divider()
    st.subheader("Interactive Table")
    st.dataframe(v1_ea_df[['title', 'true_label', 'predicted_label', 'chunk']])