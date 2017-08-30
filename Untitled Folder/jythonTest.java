import java.io.IOException;
import java.io.StringWriter;

import org.python.util.PythonInterpreter;

class jythonTest 
{

	public static void main(String ar[]) throws IOException{
		
		//Process p = Runtime.getRuntime().exec("python tryCSV.py");
		//System.out.println(p);
		
		String[] arguments = {"tjava1.py", "khoon ho gya" };
		PythonInterpreter.initialize(System.getProperties(), System.getProperties(), arguments);
		PythonInterpreter python = new PythonInterpreter();
		StringWriter out = new StringWriter();
		python.setOut(out);
		python.execfile("tjava1.py");
		String outputStr = out.toString();
		System.out.println(outputStr);
		
	}
}
