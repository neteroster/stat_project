#include "basic_preprocessor.hpp"
#include "file_handle.hpp"

#include <iostream>
#include <filesystem>

namespace fs = std::filesystem;

int main()
{
	const fs::path src_base_path{ "C:/Users/neter/Downloads/Stat/proj/comm_removed" };
	const fs::path dest_base_path{ "C:/Users/neter/Downloads/Stat/proj/merged" };
	const std::vector<std::string> langs{"cpp", "javascript", "java", "go", "rust", "python"};

	for (const auto& lang : langs)
	{
		auto lines = Files::read_all_lines_from_dir(fs::directory_entry{ src_base_path / lang }, Preprocess::gen_linepred(3));

		Files::write_lines_to_file(lines, fs::directory_entry{ dest_base_path / lang });
	}

}
