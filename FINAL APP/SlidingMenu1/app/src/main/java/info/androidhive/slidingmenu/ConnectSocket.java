package info.androidhive.slidingmenu;
import java.io.IOException;
import java.io.*;
import java.net.*;
/**
 * Created by Johannes on 30.05.2015.
 */
public class ConnectSocket {
    public void connect(String cmd) throws IOException{
        InetAddress address = InetAddress.getByName("10.0.0.1");
        Socket socket = new Socket(address, 50000);

        BufferedOutputStream bos = new BufferedOutputStream(socket.getOutputStream());

        OutputStreamWriter osw = new OutputStreamWriter(bos, "US-ASCII");

        System.out.println("Sending message...");

        osw.write(cmd);
        osw.flush();
        osw.close();
    }
}
