def translate_one_liners(sentence: str):
    dic = {'esta': 'is', 'la': 'the', 'en': 'in',
           'gato': 'cat', 'casa': 'house', 'el': 'the'}
    words = sentence.split(' ')
    return ' '.join(list(map(lambda word: dic[word], words)))


def transate_generator(sentence: str):
    dic = {'esta': 'is', 'la': 'the', 'en': 'in',
           'gato': 'cat', 'casa': 'house', 'el': 'the'}
    words = sentence.split(' ')
    translator = (dic[word] for word in words)
    translated_words = []
    for word in translator:
        translated_words.append(word)

    return ' '.join(translated_words)


def main():
    print(transate_generator('el gato esta en la casa'))


if __name__ == "__main__":
    main()
