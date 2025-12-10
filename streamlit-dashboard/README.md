# password generator dashboard

## project overview
The 'Password Generator Dashboard' is an interactive web application built with Python and Streamlit. It allows users to generate different types of passwords quickly, either randomly, as a memorable sequence of words, or as a pin code, based on their preferences.

## project structure
passwordgenerator.py:A python module that contains password generator classes.
dashboard.py:A python script that create a GUI by using streamlit.
README.md:documentaion for project solution

## requirements

1.Python 3.6 or later
2.Streamlit
3.NLTK (Natural Language Toolkit)

```pip install nltk```

After installing NLTK, you need to download the 'words' corpus. Run Python and type these commands:

```import nltk
nltk.download('words')```

then install streamlit using pip:

```pip install streamlit```


## how to run:

```streamlit run dashboard.py```






