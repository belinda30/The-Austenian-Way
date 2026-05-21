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
with open('pickles/v2_top20feat.pkl', 'rb') as f:
    v2_top20feat = pickle.load(f)

# Load pickled V1 objects
with open('pickles/v1_top20feat.pkl', 'rb') as f:
    v1_top20feat = pickle.load(f)

st.title("🔡 Top Features")

tab1, tab2 = st.tabs(["V2 – Without Proper Nouns", "V1 – With Proper Nouns"])

with tab1:
    fig, ax = plt.subplots(figsize=(7,9))
    sns.barplot(data=v2_top20feat,
            x='coefficient',
            y=v2_top20feat.index,
            hue='class',
            palette={'austen': 'darkseagreen', 'contemporary': 'thistle'},
            ax=ax)
    ax.set_title('Top 20 Most Distinctive Words - Austen vs. Contemporary (without Proper Nouns)')
    ax.set_xlabel('TF-IDF Coefficient')
    ax.set_ylabel('Word')
    st.pyplot(fig)
    st.write("""Negative Coefficient = Austen | Positive Coefficient = Contemporary
                """)
    st.divider()
    st.markdown("""**Austen's Signature**\n
*Function Words & Modal Verbs:*\n
- be, it, not, do, and, could, must, in, of, on, there – these are the invisible glue of language
- very, such, quite, always, all – intensifiers and qualifiers that reflect her ironic, hedging style\n
*Domestic Words:*
- sister, brother – reflect her domestic, family-centred world
    """)
    st.divider()
    st.markdown("""**Contemporaries' Signature**\n
*Content & Status Words:*\n
- lordship, ladyship, castle, passion, desire, servant – Aristocratic register
- upon, yet, which, that, why, who – more formal, elevated sentence constructions
    """)
    st.divider()
    st.markdown("""**The Key Contrast**\n
- Austen writes **psychologically**; her style lives in the modal verbs and qualifiers that express thought and feeling indirectly
- Her contemporaries write **dramatically**; their style lives in nouns of status, setting and emotion
    """)

with tab2:
    fig, ax = plt.subplots(figsize=(7,9))
    sns.barplot(data=v1_top20feat,
            x='coefficient',
            y=v1_top20feat.index,
            hue='class',
            palette={'austen': 'darkseagreen', 'contemporary': 'thistle'},
            ax=ax)
    ax.set_title('Top 20 Most Distinctive Words - Austen vs. Contemporary (with Proper Nouns)')
    ax.set_xlabel('TF-IDF Coefficient')
    ax.set_ylabel('Word')
    st.pyplot(fig)