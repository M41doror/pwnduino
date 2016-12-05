package com.pwn;

import android.content.Context;
import android.content.Intent;
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
       final EditText login, password, host;
        final Context context = getBaseContext();
       login = (EditText) findViewById(R.id.login);
        host = (EditText) findViewById(R.id.host);
        password = (EditText) findViewById(R.id.password);
       final Button sumbit = (Button) findViewById(R.id.sum);
        sumbit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                final Intent i = new Intent(context, MainActivity.class);
                i.putExtra("host", host.getText().toString());
                i.putExtra("user", login.getText().toString());
                i.putExtra("password", password.getText().toString());
                System.out.println(i.getExtras().toString());
                i.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);

                context.startActivity(i);
            }
        });

    }

}
