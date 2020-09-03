from pynput import keyboard
from server import send_command

def on_press(key):
    try:    
        if key == keyboard.Key.right:
            print('right')
            message = send_command('rc 0 0 0 70')
            print(message)
        
        elif key == keyboard.Key.left:
            print('left')
            message = send_command('rc 0 0 0 -70')
            print(message)
        
        elif key == keyboard.Key.up:
            print('up')
            message = send_command('rc 0 0 70 0')
            print(message)

        elif key == keyboard.Key.down:
            print('down')
            message = send_command('rc 0 0 -70 0')
            print(message)
        
        elif key.char == 'w':
            print('w')
            message = send_command('rc 0 70 0 0')
            print(message)
            print(message)
        
        elif key.char == 'a':
            print('a')
            message = send_command('rc -70 0 0 0')
            print(message)
        
        elif key.char == 's':
            print('s')
            message = send_command('rc 0 -70 0 0')
            print(message)
        
        elif key.char == 'd':
            print('d')
            message = send_command('rc 70 0 0 0')
            print(message)
        
        elif key.char == 'c':
            print('c')
            message = send_command('command')
            print(message)
        
        elif key.char == 't':
            print('t')
            message = send_command('takeoff')
            print(message)
        
        elif key.char == 'l':
            print('l')
            message = send_command('land')
            print(message)
        elif key.char == 'b':
            print('battery')
            message = send_command('battery?')
            print(message)
        elif key.char == '1':
            print('1')
            message = send_command('flip f')
        elif key.char == '2':
            print('2')
            message = send_command('flip b')
        elif key.char == '3':
            print('3')
            message = send_command('flip l')
        elif key.char == '4':
            print('4')
            message = send_command('flip r')
        
    
    except AttributeError:
            print('Invalid')

def on_release(key):
    try:
        if key == keyboard.Key.right:
            print('right')
            message = send_command('rc 0 0 0 0')
            print(message)
        
        elif key == keyboard.Key.left:
            print('left')
            message = send_command('rc 0 0 0 0')
            print(message)
        
        elif key == keyboard.Key.up:
            print('up')
            message = send_command('rc 0 0 0 0')
            print(message)

        elif key == keyboard.Key.down:
            print('down')
            message = send_command('rc 0 0 0 0')
            print(message)
        
        elif key.char == 'w':
            print('w')
            message = send_command('rc 0 0 0 0')
            print(message)
            print(message)
        
        elif key.char == 'a':
            print('a')
            message = send_command('rc 0 0 0 0')
            print(message)
        
        elif key.char == 's':
            print('s')
            message = send_command('rc 0 0 0 0')
            print(message)
        
        elif key.char == 'd':
            print('d')
            message = send_command('rc 0 0 0 0')
            print(message)
        

    except AttributeError:
        if key == keyboard.Key.esc:
            message = send_command('land')
            print(message)
            listner.stop()

with keyboard.Listener(on_press=on_press, on_release=on_release) as listner:
    listner.join()
