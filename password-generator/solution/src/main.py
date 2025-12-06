from abc import ABC,abstractmethod
import random
import string
import nltk

#nltk.download('words')

class PasswordGenerator(ABC):
    """base class for generating password"""

    @abstractmethod
    def generate(self):
        pass


class PinCodeGenerator(PasswordGenerator):
    """Class to generate a numeric pin code."""
    def __init__(self,length):
        self.length = length
    """generate a numeric pin code"""
    def generate(self):
        return ''.join(random.choice(string.digits) for _ in range(self.length))


class RandomPasswordGenerator(PasswordGenerator):
    """class to generate random password with numbers,charactors and symbols"""
    def __init__(self,length:int = 4, include_num:bool = False, include_char:bool = False , include_symb:bool = False):
        self.length = length
        self.include_char = string.ascii_letters
        if include_num:
            self.include_char += string.digits
        if include_symb:
            self.include_char +=  string.punctuation
          
    def generate(self):  
        return ''.join(random.choice(self.include_char) for _ in range(self.length)) 
    
    
class MemorablePasswordGenerator(PasswordGenerator):
    """class to generate memorable password"""
    def __init__(self, num_of_word:int = 4, capitilize:bool = False, seprator:str = '-', vocabulary:list = None):
        self.num_of_word = num_of_word
        if vocabulary is None:
            self.vocabulary = nltk.corpus.words.words()
        else:
            self.vocabulary = vocabulary    
        self.capitilize = capitilize
        self.seprator = seprator

    def generate(self):
        words_password = [random.choice(self.vocabulary)for _ in range(self.num_of_word)]
        if self.capitilize == True:
            new_words = []
            for word in words_password:
                if random.choice([True, False]):
                    new_words.append(word.upper())
                else:
                    new_words.append(word.lower())
            words_password = new_words        
        return self.seprator.join(words_password)       

           
password = MemorablePasswordGenerator(num_of_word=6,capitilize=True,seprator='/')
print(password.generate())

example = RandomPasswordGenerator(length=5,include_char=True,include_num=True,include_symb=True)
print(example.generate())

pinpass = PinCodeGenerator(length=8)
print(pinpass.generate())