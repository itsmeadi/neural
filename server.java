import java.net.*;
import java.io.*;
class soc extends Thread
{
  OutputStream ostream=null;
  PrintWriter pwrite=null;
  InputStream istream=null;
  BufferedReader receiveRead=null,keyRead=null;
  soc(Socket s)throws Exception
  {
    ostream = s.getOutputStream(); 
    pwrite = new PrintWriter(ostream, true);
 
    istream = s.getInputStream();
    receiveRead = new BufferedReader(new InputStreamReader(istream));
    keyRead = new BufferedReader(new InputStreamReader(System.in));
      
  }
  public void run1()
  {
              String receiveMessage, sendMessage;               

  // BufferedReader br = new BufferedReader(new InputStreamReader(is));
      try{
          boolean headersFinished = false;
          int contentLength = -1;

          while (!headersFinished) {
           String line = receiveRead.readLine();
           headersFinished = line.isEmpty();

           if (line.startsWith("Content-Length:")) {
               String cl = line.substring("Content-Length:".length()).trim();
               contentLength = Integer.parseInt(cl);
           }
}

// validate contentLength value
char[] buf = new char[contentLength];  //<-- http body is here
receiveRead.read(buf);
            System.out.println("Request=");

for (char c : buf) {
              System.out.print(c);
}
            System.out.println("end");

        sendMessage = keyRead.readLine(); 

pwrite.println(sendMessage);             
        pwrite.flush();
      }
      catch(Exception e){}
  }
  public void run()
  {
          String receiveMessage, sendMessage;               
try{
  int tt=0;
    //while(tt++<10)
      {
       
        if((receiveMessage = receiveRead.readLine()) != null)  
        {
          if(receiveMessage.contains("GET"))
          {
            String ss[]=receiveMessage.split(" ");
            String re=ss[1];
            String req=re.substring(1,re.length());
            System.out.println("goto ="+req);
          }
        }
      }
          // File f=new File("resp.txt","r");
           //sendMessage="HTTP/1.1 200 OK\r\nCache-Control: no-cache, private\r\nContent-Length: 107\r\nDate: Mon, 8 Sep 2017 3:53:21 GMT\r\n\r\n";
          System.out.println("2");  

          sendMessage=""; 
          sendMessage+="HTTP/1.1 200 OK\n";
           sendMessage+="Date: Mon, 27 Jul 2009 12:28:53 GMT\n";
           sendMessage+="Server: Apache/2.2.14 (Win32)\n";
           sendMessage+="Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT\n";
            sendMessage+="Content-Length: 40\n";
            sendMessage+="Content-Type: text/html\n";
            sendMessage+="Connection: Closed\n";

           sendMessage+="<html>";
           sendMessage+="<body>";
           sendMessage+="<h1>Hello, World!</h1>";
           sendMessage+="</body>";
           sendMessage+="</html>";

           System.out.println(sendMessage);  

        pwrite.println(sendMessage);             
        pwrite.flush();      
           
        
      
  }
  catch(Throwable e){System.out.println(e);}
}

}
public class server
{
  public static void main(String[] args) throws Exception
  {
      ServerSocket sersock = new ServerSocket(3000);
      System.out.println("enter.......");
      while(true)
      {
      Socket sock = sersock.accept( );   
      Thread t=new soc(sock);
      t.start();      
      }
      
      //System.out.println("client");                       
      
                     
    }                    
}                
