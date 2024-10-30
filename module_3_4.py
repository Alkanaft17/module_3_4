# Объявите функцию single_root_words и напишите в ней параметры root_word и *other_words.
def single_root_words(root_word, *other_words):
# Создайте внутри функции пустой список same_words, который пополнится нужными словами.
    same_words = []
    root_word_lower = root_word.lower()
# При помощи цикла for переберите предполагаемо подходящие слова.
    for i in other_words:
        other_words = i.lower()
# Пропишите корректное относительно задачи условие, при котором добавляются слова в результирующий список same_words.
        if root_word_lower in other_words or other_words  in root_word_lower:
            same_words.append(i)
# После цикла верните образованный функцией список same_words.
    return same_words

# Вызовите функцию single_root_words и выведете на экран(консоль) возвращённое ей значение.
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)