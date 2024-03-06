import streamlit as st
import scraping
from preprocess import preprocessing
from tensorflow.keras.models import load_model
import os

st.set_page_config(
        page_title="Chatbot Page",
)
main_path = 'Model Cooking'

st.title("Kaamala Resort Chatbot")

st.header("This chatbot can help you for the informations needed")

st.subheader("you can ask chatbot for information about kaamala resort here")

text = st.text_input('type your needs here : ')
button = st.button('send')
predict = None

if button:

    text = preprocessing(text)
    model = load_model(os.path.join(main_path,
                                    'chatbot_kaamala.h5'))

    predict = model.predict([text])
    predict = predict.argmax()

if predict == 0:

    result = scraping.description()
    st.write('Here is the description about Kaamala Resort : \n',
             str(result))

if predict == 1:

    result = scraping.facilities()
    st.write('Facilities : \n')

    for i in result:
        st.write(i)

if predict == 2:

    items, detail, link = scraping.faclities_detail()
    

    for i in range(len(items)-1):

        st.write('Facilities :')
        st.write(items[i])
    
        st.write('Descriptions :')
        st.write(detail[i])

        st.write('Reference link :')
        st.write(link[i])

if predict == 3:

    result = scraping.rooms()
    st.write('Rooms : \n')

    for i in result:
        st.write(i)
    
if predict == 4:

    items, href, infos = scraping.rooms_detail()
    leng = min(len(items), len(infos))
    leng = min(leng, len(href))

    for i in range(leng):

        st.write('Rooms :')
        st.write(items[i])
    
        st.write('Links :')
        st.write(href[i])

        st.write('Information and details :')
        st.write(infos[i])

if predict == 5:

    result = scraping.booking()
    st.write('Here is the link if you want to book at Kaamala Resort : \n',
             result)