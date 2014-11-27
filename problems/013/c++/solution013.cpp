#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main() 
{
	vector <int> l;
	vector <vector <int>> V;
	vector <int> a;
	
	ifstream file("data.txt");
	string str;
    
    while (getline(file, str))
    {
        l.clear();
		for(char c : str) {
			l.push_back(c - '0');
		}
		
		V.push_back(l);
    }
    
    int sum;
    int rem = 0;
    for(int c = V[0].size() - 1; c >= 0 ; --c) {
		sum = rem;
		for(int r = 0; r < V.size(); ++r) {
			sum += V[r][c];
			//cout << V[r][c];
		}
		//cout << " " << sum % 10 << endl;
		a.insert(a.begin(), sum % 10);
		rem = sum / 10;
	}
	
	// Add the remainder digits in front.
	while(rem > 0) {
		//cout << rem % 10 << endl;
		a.insert(a.begin(), rem % 10);
		rem /= 10;
	}
	
	for(int r = 0; r < a.size(); ++r) {
		cout << a[r];
	} cout << endl;
}
