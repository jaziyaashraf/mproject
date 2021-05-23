package com.example.designerapp;

import android.app.ProgressDialog;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
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


public class Userviewcustomizedarchitechplan extends AppCompatActivity {


    String [] name,squarefeet,expamount,description,file,status,budget;


    ListView lvs;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_userviewdesignerplan);


        lvs=(ListView) findViewById(R.id.lvs);

        SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        final String url = sh.getString("url", "") + "userview_archcustomizedplan/";

        final ProgressDialog pd = new ProgressDialog(Userviewcustomizedarchitechplan.this);
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



                                name=new String[ja.length()];
                                squarefeet=new String[ja.length()];
                                expamount=new String[ja.length()];
                                description=new String[ja.length()];
                                file=new String[ja.length()];
                                status=new String[ja.length()];
                                budget=new String[ja.length()];



                                for (int i=0;i < ja.length() ; i++)
                                {
                                    JSONObject j= ja.getJSONObject(i);
                                    name[i]= j.getString("name");
                                    expamount[i]= j.getString("expamount");
                                    description[i]= j.getString("description");
                                    squarefeet[i]= j.getString("squarefeet");
                                    file[i]= j.getString("file");
                                    status[i]= j.getString("status");
                                    budget[i]= j.getString("budget");
                                }

                                lvs.setAdapter(new cust_customizedarchplan(getApplicationContext(),name,squarefeet,expamount,description,file,status,budget));





                            } else {
                                Toast.makeText(getApplicationContext(), "Failed to sent feedback", Toast.LENGTH_LONG).show();
                            }
                        } catch (JSONException e) {
                            Toast.makeText(getApplicationContext(), "error"+ e.getMessage().toString(), Toast.LENGTH_SHORT).show();
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







    }
}
