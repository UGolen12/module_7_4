team1_num = 5  # Мастера Кода
team2_num = 6  # Волшебники Данных
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time1_avg = team1_time / score_1
time2_avg = team2_time / score_2
time_avg = (team1_time + team2_time) / tasks_total

if time1_avg < time2_avg:
    challenge_result = 'Победа команды Мастера Кода!'
elif time1_avg > time2_avg:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

print("В команде Мастера Кода участников: %s!" % team1_num)
print("Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num))
print("Команда Волшебники Данных решила задач: {}!".format(score_2))
print("Волшебники Данных решили задачи за {}с!".format(round(team2_time, 1)))
print(f"Команды решили {score_1} и {score_2} задач.")
print(f"Результат битвы: {challenge_result}")
print(f"Сегодня было решено {tasks_total} задач, в среднем по {round(time_avg, 1)} секунды на задачу!")