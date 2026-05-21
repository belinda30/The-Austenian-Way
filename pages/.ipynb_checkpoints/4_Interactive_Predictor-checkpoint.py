import streamlit as st
import pickle
import spacy
import nltk
import re
import string

nlp = spacy.load("en_core_web_md")

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

# Load V2 vectorizer and model
with open('pickles/v2_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)
with open('pickles/v2_log_reg.pkl', 'rb') as f:
    model = pickle.load(f)

def preprocess(text):
    # remove punctuation
    punctuation = string.punctuation.replace("'", "")
    no_punct = text.translate(str.maketrans(punctuation, ' ' * len(punctuation)))
    # normalise whitespace
    no_whitesp = re.sub(r'\s+', ' ', no_punct).strip()
    # tokenise
    tokens = nltk.word_tokenize(no_whitesp)
    # lemmatise with spacy
    doc = nlp(' '.join(tokens))
    lemmas = ' '.join([token.lemma_ for token in doc if token.pos_ not in ('PROPN', 'NUM') and token.text not in ('ll', 's', 'd', 've', 're')])
    # lowercase
    lowercase = lemmas.lower()
    cleaned_text = lowercase
    return cleaned_text


st.title("✍🏼 Interactive Predictor")
st.markdown("""##### Have you ever wondered if YOU sound like Austen?
Or perhaps your favourite artist? Or that blurb from that book you read the other day?\n
Well now you can know for sure!""")
user_input = st.text_area("Paste any text here and find out for yourself:", height=200)

if st.button("Predict"):
    cleaned = preprocess(user_input)
    vectorised = vectorizer.transform([cleaned])
    prediction = model.predict(vectorised)[0]
    confidence = model.predict_proba(vectorised)[0]

    st.write(f"**Prediction:** {prediction}")
    st.write(f"**Confidence:** {max(confidence):.2%}")

st.markdown("""
💡 **How to read the confidence score:** \n
- A score close to 100% means the model is very certain of its prediction.
- A score closer to 50% means the text could go either way.
""")

st.divider()
st.subheader("Example Texts")
st.markdown("##### Letter V – *Lady Susan Vernon to Mrs. Johnson*")
st.markdown("""from Jane Austen's epistolary novella *Lady Susan* (written ca. 1794)\n
❗️ Not used in the Model Training ❗️""")
st.code("""I received your note, my dear Alicia, just before I left town, 
and rejoice to be assured that Mr. Johnson suspected nothing of your 
engagement the evening before. It is undoubtedly better to deceive him 
entirely, and since he will be stubborn he must be tricked. I arrived 
here in safety, and have no reason to complain of my reception from Mr. 
Vernon; but I confess myself not equally satisfied with the behaviour of 
his lady. She is perfectly well-bred, indeed, and has the air of a woman 
of fashion, but her manners are not such as can persuade me of her being 
prepossessed in my favour. I wanted her to be delighted at seeing me. I 
was as amiable as possible on the occasion, but all in vain. She does not 
like me. To be sure, when we consider that I did take some pains to 
prevent my brother-in-law’s marrying her, this want of cordiality is not 
very surprizing, and yet it shows an illiberal and vindictive spirit to 
resent a project which influenced me six years ago, and which never 
succeeded at last.

I am sometimes disposed to repent that I did not let Charles buy Vernon 
Castle, when we were obliged to sell it; but it was a trying 
circumstance, especially as the sale took place exactly at the time of 
his marriage; and everybody ought to respect the delicacy of those 
feelings which could not endure that my husband’s dignity should be 
lessened by his younger brother’s having possession of the family estate. 
Could matters have been so arranged as to prevent the necessity of our 
leaving the castle, could we have lived with Charles and kept him single, 
I should have been very far from persuading my husband to dispose of it 
elsewhere; but Charles was on the point of marrying Miss De Courcy, and 
the event has justified me. Here are children in abundance, and what 
benefit could have accrued to me from his purchasing Vernon? My having 
prevented it may perhaps have given his wife an unfavourable impression, 
but where there is a disposition to dislike, a motive will never be 
wanting; and as to money matters it has not withheld him from being very 
useful to me. I really have a regard for him, he is so easily imposed 
upon! The house is a good one, the furniture fashionable, and everything 
announces plenty and elegance. Charles is very rich I am sure; when a man 
has once got his name in a banking-house he rolls in money; but they do 
not know what to do with it, keep very little company, and never go to 
London but on business. We shall be as stupid as possible. I mean to win 
my sister-in-law’s heart through the children; I know all their names 
already, and am going to attach myself with the greatest sensibility to 
one in particular, a young Frederic, whom I take on my lap and sigh over 
for his dear uncle’s sake.

Poor Mainwaring! I need not tell you how much I miss him, how perpetually 
he is in my thoughts. I found a dismal letter from him on my arrival 
here, full of complaints of his wife and sister, and lamentations on the 
cruelty of his fate. I passed off the letter as his wife’s, to the 
Vernons, and when I write to him it must be under cover to you. 
Ever yours,
S. VERNON.""", language=None)
st.divider()
st.markdown("##### *Twinkle, Twinkle, Little Star* by Jane Taylor")
st.markdown("Published in 1806")
st.code("""Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav'ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

'Tis your bright and tiny spark,
Lights the trav'ller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star.
""", language=None)