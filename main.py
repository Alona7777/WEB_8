from tasks import find_by_author, find_by_tag


def parts_command(input_command: str) -> list:
    list_command = []
    commands = input_command.split(':')
    print(len(commands))
    list_command.append(commands[0])
    if len(commands) == 2:
        value = commands[1].split(',')
        list_command.append(value)
    return list_command


def main():
    while True:
        input_command = input('Enter your text=>  ').lower()
        list_commands = parts_command(input_command)
        if list_commands[0] == 'name':
            name = list_commands[1][0]
            result = find_by_author(name) 
        elif list_commands[0] == 'tag':
            tag = list_commands[1][0]
            result = find_by_tag(tag)
        elif list_commands[0] == 'tags':
            result = []
            tag_1 = list_commands[1][0]
            result.append(find_by_tag(tag_1))
            tag_2 = list_commands[1][1]
            result.append(find_by_tag(tag_2))
        elif list_commands[0]== 'exit':
            print('Good buy')
            break
        else:
            result = 'Comand not found, try again'
        print(result)
    

if __name__ == "__main__":
    main()