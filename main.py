#new line here
class PurpleBananaMonkey(self, monkey_type = "Chimpanzee", color = "Purple"):  
    def __init__():
        self.monkey_type = monkey_type
        
        
def main():
    print('\n'.join(' ' * (10-x) + '*' * (x * 2 + 1) for x in range(10)) + '\n' + '\n'.join(' ' * 8 + '|' * 5 for x in range(4)))
    print("Let's get started!")
    choice = int(input("Please choose from the following\n1. GitHub\n2. Facebook\n3. Twitter\n")) # Add more choices here
    if choice == 1:
        print("https://github.com")
    else:
        giveMeAnOctocat()

def giveMeAnOctocat():
    print("""
            ./\_/\.
          . ( o.o )
           \_| ^ |    _
        -.___'.  ( ,-'
             '-.O.'-..-..   
               ; \_.-._
            ._/
        """)

if __name__ == "__main__":
    main()
