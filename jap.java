import java.io.*;
class jap
{
	int li=10;
	void add(int a[],int b[],int v)
	{
		int i=0,c=0,x;
		//int sum[]=new int[1000];
		
		while(a[i]!=0||b[i]!=0)
		{
			
			int n=a[i]+b[i]+c;
			if(n>=li)
				c=1;
			else
				c=0;
			x=n%li;
			n=n/li;
			
			tt[v][i]=x;
			i++;
			//System.out.println(tt[v][0]);
		}
			}
	int tt[][];
	boolean emp[];
	public static void main(String[] args)throws IOException {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int n=Integer.parseInt(br.readLine());
		jap e=new jap();
		e.tt=new int[10000][1000];
		e.emp=new boolean[10000];
		e.tt[0][0]=0;e.emp[0]=true;
		e.tt[1][0]=1;e.emp[1]=true;
		e.f(n);
		for (int j=0;j<n ; j++){
				for (int i=8; i>=0; i--) 
				{
				System.out.print(e.tt[n][i]);
			}
			System.out.println();
	}
	}
	int[] f(int n)
	{
		if(emp[n])
			return tt[n];
		for (int j=0;j<n ; j++)
		{
			for (int i=8; i>=0; i--) 
			{
			System.out.print(tt[n][i]);
			}
		System.out.println();
	}System.out.println("\n\n");
		System.out.println(n+" "+emp[n]);
		
		add(f(n-1),f(n-2),n);
		emp[n]=true;
		return tt[n];
	}

}
