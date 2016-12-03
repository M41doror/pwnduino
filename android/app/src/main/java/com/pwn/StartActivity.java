package com.pwn;

import android.content.Intent;
import android.graphics.Color;
import android.graphics.Typeface;
import android.os.Handler;
import android.support.v7.app.ActionBar;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.animation.AccelerateInterpolator;
import android.view.animation.AlphaAnimation;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.ImageView;
import android.widget.TextView;

public class StartActivity extends AppCompatActivity {


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setTitle("");
        Typeface custom_font = Typeface.createFromAsset(getAssets(),  "fonts/SourceCodePro-Bold.ttf");
        setContentView(R.layout.activity_start);

        TypeWriter writer = (TypeWriter)findViewById(R.id.Typewriter);

        //Add a character every 150ms
        writer.setCharacterDelay(200);
        writer.setTypeface(custom_font);
        writer.setTextColor(Color.WHITE);
        writer.animateText("pwnduino_");

        final Intent i = new Intent(this, MainActivity.class);

        fadeOutAndHideImage(writer, i);
    }

    public void fadeOutAndHideImage(final TextView img, final Intent x) {

        Animation fadeOut = new AlphaAnimation(1, 0);
        fadeOut.setInterpolator(new AccelerateInterpolator());
        fadeOut.setDuration(3100);

        fadeOut.setAnimationListener(new Animation.AnimationListener() {
            public void onAnimationEnd(Animation animation) {
                img.setVisibility(View.GONE);
                startActivity(x);



            }

            public void onAnimationRepeat(Animation animation) {
            }

            public void onAnimationStart(Animation animation) {
            }
        });

        img.startAnimation(fadeOut);

    }

}
