package com.example.designerapp;

import android.app.ProgressDialog;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.View;
import android.widget.Button;
import android.widget.ListView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.android.volley.AuthFailureError;
import com.android.volley.NetworkResponse;
import com.android.volley.Request;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class Userviewcart extends AppCompatActivity {

    String [] id,date,furniturename,Amount,file,qty;

    @Override
    public void onBackPressed() {

        Intent ins= new Intent(getApplicationContext(),Userhome.class);
        startActivity(ins);
    }

    ListView lvs;
    Button bts;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_userviewcart);

        lvs=(ListView) findViewById(R.id.lvs);
        bts=(Button) findViewById(R.id.button12);


        SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        final String url = sh.getString("url", "") + "cust_viewcart/";

        final ProgressDialog pd = new ProgressDialog(Userviewcart.this);
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

                                JSONArray ja= obj.getJSONArray("data");



                                id=new String[ja.length()];
                                date=new String[ja.length()];
                                furniturename=new String[ja.length()];
                                Amount=new String[ja.length()];
                                file=new String[ja.length()];
                                qty=new String[ja.length()];

                                for (int i=0;i < ja.length() ; i++)
                                {
                                    JSONObject j= ja.getJSONObject(i);
                                    id[i]= j.getString("id");
                                    date[i]= j.getString("date");
                                    furniturename[i]= j.getString("furniturename");
                                    Amount[i]= j.getString("Amount");
                                    file[i]= j.getString("file");
                                    qty[i]= j.getString("qty");

                                }
                                lvs.setAdapter(new Cust_cart(getApplicationContext(),id,date,furniturename,Amount,file,qty));
                            } else {
                                Toast.makeText(getApplicationContext(), "No Items in cart", Toast.LENGTH_LONG).show();
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
                        Toast.makeText(getApplicationContext(), "VOlley error", Toast.LENGTH_SHORT).show();
                    }
                }) {


            @Override
            protected Map<String, String> getParams() throws AuthFailureError {
                Map<String, String> params = new HashMap<>();

                SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

                params.put("lid",sh.getString("lid",""));

                return params;
            }


            @Override
            protected Map<String, DataPart> getByteData() {
                Map<String, DataPart> params = new HashMap<>();
                return params;
            }
        };

        Volley.newRequestQueue(getApplicationContext()).add(volleyMultipartRequest);




        bts.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                ////////////////////////////////



                SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                final String url = sh.getString("url", "") + "carttoorder/";

                final ProgressDialog pd = new ProgressDialog(Userviewcart.this);
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

                                        Toast.makeText(getApplicationContext(), "Order sent successfully", Toast.LENGTH_LONG).show();

                                        Intent ins = new Intent(getApplicationContext(),Userviewcart.class);
                                        startActivity(ins);




                                    } else {
                                        Toast.makeText(getApplicationContext(), "Failed to order", Toast.LENGTH_LONG).show();
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
                                Toast.makeText(getApplicationContext(), "VOlley error", Toast.LENGTH_SHORT).show();
                            }
                        }) {


                    @Override
                    protected Map<String, String> getParams() throws AuthFailureError {
                        Map<String, String> params = new HashMap<>();

                        SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

                        params.put("lid",sh.getString("lid",""));

                        return params;
                    }


                    @Override
                    protected Map<String, DataPart> getByteData() {
                        Map<String, DataPart> params = new HashMap<>();
                        return params;
                    }
                };

                Volley.newRequestQueue(getApplicationContext()).add(volleyMultipartRequest);












                ////////////////////////////////









            }
        });





    }
}
