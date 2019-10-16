# import string sturvs
import string

def count(tokens):
    # word freq
    word_count = {}

    # count the word freq
    for token in tokens:
        if token not in word_count:
            word_count[token] = 0

        word_count[token] += 1

    return word_count

def sortDictionary(word_count, reverse=True):
    # sort from ascending to desc
    return sorted(word_count.items(),  key=lambda x: x[1], reverse=reverse)

def tokenize(text):
    # strip the nneccesary
    text = text.strip()

    # run a for loop on text words
    for word in text.split():
        token = word.strip()
        
        # remove punctuations
        for p in string.punctuation:
            token = token.replace(p, '')

        yield token

def loadTextFile(filepath):
    try:
        with open('{}.txt'.format(filepath), 'r') as f:
            # read text file contents
            return f.read()
    
    except Exception as e:
        print(e)

def main():
    # the path to txt file to load
    filepath = '2000010'

    # get the text file contents
    text = loadTextFile(filepath)
    
    if text is None:
        return

    # get the tokens
    tokens = tokenize(text)

    # get the word freq
    word_freq = count(tokens)

    # sort the word freq dictinary
    sorted_word_tuple = sortDictionary(word_freq)

    print('{:<15s} {:<4s}'.format('Word', 'Freq'))
    print('========================================')
    for word, freq in sorted_word_tuple:
        print('{:<15s} {:<4d}'.format(word, freq))
        if freq < 10:
            break

if __name__ == "__main__":
    main()
