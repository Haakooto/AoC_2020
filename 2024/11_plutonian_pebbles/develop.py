from main import alt

if alt == 1:
    from solver import solver_alt1 as solver
elif alt == 2:
    from solver import solver_alt2 as solver
elif alt == 3:
    from solver import solver1_alt3 as solver1, solver2_alt3 as solver2
from solver import func_that_does_the_thing

test1 = "test_input.txt", 1
if alt != 3:
    solver(*test1)
else:
    solver1(*test1)
