class Queue:
    def __init__(self):
        self.input_stack: list[any] = []
        self.output_stack: list[any] = []

    def push(self, x) -> None:
        self.input_stack.append(x)

    def pop(self) -> any:
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        return self.output_stack.pop()

    def peek(self) -> any:
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        return self.output_stack[-1]

    def empty(self) -> bool:
        return not self.input_stack and not self.output_stack


def main():
    q = Queue()
    q.push(3)
    q.push(1)
    q.push(2)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.empty())

if __name__ == "__main__":
    main()
