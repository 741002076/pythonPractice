from autoAddTag.handlers import HTMLRenderer
from autoAddTag.markup import BasicTextParser


def main():
    f = open('test_input.txt');
    # b = util.blocks(f)
    handler = HTMLRenderer()
    parser = BasicTextParser(handler)
    parser.parse(f)



if __name__ == '__main__':
    main()
