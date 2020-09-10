STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
# Opening file to be read
    with open(file, "r") as f:
        file_contents = f.read()


# # Taking away punctuation and lowercase all words
    word_list = file_contents.lower().replace(',',' ').replace('.',' ').replace('!',' ').split()
    # print(word_list)

    nice_list = []
    for word in word_list:
        if word not in STOP_WORDS:
            nice_list.append(word)
    # print(nice_list)

    d = {}
    for word in nice_list:
        if word not in d.keys():
            d[word] = 1
        else:
            d[word] += 1 
    print(d)
                


        



     
    



if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
