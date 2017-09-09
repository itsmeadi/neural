import java.io.BufferedReader;
import java.io.InputStreamReader;
class jap2
{
	public static void main(String[] args)throws Exception
	{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		//int n=Integer.parseInt(br.readLine());
		tree tr=new tree();
		tr.insert(5);
		tr.insert(2);
		tr.insert(8);
		tr.insert(1);
		tr.insert(3);
		tr.insert(6);
		tr.insert(10);
		tr.level();
		queue s=new queue();
		
		
		//jap2 j=new jap2();
		//j.print_depth(root);

	}	
	queue q=null;
	public void print_depth()
	{
		while(q.start!=q.end)
		{
			q.pop();
		}
	}
	public void print_dep(tree root)
	{
		if(root==null)
			return;
		q.push(root);
		print_dep(root.left);
		print_dep(root.right);
	}
}
class queue
{
	tree v;
	queue start=null,next=null,end=null;
	void push(tree n)
	{
		if(start==null)
		{
			start=new queue();
			start.v=n;
			start.next=null;
			end=start;
			return;
		}
		queue temp=new queue();
		temp.v=n;
		temp.next=null;
		end.next=temp;
		end=temp;

	}
	tree pop()
	{
		if(start==null)
		{
			System.out.println("Emptyy");
			return null;
		}
		tree v=start.v;
		start=start.next;
		return v;
	}
}
class tree
{
	int v;
	tree left,right,root=null;
	public tree add(int n)
	{
		tree t=new tree();
		t.left=t.right=null;
		t.v=n;
		return t;
	}	
	public void insert(int n)
	{
		insert(this.root,n);
	}

	public void insert(tree root,int n)
	{
		if(this.root==null)
		{
			this.root=add(n);
		}
		else if(n>root.v)
		{
			if(root.right==null)
			{
				root.right=add(n);
			return;
			}
			insert(root.right,n);
		}
		else if(n<root.v)
		{
			if(root.left==null)
				{
				root.left=add(n);
				return;
				}
			insert(root.left,n);
		}
	}
	public void inorder()
	{
		inorder(root);
	}

	public void inorder(tree root)
	{
		if(root==null)
			return;
		inorder(root.left);
		System.out.println(root.v);
		inorder(root.right);
	}
	public void level()
	{
		queue q=new queue();
		tree lroot=this.root;
		q.push(lroot);
		while(q.start!=null)
		{
			lroot=q.pop();
			System.out.println(lroot.v);
			if(lroot.left!=null)
				{q.push(lroot.left);
								//System.out.println("le="+lroot.left.v);
				}
			if(lroot.right!=null)
			{		
							q.push(lroot.right);
							//System.out.println("ri"+lroot.right.v);
					}
		}
	}
}