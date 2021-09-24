import streamlit as st
from happytransformer import HappyGeneration, GENSettings

form = st.form(key='myform')
text_input = form.text_input('How should the text start?')
model_to_use = form.radio('Model to use:', ['GPT-Neo', 'My Model'])
number = form.number_input('Text length', step=1, value=15)
numbeams = form.number_input('How many beams', step=1, value=1)
submit_button = form.form_submit_button('Submit')

settings = GENSettings(min_length=number, max_length=number+50, no_repeat_ngram_size=2, num_beams=numbeams)

if model_to_use == 'GPT-Neo':
    happy_gen = HappyGeneration("GPT-NEO", 'EleutherAI/gpt-neo-125M')

if model_to_use == 'My Model':
    happy_gen = HappyGeneration(load_path='10epochs_loss1_58')
if len(text_input) > 0:
    result = happy_gen.generate_text(text_input, args=settings)
    st.write(result.text)
