from datetime import date

now = date.today()
print(now)  # 2017-06-04
print(repr(now))  # datetime.date(2017, 6, 4)

s = now.strftime('%m-%d-%y. %d %b %Y is a %A on the %d say of %B')
print(s)  # 06-04-17. 04 Jun 2017 is a Sunday on the 04 say of June


birthday = date(1980, 11, 2)
age = now - birthday

print(age.days)  # 13363
