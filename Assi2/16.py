# write a python program to create a chain of function decorators (bold,italic,underline etc.)

def bold(func):
    def wrapper(text):
        return f"<b>{func(text)}</b>"
    return wrapper

def italic(func):
    def wrapper(text):
        return f"<i>{func(text)}</i>"
    return wrapper

def underline(func):
    def wrapper(text):
        return f"<u>{func(text)}</u>"
    return wrapper

@bold
@italic
@underline
def format_text(text):
    return text

print(format_text("Hello, world!"))
