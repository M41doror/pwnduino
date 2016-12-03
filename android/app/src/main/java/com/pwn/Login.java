package com.pwn;

import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.ActionBar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class Login extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.login_view);
        setTitle("C: > pwn ");
        EditText login, password;
        login = (EditText) findViewById(R.id.login);
        password = (EditText) findViewById(R.id.password);
        Button sumbit = (Button) findViewById(R.id.sum);
    

    }

}
