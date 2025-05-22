def number_of_words(content):
    split_words = content.split()
    return len(split_words)

def char_appearances(text):
    words = text.split()
    dictionary = {}
    for w in words:
        for c in w:
            lletter = c.lower()
            if lletter not in dictionary:
                dictionary[lletter] = 1
            else:
                dictionary[lletter] += 1
    return dictionary

def sorted_dictionary(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict
