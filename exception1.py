"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

question = {'Как дела?': 'Хорошо!', 'Что делаешь?': 'Программирую'}

def ask_user():
  try:
    while True:
      user_say = input('Пользователь: ')
      if user_say == "Как дела?":
          print(question['Как дела?'])
      elif user_say == "Что делаешь?":
          print(question['Что делаешь?'])
  except(KeyboardInterrupt):
      print('Пока!')
    
if __name__ == "__main__":
    ask_user()
