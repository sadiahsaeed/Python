# Comparison of factorial function vs Stirling approximation for factorial
import math
import matplotlib.pyplot as plt

e = 2.718
num = range(0, 143)
number = []
factorial = []
stirling_approx = []

for n in num:
    ft = math.factorial(n)  # factorial built_in functon
    stir_fact = (math.sqrt(2 * 3.14 * n) * math.pow(e, -n) * math.pow(n, n))

    number.append(n)
    factorial.append(ft)
    stirling_approx.append(stir_fact)

plt.plot(number, factorial, linewidth=1, markersize=12)
plt.plot(number, stirling_approx, color='green', linestyle='dashed', linewidth=2, markersize=12)
plt.xlabel("Numbers")
plt.ylabel("Factorial")
plt.legend(['Factorial Function', 'Stirling Approximation'])
plt.show()
