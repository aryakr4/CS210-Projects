"""jumbler:  List dictionary words that match an anagram.
2022-09-30 by Arya Krishnagiri

Credits: Areyan
A. Nother Student, And Another:  Sketched pseudocode together
Our Friend:  Helped debug
"""

DICT = "dict.txt"

        

def find(anagram: str):
    """Print words in DICT that match anagram.
  
  >>> find("gamma")
  gamma
  
  >>> find("nosuchword")

  >>> find("MAGAM")
  gamma

  >>> find("KAWEA")
  awake

  
  """
    dict_file = open(DICT, "r")
    for line in dict_file:
        word = line.strip()
        if normalize(word) == normalize(anagram):
            print(word)
            

def normalize(word: str) -> list[str]:
        lowerword = list(word.lower())
        return sorted(lowerword)
        
        
            
def main(): 
    anagram = input("Anagram to find>")
    find(anagram)
if __name__ == "__main__":
        main()
    




