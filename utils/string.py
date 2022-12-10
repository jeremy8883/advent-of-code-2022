def insert_every(str, value, every):
    acc = ""
    for i, char in enumerate(str):
        if i != 0 and i % every == 0:
            acc = acc + value
        acc = acc + char
    return acc
