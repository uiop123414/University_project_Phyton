import finviz
import pprint


def main():
    a = finviz.get_stock('MSFT')
    print(finviz.Portfolio)
    pprint.pprint(a)


if __name__ == '__main__':
    main()
