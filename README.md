# Benchmark_Test_To_Analyze_Performance_Of_Code_Generating_Foundation_Models
Repo for Master Thesis

Overview:

This repository contains the implementation scripts which can be used to conduct performance evaluations of codex by OpenAI. This repo contains scripts to perform three different experiments for performance evaluation. Experiment A generates single samples of python codes per problem. Experiment B generates single samples of java codes per problem. Experiment C has two sets of model parameter inputs and generates single and five samples per problem for both parameter sets. Functional correctness of programs is verified and pass@k metric is used to analyze performance. The data folder contains the competitive questions dataset which is used to conduct the tests. The automatically generated programs for questions dataset is stored in the generated codes folder based on the experimental test being conducted. The intermediate results and the final performance results are stored in their respective folders.

Steps:

1. Clone the repository to your local machine.
2. Go to main.py python script.
3. The default experiment conducted will be Experiment A. User has to change variable names in main.py to perform different experimental tests.
3. Make appropriate changes to run different experimental tests. More information is commented in the main script on where and how to select experiment.
4. Run the command "python main.py"

Note:

* There is a wait time after each generated code to avoid API exceptions regarding limited token exchange rate per minute.
* Category wise results can be observed in the results folder for all the experimental tests
* An API key from OpenAI is necessary to execute this project. Communication via API is only possible after saving API key obtained through their private beta as an environment variable
