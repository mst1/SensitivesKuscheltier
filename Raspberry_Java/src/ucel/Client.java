package ucel;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.Socket;

import javax.swing.*;

public class Client extends JFrame implements ActionListener {
	JButton ledwhite, ledblank, ledr, ledg, ledb, ledmagenta, ledtuerkis,
			ledyellow, shutd, killsoft, reboot;
	JLabel welcome;

	public Client() {
		super("ProjectPi Client");
		setLayout(new BorderLayout());
		JPanel oben = new JPanel(new GridLayout(1, 2));
		JPanel unten = new JPanel(new GridLayout(3, 3));
		ImageIcon _icon = new ImageIcon("src/ucel/logo.gif");
		_icon.setImage(_icon.getImage().getScaledInstance(250, 250, Image.SCALE_DEFAULT));
		JLabel logo = new JLabel(_icon);
		welcome = new JLabel("Willkommen zur Project Pi - Remotesteuerung!");
		welcome.setFont(new Font("Arial", Font.BOLD, 22));
		ledwhite = new JButton("Weiﬂes Licht");
		ledblank = new JButton("Kein Licht");
		ledr = new JButton("Rotes Licht");
		ledg = new JButton("Gruenes Licht");
		ledb = new JButton("Blaues Licht");
		ledmagenta = new JButton("Magenta Licht");
		ledtuerkis = new JButton("Tuerkises Licht");
		ledyellow = new JButton("Gelbes Licht");
		shutd = new JButton("Herunterfahren");
		killsoft = new JButton("Software beenden");
		reboot = new JButton("Neu starten");
		oben.add(welcome);
		oben.add(logo);
		unten.add(ledwhite);
		unten.add(ledblank);
		unten.add(ledr);
		unten.add(ledg);
		unten.add(ledb);
		unten.add(ledmagenta);
		unten.add(ledtuerkis);
		unten.add(ledyellow);
		unten.add(shutd);
		unten.add(killsoft);
		unten.add(reboot);
		add(oben, BorderLayout.NORTH);
		add(unten);
		setSize(700, 500);
		setVisible(true);
		ledwhite.addActionListener(this);
		ledblank.addActionListener(this);
		ledr.addActionListener(this);
		ledg.addActionListener(this);
		ledb.addActionListener(this);
		ledmagenta.addActionListener(this);
		ledtuerkis.addActionListener(this);
		ledyellow.addActionListener(this);
		ledwhite.setActionCommand("ledwhite");
		ledblank.setActionCommand("ledblank");
		ledr.setActionCommand("ledred");
		ledg.setActionCommand("ledgreen");
		ledb.setActionCommand("ledblue");
		ledmagenta.setActionCommand("ledmagenta");
		ledtuerkis.setActionCommand("ledtuerkis");
		ledyellow.setActionCommand("ledyellow");
		shutd.setActionCommand("shutd");
		killsoft.setActionCommand("killsoft");
		reboot.setActionCommand("reboot");
		setDefaultCloseOperation(3);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		sendCommand(e.getActionCommand());
	}

	public void sendCommand(String command) {
		Socket server = null;
		PrintWriter out = null;
		try {
			server = new Socket(InetAddress.getByName("10.0.0.1"), 50000);
			out = new PrintWriter(server.getOutputStream());
		} catch (IOException ex) {
			ex.printStackTrace();
		}
		out.print(command);
		out.flush();
		out.close();
	}

	public static void main(String[] args) {
		new Client();
	}
}