#include <algorithm>
#include <string_view>
#include <iostream>
#include <vector>

namespace Preprocess
{
	bool shorter_than(std::string_view s, std::size_t target_len)
	{
		return std::count_if(s.begin(), s.end(), [](char s) { return s != ' '; }) < target_len;
	}

	bool all_whitespace(std::string_view s)
	{
		for (char c : s) if (c != ' ') return false;
		return true;
	}

	auto gen_linepred(std::size_t target_len)
	{
		return [=](std::string_view s)
			{
				bool p = (!shorter_than(s, target_len))
				   	  && (!all_whitespace(s));
				if (!p) std::cout << "Filtered: " << s << '\n';
				return p;
			};
	}
}
