from textblob import TextBlob


def translate_(text_to_translate, to):
    blob = TextBlob(text_to_translate)
    return blob.translate(to=to)


