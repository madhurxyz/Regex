import re

def clean(text):
    remove = re.sub(r'(?:(?:(^[\w]+[\'\-]?[\w]*))|(^(?:[\w]+[\'\-]?[\w]*[\'\-]?)+)|(^(?:[\$]?[\w]+[\'\-]?[\w]*)+))', '', text).split()
    # remove = re.sub(r'[^\w\'?\w\$\s]', '', text).split()
    # remove = re.sub(r'(^[\w\'?\w]*[\$\s])', '', text).split()


    return remove


if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        source = open(filename).read()
        clean = clean(source)
        print clean
