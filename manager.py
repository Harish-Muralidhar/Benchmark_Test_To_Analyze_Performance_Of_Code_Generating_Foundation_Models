"""
This script controls the different experimental tests
It sets parameters and performs end-to-end process via connecting scripts
"""
from read import process_experiment
from verification import verify_programs


# generating single samples of python code
def execute_experiment_a():
    prompt = "Write a python_files code for the following problem.\nImport the necessary libraries.\n"
    token_size = 4000
    temperature_value = 0.7
    k_value = 1
    extension = ".py"

    process_experiment(prompt, token_size, temperature_value, k_value, extension, "a")
    verify_programs(temperature_value, k_value, extension, "a")

    return


# generating single samples of java code
def execute_experiment_b():
    prompt = "Write a java code for the following problem.\nImport the necessary libraries.\n"
    token_size = 4000
    temperature_value = 0.7
    k_value = 1
    extension = ".java"

    process_experiment(prompt, token_size, temperature_value, k_value, extension, "b")
    verify_programs(temperature_value, k_value, extension, "b")

    return


# generating single and five samples per problem of python code
# parameter set one - temperature:0.7 max_token:4000
# parameter set two - temperature:0.3 max_token:500
def execute_experiment_c():
    prompt = "Write a python_files code for the following problem.\nImport the necessary libraries.\n"
    extension = ".py"

    process_experiment(prompt, 4000, 0.7, 1, extension, "c")
    verify_programs(0.7, 1, extension, "c")

    process_experiment(prompt, 4000, 0.7, 5, extension, "c")
    verify_programs(0.7, 5, extension, "c")

    process_experiment(prompt, 500, 0.3, 1, extension, "c")
    verify_programs(0.3, 1, extension, "c")

    process_experiment(prompt, 500, 0.3, 5, extension, "c")
    verify_programs(0.3, 5, extension, "c")
    return
