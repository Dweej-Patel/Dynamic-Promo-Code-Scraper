import re as regex
from bs4 import BeautifulSoup

class CodeParse():

    def __init__(self):
        self.array = []
    
    def input(self, text):
        self.array.append(text)
    
    #Check if code is in array
    def search_in_arr(self, text):
        return (text in self.array)
    
    #Parse text to find code
    def search_for_code(self, text):
        code = regex.search(r"\bFREE([A-Z0-9]{5})\s", text)
        if code:
            return code.group()
        else:
            return None


class Input_Checker():
    
    def __init__(self):
        self.code_parser = CodeParse()

    #Parse code and check if code is in the input array already.
    #If code is not found or in input array then return None.
    #If new input code is found return code
    def input_this(self, text):
        code = self.code_parser.search_for_code(text)
        if code:
            if not self.code_parser.search_in_arr(code):
                self.code_parser.input(code)
                return code
            else:
                return None
        else:
            return None

    def tester(self):
        return self.code_parser.array
    

class Beautiful_Soup():

    def __init__(self):
        self.input = Input_Checker()

    #Extract code from HTML
    def find_new_code(self, res):
        if (res):
            soup = BeautifulSoup(res, 'lxml')
            all_tweets = soup.find_all('p', {'class': 'TweetTextSize TweetTextSize--normal js-tweet-text tweet-text'})
            new_code = None
            for tweet in all_tweets:
                text = tweet.text
                new_code = self.input.input_this(text)
                if new_code:
                    break
            if new_code:
                return new_code
            else:
                return None
        else:
            return None

    def array(self):
        return self.input.tester()