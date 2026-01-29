def save_message(path, msg):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(msg)


def append_message(path, msg):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(msg + "\n")


def load_message(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return ""
