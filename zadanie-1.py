# Znajdź średnią zmodyfikowanej listy.
#
# Twoim zadaniem jest zmodyfikowanie listy przypisanej do zmiennej `numbers` w taki sposób, aby każdy jej element
# zaokrąglić do pełnej dziesiątki. Postaraj się nie tworzyć nowej listy będącej zmodyfikowaną listą `numbers`,
# lecz zmodyfikować listę `numbers`.
#
# Po zaokrągleniu każdego elementu listy `numbers` pozbądź się jej największego oraz najmniejszego elementu,
# a następnie do zmiennej `mean_number` przypisz średnią z ostatecznie zmodyfikowanej listy.
#
# **Podsumowując:**
#
# 1. zaokrąglij każdy element numbers do pełnej 10 (np. 5 -> 10, 32 -> 30)
# 2. znajdź, a następnie pozbądź się największego oraz najmniejszego elementu zmodyfikowanej listy
# 3. policz średnią z ostatecznie zmodyfikowanej listy `numbers` i przypisz ją do zmiennej `mean_number`

numbers = [5, 32, 56, 2, 2, 16, 7, 10, 23, 100]
mean_number = 0

numbers = [round(i/10) * 10 for i in numbers]

min_num = min(numbers)
max_num = max(numbers)
numbers.remove(min_num)
numbers.remove(max_num)

print(numbers)



