import datetime

months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
days = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

your_date = datetime.date.today()
month = your_date.month
year = your_date.year # Today's year
month_name = months[month - 1] # Today's month
years = (year - 2005) + 1 # Years of FLISoL

location = "Instituto Universitario de México"
schedule = "9:00 a 18 horas"
# Date of the event
m = 5 # Month
d = 6 # Day
dt = datetime.date(year, m, d)
m = months[m - 1] # Month name
week_day = dt.weekday() # Day of
week_day = days[week_day] # the week
dt = str(week_day) + " " + str(d) + " de " + str(m)
dt2 = str(d) + " de " + str(m)
