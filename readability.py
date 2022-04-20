import cs50 as cs

def ColemanLiau(Letters, Words, Sentences):
    L = Letters / Words * 100
    S = Sentences / Words * 100
    index = 0.0588 * L - 0.296 * S - 15.8
    return index

def countLetters(text):
    letters = 0
    n = len(text)
    for k in range(0, n):
        if text[k] >= 'a' and text[k] <= 'z':
            letters += 1
        if text[k] >= 'A' and text[k] <= 'Z':
            letters += 1
    return letters

def countWords(text):
    wordCount = 0
    n = len(text)
    if n == 0:
        return 0
    for i in range(1, n):
        if not text[i - 1].isspace() and text[i].isspace():
            wordCount += 1
    if not text[n - 1].isspace():
        wordCount += 1
    return wordCount

def countSentences(text):
    sentences = 0
    n = len(text)
    for j in range(0, n):
        if text[j] == '.' or text[j] == '!' or text[j] == '?':
            sentences += 1
    return sentences

text = cs.get_string("Text: ")
letters = countLetters(text)
words = countWords(text)
sentences = countSentences(text)

gradeLevel = ColemanLiau(letters, words, sentences)
roundedGrade = round(gradeLevel)
if roundedGrade <= 0:
    print("Before Grade 1")
elif roundedGrade >= 16:
    print("Grade 16+")
elif roundedGrade > 0 and roundedGrade < 16:
    print("Grade", roundedGrade)
