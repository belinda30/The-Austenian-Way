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

# Load pickled V1 objects
with open('pickles/v1_top20feat.pkl', 'rb') as f:
    v1_top20feat = pickle.load(f)

# Load pickled V2 objects
with open('pickles/v2_top20feat.pkl', 'rb') as f:
    v2_top20feat = pickle.load(f)

st.title("🔡 Top Features")

tab1, tab2 = st.tabs(["V1 – With Proper Nouns", "V2 – Without Proper Nouns"])

with tab1:
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

with tab2:
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
*Function Words:*\n
- be, it, not, do, and, in, of, on, there – the invisible glue of language, they don't carry meaning on their own but determine how ideas are connected and structured.\n
*Modal Verbs:*\n
- could, must – express degrees of certainty, obligation and social nuance, carrying psychological and moral weight in Austen's prose.\n
*Intensifiers & Qualifiers:*\n
- very, such, quite, always, all – reflect her ironic, hedging style, softening or emphasising judgments without being direct about them.\n
*Domestic Words:*
- sister, brother – reflect her domestic, family-centred world
    """)
    st.divider()
    st.markdown("""**Contemporaries' Signature**\n
*Nouns of Status & Setting:*\n
- lordship, ladyship, castle, servant – aristocratic and Gothic register, describing the physical and social world around characters.\n
*Nouns of Emotion:*\n
- passion, desire – direct, explicit expression of feeling, contrasting with Austen's indirect psychological hedging.\n
*Formal Connectives:*\n
- upon, yet, which, that – elevated, formal sentence constructions reflecting a more extravagant prose style.
    """)
    st.divider()
    st.markdown("""**The Key Contrast**\n
- Austen writes **psychologically**; her style lives in the modal verbs and qualifiers that express thought and feeling indirectly
- Her contemporaries write **dramatically**; their style lives in nouns of status, setting and emotion
    """)