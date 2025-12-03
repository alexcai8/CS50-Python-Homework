def main():
    d=input("Greeting: ")
    evaluate(d)

def evaluate(d):
        d=d.lower()
        d=d.strip()
        if d.startswith("hello")==True:
           print("$0")
        elif d.startswith("hello")==False and d.startswith("h"):
            print("$20")
        else:
             print("$100")

main()

