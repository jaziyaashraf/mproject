package com.example.designerapp;

import android.app.ProgressDialog;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.net.Uri;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Base64;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.RadioButton;
import android.widget.Spinner;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.android.volley.AuthFailureError;
import com.android.volley.NetworkResponse;
import com.android.volley.Request;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;
import java.net.URISyntaxException;
import java.util.HashMap;
import java.util.Map;

public class User_Sent_customizedplan extends AppCompatActivity implements View.OnClickListener {

    EditText ed_name,ed_totalsquarefeet, ed_expamoutn,edsescription;

    Spinner s;
    RadioButton r_m,r_f;
    Button b;
    ImageView im;


    String sel_dist;
    SharedPreferences sh;
    String url="";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_useraddcustomizedarchplan);
        ed_name=(EditText)findViewById(R.id.ed_name);
        ed_totalsquarefeet=(EditText)findViewById(R.id.ed_dob);
        ed_expamoutn=(EditText)findViewById(R.id.ed_housnme);
        edsescription=(EditText)findViewById(R.id.ed_place);

        b=(Button)findViewById(R.id.button3);
        im=(ImageView) findViewById(R.id.imageView);
        im.setOnClickListener(this);

        b.setOnClickListener(this);

        sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        url = sh.getString("url", "") + "and_customplan/";

    }

    String gender="";

    @Override
    public void onClick(View v) {

        if(v==im)
        {
            showfilechooser(1);

        }
        else {


            final String name = ed_name.getText().toString();
            final String squarefeet = ed_totalsquarefeet.getText().toString();
            final String expamnt = ed_expamoutn.getText().toString();
            final String description = edsescription.getText().toString();


            final ProgressDialog pd = new ProgressDialog(User_Sent_customizedplan.this);
            pd.setMessage("Uploading....");
            pd.show();
            VolleyMultipartRequest volleyMultipartRequest = new VolleyMultipartRequest(Request.Method.POST, url,
                    new Response.Listener<NetworkResponse>() {
                        @Override
                        public void onResponse(NetworkResponse response) {
                            try {
                                pd.dismiss();
                                JSONObject obj = new JSONObject(new String(response.data));
                                String dis = obj.getString("status");
                                if (dis.equalsIgnoreCase("ok")) {
                                    Toast.makeText(getApplicationContext(), "successfully created", Toast.LENGTH_LONG).show();
                                    Intent ins=new Intent(getApplicationContext(),Userhome.class);
                                    startActivity(ins);
                                } else {
                                    Toast.makeText(getApplicationContext(), "Failed to create", Toast.LENGTH_LONG).show();
                                }
                            } catch (JSONException e) {
                                Toast.makeText(getApplicationContext(), "error", Toast.LENGTH_SHORT).show();
                                e.printStackTrace();
                            }
                        }
                    },
                    new Response.ErrorListener() {
                        @Override
                        public void onErrorResponse(VolleyError error) {
                            Toast.makeText(getApplicationContext(), error.getMessage(), Toast.LENGTH_SHORT).show();
                        }
                    }) {


                @Override
                protected Map<String, String> getParams() throws AuthFailureError {
                    Map<String, String> params = new HashMap<>();

                    SharedPreferences sh=PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

                    params.put("name", name);
                    params.put("description", description);
                    params.put("amount", expamnt);
                    params.put("squarefeet", squarefeet);
                    params.put("lid",sh.getString("lid",""));



                    return params;
                }


                @Override
                protected Map<String, DataPart> getByteData() {
                    Map<String, DataPart> params = new HashMap<>();

                    params.put("img",new DataPart("a.jpg",byteArray));
                    return params;
                }
            };

            Volley.newRequestQueue(this).add(volleyMultipartRequest);

        }
    }


    String path, atype, fname, attach, attatch1;
    byte[] byteArray = null;

    void showfilechooser(int string) {
        // TODO Auto-generated method stub
        Intent intent = new Intent(Intent.ACTION_GET_CONTENT);
        //getting all types of files

        intent.setType("*/*");
        intent.addCategory(Intent.CATEGORY_OPENABLE);

        try {
            startActivityForResult(Intent.createChooser(intent, "Select a File to Upload"), string);
        } catch (android.content.ActivityNotFoundException ex) {
            // Potentially direct the user to the Market with a Dialog
            Toast.makeText(getApplicationContext(), "Please install a File Manager.", Toast.LENGTH_SHORT).show();

        }
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        if (resultCode == RESULT_OK) {
            if (requestCode == 1) {
                ////
                Uri uri = data.getData();

                try {
                    path = FileUtils.getPath(this, uri);

                    File fil = new File(path);
                    float fln = (float) (fil.length() / 1024);
                    atype = path.substring(path.lastIndexOf(".") + 1);


                    fname = path.substring(path.lastIndexOf("/") + 1);

                } catch (URISyntaxException e) {
                    e.printStackTrace();
                }

                try {

                    File imgFile = new File(path);

                    if (imgFile.exists()) {

                        Bitmap myBitmap = BitmapFactory.decodeFile(imgFile.getAbsolutePath());
                        im.setImageBitmap(myBitmap);

                    }


                    File file = new File(path);
                    byte[] b = new byte[8192];
                    Log.d("bytes read", "bytes read");

                    InputStream inputStream = new FileInputStream(file);
                    ByteArrayOutputStream bos = new ByteArrayOutputStream();

                    int bytesRead = 0;

                    while ((bytesRead = inputStream.read(b)) != -1) {
                        bos.write(b, 0, bytesRead);
                    }
                    byteArray = bos.toByteArray();

                    String str = Base64.encodeToString(byteArray, Base64.NO_WRAP);
                    attach = str;


                } catch (Exception e) {
                    Toast.makeText(this, "String :" + e.getMessage().toString(), Toast.LENGTH_LONG).show();
                }

                ///

            }
        }

    }
