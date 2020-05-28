web_reg_find("Text=textcheck1", "SaveCount=TextCount1", LAST); 
 lr_start_transaction("Transaction1")
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

 if(TextCount1){ 
 lr_end_transaction("Transaction1",LR_PASS)
} 
 else { 
 lr_end_transaction("Transaction1",LR_FAIL)
}

web_reg_find("Text=textcheck2", "SaveCount=TextCount2", LAST); 
 lr_start_transaction("Transaction2")
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

 if(TextCount2){ 
 lr_end_transaction("Transaction2",LR_PASS)
} 
 else { 
 lr_end_transaction("Transaction2",LR_FAIL)
}

web_reg_find("Text=textcheck3", "SaveCount=TextCount3", LAST); 
 lr_start_transaction("Transaction3")
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

 if(TextCount3){ 
 lr_end_transaction("Transaction3",LR_PASS)
} 
 else { 
 lr_end_transaction("Transaction3",LR_FAIL)
}
