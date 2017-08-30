import java.io.*;
import java.util.*;
class driver
{
	public static void main(String[] args)throws Exception 
	{
		BufferedReader br=new BufferedReader (new InputStreamReader(System.in));

		ProcessBuilder pb = new ProcessBuilder("python","tf.py");
		Process proc = pb.start();

		// Start reading from the program
		Scanner in = new Scanner(proc.getInputStream());
		// Write a few commands to the program.
		PrintWriter out = new PrintWriter(proc.getOutputStream());
		out.println(br.readLine());
		out.flush();

		System.out.println(in.nextLine());
		out.flush();
		
		
		}	
}