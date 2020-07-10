
web_reg_find("Text=textCheck1", "SaveCount=TextCount", LAST); 
 lr_start_transaction("Name1");
       
web_submit_data("login.pl",
"Action=http://127.0.0.1:1080/cgi-bin/login.pl",
"Method=POST",
"TargetFrame=body",
"RecContentType=text/html",
"Referer=http://127.0.0.1:1080/cgi-bin/nav.pl?in=home",
"Snapshot=t2.inf",
"Mode=HTML",
ITEMDATA,
"Name=userSession", "Value=123211.212069664zDDHzHzpHcAiDDDDDiAczpAzADcf", ENDITEM,
"Name=username", "Value=jojo", ENDITEM,
"Name=password", "Value=bean", ENDITEM,
"Name=JSFormSubmit", "Value=off", ENDITEM,
"Name=login.x", "Value=66", ENDITEM,
"Name=login.y", "Value=12", ENDITEM,
  LAST);

web_submit_data("login.pl",
"Action=http://127.0.0.1:1080/cgi-bin/login.pl",
"Method=POST",
"TargetFrame=body",
"RecContentType=text/html",
"Referer=http://127.0.0.1:1080/cgi-bin/nav.pl?in=home",
"Snapshot=t2.inf",
"Mode=HTML",
ITEMDATA,
"Name=userSession", "Value=123211.212069664zDDHzHzpHcAiDDDDDiAczpAzADcf", ENDITEM,
"Name=username", "Value=jojo", ENDITEM,
"Name=password", "Value=bean", ENDITEM,
"Name=JSFormSubmit", "Value=off", ENDITEM,
"Name=login.x", "Value=66", ENDITEM,
"Name=login.y", "Value=12", ENDITEM,
  LAST);


 if(atoi(lr_eval_string("{textCheck1}")) > = 0){ 
 lr_end_transaction("Name1",LR_PASS);
} 
 else { 
 lr_end_transaction("Name1",LR_FAIL);
}
 lr_think_time(2); 
web_reg_find("Text=textCheck2", "SaveCount=TextCount", LAST); 
 lr_start_transaction("Name2");
       web_submit_data("login.pl",
"Action=http://127.0.0.1:1080/cgi-bin/login.pl",
"Method=POST",
"TargetFrame=body",
"RecContentType=text/html",
"Referer=http://127.0.0.1:1080/cgi-bin/nav.pl?in=home",
"Snapshot=t2.inf",
"Mode=HTML",
ITEMDATA,
"Name=userSession", "Value=123211.212069664zDDHzHzpHcAiDDDDDiAczpAzADcf", ENDITEM,
"Name=username", "Value=jojo", ENDITEM,
"Name=password", "Value=bean", ENDITEM,
"Name=JSFormSubmit", "Value=off", ENDITEM,
"Name=login.x", "Value=66", ENDITEM,
"Name=login.y", "Value=12", ENDITEM,
  LAST);



 if(atoi(lr_eval_string("{textCheck2}")) > = 0){ 
 lr_end_transaction("Name2",LR_PASS);
} 
 else { 
 lr_end_transaction("Name2",LR_FAIL);
}
 lr_think_time(2);