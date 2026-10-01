def get_day_of_week(day, month, year):
  month_code = {
  1: 1, 2: 4, 3: 4, 4: 0, 5: 2, 6: 5, 7: 0, 8: 3, 9: 6, 10: 1, 11: 4, 12: 6
  }

  days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

  century = year // 100 # this give you the century 2026-->26
  last_two_digits = year % 100  # This gives you the last two digits of the century eg: 2026--->26
  year_code = last_two_digits + (last_two_digits // 4)
  month_code =month_code[month]
  if century == 16 or century == 20: 
    century_code = 6 
  elif century == 17 or century == 21:
    century_code = 4
  elif century == 18 or century == 22:
    century_code = 2
  elif century == 19 or century == 23:
    century_code = 0 
  else: 
    print("error: century not recognized.")

  is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

  if is_leap and month == 1:
    month_code = 0 # 1 minus 1
  elif is_leap and month == 2:
    month_code = 3

  total = year_code + month_code + century_code + day
  remainder = total % 7
  return days_of_week[remainder]

test_day = int(input("enter a day: "))
test_month = int(input("enter a month: "))
test_year = int(input("enter a year: "))

result = get_day_of_week(test_day, test_month, test_year)
print(f"The date {test_day}/{test_month}/{test_year} falls on a: {result}")