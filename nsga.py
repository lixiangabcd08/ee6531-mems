from solution import Solution

class NSGA:
    def __init__(self):
        pass

    def is_dominated(self, solution_1, solution_2):
        if solution_1.objective_1 > solution_2.objective_1 and solution_1.objective_2 > solution_2.objective_2 \
            and solution_1.objective_3 > solution_2.objective_3:
            return True
        else:
            return False

