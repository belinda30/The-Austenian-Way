import streamlit as st
import base64

# Decoding JPG
def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Lady Susan Manuscript for Background
img = get_base64_image("Lady_Susan_Manuscript_pg10.jpg")

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

key_findings = {
     "V1 — With Proper Nouns":[
         "**High accuracy (LR: 98.1%, RF: 91.5%)** — however, proper nouns inflate performance. The model partly recognises character names rather than pure writing style.",
         """**Logistic Regression is the better model** —\n
LR works particularly well with high-dimensional sparse TF-IDF data, which is why it outperforms Random Forest here.""",
         """**The top features are revealing** — \n
Austen's novels revolve around her heroines but equally around male figures, with 'mr' being the second highest Austen feature, reflecting the central role of courtship and marriage in her narratives.""",
         """**The drop between V1 and V2 is meaningful** — 
* LR drops from 98.1% => 95.6% (small, model remains robust) \n 
* RF drops from 91.5% => 84.8% (larger, showing RF relied more heavily on proper nouns)""",
         """**The true answer to the question lies in V2** — \n
however, the character names alone are apparently distinctive enough to be seen as Austen-specific."""
     ],
    "V2 – Without Proper Nouns":[
       """**Strong accuracy (LR: 95.6%, RF: 84.8%)** — \n
even without proper nouns, both models perform well, confirming Austen's style is genuinely distinctive.""",
        """**Logistic Regression remains better model** — \n
removing proper nouns gives a more honest stylometric result, and LR still handles the task robustly.""",
        """***Persuasion* is the hardest novel to classify** — \n
appearing at the top of the misclassification charts in both V1 and V2, suggesting it is Austen's most stylistically atypical novel.""",
       """***Belinda* by Maria Edgeworth is the most confused contemporary novel** — \n
this is a meaningful finding, as Edgeworth was a direct influence on Austen and their domestic social fiction shares many stylistic features, making it genuinely harder for the model to distinguish between the two.""", """See below..."""]}

st.title("📜 Conclusion")
st.subheader("❓ Research Question:")
st.subheader("Is Austen's writing style statistically distinctive enough that a machine can recognise it?")
st.table(key_findings, border="horizontal")
st.divider()
st.subheader("❗️ Answer to the Research Question:")
st.markdown("""#### **YES!** \n
Austen's writing style is statistically distinctive enough that a machine can recognise it. \n
Her style is characterised by **function words** and **modal verbs** such as 'be', 'very', 'must', 'could', 'not', reflecting her **ironic**, **hedging** and **psychologically precise prose**. \n 
Her contemporaries, by contrast, lean toward **dramatic content words** like 'castle', 'passion', 'lordship', which read as a more **elevated register**.""")
st.divider()
st.subheader("Thank you for your attention!")
st.divider()

# Jane Austen's Portrait
st.image("Jane_Austen_Portrait.jpg", caption="Portrait of Jane Austen, ca. 1810")