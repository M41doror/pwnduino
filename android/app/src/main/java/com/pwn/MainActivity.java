package com.pwn;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import com.jcraft.jsch.*;
import java.awt.*;
import javax.swing.*;
import java.io.*;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        JSch jsch=new JSch();
        
    }
}
