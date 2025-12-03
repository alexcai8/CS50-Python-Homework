def main():
    d=input("Expression: ")
    result(d)

def result(d):
    d=d.split(" ")

    x=int(d[0])
    z=int(d[2])
    y=d[1]

    if y=="+":
        print("{:.1f}".format(x+z))
    elif y=="-":
        print("{:.1f}".format(x-z))
    elif y=="*":
        print("{:.1f}".format(x*z))
    else:
        print("{:.1f}".format(x/z))
main()

