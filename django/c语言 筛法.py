#include <stdio.h>  
int a[2000005]={0};//初始化  
int main()  
{  
    int n,i,j;  
    /*筛法求素数*/  
    for(i=2;i<=1000003;i++)  
        if(a[i]==0)//如果是标记过的，则直接执行i++   
            for(j=i+i;j<=2000005;j=j+i)  
                a[j]=1;//依次筛去i的倍数，即标记合数   
    while(scanf("%d",&n)!=EOF)  
    {  
        if(n==0)  
            break;  
        for(i=2;i<=n;i++)  
            if(a[i]==0)   
                printf("%d ",i);//输出未标记的下标（素数）  
        printf("\n");  
    }  
    return 0;  
}  
