package com.example.designerapp;


import androidx.appcompat.app.AppCompatActivity;

import android.app.ProgressDialog;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import android.widget.ListView;
import android.widget.Toast;

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


public class Cust_viewfurnitureshops extends AppCompatActivity {



    String [] shop_name,ownername,phone,email,district,state,city,id;

    ListView lvs;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_cust_viewfurnitureshops);

        lvs=(ListView) findViewById(R.id.lvs);

        SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        final String url = sh.getString("url", "") + "userviewfurnitureshops/";


        VolleyMultipartRequest volleyMultipartRequest = new VolleyMultipartRequest(Request.Method.POST, url,
                new Response.Listener<NetworkResponse>() {
                    @Override
                    public void onResponse(NetworkResponse response) {
                        try {

                            JSONObject obj = new JSONObject(new String(response.data));
                            String dis = obj.getString("status");
                            if (dis.equalsIgnoreCase("ok")) {
                                JSONArray ja= obj.getJSONArray("data");



                                id=new String[ja.length()];
                                shop_name=new String[ja.length()];
                                ownername=new String[ja.length()];
                                phone=new String[ja.length()];
                                email=new String[ja.length()];
                                district=new String[ja.length()];
                                state=new String[ja.length()];
                                city=new String[ja.length()];

                                for (int i=0;i < ja.length() ; i++)
                                {
                                    JSONObject j= ja.getJSONObject(i);
                                    id[i]= j.getString("id");
                                    shop_name[i]= j.getString("shop_name");
                                    ownername[i]= j.getString("ownername");
                                    phone[i]= j.getString("phone");
                                    email[i]= j.getString("email");
                                    district[i]= j.getString("district");
                                    state[i]= j.getString("state");
                                    city[i]= j.getString("city");
                                }

                                lvs.setAdapter(new customfurnitureshops(getApplicationContext(),shop_name,ownername,phone,email,district,state,city,id));








                            } else {
                                Toast.makeText(getApplicationContext(), "Failed to sent feedback", Toast.LENGTH_LONG).show();
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

                params.put("empid",sh.getString("empid",""));




                return params;
            }


            @Override
            protected Map<String, DataPart> getByteData() {
                Map<String, DataPart> params = new HashMap<>();
                return params;
            }
        };

        Volley.newRequestQueue(getApplicationContext()).add(volleyMultipartRequest);










    }
}
