def Quest_Life(d):
        d=d.strip()
        if d=="42":
                print("Yes")
        else:
                d=d.lower()
                d=d.replace(" ","-")
                #print(d)
                if d=="forty-two":
                        print("Yes")
                else:
                        print("No")



def main():
    d=input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    Quest_Life(d)

main()

