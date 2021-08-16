import re
def main():
    original = input()
    sub = input()
    if re.search(sub, original):
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    main()