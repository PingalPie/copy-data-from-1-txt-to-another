import fileinput as fi
# This module replaces the word <|SPACE|> with a new line (code line 18)

def writer():
    with open("c:/PycharmProjects/copy_data_from_1_file_to_another/input.txt", "w") as writer:
        data = input("Whatever you will write will be present in input.txt - ")
        writer.write(data)
# This is a input function whatever you will write that will come in input.txt

def copy():
    with open("c:/PycharmProjects/copy_data_from_1_file_to_another/input.txt", "r") as f:
        with open("c:/PycharmProjects/copy_data_from_1_file_to_another/copyied.txt", "w") as f1:
            font = f.read()
            f1.write(font)
# This is a function to copy data from input.txt and paste it in copyied.txt

def editer():
    with fi.FileInput("c:/PycharmProjects/copy_data_from_1_file_to_another/copyied.txt", inplace=True, backup=".bak") as r:
        for line in r:
            print(line.replace(' ', '''
'''), end='')
# This function replaces <|SPACE|> with new line this will also create one backup file with extention .bak

if __name__ == '__main__':
    writer()
    copy()
    editer()
# This will run the code
