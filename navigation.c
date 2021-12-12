#include <stdio.h>
#include <stdlib.h>


int main()
{

	int vert=0;
	int horiz=0;
	char dir='E';
	char* dirch="NESW";
	char input[10];
	char letter;
	int num, i;


	while(scanf("%c%d\n",&letter,&num) != EOF)
	{
		printf("%c ",letter);
		printf("%d\n",num);

		if (letter == 'F')
		{
			if (dir == 'E') 
				horiz += num;
			if (dir == 'W') 
				horiz -= num;
			if (dir == 'N')
				vert += num;
			if (dir == 'S') 
				vert -= num;
		}
		if (letter == 'L')
		{
			num = num / 90;
			
			for (i=0; i != 4; i++)
			{
				if (dirch[i] == dir)
				{
					break;
				}
			} 
			for(int j=0; j < num;j++)
			{
				i--;
				if (i < 0)
					i = 3;
			}
			dir=dirch[i];

		}	
		if (letter == 'R')
		{
			num = num / 90;
			
			for (i=0; i != 4; i++)
			{
				if (dirch[i] == dir)
				{
					break;
				}
			} 
			for(int j=0; j < num;j++)
			{
				i++;
				if (i > 3)
					i = 0;
			}
			dir=dirch[i];

		}
		if (letter == 'N')
		{
			vert += num;
		}
		if (letter == 'S')
		{
			vert -= num;
		}
		if (letter == 'E')
		{
			horiz += num;
		}
		if (letter == 'W')
		{
			horiz -= num;
		}
		
	}
	printf("result: %d\n", abs(horiz)+abs(vert));
	return 0;
}



/*while read p
do
	LETTER=${p:0:1}
	NUM=${p:1}


	if [[ $LETTER == "F" ]]
	then
		if [[ $DIR == 'E' ]]
		then
			HORIZ=$(($HORIZ+$NUM))
		fi
		if [[ $DIR == 'W' ]]
		then
			HORIZ=$(($HORIZ-$NUM))
		fi
		if [[ $DIR == 'N' ]]
		then
			VERT=$(($VERT+$NUM))
		fi
		if [[ $DIR == 'S' ]]
		then
			VERT=$(($VERT-$NUM))
		fi
	fi
	if [[ $LETTER == "L" ]]
	then
			
	
		
	

	break  
done < input */
