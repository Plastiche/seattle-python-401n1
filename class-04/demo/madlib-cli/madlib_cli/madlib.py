list_of_words = []

def set_file_contents():
    file_path = 'madlib_cli/mad-lib.txt'
    return file_path


def get_file_contents(path, path_flag):
    with open(path, path_flag) as madlib:
        try:
            madlib = madlib.read()
        except IOError:
            print('Cannot find file' + path)
    return madlib


def get_language_from_file(initial_file):
    ending = 0
    for letter in range(initial_file.count('{')):
        beginning = initial_file.find('{', ending)
        ending = initial_file.find('}', beginning)
        word = initial_file[beginning: ending + 1]
        list_of_words.append(word)


    for word in list_of_words:
        question = f'Please give me a {word}:'
        user_input = input(question)
        initial_file = initial_file.replace(word, user_input)

    print(initial_file)


if __name__ == '__main__':
    fpath = set_file_contents()
    madlib = get_file_contents(fpath, 'r')
    get_language_from_file(madlib)
