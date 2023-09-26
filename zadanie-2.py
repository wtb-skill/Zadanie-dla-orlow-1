# Stwórz funkcję, która sprawdza, czy możemy zbudować most

# Naszym zadaniem jest zbudowanie mostu pomiędzy punktem A i punktem B.
#
# Do dyspozycji mamy **płytę** oraz **łącznik**, które mają określone długości.
#
# Płyt nie możemy dzielić na mniejsze części, ustawiamy je jedna obok drugiej. Płyty muszą być połączone ze sobą za pomocą
# łącznika. Łącznik stanowi połowę długości płyty.
#
# Stwórz funkcję `build_bridge`, która będzie zwracać wartość `True`, jeśli mając płytę o długości danej zmienną `chunk`
# jesteśmy w stanie zbudować most o długości danej zmienną `goal`.
#
# Niech funkcja `build_bridge` zwraca wartość `False`, jeśli zbudowanie mostu przy założeniu zmiennych `chunk` oraz `goal`
# nie jest możliwe.
#
# Na przykład:
#
# Jeśli `goal` to 20, a `chunk` to 2 - wtedy możemy użyć 7 płyt i 6 łączników. Możemy zbudować most, a funkcja powinna
# zwracać wartość `True`.
#
# Z drugiej strony, jeśli `goal` to 18, a `chunk` to 2 - wtedy NIE możemy zbudować mostu, a funkcja powinna zwracać
# wartość `False`.


def build_bridge(goal, chunk):
    if (goal - chunk) % (1.5 * chunk) == 0:
        return True
    else:
        return False

test = [(20, 2), (18, 2), (15, 3), (100, 10)]

for pair in test:
    goal, chunk = pair
    print(f"Czy zbuduje się most wielkości goal={goal} z chunk={chunk}? \n"
          f"Odpowiedź: {build_bridge(goal=goal, chunk=chunk)}.")

