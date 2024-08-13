def transform_text(text):
    vowels = 'aeiouAEIOU'
    transformed_text = ''
    
    for char in text:
        if char in vowels:
            transformed_text += '-'
        elif char.isalpha():
            transformed_text += '.'
        else:
            transformed_text += char

    return transformed_text

input_text = "" # Enter text
output_text = transform_text(input_text)
print(output_text)
