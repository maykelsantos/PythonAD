import datetime

# ------------
hoje = datetime.datetime.today()
print(hoje)
print(type(hoje))

# ----------------
hoje1 = datetime.datetime.today().date()
print(hoje1)

# ----------------
data = datetime.datetime.today().date()

ano = data.year
mes = data.month
dia = data.day

print(dia, mes, ano)

# -------------
dataAntiga = datetime.date(1994, 9, 12)

print(hoje1 - dataAntiga) # necessário ser o mesmo formato de data

# Ajuste de formato

print(hoje1.strftime('%d/%m/%y'))
print(dataAntiga.strftime('%d/%m/%y'))

print(dataAntiga + datetime.timedelta(days=6012))