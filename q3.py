"""For question 3."""
import numpy as np
from scipy import stats
from scipy.integrate import quad




# put results in LaTeX format to include in the main assignment pdf
tex = f"""
\\section{{Numerically calculate the probability that a number drawn
from a $\\chi^2$ distribution with $n=2$ degrees of freedom will be larger
than $\\chi^2=5$. Do the same for $n=10$. Do not use a lookup table or a
pre-existing function to evaluate the answer, but calculate it for yourself
as if you had just discovered the $\\chi^2$ distribution for the first time.}}

\\begin{{itemize}}
    \\item $\\operatorname{{P}}(\\chi^2_{{5}} < 5) = {answer_5:.2f}$.

    \\item $\\operatorname{{P}}(\\chi^2_{{10}} < 5) = {answer_10:.2f}$.
\\end{{itemize}}
"""
with open("2.tex", 'w', encoding="utf-8") as outputfile:
    outputfile.write(tex)
