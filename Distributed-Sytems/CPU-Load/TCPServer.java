

import java.io.*;
import java.net.*;
import java.util.ArrayList;
import java.util.Collections;


class TCPServer
{
   static ArrayList<Double> loads = new ArrayList<Double>();
   static int count = 0;
   public static void main(String argv[]) throws Exception
      {
         String line;
         ServerSocket welcomeSocket = new ServerSocket(6789);
         while(true)
         {
            Socket connectionSocket = welcomeSocket.accept();
            BufferedReader inFromClient =
            new BufferedReader(new InputStreamReader(connectionSocket.getInputStream()));
            DataOutputStream outToClient = new DataOutputStream(connectionSocket.getOutputStream());
            line = inFromClient.readLine();
            double value = Double.parseDouble(line);
            max(value);
         }
      }
   public static void max(double x)
   {
        count+=1;
        loads.add(x);
        if (count == 3)
        {
            System.out.println("\nMax CPU Load:"+Collections.max(loads));
            System.out.println("\nMin CPU Load:"+Collections.min(loads));
            if (loads.get(0) > loads.get(1) && loads.get(0) > loads.get(2))
            {
                System.out.println("\nMachine 1 is the highest");
            }
            else if ( loads.get(1) > loads.get(0) && loads.get(1) > loads.get(2))
            {
                System.out.println("\nMachine 2 is the highest");
            }
            else if ( loads.get(2) > loads.get(0) && loads.get(2) > loads.get(1))
            {
                System.out.println("\nMachine 2 is the highest");
            }
        }
   }
} 
