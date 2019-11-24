
# 1.Пользователь вводит свое имя и возраст вывести строку в формате 
# - “Hello {username} your age is {age}”, заменить текст в фигурных скобках на значения введенные пользователем.
username = input("Enter your name : ")
age = input("Enter your age : ")
print ('Hello' + ' ' + username + ' ' + 'your age is:' + age + '!')



# 2.Пользователь вводит число,
#  вывести его в 132 степени и Показать его остаток от деления на 3.
#  Вывод должен быть в одну строку с пояснениями.
number = int(input("Enter number: "))
result = pow(number, 132, 3)
print ('The remainder of dividing by 3 numbers ',
 str(number), ' to the power of 132 is: ', str(result))



# 3.Дан список из целых чисел длиной N подсчитать количество четных чисел в списке
list_of_numbers = [1, 2, 2, 2, 22, 1, 3, 246]
even = 0
for number in list_of_numbers: 
    if number % 2 == 0: 
        even += 1
print("The number of even numbers in the list is: ", even) 



# 4.Дан список целых чисел длиной N 
# найти наибольший элемент в списке и наименьший элемент в списке
list_of_numbers = [1, 2, 2, 2, 22, 1, 3, -246, -1000, 555]
list_of_numbers.sort()
print ('Highest number is ', list_of_numbers[-1], ' and lowest number is ', list_of_numbers[0])



# 5.Дан список строк длиной N,
# поменять местами самую длинную и самую короткую строку в списке
list_str = ['ddgdfgsdgfd', 'aa', 'a', 'ab', 'abcdd', 'asd', 'resgg']
max_str = max(list_str, key=len)
max_index = int(list_str.index(max_str))
print (max_index)
min_str = min(list_str, key=len)
min_index = int(list_str.index(min_str))
print (min_index)
print (list_str)
list_str[max_index], list_str[min_index] = list_str[min_index], list_str[max_index]
print (list_str)


