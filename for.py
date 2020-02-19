"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

students_scores = [
  {'school_class': '4a', 'scores': [3,4,4,5,2]}, 
  {'school_class': '4b', 'scores': [5,5,3,5,4]}
]

students_average_score = []

def main():
  for s in students_scores:
      students_average_score.append(sum(s['scores'])/len(s['scores']))
      print(f"Средняя оценка для класса {s['school_class']} : {(sum(s['scores']) / len(s['scores']))}")

  school_average_score = sum(students_average_score)/len(students_average_score)
  print(f"Средняя оценка по школе: {school_average_score}")
  
main()