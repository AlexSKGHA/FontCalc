import string

def wordList(sentence):
    words = []
    word = ''
    for k,v in enumerate(sentence):
        word += v
        if v == ' ' or k == len(sentence) - 1:
            words.append(word)
            word = ''
    return words
    

russianABC='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
digits = string.digits

storage = dict()

raw_data = (
    ('ГЕЗС23567890',(2.5,3.5,5.0)),
    ('АДМЮЫ',(3.5,4.9,7.0)),
    ('ХФШЩЖ',(4.0,5.6,8.0)),
    ('БВЁИЙКЛНОПРТУЦЧЪЬЭЯ4',(3.0,4.0,6.0)),
    ('зс',(2.0,2.8,4.0)),
    ('мыю',(3.5,4.9,7.0)),
    ('хфшщт',(4.0,5.6,8.0)),
    ('абвгдеёжийклнопрсучъьэя',(2.5,3.5,5.0)),
    ('1',(1.5,2.1,3.0)),
    (' ',(3.0,4.2,6.0))
)

for k, v in raw_data:
    for i in k:
        storage[i] = v    

#additional data
distance_between_letters = 1.0,1.4,2.0                   
height_of_some_lowercase_letters = 5.0,7.0,10.0

while True:
    input_data = input('Enter a sentence: ')
    size = int(input('Enter a font: '))
    words = wordList(input_data)
    result = 0
    for word in words:
        for letter in word:
            print(letter, storage[letter][size])
            result += storage[letter][size]
        result += distance_between_letters[size] * (len(word) - 1)
    print(result, 'mm')
