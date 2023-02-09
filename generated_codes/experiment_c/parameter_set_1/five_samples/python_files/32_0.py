/*

*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int test_cases;
    int year;
    int days;
    int month = 1;
    int day_of_week;
//    int day_of_month = 1;

    printf("Enter the number of test cases\n");
    scanf("%d", &test_cases);

    int *test_case_result = (int *) calloc(test_cases, sizeof(int));

    for (int test_case = 0; test_case < test_cases; ++test_case)
    {
        printf("Enter the year\n");
        scanf("%d", &year);

        days = (year - 1900) * 365;

        month = 1;
        //We will substitute all the leap years with the date 29th Feb 2000
        for (int leap_year = 1900; leap_year < year; ++leap_year)
        {
            if ((leap_year%4 == 0 && leap_year%100 != 0) || leap_year%400 == 0)
            {
                days += 1;
            }
        }

        if (year > 1900)
        {
            day_of_week = (days + 1) % 7;
        }
        else
        {
            day_of_week = 1;
        }

        printf("The day on the 1st Jan %d is %s\n", year, (day_of_week == 1 ? "monday" : (day_of_week == 2 ? "tuesday" : (day_of_week == 3 ? "wednesday" : (day_of_week == 4 ? "thursday" : (day_of_week == 5 ? "friday" : (day_of_week == 6 ? "saturday" : "sunday")))))));
    }

    return 0;
}