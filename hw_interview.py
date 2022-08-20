class Stack:
    def __init__(self, stack_list):
        self.stack_list = stack_list

    def my_is_empty(self):
        if self.stack_list:
            return True
        else:
            return False

    def my_push(self, new_element):
        self.stack_list.insert(0, new_element)

    def my_pop(self):
        first_element = self.stack_list[0]
        del self.stack_list[0]
        return first_element

    def my_peek(self):
        return self.stack_list[0]

    def my_size(self):
        return len(self.stack_list)


if __name__ == '__main__':
    string = input('Ввведи скобки: ')
    list_stack = list(string)
    stack = Stack(list_stack)
    i = 0
    while i < stack.my_size():
        if list_stack[i] not in (')', ']', '}'):
            i += 1
            if i == stack.my_size():
                print(f'Несбалансированно')
        else:
            if list_stack[i] == ')' and list_stack[i-1] == '(':
                del list_stack[i]
                del list_stack[i-1]
                i -= 1
                if stack.my_size() == 0:
                    print(f'Cбалансированно')
                    break
            elif list_stack[i] == ']' and list_stack[i-1] == '[':
                del list_stack[i]
                del list_stack[i - 1]
                i -= 1
                if stack.my_size() == 0:
                    print(f'Cбалансированно')
                    break
            elif list_stack[i] == '}' and list_stack[i-1] == '{':
                del list_stack[i]
                del list_stack[i - 1]
                i -= 1
                if stack.my_size() == 0:
                    print(f'Cбалансированно')
                    break
            else:
                print(f'Несбалансированно')
                break
    print(list_stack)


