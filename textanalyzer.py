Let's consider a scenario where you are analyzing customer feedback for a product. You have a large dataset of customer reviews in the form of strings, and you want to extract useful information from them using the three identified tasks:

Task 1. String in lower case: You want to Pre-process the customer feedback by converting all the text to lowercase. This step helps standardize the text. Lower casing the text allows you to focus on the content rather than the specific letter casing.

Task 2. Frequency of all words in a given string: After converting the text to lowercase, you want to determine the frequency of each word in the customer feedback. This information will help you identify which words are used more frequently, indicating the key aspects or topics that customers are mentioning in their reviews. By analyzing the word frequencies, you can gain insights into the most common issues raised by customers.

Task 3. Frequency of a specific word: In addition to analyzing the overall word frequencies, you want to specifically track the frequency of a particular word that is relevant to your analysis. For example, you might be interested in monitoring how often the word "reliable" appears in the customer reviews to gauge customer sentiment about the product's reliability. By focusing on the frequency of a specific word, you can gain a deeper understanding of customer opinions or preferences related to that particular aspect.

By performing these tasks on the customer feedback dataset, you can gain valuable insights into customer sentiment



Step-1 Define a string.
givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

Step-2 Define the class and its attributes:

    Create a class named TextAnalyzer.
    Define the constructor __init__ method that takes a text argument.



# Please do not run this code cell as it is incomplete and will produce an error.

# Let's create a class called TextAnalyzer to analyze text.
class TextAnalyzer(object):
    # The __init__ method initializes the class with a 'text' parameter.
    # We will store the provided 'text' as an instance variable.
    def __init__(self, text):

Step-3 Implement a code to Format the text in Lowercase:


    Inside the constructor,we will convert the text argument to lowercase using the lower() method.
    Then, will Remove punctuation marks (periods, exclamation marks, commas, and question marks) from the text using the replace() method.
    At last, we will Assign the formatted text to a new attribute called fmtText.


# Press Shift+Enter to run the code.
class TextAnalzer(object):
    
    def __init__ (self, text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        
        # make text lowercase
        formattedText = formattedText.lower()
        
        self.fmtText = formattedText

Step-4 Implement a code to count the Frequency of all unique words:¶

In this step, we will Implement the freqAll() method with the below parameters:

    Split the fmtText attribute into individual words using the split() method.
    Create an empty dictionary to store the word frequency.
    Iterate over the list of words and update the frequency dictionary accordingly.
    Use count method for counting the occurence
    Return the frequency dictionary.
#Press shift+Enter to run the code
class TextAnalyzer(object):
    
    def __init__ (self, text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        
        # make text lowercase
        formattedText = formattedText.lower()
        
        self.fmtText = formattedText
        
    def freqAll(self):        
        # split text into words
        wordList = self.fmtText.split(' ')
        
        # Create dictionary
        freqMap = {}
        for word in set(wordList): # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)
        
        return freqMap

Step-5 Implement a code to count the Frequency of a specific word:

In step-5, we have to Implement the freqOf(word) method that takes a word argument:

    Create method and pass the word that need to be found
    Get the freqAll method for look for count and check if that word is in the list.
    Return the count.


#Press Shift+Enter to run the code
class TextAnalyzer(object):
    
    def __init__ (self, text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        
        # make text lowercase
        formattedText = formattedText.lower()
        
        self.fmtText = formattedText
        
    def freqAll(self):        
        # split text into words
        wordList = self.fmtText.split(' ')
        
        # Create dictionary
        freqMap = {}
        for word in set(wordList): # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)
        
        return freqMap
    
    def freqOf(self,word):
        # get frequency map
        freqDict = self.freqAll()
        
        if word in freqDict:
            return freqDict[word]
        else:
            return 0

Now, We have successfully created a class with 3 methods

Part-B

In Part B, we will be calling the functions created in Part A, allowing the functions to execute and generate output.

Step-1 Create an instance of TextAnalyzer Class.

    Instantiate the TextAnalyzer class by passing the given string as an argument.

# type your code here
analyzed = TextAnalyzer(givenstring)

Step-2 Call the function that converts the data into lowercase

# Press Shift+Enter to run the code.
print("Formatted Text:", analyzed.fmtText)

We have successfully converted string into lowercase.

Step-3 Call the function that counts the frequency of all unique words from the data.

# Press Shift+Enter to run the code.
freqMap = analyzed.freqAll()
print(freqMap)

We have successfully calculated the frequency of all unique words in the string.

Step-4 Call the function that counts the frequency of specific word.

Here, we will call the function that counts the frequency of the word "lorem"

Print the output.**

# type your code here
word = "lorem"
frequency = analyzed.freqOf(word)
print("The word",word,"appears",frequency,"times.")

We have successfully calculated the frequency of all specified words.

