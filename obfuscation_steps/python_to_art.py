import tokenize
import keyword
from token import NL, NEWLINE, NAME

def load_image(path):
    with open(path) as i:
        return i.read()

def code_to_one_line(tokens):
    output = ""
    for token in tokens:
       if token.type in (NL, NEWLINE):
           output += " "
       elif token.type == NAME and keyword.iskeyword(token.string):
           output += f" {token.string} "
       else:
           output += f"{token.string}"

    return output

def rewrite_image(image_stream, python_code_stream):
    output = ""
    j = 0; i = 0
    while i < len(image_stream):
        if image_stream[i] == ' ':
            output += " "
        elif image_stream[i] == '\n':
            output += " \\\n"
        else:
            if j < len(python_code_stream):
                output += python_code_stream[j]
                j += 1
            else:
                output += image_stream[i]
        i += 1

    output += python_code_stream[j:]

    return output

def create_one_line_code():
    with tokenize.open('nvm5.py') as f, open("nvm5_oneline.py", "w") as output_file:
        tokens = tokenize.generate_tokens(f.readline)
        one_line = code_to_one_line(tokens)
        output_file.write(one_line)


if __name__ == "__main__":
    create_one_line_code()
    image_stream = load_image("image.txt")
    pyc = open("nvm5_oneline.py").read()
    output = rewrite_image(image_stream, pyc)
    with open("nvm_cool.py", "w") as o:
        o.write(output)



