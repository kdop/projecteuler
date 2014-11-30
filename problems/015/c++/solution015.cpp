#include <iostream>

using namespace std;

int xMax = 2;
int yMax = 2;
uint64_t routes = 0;

void nextMove(int x, int y) {
	int xtmp;
	int ytmp;
	
	if (x < xMax) {
		//cout << "move left" << endl;
		xtmp = x + 1;
		nextMove(xtmp, y);
	}
		
	if (y < yMax) {
		//cout << "move down" << endl;
		ytmp = y + 1;
		nextMove(x, ytmp);
	}
	
	if (x == xMax && y == yMax) {
		//cout << x << "," << y << endl;
		routes++;
	}
}

int main() {
	nextMove(0, 0);
	cout << routes << endl;
	return 0;
}
