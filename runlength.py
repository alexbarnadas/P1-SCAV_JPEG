def encode(message):
    encoded_message = ""
    i = 0

    while i <= len(message) - 1:
        count = 1
        ch = message[i]
        j = i
        while j < len(message) - 1:
            if message[j + 1] == message[j]:
                count = count + 1
                j = j + 1
            else:
                break
        encoded_message = encoded_message + str (count) + ch
        i = j + 1
    return encoded_message


# Provide different values for message and test your program
sequence = input('Give me a bit sequence:   ')
encoded_message = encode(sequence)
print('Which  in run length is: ', encoded_message)

'''
Credits to:
https://www.geeksforgeeks.org/run-length-encoding-python/
'''
