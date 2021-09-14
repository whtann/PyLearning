import sys


def load(file):
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            # list comprehension - converts every word in list to lowercase
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file),
              file=sys.stderr)
        sys.exit(1)


def palindrome(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return palindrome(word[1:-1])


def main():
    word_list = load('2of4brif.txt')
    pali_list = []

    for word in word_list:
        # done with both recursion and loop
        if len(word) > 1 and word == word[::-1] and palindrome(word):
            pali_list.append(word)

    print("\nNumber of palindromes found = {}\n".format(len(pali_list)))
    print(*pali_list, sep='\n')


if __name__ == "__main__":
    main()
