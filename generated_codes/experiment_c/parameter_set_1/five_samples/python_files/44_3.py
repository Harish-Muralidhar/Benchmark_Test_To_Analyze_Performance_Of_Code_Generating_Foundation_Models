/*

*/

#include<stdio.h>
#include<string.h>

#define MAX_ACTIVITY_SIZE	100
#define MAX_ACTIVITY_LEN	50
#define MAX_ACTIVITY_NAME	20
#define MAX_RANK_VALUE		5000
#define MAX_SEVIRITY_VALUE	1000

int getLadduCount(char activity[MAX_ACTIVITY_NAME], int rank, int sevirity, int origin)
{
	int ladduCount = 0;

	if(rank <= 0)
		return ladduCount;

	if(origin == 0)
	{
		if(strcmp(activity, "CONTEST_WON") == 0)
		{
			ladduCount = 300 + (rank < 20?(20 - rank):0);
		}
		else if(strcmp(activity, "TOP_CONTRIBUTOR") == 0)
		{
			ladduCount = 300;
		}
		else if(strcmp(activity, "BUG_FOUND") == 0)
		{
			ladduCount = sevirity;
		}
		else if(strcmp(activity, "CONTEST_HOSTED") == 0)
		{
			ladduCount = 50;
		}
	}
	else
	{
		if(strcmp(activity, "CONTEST_WON") == 0)
		{
			ladduCount = 300 + (rank < 20?(20 - rank):0);
		}
		else if(strcmp(activity, "TOP_CONTRIBUTOR") == 0)
		{
			ladduCount = 300;
		}
		else if(strcmp(activity, "BUG_FOUND") == 0)
		{
			ladduCount = sevirity;
		}
		else if(strcmp(activity, "CONTEST_HOSTED") == 0)
		{
			ladduCount = 50;
		}
	}

	return ladduCount;
}

int getTotalMonths(int ladduCount, int origin)
{
	int months = 0;

	if(origin == 0)
	{
		while(ladduCount >= 200)
		{
			ladduCount -= 200;
			months++;
		}
	}
	else
	{
		while(ladduCount >= 400)
		{
			ladduCount -= 400;
			months++;
		}
	}

	return months;
}

int main()
{
	int testCases = 0, origin = 0, rank = 0, sevirity = 0, i = 0, j = 0, k = 0, ladduCount = 0, totalLadduCount = 0, months = 0;
	char activity[MAX_ACTIVITY_LEN] = {0}, activities[MAX_ACTIVITY_SIZE][MAX_ACTIVITY_LEN] = {0};
	char originType[MAX_ACTIVITY_NAME] = {0};

	scanf("%d", &testCases);

	for(i = 0; i < testCases; i++)
	{
		scanf("%d %s", &k, originType);
		origin = (strcmp(originType, "INDIAN") == 0)?0:1;

		for(j = 0; j < k; j++)
		{
			scanf("%s", activity);
			strcpy(activities[j], activity);
		}

		for(j = 0; j < k; j++)
		{
			strcpy(activity, activities[j]);

			if(strcmp(activity, "CONTEST_WON") == 0)
			{
				scanf("%d", &rank);
				ladduCount = getLadduCount("CONTEST_WON", rank, 0, origin);
			}
			else if(strcmp(activity, "TOP_CONTRIBUTOR") == 0)
			{
				ladduCount = getLadduCount("TOP_CONTRIBUTOR", 0, 0, origin);
			}
			else if(strcmp(activity, "BUG_FOUND") == 0)
			{
				scanf("%d", &sevirity);
				ladduCount = getLadduCount("BUG_FOUND", 0, sevirity, origin);
			}
			else if(strcmp(activity, "CONTEST_HOSTED") == 0)
			{
				ladduCount = getLadduCount("CONTEST_HOSTED", 0, 0, origin);
			}

			totalLadduCount += ladduCount;
		}

		months = getTotalMonths(totalLadduCount, origin);

		printf("%d\n", months);

		totalLadduCount = 0;
		months = 0;
	}

	return 0;
}