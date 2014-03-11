import java.io.*;
import java.net.*;
import java.lang.management.ManagementFactory;
import java.lang.management.OperatingSystemMXBean;
class TCPClient
{
 public static void main(String argv[]) throws Exception
 {
  String sentence;
  String modifiedSentence;
  BufferedReader inFromUser = new BufferedReader( new InputStreamReader(System.in));
  Socket clientSocket = new Socket("10.30.9.73", 6789);
  DataOutputStream outToServer = new DataOutputStream(clientSocket.getOutputStream());
  BufferedReader inFromServer = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
  OperatingSystemMXBean osBean = (OperatingSystemMXBean) ManagementFactory.getOperatingSystemMXBean();
  double load_value = osBean.getSystemLoadAverage();
  //double load_value = 1.98;
  String load_string = String.valueOf(load_value);
  outToServer.writeBytes(load_string);
  clientSocket.close();
 }
}
