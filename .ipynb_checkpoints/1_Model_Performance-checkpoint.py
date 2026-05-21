import streamlit as st
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
cmap = LinearSegmentedColormap.from_list('custom', ['thistle', 'darkseagreen'])

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
with open('pickles/v2_cm_LR.pkl', 'rb') as f:
    v2_cm_LR = pickle.load(f)
with open('pickles/v2_cm_RF.pkl', 'rb') as f:
    v2_cm_RF = pickle.load(f)
with open('pickles/v2_log_reg.pkl', 'rb') as f:
    v2_log_reg = pickle.load(f)
with open('pickles/v2_ran_for.pkl', 'rb') as f:
    v2_ran_for = pickle.load(f)
with open('pickles/v2_as_lr.pkl', 'rb') as f:
    v2_as_lr = pickle.load(f)
with open('pickles/v2_as_rf.pkl', 'rb') as f:
    v2_as_rf = pickle.load(f)
with open('pickles/v2_cr_lr.pkl', 'rb') as f:
    v2_cr_lr = pickle.load(f)
with open('pickles/v2_cr_rf.pkl', 'rb') as f:
    v2_cr_rf = pickle.load(f)


# Load pickled V1 objects
with open('pickles/v1_cm_LR.pkl', 'rb') as f:
    v1_cm_LR = pickle.load(f)
with open('pickles/v1_cm_RF.pkl', 'rb') as f:
    v1_cm_RF = pickle.load(f)
with open('pickles/v1_log_reg.pkl', 'rb') as f:
    v1_log_reg = pickle.load(f)
with open('pickles/v1_ran_for.pkl', 'rb') as f:
    v1_ran_for = pickle.load(f)
with open('pickles/v1_as_lr.pkl', 'rb') as f:
    v1_as_lr = pickle.load(f)
with open('pickles/v1_as_rf.pkl', 'rb') as f:
    v1_as_rf = pickle.load(f)
with open('pickles/v1_cr_lr.pkl', 'rb') as f:
    v1_cr_lr = pickle.load(f)
with open('pickles/v1_cr_rf.pkl', 'rb') as f:
    v1_cr_rf = pickle.load(f)

st.title("📊 Model Performance")

tab1, tab2 = st.tabs(["V2 – Without Proper Nouns", "V1 – With Proper Nouns"])

with tab1:
    lr_tab, rf_tab = st.tabs(['Logistic Regression', 'Random Forest'])
    
    with lr_tab:  
        st.subheader("Accuracy Score")
        st.metric(label="Logistic Regression", value=f"{v2_as_lr:.2%}")
        st.divider()
        st.subheader("Classification Report")
        st.code(v2_cr_lr, language=None)
        st.divider()
        st.subheader("Confusion Matrix")
        fig, ax = plt.subplots()
        sns.heatmap(v2_cm_LR,
                    annot=True,
                    fmt='d',
                    xticklabels=['austen', 'contemporaries'],
                    yticklabels=['austen', 'contemporaries'],
                    cmap=cmap,
                    linewidths=0.5,
                    ax=ax)
        ax.set_xlabel('Predicted')
        ax.set_ylabel('Actual')
        ax.set_title('Austen vs. Contemporaries - Logistic Regression')
        st.pyplot(fig)
        st.write("""**V2 — Logistic Regression (Without Proper Nouns)**

- 241 Austen chunks correctly identified as Austen ✅
- 7 Austen chunks wrongly called Contemporary ❌
- 15 Contemporary chunks wrongly called Austen ❌
- 256 Contemporary chunks correctly identified ✅""")
    
    with rf_tab:
        st.subheader("Accuracy Score")
        st.metric(label="Random Forest", value=f"{v2_as_rf:.2%}")
        st.divider()
        st.subheader("Classification Report")
        st.code(v2_cr_rf, language=None)
        st.divider()
        st.subheader("Confusion Matrix")
        fig, ax = plt.subplots()
        sns.heatmap(v2_cm_RF,
                    annot=True,
                    fmt='d',
                    xticklabels=['austen', 'contemporaries'],
                    yticklabels=['austen', 'contemporaries'],
                    cmap=cmap,
                    linewidths=0.5,
                    ax=ax)
        ax.set_xlabel('Predicted')
        ax.set_ylabel('Actual')
        ax.set_title('Austen vs. Contemporaries - Random Forest')
        st.pyplot(fig)
        st.write("""**V2 — Random Forest (Without Proper Nouns)**

- 236 Austen chunks correctly identified as Austen ✅
- 12 Austen chunks wrongly called Contemporary ❌
- 66 Contemporary chunks wrongly called Austen ❌
- 205 Contemporary chunks correctly identified ✅""")

with tab2:
    lr_tab, rf_tab = st.tabs(['Logistic Regression', 'Random Forest'])
    
    with lr_tab:  
        st.subheader("Accuracy Score")
        st.metric(label="Logistic Regression", value=f"{v1_as_lr:.2%}")
        st.divider()
        st.subheader("Classification Report")
        st.code(v1_cr_lr, language=None)
        st.divider()
        st.subheader("Confusion Matrix")
        fig, ax = plt.subplots()
        sns.heatmap(v1_cm_LR,
                    annot=True,
                    fmt='d',
                    xticklabels=['austen', 'contemporaries'],
                    yticklabels=['austen', 'contemporaries'],
                    cmap=cmap,
                    linewidths=0.5,
                    ax=ax)
        ax.set_xlabel('Predicted')
        ax.set_ylabel('Actual')
        ax.set_title('Austen vs. Contemporaries - Logistic Regression')
        st.pyplot(fig)
        st.write("""**V1 — Logistic Regression (With Proper Nouns)**

- 236 Austen chunks correctly identified as Austen ✅
- 7 Austen chunks wrongly called Contemporary ❌
- 3 Contemporary chunks wrongly called Austen ❌
- 274 Contemporary chunks correctly identified ✅""")
    
    with rf_tab:
        st.subheader("Accuracy Score")
        st.metric(label="Random Forest", value=f"{v1_as_rf:.2%}")
        st.divider()
        st.subheader("Classification Report")
        st.code(v1_cr_rf, language=None)
        st.divider()
        st.subheader("Confusion Matrix")
        fig, ax = plt.subplots()
        sns.heatmap(v1_cm_RF,
                    annot=True,
                    fmt='d',
                    xticklabels=['austen', 'contemporaries'],
                    yticklabels=['austen', 'contemporaries'],
                    cmap=cmap,
                    linewidths=0.5,
                    ax=ax)
        ax.set_xlabel('Predicted')
        ax.set_ylabel('Actual')
        ax.set_title('Austen vs. Contemporaries - Random Forest')
        st.pyplot(fig)
        st.write("""**V1 — Random Forest (With Proper Nouns)**

- 229 Austen chunks correctly identified as Austen ✅
- 14 Austen chunks wrongly called Contemporary ❌
- 30 Contemporary chunks wrongly called Austen ❌
- 247 Contemporary chunks correctly identified ✅""")
