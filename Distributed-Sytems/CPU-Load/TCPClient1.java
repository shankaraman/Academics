import java.io.*;
import java.net.*;
import java.lang.management.ManagementFactory;
import java.lang.management.OperatingSystemMXBean;
class TCPClient1
{
 public static void main(String argv[]) throws Exception
 {
  String sentence;
  String modifiedSentence;
  BufferedReader inFromUser = new BufferedReader( new InputStreamReader(System.in));
  Socket clientSocket = new Socket("localhost", 6789);
  DataOutputStream outToServer = new DataOutputStream(clientSocket.getOutputStream());
  BufferedReader inFromServer = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
  OperatingSystemMXBean osBean = (OperatingSystemMXBean) ManagementFactory.getOperatingSystemMXBean();
  double load_value = osBean.getSystemLoadAverage();
  String load_string = String.valueOf(load_value);
  outToServer.writeBytes(load_string + '\n');
  clientSocket.close();
 }
}
