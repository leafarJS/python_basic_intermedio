### Dates ###
from datetime import timedelta
from datetime import date
from datetime import time
from datetime import datetime
# modulo de operaciones con fechas

now = datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

# metodo numerico
timestamp = now.timestamp()
print(timestamp)

# crear una fecha
year_2023 = datetime(2023, 2, 17)
print(year_2023)


current_time = time()
print(current_time.isoformat())
print(current_time.hour)
print(current_time.min)
print(current_time.second)

# time sin parametros es el resultado cero 0
current_time = time(15, 18, 22)
print(current_time.isoformat())
print(current_time.hour)
print(current_time.minute)
print(current_time.second)


current_date = date.today()
print(current_date)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2025, 12, 25)
print(current_date)

# modificar una fecha
current_date = date(2027, 12, 25)
print(current_date)


current_date = date(current_date.year,
                    current_date.month - 1,
                    current_date.day)
print(current_date.month)


# operar con diferentes fechas

time_delta = timedelta()
print(time_delta)

diff = year_2023 - now
print(diff)

diff = year_2023.date() - current_date
print(diff)

init_timedelta = timedelta(200, 10, 15, 125, 25, 2.5, 3.5)
end_timedelta = timedelta(400, 20, 30, 250, 50, 5.0, 7.0)
print(init_timedelta - end_timedelta)
print(init_timedelta + end_timedelta)
