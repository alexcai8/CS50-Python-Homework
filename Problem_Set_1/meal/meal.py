def main():
    d=input("What time is it? ")
    actual_time=round(convert(d),2)
    if 7.00<=actual_time<=8.00:
        print("breakfast time")
    elif 12.00<=actual_time<=13.00:
        print("lunch time")
    elif 18.00<=actual_time<=19.00:
        print("dinner time")

def convert(time):
    hour,minute=time.split(":")
    hour=float(hour)
    minute=float(minute)/60
    time = hour + minute
    return time

if __name__ == "__main__":
    main()

