import re
import os

c_style_comment_regex = r"(?:\/\/(?:\\\n|[^\n])*\n)|(?:\/\*[\s\S]*?\*\/)|((?:R\"([^(\\\s]{0,16})\([^)]*\)\2\")|(?:@\"[^\"]*?\")|(?:\"(?:\?\?'|\\\\|\\\"|\\\n|[^\"])*?\")|(?:'(?:\\\\|\\'|\\\n|[^'])*?'))"

source_dirs = [
    "../../../raw_source/cpp",
    "../../../raw_source/javascript",
    "../../../raw_source/java",
    "../../../raw_source/go",
    "../../../raw_source/rust"
]

result_dirs = [
    "../../../comm_removed/cpp",
    "../../../comm_removed/javascript",
    "../../../comm_removed/java",
    "../../../comm_removed/go",
    "../../../comm_removed/rust"
]

for i in range(len(source_dirs)):
    for root, source_dir, files in os.walk(source_dirs[i]):
        for file in files:
            try:
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    content = f.read()
                    content = re.sub(c_style_comment_regex, "", content)
                    with open(os.path.join(result_dirs[i], file), "w", encoding="utf-8") as f2:
                        f2.write(content)
            except Exception as e:
                with open(os.path.join(root, file), "r", encoding="gb2312") as f:
                    content = f.read()
                    content = re.sub(c_style_comment_regex, "", content)
                    with open(os.path.join(result_dirs[i], file), "w", encoding="utf-8") as f2:
                        f2.write(content)