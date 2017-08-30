 import java.io.*;
import java.util.*;
class test2
{
	public static void main(String[] args)throws IOException 
	{
		

	}
	public void a()
	{
		Process cPgm = Runtime.exec("python tst.py");
		OutputStream stdin = cPgm.getOutputStream();
		stdin.write("3".getBytes());
		stdin.flush();
		cPgm.waitFor();
	}
}