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


public class viewcategory extends AppCompatActivity {

    String [] id,catname;
    ListView lvs;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_viewcategory);

        lvs=(ListView) findViewById(R.id.lvs);

        lvs=(ListView) findViewById(R.id.lvs);

        SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        final String url = sh.getString("url", "") + "userviewfurnitureshopaddedcategory/";

        final ProgressDialog pd = new ProgressDialog(viewcategory.this);
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
                                catname=new String[ja.length()];


                                for (int i=0;i < ja.length() ; i++)
                                {
                                    JSONObject j= ja.getJSONObject(i);
                                    id[i]= j.getString("id");
                                    catname[i]= j.getString("catname");

                                }

                                lvs.setAdapter(new customcategory(getApplicationContext(),id,catname));

//                                lvs.setAdapter(new Cust_viewdesignerplan(getApplicationContext(),id,design_name,file,date,amount,description));








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

                params.put("shopid",sh.getString("shopid",""));




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
