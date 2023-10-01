import re
import os

py_multiline_comment_regex = re.compile(r"(['\"])\1\1(.*?)\1{3}", re.DOTALL)
py_singleline_comment_regex = re.compile(r"#.*$", re.MULTILINE)

source_dirs = [
    "../../../raw_source/python"
]

result_dirs = [
    "../../../comm_removed/python"
]

for i in range(len(source_dirs)):
    for root, source_dir, files in os.walk(source_dirs[i]):
        for file in files:
            try:
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    content = f.read()
                    content = re.sub(py_multiline_comment_regex, "", content)
                    content = re.sub(py_singleline_comment_regex, "", content)
                    with open(os.path.join(result_dirs[i], file), "w", encoding="utf-8") as f2:
                        f2.write(content)
            except Exception as e:
                with open(os.path.join(root, file), "r", encoding="gb2312") as f:
                    content = f.read()
                    content = re.sub(py_multiline_comment_regex, "", content)
                    content = re.sub(py_singleline_comment_regex, "", content)
                    with open(os.path.join(result_dirs[i], file), "w", encoding="utf-8") as f2:
                        f2.write(content)
