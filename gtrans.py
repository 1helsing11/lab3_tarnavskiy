from my_package.gt_translator import *

text_to_translate = "Привіт, чудовий світ"

in_polish = translate(text_to_translate, dest='pl')
in_chinese = translate(text_to_translate, src='ukrainian',  dest='zh-cn')
in_estonian = translate(text_to_translate, src='uk',  dest='estonian')

detected_lang = lang_detect(text_to_translate, set='lang')

detected_lang_name = translate(code_lang(detected_lang))
detected_lang_confidence = lang_detect(text_to_translate, set='confidence')

print(
    f'''Текст: {text_to_translate}
Виявлена мова оригіналу: {detected_lang_name} (достовірність 100%)
Переклади:
  Польською: {in_polish}
  Німецькою: {in_chinese}
  Естонською: {in_estonian}\n
  '''
)

show_table = True if input("Показати таблицю мов? (+/-): ") == '+' else False

if show_table:
    text_for_example = ''
    text_for_example = input("Текст для прикладу: ")
    language_list('screen', text=text_for_example)

    if input("Зберегти цю таблицю до файлу? (+/-): ") == '+':
        language_list('file', text=text_for_example)
