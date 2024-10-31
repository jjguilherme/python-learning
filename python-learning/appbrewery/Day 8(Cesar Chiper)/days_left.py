def life_in_days(age):
    days_left = (90*365) - (age*365)
    return days_left

age = int(input("What is your age? "))

days_left = life_in_days(age)

print(f"You have {days_left} days left until you turn 90.")


#def life_in_weeks(age):
 #   years_remaining = 90 - age
  #  weeks_remaining = years_remaining * 52
   # print(f"You have {weeks_remaining} weeks left.")


#life_in_weeks(12)


