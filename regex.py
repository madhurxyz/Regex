import re

def clean(text):
    remove = re.sub(r'(^[\w]+[\'\-]?[\w]*)', '', text).split()
    for word in remove:
        if word is "hadn't":
            print word

    return remove


if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        source = open(filename).read()
        clean = clean(source)
        # print clean
