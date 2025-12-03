def convert(string):
    string=string.replace(":)", "🙂")
    string=string.replace( ":(", "🙁")
    print(string)


def main():
    word =input("Enter your word: ")
    convert(word)

main()
