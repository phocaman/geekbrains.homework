# № 2

# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры
# как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


def user_data(first_name, last_name, birth_year, city, e_address, phone):
    print(f"{first_name} {last_name}, {birth_year}, г. {city}, {e_address}, тел. {phone}")


user_data(first_name='Георгий', last_name='Еремин', birth_year=1979, city='Калининград',
          e_address='abc@xyz.com', phone='+01234567890')