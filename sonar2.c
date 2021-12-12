#include <stdio.h>
#include <stdlib.h>


int main()
{
	int i=0, j=0, input, result, prevresult=0, finalresult=0;
	int measure1,measure2,measure3;

	while(scanf("%d", &input) != EOF)
	{
		if (i == 0)
		{
			measure1=input;
			i++;
		}
		else if (i == 1)
		{
			measure2=input;
			i++;
		}
		else if (i == 2)
		{
			measure3=input;
			//printf("%d\n", *measure3);
			prevresult=measure1+measure2+measure3;
			i++;
		}
		else
		{
			measure1=measure2;
			measure2=measure3;
			measure3=input;
			result=measure1+measure2+measure3;
			if (prevresult > 0 && result > prevresult)
				finalresult++;
			prevresult=result;
/*			printf("measure1 = %d\n", measure1);
			printf("measure2 = %d\n", measure2);
			printf("measure3 = %d\n", measure3);
			printf("prevresult = %d\n", prevresult);
			printf("result = %d\n", result);
			printf("\n");
*/			
		}
	}
	printf("%d\n", finalresult);
	return 0;
}
