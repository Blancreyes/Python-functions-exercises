# Your code goes here:
def render_person(name, birth_date, eyes_color, age, gender):
    string= name+" is a "+str(age)+" years old "+gender+" born in "+str(birth_date)+" with "+eyes_color+" eyes"
    return string


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))