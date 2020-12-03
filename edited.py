import sys
import clipboard
print('Your text', end=''); message = str(input('  :  '))

MAGIC_CHAR = '\u202b'

res = f'{MAGIC_CHAR} {message} {MAGIC_CHAR}'

clipboard.copy(res)
print("\nSuccessfully Copied Text to Clipboard!\nEnter any key to exit ... ", end = "")

input()
print()