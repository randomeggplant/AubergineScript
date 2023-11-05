import PlainScript

while True:
    text = input('PlainScript > ')
    result, error = PlainScript.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)