"""
This script is used to read and modify input descriptions
"""
import pandas as pd
import os
from output import save_responses
from model import run_model

# questions dataset details
CODECHEF_PROBLEMS_PATH = ".\\data\\codechef"
INTERMEDIATE_RESULTS_PATH = ".\\intermediate_results"
CODECHEF_PROMPTS_FILE_NAMES = "description.txt"


# extract filepaths for problem description files
def get_input_paths():
    input_files_paths = []
    for path, subdirs, files in os.walk(CODECHEF_PROBLEMS_PATH):
        for name in files:
            if name == CODECHEF_PROMPTS_FILE_NAMES:
                input_files_paths.append(os.path.join(path, name))
    return input_files_paths


# read problems into dataframe
def read_codechef_data():
    files = get_input_paths()
    data = []
    prompt_id = 0
    for file in files:
        prompt_id += 1
        with open(file, encoding="utf-8") as problem:
            prompt = problem.read()
        data.append([prompt_id, file, prompt])
    data_ = pd.DataFrame(data, columns=["task_id", "path", "prompt"])
    return data_


# modify and pass problem descriptions to model
def process_experiment(prompt, max_tokens, temperature, k, extension, experiment_name):
    # read data
    problems_data = read_codechef_data()
    problems_store = "problem_info.xlsx"
    problems_data.to_excel(os.path.join(INTERMEDIATE_RESULTS_PATH, problems_store), index=False)

    for problem_id, problem_row in problems_data.iterrows():

        # modify input
        print("Generating Code for Question", problem_id)
        problem_description = problem_row["prompt"]
        modified_description = f"\"\"\"\n{prompt}{problem_description}\n\"\"\""

        # pass parameters to Codex API
        i = 0
        while i < k:
            model_generated_code = run_model(modified_description, temperature, max_tokens)
            filename = problem_id
            if k != 1:
                filename = f"{problem_id}_{i}"
            filename_ = f"{filename}{extension}"

            if experiment_name == "a":
                save_responses(os.path.join(".\\generated_codes\\experiment_a\\python_files", filename_),
                               model_generated_code)
            elif experiment_name == "b":
                save_responses(os.path.join(".\\generated_codes\\experiment_b\\java_files", filename_),
                               model_generated_code)
            else:
                if temperature == 0.7:
                    if k == 1:
                        save_responses(os.path.join(".\\generated_codes\\experiment_c\\parameter_set_1\\single_sample\\"
                                                    "python_files", filename_), model_generated_code)
                    else:
                        save_responses(os.path.join(".\\generated_codes\\experiment_c\\parameter_set_1\\five_samples\\"
                                                    "python_files", filename_), model_generated_code)
                else:
                    if k == 1:
                        save_responses(os.path.join(".\\generated_codes\\experiment_c\\parameter_set_2\\single_sample\\"
                                                    "python_files", filename_), model_generated_code)
                    else:
                        save_responses(os.path.join(".\\generated_codes\\experiment_c\\parameter_set_2\\five_samples\\"
                                                    "python_files", filename_), model_generated_code)
            i = i + 1
    return
