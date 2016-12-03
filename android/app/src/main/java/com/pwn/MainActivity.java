package com.pwn;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

import com.jcraft.jsch.Channel;
import com.jcraft.jsch.ChannelExec;
import com.jcraft.jsch.ChannelSftp;
import com.jcraft.jsch.JSch;
import com.jcraft.jsch.JSchException;
import com.jcraft.jsch.Session;
import com.jcraft.jsch.UserInfo;



import java.io.InputStream;
import java.util.Properties;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        setTitle("C: > pwn ");
        final TextView console = (TextView) findViewById(R.id.console);
        /*JSch jsch = new JSch();
        String user ="derek";

        String host = "10.55.176.112";
        UserInfo ui = new UserInfo() {
            @Override
            public String getPassphrase() {
                return null;
            }

            @Override
            public String getPassword() {
                return null;
            }

            @Override
            public boolean promptPassword(String s) {
                return false;
            }

            @Override
            public boolean promptPassphrase(String s) {
                return false;
            }

            @Override
            public boolean promptYesNo(String s) {
                return false;
            }

            @Override
            public void showMessage(String s) {

            }
        };


        try {
            Session session = jsch.getSession(host, user, 22);
            session.setUserInfo(ui);
            session.connect();
            Channel channel = session.openChannel("exec");

            channel.setInputStream(null);

            String command = "dir";
            ((ChannelExec) channel).setCommand(command);

            ((ChannelExec) channel).setErrStream(System.err);
            try {
                InputStream in = channel.getInputStream();
                channel.connect();
                byte[] tmp = new byte[1024];
                while (true) {
                    while (in.available() > 0) {
                        int i = in.read(tmp, 0, 1024);
                        if (i < 0) break;
                        System.out.print("hello"+new String(tmp, 0, i));
                    }
                    if (channel.isClosed()) {
                        if (in.available() > 0) continue;
                        System.out.println("exit-status: " + channel.getExitStatus());
                        break;
                    }
                    try {
                        Thread.sleep(1000);
                    } catch (Exception ee) {
                    }
                }

                channel.disconnect();

                session.disconnect();

            } catch (Exception e) {

                System.out.println(e);

            }


        }catch (JSchException je){


            System.out.println("Erorr " + je);
        }



    */
        new Thread(new Runnable() {
            @Override
            public void run() {

                Session session;
                JSch jsch;
                try {
                    jsch = new JSch();

                    /*session = jsch.getSession("derek", "10.55.176.112", 22);
                    session.setPassword("password");
*/
                    session = jsch.getSession("vmware", "theeditor.ddns.net", 22);
                    session.setPassword("123");
                    // Avoid asking for key confirmation
                    Properties prop = new Properties();
                    prop.put("StrictHostKeyChecking", "no");
                    session.setConfig(prop);

                    session.connect();

                    if(session.isConnected()){
                        console.setText(console.getText() + "\nSession Connected...");
                        Channel channel = session.openChannel("sftp");
                        System.out.println("Getting connected");
                        channel.connect();
                        console.setText(console.getText() + "\nChannel Connected...");
                        System.out.println("connected successfully");

                        console.setText(console.getText() + "\nGood to go. :)");
                        ChannelSftp sftpChannel = (ChannelSftp) channel;

                        System.out.println("Directory:" + sftpChannel.pwd());

                        sftpChannel.mkdir("Derek");


                        System.out.println(this.getClass().getSimpleName() + " CONNECTED");
                        System.out.println(this.getClass().getSimpleName() + " YOO " + jsch.getIdentityRepository().getName()+" "+session.getClientVersion() + " " + session.isConnected());
                    }else{
                        System.out.println(this.getClass().getSimpleName() + " NOT CONNECTED");
                    }
                }catch (Exception e){
                    e.printStackTrace();
                }
            }
        }).start();}
    }

