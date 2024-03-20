#include <bits/stdc++.h>

struct DataFrame {

};

struct Backtest {
	std::vector<std::string> symbols;
	using unit_type = long long;
	std::vector<unit_type> units;
	using amount_type = long double;
	std::vector<amount_type> positions;
	amount_type amount;
	using rate_type = long double;
	rate_type maker_ftc;
	rate_type maker_ptc;
	rate_type taker_ftc;
	rate_type taker_ptc;
	using seq_type = int;
	seq_type trade_seq_num;
	Backtest() = default;
	void buy();
	void sell();
	void run(std::string start_date, std::string end_date);
};

void gridtrading() {

}

auto main() -> int {
	std::string data_path = "TSLA.csv";
	return 0;
}
