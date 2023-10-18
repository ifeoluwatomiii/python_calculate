name_1 = input("What is your name? :" )
name_2 = input("What is your name? :")
name_3 = input("What is your name? :")

slices_in_the_pizza = int(input("How many slices in the pizza :"))
price_of_the_pizza = float(input("What is the price of the pizza :"))

percentage_eaten_by_person_1 = float(input(name_1 + "what percentage of the pizza did you eat? :"))
percentage_eaten_by_person_2 = float(input(name_2 + "what percentage of the pizza did you eat? :"))
percentage_eaten_by_person_3 = float(input(name_3 + "what percentage of the pizza did you eat? :"))

number_of_slices_eaten_by_person_1 =(percentage_eaten_by_person_1/100) * slices_in_the_pizza
number_of_slices_eaten_by_person_2 =(percentage_eaten_by_person_2/100) * slices_in_the_pizza
number_of_slices_eaten_by_person_3 =(percentage_eaten_by_person_3/100) * slices_in_the_pizza

price_payed_by_name_1 =(percentage_eaten_by_person_1/100) * price_of_the_pizza
price_payed_by_name_2 =(percentage_eaten_by_person_2/100) * price_of_the_pizza
price_payed_by_name_3 =(percentage_eaten_by_person_3/100) * price_of_the_pizza

print(name_1 + " has eaten " + str(number_of_slices_eaten_by_person_1) + " slices and has payed $ " + str (price_payed_by_name_1))
print(name_2 + " has eaten " + str(number_of_slices_eaten_by_person_2) + " slices and has payed $ " + str (price_payed_by_name_2))
print(name_3 + " has eaten " + str(number_of_slices_eaten_by_person_3) + " slices and has payed $ " + str (price_payed_by_name_3))