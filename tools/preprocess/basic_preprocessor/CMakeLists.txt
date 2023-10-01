# CMakeList.txt: basic_preprocessor 的 CMake 项目，在此处包括源代码并定义
# 项目特定的逻辑。
#

set(REQUIRED)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED True)

find_package(re2 REQUIRED)

# 将源代码添加到此项目的可执行文件。
add_executable (basic_preprocessor "basic_preprocessor.hpp" "file_handle.hpp" "main.cpp")

target_link_libraries(basic_preprocessor PRIVATE re2::re2)

# TODO: 如有需要，请添加测试并安装目标。
