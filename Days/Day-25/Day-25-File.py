def greeter():
    name = input("Please enter your name: ").strip().title()
    print(f"Hello, {name or 'World'}!")

greeter()