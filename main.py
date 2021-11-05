from train import *
from experiment import *
from PosT import *
from pyvi import ViTokenizer

text=(input("Enter your string: "))
print("Tagged: ")
print(postagging(ViTokenizer.tokenize(text)))
