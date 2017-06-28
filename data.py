import datetime

months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
days = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

your_date = datetime.date.today()
month = your_date.month
year = your_date.year
month_name = months[month - 1]
years = (year - 2005) + 1

location = "Instituto Universitario de México"
schedule = "9:00 a 18 horas"
m = 5
d = 6
dt = datetime.date(year, m, d)
m = months[m - 1]
week_day = dt.weekday()
week_day = days[week_day]
dt = str(week_day) + " " + str(d) + " de " + str(m)
dt2 = str(d) + " de " + str(m)
