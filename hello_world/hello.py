import argparse

def main():
    parser = argparse.ArgumentParser(description='Prints a greeting message to the user.')
    parser.add_argument('name', nargs='?', help='the name of the user')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0', help='show program\'s version number and exit')

    args = parser.parse_args()

    if args.name:
        print(f'Hello, {args.name}!')
    else:
        parser.print_usage()

if __name__ == '__main__':
    main()
