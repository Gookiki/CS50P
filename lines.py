import sys
import tokenize


def main():
    if len(sys.argv) != 2 or not sys.argv[1].endswith('.py'):
        sys.exit(1)

    try:
        with tokenize.open(sys.argv[1]) as file:
            tokens = tokenize.generate_tokens(file.readline)
            code_lines = set()
            for tok in tokens:
                if tok.type in (
                    tokenize.COMMENT,
                    tokenize.NL,
                    tokenize.NEWLINE,
                    tokenize.ENCODING,
                    tokenize.ENDMARKER,
                    tokenize.INDENT,
                    tokenize.DEDENT,
                    tokenize.STRING,
                ):
                    continue
                code_lines.add(tok.start[0])
    except FileNotFoundError:
        sys.exit(1)

    print(len(code_lines))


if __name__ == '__main__':
    main()
