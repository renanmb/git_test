from greets import greetings
from translate import Translator

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

translator = Translator(to_lang='pt')
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    for g in greetings:
        print(g.title()+"!")
        print(translator.translate(g).title())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
