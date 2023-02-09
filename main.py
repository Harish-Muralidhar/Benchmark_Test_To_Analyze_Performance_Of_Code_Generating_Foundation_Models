"""
This is the main script to be run in order to conduct the experiments. Selection of experimental test can be done here
go to function call execute_test(experiment_name) and change experiment name as required
"""
from manager import execute_experiment_a, execute_experiment_b, execute_experiment_c

# different experiment names
EXPERIMENT_A = "experiment_a"
EXPERIMENT_B = "experiment_b"
EXPERIMENT_C = "experiment_C"


def execute_test(test_name):
    if test_name == EXPERIMENT_A:
        execute_experiment_a()
    elif test_name == EXPERIMENT_B:
        execute_experiment_b()
    elif test_name == EXPERIMENT_C:
        execute_experiment_c()
    else:
        print("Enter valid experiment name")
    return


if __name__ == "__main__":
    print("The chosen experiment is:")

    # change experiment name based on which experimental test has to be performed
    experiment_name = EXPERIMENT_A
    print(experiment_name)
    execute_test(experiment_name)

