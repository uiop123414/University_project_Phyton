import finviz
import pprint
import sys


def main():
    a = None
    try:
        a = finviz.get_stock('jklsfd')
    except Exception:
        print(f"invalid name")
        sys.exit()

    print(finviz.Portfolio)
    pprint.pprint(a.get('P/C'))
    pprint.pprint(a.keys())


if __name__ == '__main__':
    main()
