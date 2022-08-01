import enchant
import itertools

def main():
    d = enchant.Dict("en_US")
    
    letters = input("What letters are given:")
    sep_letters = [l for l in letters]
    
    combos = []
    for l in range(0, len(letters) + 1):
        for subset in itertools.combinations(letters, l):
            combos.append(subset)
            
    suggestions = []
    temp = ""
    for num, combo in enumerate(combos):
        for letters in combo:
            temp += letters
        if len(temp) > 2:
            suggestions.append(temp)
        temp = ""
        
    allSugs = []
    for x in suggestions:
        allSugs += itertools.permutations(x)
    
    finalSugs = []
    temp2 = ""
    for t in allSugs:
        for letter in t:
            temp2 += letter
        finalSugs.append(temp2)
        temp2 = ""
    
    for x in finalSugs:
        if not d.check(x):
            finalSugs.remove(x)
            
    threeletwords = [i for i in finalSugs if len(i) == 3]
    fourletwords = [i for i in finalSugs if len(i) == 4]
    fiveletwords = [i for i in finalSugs if len(i) == 5]
    
    print(f"Three letters:\n {threeletwords}")
    print(f"Four Letters:\n {fourletwords}")
    print(f"Five Letters:\n {fiveletwords}")
    
if __name__ == "__main__":
    main()