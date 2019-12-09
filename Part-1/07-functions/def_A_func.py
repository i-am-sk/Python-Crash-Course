def greet_user():
    """Display a simple greeting."""
    print("Hello, User!")

greet_user()

#### Passing info to a func

def greet_user(username):
    print(f"Hello, {username.title()}!")

greet_user("sai")

def favorite_book(title):
    print(f"One of my favorite book is {title.title()}")

favorite_book("Alice in Wonderland")