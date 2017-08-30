import java.io.*;
import java.util.*;
class test 
{
	public static void main(String[] args)throws IOException 
	{
		BufferedReader br=new BufferedReader (new InputStreamReader(System.in));

		ProcessBuilder pb = new ProcessBuilder("python","tf.py");
		Process proc = pb.start();

// Start reading from the program
		final Scanner in = new Scanner(proc.getInputStream());
		new Thread() {
		    public void run() {
		        while (in.hasNextLine())
		            System.out.println(in.nextLine());
		    }
		}.start();

		// Write a few commands to the program.
		PrintWriter out = new PrintWriter(proc.getOutputStream());
		System.out.println("here");
		out.println(br.readLine());
		out.flush();
		while (in.hasNextLine())
		System.out.println(in.nextLine());
		
		out.println(br.readLine());
		out.flush();
		while (in.hasNextLine())
		
		System.out.println(in.nextLine());
		fn()
		
		}	
		public void fn()
		{

		}
}