class FooBar:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

def main():
    foo_bar = FooBar(42)
    print("Initial value:", foo_bar.get_value())
    
    foo_bar.set_value(100)
    print("Updated value:", foo_bar.get_value())

if __name__ == "__main__":
    main()
