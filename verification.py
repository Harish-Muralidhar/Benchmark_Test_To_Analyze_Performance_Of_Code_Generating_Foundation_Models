"""
This script is used to check the functional correctness of generated codes
it also generates success reports
"""
import pandas as pd
import os
import subprocess
import re
from metric import compute_metric

# generated code paths for different experimental tests
EXPERIMENT_A_SINGLE_SAMPLE_PATHS = ".\\generated_code\\experiment_a\\python_files"
EXPERIMENT_B_SINGLE_SAMPLE_PATHS = ".\\generated_codes\\experiment_b\\java_files"
EXPERIMENT_C_SINGLE_SAMPLE_PATHS_P_ONE = ".\\generated_code\\experiment_a\\python_files"
EXPERIMENT_C_FIVE_SAMPLES_PATHS_P_ONE = ".\\generated_codes\\experiment_c\\parameter_set_1\\five_samples\\python_files"
EXPERIMENT_C_SINGLE_SAMPLE_PATHS_P_TWO = ".\\generated_codes\\experiment_c\\parameter_set_2\\single_sample\\" \
                                         "python_files"
EXPERIMENT_C_FIVE_SAMPLES_PATHS_P_TWO = ".\\generated_codes\\experiment_c\\parameter_set_2\\five_samples\\python_files"

# types of generated codes
PYTHON_EXTENSION = ".py"
JAVA_EXTENSION = ".java"

# file with expected output and sample inputs
INPUT_PROBLEM_TEST_CASES = ".\\test_cases\\problem_test_cases.xlsx"


# extract complete filepath of generated code
def get_paths(filename, folder_path):
    for path, subdirs, files in os.walk(folder_path):
        for name in files:
            if name == filename:
                return os.path.join(path, name)


# stdin and stdout operations for python programs
def execute_python_program(inputs, program_file):
    try:
        proc = subprocess.Popen(["python", program_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, shell=True)
        out, _ = proc.communicate(bytes(inputs, "utf-8"))
        output_ = out.decode('utf-8').strip()
        return output_
    except Exception as e:
        print("cannot execute program")
        return e


# stdin and stdout operation for java programs
def execute_java_program(inputs, program_file):
    try:
        subprocess.check_call(['javac', program_file])
        java_class, ext = os.path.splitext(program_file)
        cmd = ['java', java_class]
        proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out, _ = proc.communicate(bytes(inputs, "utf-8"))
        output_ = out.decode('utf-8').strip()
        return output_
    except Exception as e:
        print("cannot execute program")
        return e


# generate verification report for different experiments
def verify_programs(temperature_, k, ext, test):
    test_cases = pd.read_excel(INPUT_PROBLEM_TEST_CASES)
    for index, row in test_cases.iterrows():
        sample_id = row["problem id"]

        i = 0
        while i < k:
            if k == 1:
                required_file = f"{sample_id}{ext}"
            else:
                required_file = f"{sample_id}_{i}{ext}"

            if test == "a":
                sample_file = get_paths(required_file, EXPERIMENT_A_SINGLE_SAMPLE_PATHS)
                print("FILE NAME")
                print(sample_file)
                actual_output = execute_python_program(row["example input"], sample_file)
                test_cases.at[index, "actual output"] = actual_output
                status_column_name = "status"

            elif test == "b":
                sample_file = get_paths(required_file, EXPERIMENT_B_SINGLE_SAMPLE_PATHS)
                print("FILE NAME")
                print(sample_file)
                actual_output = execute_java_program(row["example input"], sample_file)
                test_cases.at[index, "actual output"] = actual_output
                status_column_name = "status"

            else:
                if temperature_ == 0.7:
                    if k == 1:
                        sample_file = get_paths(required_file, EXPERIMENT_C_SINGLE_SAMPLE_PATHS_P_ONE)
                        print("FILE NAME")
                        print(sample_file)
                        actual_output = execute_python_program(row["example input"], sample_file)
                        test_cases.at[index, "actual output"] = actual_output
                        status_column_name = "status"
                    else:
                        sample_file = get_paths(required_file, EXPERIMENT_C_FIVE_SAMPLES_PATHS_P_ONE)
                        print("FILE NAME")
                        print(sample_file)
                        actual_output = execute_python_program(row["example input"], sample_file)
                        test_cases.at[index, f"x_{i}"] = actual_output
                        status_column_name = f"status x_{i}"
                else:
                    if k == 1:
                        sample_file = get_paths(required_file, EXPERIMENT_C_SINGLE_SAMPLE_PATHS_P_TWO)
                        print("FILE NAME")
                        print(sample_file)
                        actual_output = execute_python_program(row["example input"], sample_file)
                        test_cases.at[index, "actual output"] = actual_output
                        status_column_name = "status"
                    else:
                        sample_file = get_paths(required_file, EXPERIMENT_C_FIVE_SAMPLES_PATHS_P_TWO)
                        sample_file = get_paths(required_file, EXPERIMENT_A_SINGLE_SAMPLE_PATHS)
                        print("FILE NAME")
                        print(sample_file)
                        actual_output = execute_python_program(row["example input"], sample_file)
                        test_cases.at[index, f"x_{i}"] = actual_output
                        status_column_name = f"status x_{i}"

            print("EXPECTED OUTPUT")
            print(row["expected output"])

            print("ACTUAL OUTPUT")
            print(actual_output)

            if str(actual_output).strip() == str(row["expected output"]).strip():
                status = "success"
            else:
                status = "failure"

            test_cases.at[index, status_column_name] = status

            print("STATUS")
            print(status)
            print("\n\n")

            i = i + 1

    if temperature_ == 0.7:
        temp = "p_one"
    else:
        temp = "p_two"
    verification_report = f"{test}_{k}_{temp}_verification_report.xlsx"
    verification_report_path = os.path.join(".\\intermediate_results", verification_report)
    test_cases.to_excel(verification_report_path, index=False)
    compute_metric(temp, k, test, verification_report_path)
