"""
Tasks
    1. Read Invictus into string
    2. Split string into words and print words
    3. Create a map of unique words and use counts and print
    4. Created sorted array of unique words decending in use count
"""

def main():
    contents = load('invictus.txt')
    words = to_words(contents)

    print("Words ({}):".format(len(words)))

    for w in words:
        print('|' + w + '|')

    print('')
    print('Unique:')

    unique = unique_words(words)
    for value in unique:
        print("|{}|{}|".format(value["word"], value["count"]))

    print('')
    print('Sorted unique:')

    sorted_unique = sort_words_by_use(unique)
    for value in sorted_unique:
        print("|{}|{}|".format(value["word"], value["count"]))

def load(path):
    with open(path, 'r') as file:
        data = file.read().replace('\n', '')
        return data

def to_words(contents):
    contents = contents.lower()
    contents = contents.replace('\n', '').replace('\t', '').replace('.', ' ').replace(',', ' ')
    words = contents.split(' ')
    filtered = list(filter(lambda w: w != '', words))
    return filtered

def unique_words(words):
    unique = {}
    for w in words:
        if unique.get(w) == None:
            unique[w] = 1
        else:
            unique[w] = unique[w] + 1

    out = []
    for k in unique.keys():
        out.append({ "word": k, "count": unique[k] })

    return out

def sort_words_by_use(words):
    return sorted(words, key=lambda w: w['count'], reverse=True)

main()