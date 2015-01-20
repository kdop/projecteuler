#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main()
{
	vector <unsigned int> a;
	int rem = 0;
	int tmp = 0;
	int sum_of_elems = 0;
	
	a.push_back(2);
	for(int i = 0; i < 999; i++) {
		for(int d = a.size()-1; d >= 0; d--) {
			tmp = rem + a[d] * 2;
			a[d] = tmp % 10;
			rem = tmp / 10;
		}
		
		// Add the remainder in front.
		while(rem > 0) {
			a.insert(a.begin(), rem % 10);
			rem /= 10;
		}
	}
	
	sum_of_elems = std::accumulate(a.begin(),a.end(),0);
	
	cout << sum_of_elems << endl;
}
