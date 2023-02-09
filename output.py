"""
This script is used to parse and store model outputs
"""
import time


# extract code from complete model output
def parse_result(codex_output):
    if 'choices' in codex_output:
        x = codex_output['choices']
        if len(x) > 0:
            print("Code generated Successfully")
            # print(x[0]['text'])
            return x[0]['text']
        else:
            return ''
    else:
        return ''


# save model generated code locally
def save_responses(file_save_path, content):
    if '\'\'\'' in content:
        content = f"'''\n{content}"
    elif "\"\"\"" in content:
        content = f'"""\n{content}'
    elif '*/' in content:
        content = f'/*\n{content}'
    print("Saving code as file")
    with open(file_save_path, "w", encoding="UTF-8") as code_file:
        code_file.write(content)
    print("File saved successfully.")
    print("waiting....")
    time.sleep(80)
    print("wait time over\n\n")
