"""
This script is used to compute pass@k metric
"""
import os.path
import pandas as pd
import numpy as np

# category wise information
easy_category_begin = 0
easy_category_end = 49
hard_category_begin = 50
hard_category_end = 99
medium_category_begin = 100
medium_category_end = 149

# final computations folder
results_folder = ".\\results"


# pass@k computation
def pass_k(n_, c_, k_):
    if (n_-c_) < k_:
        return 1.0
    return 1.0 - np.prod(1.0-k_/np.arange(n_-c_+1, n_+1))


# percentage conversion
def evaluate(no, co, ko):
    performance_evaluation = "{:.2f}".format(pass_k(no, co, ko) * 100)
    performance_evaluation = f"{performance_evaluation}%"
    return performance_evaluation


# counting correct samples from success report
def get_correct_samples(number_of_problems, report_, selected_column):
    i = 0
    temp = 0
    correct_sample = 0
    easy_correct_samples = 0
    medium_correct_samples = 0
    hard_correct_samples = 0
    while i < number_of_problems:
        temp_df = report_.loc[report_['problem id'] == i]
        status_list = temp_df[selected_column].unique().tolist()
        if "failure" not in status_list:
            correct_sample = correct_sample + 1
            temp = temp + 1
        if i == easy_category_end:
            easy_correct_samples = temp
            temp = 0
        if i == hard_category_end:
            hard_correct_samples = temp
            temp = 0
        if i == medium_category_end:
            medium_correct_samples = temp
            temp = 0
        i = i + 1

    return correct_sample, easy_correct_samples, medium_correct_samples, hard_correct_samples


# k=1 settings
def set_properties_single_sample(success_report):
    report = pd.read_excel(success_report)
    total_problems = 150
    required_column = "status"
    c_, e_, m_, h_ = get_correct_samples(total_problems, report, required_column)
    n_ = 150
    k_ = 1
    return n_, c_, k_, e_, m_, h_


# k=5 settings
def set_properties_five_samples(success_report):
    c_ = 0
    c__ = 0
    e_ = 0
    e__ = 0
    m_ = 0
    m__ = 0
    h_ = 0
    h__ = 0
    i = 0
    report = pd.read_excel(success_report)
    while i < 5:
        required_column = f"status x_{i}"
        required_df_ = report[["problem id", "problem path", required_column]]
        total_problems = 150
        c_, e_, m_, h_ = get_correct_samples(total_problems, required_df_, required_column)
        c__ = c__ + c_
        e__ = e__ + e_
        m__ = m__ + m_
        h__ = h__ + h_
        i = i + 1
    n_ = 750
    k_ = 5
    return n_, c__, k_, e__, m__, h__


# saving computations
def compute_metric(temp_, k_value, test, verification_report):
    results_file = f"{test}_{k_value}_{temp_}_results.xlsx"
    results_path = os.path.join(results_folder, results_file)
    if test == "a":
        n, c, k, easy, medium, hard = set_properties_single_sample(verification_report)
        performance_complete = evaluate(n, c, k)
        single_sample_overall = ["overall", "pass@1", n, c, k, performance_complete]
        performance_easy = evaluate(50, easy, k)
        single_sample_easy = ["easy", "pass@1", 50, easy, k, performance_easy]
        performance_medium = evaluate(50, medium, k)
        single_sample_medium = ["medium", "pass@1", 50, medium, k, performance_medium]
        performance_hard = evaluate(50, hard, k)
        single_sample_hard = ["hard", "pass@1", 50, hard, k, performance_hard]

        values = [single_sample_overall, single_sample_easy, single_sample_medium, single_sample_hard]
        result_dataframe = pd.DataFrame(values,
                                        columns=["category", "metric", "number of samples", "number of correct samples",
                                                 "k value",
                                                 "Performance evaluation"])
        result_dataframe.to_excel(results_path, index=False)

    elif test == "b":
        n, c, k, easy, medium, hard = set_properties_single_sample(verification_report)
        performance_complete = evaluate(n, c, k)
        single_sample_overall = ["overall", "pass@1", n, c, k, performance_complete]
        performance_easy = evaluate(50, easy, k)
        single_sample_easy = ["easy", "pass@1", 50, easy, k, performance_easy]
        performance_medium = evaluate(50, medium, k)
        single_sample_medium = ["medium", "pass@1", 50, medium, k, performance_medium]
        performance_hard = evaluate(50, hard, k)
        single_sample_hard = ["hard", "pass@1", 50, hard, k, performance_hard]
        values = [single_sample_overall, single_sample_easy, single_sample_medium, single_sample_hard]
        result_dataframe = pd.DataFrame(values,
                                        columns=["category", "metric", "number of samples", "number of correct samples",
                                                 "k value",
                                                 "Performance evaluation"])
        result_dataframe.to_excel(results_path, index=False)

    elif test == "c":
        if k_value == 1:
            n, c, k, easy, medium, hard = set_properties_single_sample(verification_report)
            performance_complete = evaluate(n, c, k)
            single_sample_overall = ["overall", "pass@1", n, c, k, performance_complete]
            performance_easy = evaluate(50, easy, k)
            single_sample_easy = ["easy", "pass@1", 50, easy, k, performance_easy]
            performance_medium = evaluate(50, medium, k)
            single_sample_medium = ["medium", "pass@1", 50, medium, k, performance_medium]
            performance_hard = evaluate(50, hard, k)
            single_sample_hard = ["hard", "pass@1", 50, hard, k, performance_hard]
            values = [single_sample_overall, single_sample_easy, single_sample_medium, single_sample_hard]
            result_dataframe = pd.DataFrame(values,
                                            columns=["category", "metric", "number of samples",
                                                     "number of correct samples",
                                                     "k value",
                                                     "Performance evaluation"])
            result_dataframe.to_excel(results_path, index=False)
        else:
            n, c, k, e, m, h = set_properties_five_samples(verification_report)
            performance_complete = evaluate(n, c, k)
            five_samples_overall = ["overall", "pass@5", n, c, k, performance_complete]
            performance_easy = evaluate(250, e, k)
            five_samples_easy = ["easy", "pass@5", 250, e, k, performance_easy]
            performance_medium = evaluate(250, m, k)
            five_samples_medium = ["medium", "pass@5", 250, m, k, performance_medium]
            performance_hard = evaluate(250, h, k)
            five_samples_hard = ["hard", "pass@5", 250, h, k, performance_hard]
            values = [five_samples_overall, five_samples_easy, five_samples_medium, five_samples_hard]
            result_dataframe = pd.DataFrame(values, columns=["category", "metric", "number of samples",
                                                             "number of correct samples", "k value",
                                                             "Performance evaluation"])
            result_dataframe.to_excel(results_path, index=False)














