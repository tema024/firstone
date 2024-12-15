text = input()

key = ["ЕШ", "ГИ", "ПФ", "ЖР", "ОВ", "НЖ", "ЩЕ", "ЮН",
    "ЭА", "БТ", "ЭА", "ЧК", "МД", "ЯЛ", "ХЬ", "ЫЙ", "ЦО",
    "ИЯ", "ЛЧ", "ДЁ", "ШС", "АП", "РГ", "СМ", "ЙЗ", "ЗЫ",
    "ВХ", "ЬБ", "ЁЦ", "КЭ", "ТУ", "ФЮ",
    "еш", "ги", "пф", "жр", "ов", "нж", "ще", "юн", "эа",
    "бт", "за", "чк", "мд", "ял", "хь", "ый", "цо", "ия",
    "лч", "дё", "шс", "ап", "рг", "см", "йз", "зы", "вх",
    "ьб", "ёц", "кэ", "ту", "фю"]

dict = {}
for pair in key:
    en, de = pair[0], pair[1]
    dict[en] = de

decrypted = ""
for char in text:
    if char in dict:
        decrypted += dict[char]
    else:
        decrypted += char

print("Зашифрованный текст:", text)
print("Расшифрованный текст:", decrypted)
