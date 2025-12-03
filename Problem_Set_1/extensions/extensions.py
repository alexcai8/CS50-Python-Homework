def main():
    d=input("File name: ")
    file_type(d)


def file_type(d):
    d=d.strip()
    d=d.lower()
    if d.endswith(".gif")==True and d.count(".gif")==1:
        print("image/gif")
    elif d.endswith(".jpg")==True and d.count(".jpg")==1:
        print("image/jpeg")
    elif d.endswith(".jpeg")==True and d.count(".jpeg")==1:
        print("image/jpeg")
    elif d.endswith(".png")==True and d.count(".png")==1:
        print("image/png")
    elif d.endswith(".txt")==True and d.count(".txt")==1:
        print("text/plain")
    elif d.endswith(".pdf")==True and d.count(".pdf")==1:
        print("application/pdf")
    elif d.endswith(".zip")==True and d.count(".zip")==1:
        print("application/zip")
    else:
        print("application/octet-stream")


main()
