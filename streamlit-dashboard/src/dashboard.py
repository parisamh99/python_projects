import streamlit as st
from passwordgenerator import PinCodeGenerator,RandomPasswordGenerator,MemorablePasswordGenerator

st.image("images/banner.jpeg")
st.title("Password Generator Dashboard")

options = st.radio("select password generator type",
                   ('Pin code','Random generator','Memorable generator'))

if options == "Pin code":
    length = st.slider('select the length of your pass',4,32)
    generator = PinCodeGenerator(length)


elif options == 'Random generator':
    length = st.slider('select the length of your pass',4,10)
    include_num = st.toggle('include number')
    include_symb = st.toggle('include symble')
    generator = RandomPasswordGenerator(length,include_num,include_symb)

elif options == 'Memorable generator':
    num_of_word = st.slider('select the number of word for your pass',2,8)
    capitilize = st.toggle('Capitilization')
    seprator = st.text_input('seprator',value='-')
    generator = MemorablePasswordGenerator(num_of_word,capitilize,seprator)


password = generator.generate()  
st.write("Your password is:")
st.header(fr"``` {password} ```") 