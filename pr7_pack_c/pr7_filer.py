
def file_create(name):
    with open(name, "x", encoding="utf-8") as f:
        f.write("")
    return True

def save_file(name, data):
    with open(name, "w", encoding="utf-8") as f:
        f.write(data)
    return True

def open_read(name):
    with open(name, "r", encoding="utf-8") as f:
        return f.read()

def plus_write(name, data):
    with open(name, "a", encoding="utf-8") as f:
        f.write(data)
    return True
