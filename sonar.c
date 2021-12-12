#include <stdio.h>
#include <stdlib.h>

int main()
{
	int i, input, previnput=0, result=0;

	while(scanf("%d", &input) != EOF)
	{
		if (previnput == 0 || input < previnput)
			previnput=input;
		else if (input > previnput)
		{
			previnput=input;
			result++;
		}
	}
	printf("%d\n", result);
}
