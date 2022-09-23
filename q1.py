"""For question 1."""
import numpy as np
from scipy import stats


def main():
    """Do question 1, write results to 1.tex"""

    # open file, read into array
    x, y, z = np.array(np.loadtxt("fakedata.out")).transpose()

    # get means
    mean_text = \
        f"$\\overline{{X}} = {np.mean(x):.2f},"\
        f" \\overline{{Y}} = {np.mean(y):.2f},"\
        f" \\overline{{Z}} = {np.mean(z):.2f}$."
    print(mean_text)

    # get standard deviations
    std_text = \
        f"$\\sigma_{{X}} = {np.std(x):.2f},"\
        f" \\sigma_{{Y}} = {np.std(y):.2f},"\
        f" \\sigma_{{Z}} = {np.std(z):.2f}$."
    print(std_text)

    # get correlation coefficients
    cor_text = \
        f"$C_{{X,Y}} = {np.corrcoef(x,y)[0,1]:.2f},"\
        f" C_{{X,Z}} = {np.corrcoef(x,z)[0,1]:.2f},"\
        f" C_{{Y,Z}} = {np.corrcoef(y,z)[0,1]:.2f}$."
    print(cor_text)

    # get skewness
    skew_text = \
        f"$\\operatorname{{Skew}}(X) = {stats.skew(x):.2f},"\
        f" \\operatorname{{Skew}}(Y) = {stats.skew(y):.2f},"\
        f" \\operatorname{{Skew}}(Z) = {stats.skew(z):.2f}$."
    print(skew_text)

    # put results in LaTeX format to include in the main assignment pdf
    tex = f"""
    \\section{{\\texttt{{fakedata.out}} contains 200 observations
    of three random variables: \\texorpdfstring{{$X$}}{{X}},
    \\texorpdfstring{{$Y$}}{{Y}}, and \\texorpdfstring{{$Z$}}{{Z}}
    (each variable in its own column, listed in that order).
    Calculate the following for this data:}}

    \\begin{{enumerate}}[label=\\textbf{{\\Alph*}}.]
        \\item The mean values of $X$, $Y$, and $Z$.

        {mean_text}

        \\item The standard deviations for all three variables.

        {std_text}

        \\item The three correlation coefficients between the three variables.

        {cor_text}

        \\item The skew for $X$, $Y$, and $Z$.
        
        {skew_text}
    \\end{{enumerate}}
    """
    with open("1.tex", 'w', encoding="utf-8") as outputfile:
        outputfile.write(tex)


if __name__ == "__main__":
    main()
