from textblob import TextBlob


def auto_correct(sentence):
    blob = TextBlob(sentence)
    corrected_text = str(blob.correct())
    return corrected_text

misspelled_sentence = "I love mchine learnning"  
corrected_sentence = auto_correct(misspelled_sentence)
print("Original:", misspelled_sentence)
print("Corrected:", corrected_sentence)
