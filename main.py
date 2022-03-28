import finviz
import pprint


def main():
    a = finviz.get_stock('MSFT')
    pprint.pprint(a)


if __name__ == '__main__':
    main()
