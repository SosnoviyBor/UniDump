import collections
import math

############################################################
# Problem 1a

def findAlphabeticallyLastWord(text:str):
    """
    Given a string |text|, return the word in |text| that comes last
    alphabetically (that is, the word that would appear last in a dictionary).
    A word is defined by a maximal sequence of characters without whitespaces.
    You might find max() and list comprehensions handy here.
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    return sorted(text.split(" "))[-1]
    raise Exception("Not implemented yet")
    # END_YOUR_CODE

############################################################
# Problem 1b

def euclideanDistance(loc1, loc2):
    """
    Return the Euclidean distance between two locations, where the locations
    are pairs of numbers (e.g., (3, 5)).
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    return math.sqrt((loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2)
    raise Exception("Not implemented yet")
    # END_YOUR_CODE

############################################################
# Problem 1c

def mutateSentences(sentence):
    """
    Given a sentence (sequence of words), return a list of all "similar"
    sentences.
    We define a sentence to be similar to the original sentence if
      - it as the same number of words, and
      - each pair of adjacent words in the new sentence also occurs in the original sentence
        (the words within each pair should appear in the same order in the output sentence
         as they did in the orignal sentence.)
    Notes:
      - The order of the sentences you output doesn't matter.
      - You must not output duplicates.
      - Your generated sentence can use a word in the original sentence more than
        once.
    Example:
      - Input: 'the cat and the mouse'
      - Output: ['and the cat and the', 'the cat and the mouse', 'the cat and the cat', 'cat and the cat and']
                (reordered versions of this list are allowed)
    """
    # BEGIN_YOUR_CODE (our solution is 20 lines of code, but don't worry if you deviate from this)
    words = sentence.split(" ")
    wordCombos = {}
    for i in range(len(words)-1):
        if not words[i] in wordCombos.keys():
            wordCombos[words[i]] = [words[i+1]]
        elif not words[i+1] in wordCombos[words[i]]:
            wordCombos[words[i]].append(words[i+1])
    
    mutatedSentences = []
    def constructSentence(newSentence:list[str], word:str) -> None:
        if len(newSentence) == len(words):
            mutatedSentences.append(" ".join(newSentence))
            return
        if word not in wordCombos.keys() or " ".join(newSentence) in mutatedSentences:
            return
        for newWord in wordCombos[word]:
            sen = newSentence.copy()
            sen.append(newWord)
            constructSentence(sen, newWord)
        
    for k in wordCombos.keys():
        constructSentence([k], k)
    
    return mutatedSentences
    raise Exception("Not implemented yet")
    # END_YOUR_CODE

def sparseVectorDotProduct(v1, v2):
    """
    Given two sparse vectors |v1| and |v2|, each represented as collections.defaultdict(float), return
    their dot product.
    You might find it useful to use sum() and a list comprehension.
    This function will be useful later for linear classifiers.
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    # print(f"{dict(v1) = }\n{dict(v2) = }")
    product = 0
    for k in v1.keys():
        if k in v2.keys():
            product += v1[k] * v2[k]
    return product
    raise Exception("Not implemented yet")
    # END_YOUR_CODE

############################################################
# Problem 1e

def incrementSparseVector(v1, scale, v2):
    """
    Given two sparse vectors |v1| and |v2|, perform v1 += scale * v2.
    This function will be useful later for linear classifiers.
    """
    # BEGIN_YOUR_CODE (our solution is 2 lines of code, but don't worry if you deviate from this)
    for k in set(list(v2.keys()) + list(v1.keys())):
        v1[k] += scale * v2[k]
    return v1
    raise Exception("Not implemented yet")
    # END_YOUR_CODE

def findSingletonWords(text):
    """
    Splits the string |text| by whitespace and returns the set of words that
    occur exactly once.
    You might find it useful to use collections.defaultdict(int).
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    # до біса ваші тернарні оператори, не люблю їх
    wordCount = {}
    for word in text.split(" "):
        if word not in wordCount:
            wordCount[word] = 1
        else:
            wordCount[word] += 1
    result = set()
    for word in wordCount.keys():
        if wordCount[word] == 1:
            result.add(word)
    return result
    raise Exception("Not implemented yet")
    # END_YOUR_CODE

############################################################
# Problem 1g

def computeLongestPalindromeLength(text):
    """
    A palindrome is a string that is equal to its reverse (e.g., 'ana').
    Compute the length of the longest palindrome that can be obtained by deleting
    letters from |text|.
    For example: the longest palindrome in 'animal' is 'ama'.
    Your algorithm should run in O(len(text)^2) time.
    You should first define a recurrence before you start coding.
    """
    # BEGIN_YOUR_CODE (our solution is 19 lines of code, but don't worry if you deviate from this)
    n = len(text)
    # 1 чи 0 літер - завжди паліндром довжини 1 чи 0 відповідно
    if n <= 1:
        return n
    
    dp = [0 for _ in range(n)]
    dpPrev = [0 for _ in range(n)]
    # зправа наліво з передостанньої літери
    for i in range(n - 1, -1, -1):
        # кожна літера сама по собі - завжди паліндром довжини 1
        dp[i] = 1
        # літери після text[i]
        for j in range(i + 1, n):
            if text[i] == text[j]:
                # +2 довжини, якщо літери збігаються
                dp[j] = dpPrev[j - 1] + 2
            else:
                # або залишаємо попередній найдовший паліндром
                dp[j] = max(dpPrev[j], dp[j - 1])
        dpPrev = dp[:]
    return dp[-1]
    raise Exception("Not implemented yet")
    # END_YOUR_CODE
