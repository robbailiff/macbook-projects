import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
print("\n")

MY_DIR = os.path.join(BASE_DIR, 'portfolio', 'templates')
print(MY_DIR)