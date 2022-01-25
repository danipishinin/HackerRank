#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
  string names[9] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

	int a;
	int b;
	cin >> a >> b;
	for (int n = a; n <= b; n++)
	{
		if (n >= 1 && n <= 9)
		{
			cout << names[n - 1] << "\n";
		}
		else if (n % 2 == 0)
		{
			cout << "even\n";
		}
		else
		{
			cout << "odd\n";
		}
	}

	return 0;
}