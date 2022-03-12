# 3. Написать функцию thesaurus(),
# принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена,
# начинающиеся с соответствующей буквы. Например:
# >>>  thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }

def thesaurus(*names):
    list_name = [*names]
    directory = {}
    for name in list_name:
        name.capitalize()
        char = name[0]
        dict_1 = {char : name}
        directory.update(dict_1)

    return directory

print(thesaurus("Иван", "Мария", "Петр", "Илья"))






