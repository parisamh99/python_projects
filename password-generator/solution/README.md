# password generator
in this project we generate password with OOP in three ways:
1.Random password
2.Memorable password
3.pincode password

## how it works
The password generator uses the Python random module to generate passwords based on user preferences. The generator is split into three classes, each representing a different type of password generation:

RandomPasswordGenerator generates a completely random password of a specified length, optional with numbers, and symbols.
MemorablePasswordGenerator creates a password made up of a set number of randomly chosen words from the NLTK English language corpus. It can optionally separate the words with a separator and use capitalized words.
PinCodeGenerator creates a numeric password of a specified length.
Each generator class inherits from a base PasswordGenerator class. They each override the base class's generate() method in order to provide their own unique password generation functionality.


## Requirements
1. python3.10+
2. nltk

to install nlk:

```
pip install nltk
```

After installing NLTK, you need to download the 'words' corpus. Run Python and type these commands:
```
import nltk
nltk.download('words')
```

## runnig the project
```
export PYTHONPATH="${PYTHONPATH}:/your/path/to/main/directory"
cd src
python3 main.py
```