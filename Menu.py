class Menu:
    def __init__(self, header, options, func=None):
        self.header = header
        self.options = options
        self.func = func
    
    def get_option(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Please enter an integer")
    
    def show(self):
        print(self.header)
        for i in range(len(self.options)):
            print(f"{i+1}. {self.options[i][0]}")
        
        opt = self.get_option("Option: ")

        if opt < 1 or opt > len(self.options):
            print("Invalid option\n")
            return self.show()
        
        # Execute the option
        if callable(self.options[opt-1][1]):
            if self.options[opt-1][1].__name__ == "get_custom_duration":
                arg = self.options[opt-1][1]()
                self.func(arg)
            else:
                self.options[opt-1][1]()
        elif isinstance(self.options[opt-1][1], int) and self.func:
            arg = self.options[opt-1][1]
            self.func(arg)