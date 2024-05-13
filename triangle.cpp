#include<iostream>
using namespace std;
int main()
{
   int a,b,c;

    cout<<"enter first ";
    cin>>a;
    
    cout<<"enter sec ";
    cin>>b;
    
    cout<<"enter third ";
    cin>>c;
    if(a==b&&b==c)
    {
        cout<<"equal";
    }
    else if(a==b || b==c ||c==a)
    {
        cout<<"isosce";
    }
    else
    {
        cout<<"scalane";
    }
    return 0;
}