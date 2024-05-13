#include<iostream>
using namespace std;
int main ()
{
   int a,b,c;
   
    cout<<"enter first ";
    cin>>a;
    
    cout<<"enter first ";
    cin>>b;
    
    cout<<"enter first ";
    cin>>c;
    if(a<90&&b<90&&c<90)
    {
        cout<<"acute";
    }
   else if((a>90&&b<90&&c<90)||(b>90&&c<90&&a<90)||(c>90&&a<90&&b<90))
    {
        cout<<"obtuse";
    }
     else if((a==90&&b<90&&c<90)||(b==90&&a<90&&c<90)||(c==90&&a<90&&b<90))
     {
        cout<<"right";
     }
     return 0;

}