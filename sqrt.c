#include<stdio.h>
int square(int n){
    return n*n;
}
main()
{
    int num;
    printf("enter a number");
    scanf("%d",&num);
    int value= square(num);
    printf("%d",value);
}