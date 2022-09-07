"""Run all the python scripts, then run pdflatex to make the final pdf."""
import os
import q1
import q2

q1.main()
q2.main()
# no code for q3 or q4

os.system("pdflatex main.tex")
