import streamlit as st
from textblob import TextBlob
from googletrans import Translator


#image = Image.open("textblob.jpg")  
#st.image(image, use_column_width=True)

translator = Translator()
st.title('Uso de textblob')

st.subheader("Please enter the sentence you want to analyze in Spanish in the text field.")
with st.sidebar:
               st.subheader("Polarity and Subjectivity")
               ("""
                Polarity: Indicates whether the sentiment expressed in the text is positive, negative, or neutral. 
Its value ranges from -1 (very negative) to 1 (very positive), with 0 representing neutral sentiment.
                
               Subjectivity: Measures how much of the content is subjective (opinions, emotions, beliefs) versus objective
(facts). It ranges from 0 to 1, where 0 is completely objective and 1 is completely subjective.

                 """
               ) 


with st.expander('Analyzing Polarity and Subjectivity in a Text'):
    text1 = st.text_area('Please write: ')
    if text1:

        translation = translator.translate(text1, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)
        #blob = TextBlob(text1)
       
        
        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))
        x=round(blob.sentiment.polarity,2)
        if x >= 0.5:
            st.write( 'It's a positive feeling. 😊')
        elif x <= -0.5:
            st.write( 'It's a negative feeling. 😔')
        else:
            st.write( 'It's a neutral feeling. 😐')

with st.expander('Corrección en inglés'):
       text2 = st.text_area('Escribe por favor: ',key='4')
       if text2:
          blob2=TextBlob(text2)
          st.write((blob2.correct())) 
