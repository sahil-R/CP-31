#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    int num;
    int ans;
    cin>>t;
    while(t--)
    {
        cin>>num;
        ans = 0;

        for(int k=1; k<=num; k++)
        {
            int r = 0;
            while(k>0)
            {
                if(r>1)
                    break;

                if(k%10 != 0)   r++;
                k=k/10;
            }
            if(r==1)
                ans++;
        }

        cout<<ans;

    }

    return 0;
}