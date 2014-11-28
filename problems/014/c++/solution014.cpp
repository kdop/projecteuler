#include <iostream>

using namespace std;

uint64_t collatz_length(uint64_t i)
{
	uint64_t c = 0;
	
	if (i < 1 || i % 1 != 0)
		return 0;
		
	while(i != 1) {
		i = (i % 2 == 0 ? i/2 : (3*i)+1);
		c++;
	} c++; // +1 for 1, the last number of the sequence.
	
	return c;
}

int main()
{
	uint64_t max = 0;
	uint64_t maxn = 0;
	
	for(uint64_t n = 0; n < 1000000; ++n) {
		if (collatz_length(n) > max) {
			max = collatz_length(n);
			maxn = n;
		}
	}
	
	cout << maxn << ": " << max << endl;
}
