"""For question 2."""
import numpy as np
from scipy import stats
from scipy.integrate import quad


def main():
    """Do question 2, write results to 2.tex"""

    # p(x^2_n > 5) = integral of pdf from 5 to infinity
    # the lambda functions are there to set n=5 or 10 in the general chi2 pdf,
    # quad integrates that function between the bounds we give it (5 and inf),
    # and the [0] at the end is there since quad returns (result, error)
    answer_5 = quad(lambda x: stats.chi2.pdf(x, 5), 5, np.inf)[0]
    print("Answer for n=5:", answer_5)

    answer_10 = quad(lambda x: stats.chi2.pdf(x, 10), 5, np.inf)[0]
    print("Answer for n=10:", answer_10)

    # put results in LaTeX format to include in the main assignment pdf
    tex = f"""
    \\section{{Numerically calculate the probability that a number drawn
    from a \\texorpdfstring{{$\\chi^2$}}{{chi-squared}} distribution with 
    \\texorpdfstring{{$n=5$}}{{n=5}} degrees of freedom will be larger
    than \\texorpdfstring{{$\\chi^2=5$}}{{chi-squared=5}}.
    Do the same for \\texorpdfstring{{$n=10$}}{{n=10}}.
    Do not use a lookup table or a pre-existing function to evaluate the
    answer, but calculate it for yourself as if you had just discovered the
    \\texorpdfstring{{$\\chi^2$}}{{chi-squared}}
    distribution for the first time.}}

    \\begin{{itemize}}
        \\item $\\operatorname{{P}}(\\chi^2_{{5}} < 5) = {answer_5:.2f}$.

        \\item $\\operatorname{{P}}(\\chi^2_{{10}} < 5) = {answer_10:.2f}$.
    \\end{{itemize}}
    """
    with open("2.tex", 'w', encoding="utf-8") as outputfile:
        outputfile.write(tex)


if __name__ == "__main__":
    main()
