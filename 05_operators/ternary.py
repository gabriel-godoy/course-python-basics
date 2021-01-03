#!python3

lockdown = False
grana = 30

status = 'Em casa' if lockdown or grana <= 100 else 'Uhuuuu'

print(f'O status é "{status}"')
