#include <filesystem>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>

namespace fs = std::filesystem;

namespace Files
{
	template <typename Pred>
	std::vector<std::string> read_lines_from_file(const fs::directory_entry& f, Pred&& p)
	{
		std::ifstream input{ f.path() };
		std::vector<std::string> res;

		for (std::string line; std::getline(input, line); ) if (p(line))
			res.push_back(line);

		return res;
	}

	template <typename Pred>
	std::vector<std::string> read_all_lines_from_dir(const fs::directory_entry& dir, Pred&& p)
	{
		std::vector<std::string> res;
		for (const auto& f : fs::directory_iterator{ dir })
		{
			auto lines = read_lines_from_file(f, std::move(p));
			res.insert
			(
				res.end(),
				std::make_move_iterator(lines.begin()),
				std::make_move_iterator(lines.end())
			);
		}

		return res;
	}

	void write_lines_to_file(const std::vector<std::string>& s, const fs::directory_entry& f)
	{
		std::ofstream of;
		of.open(f);
		for (const auto& line : s)
		{
			of << line << '\n';
		}
		of.close();
	}
}
