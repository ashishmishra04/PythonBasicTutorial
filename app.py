
import os

print("Running all Python tutorial files in order:\n")

py_files = [
    '1_variables_info.py',
    '2_numbers_info.py',
    '3_strings_info.py',
    '4_boolean_info.py',
    '5_intput_data.py',
    '6_control_flow.py',
    '7_functions.py',
    '8_data_structure.py',
]

for fname in py_files:
    print(f"\n--- Running {fname} ---")
    with open(fname, encoding='utf-8') as f:
        code = f.read()
    exec(code, {'__name__': '__main__'})
