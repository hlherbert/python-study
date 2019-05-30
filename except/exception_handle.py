try:
    text=input('enter something-->')
except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('you cancelled the operation.')
else:
    print('you entered: {}'.format(text))
