#include <iostream>
#include <stdint.h>
#include <stdlib.h>


using namespace std;

uint64_t *line_buffer;
uint64_t n;


uint64_t calculate(int x, int y) {
	// Last row routes.
	for(int i=x-1; i>=0; i--)
		line_buffer[i] = 1 + x - i;
		
	for(int xt=x-2; xt >=0; xt--) {
		for(int yt=y-1; yt >=0; yt--) {
			if (yt == y-1)
				n = line_buffer[yt] + 1;
			else
				n = line_buffer[yt] + n;
			
			line_buffer[yt] = n;
		}
	}
	
	return n;
}

int main() {
	//nextMove(0, 0);
	//cout << routes << endl;
	
	int x, y;
	
	cout << "give matrix columns #:"; cin >> x;
	cout << "give matrix rows #:"; cin >> y;
	
	// line_buff keeps the previously calculated row.
	line_buffer = (uint64_t *)malloc(y * sizeof(uint64_t));
			
	calculate(x, y);
	
	cout << "answer:" << n << endl;
	
	free(line_buffer);
	
	return 0;
}
