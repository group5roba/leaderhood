# პირველი ამოცანა
def human_years_cat_years_dog_years(human_years):
    cat_year = 0
    dog_year = 0
    if human_years == 1:
        cat_year += 15
        dog_year += 15
    elif human_years == 2:
        cat_year += 24
        dog_year += 24
    else:
        cat_year += 24 + (human_years - 2) * 4
        dog_year += 24 + (human_years - 2) * 5
    return[human_years, cat_year, dog_year]


# მეორე ამოცანა
def nearest_sq(n):
    num = round(n ** 0.5)
    return num ** 2