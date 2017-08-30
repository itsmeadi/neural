import java.io.IOException;
import java.io.StringWriter;

import org.python.util.PythonInterpreter;

class jt
{

	public static void main(String ar[]) throws IOException{
		
		//Process p = Runtime.getRuntime().exec("python tryCSV.py");
		//System.out.println(p);
		PythonInterpreter interp = new PythonInterpreter();
		StringWriter out = new StringWriter();
		interp.exec("import sys");
		interp.exec("print sys.version");
		interp.exec("sys.path.append('~\\Downloads\\pyt\\jython-standalone-2.7.0\\Lib')");
		interp.exec("sys.path.append('~\\Downloads\\pyt\\jython-standalone-2.7.0\\Lib\\site-packages')");

		interp.exec("import textblob");
		
		
	}
}
