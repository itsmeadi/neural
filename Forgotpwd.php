<?php

$data = array (
	"sessionId" => "10001.SES.27.10.2016.11.11.41.11",
	"deviceUUId" => "bad111ca71039aad",
	"txId" => "",
	"type" => 3,
	"subType" => 0,
	"action" => 8, //It will return the all ObjectID Lists of the table
	"OID" => "",
	"fromTime" => "",
	"toTime" => "",
	"index" => 0,
	"idList" => array(),
	"info" =>array(array("type" => 1,
			     "purpose" => 2,
			     "value" => "9716108706",
			     //"deviceUUId" => "bad111ca71039aad",
			     "countryCode" => "+91",
			    "enterpriseCode" => "DEFAULT_CC"))

	);
	
	

// json encode data

//$cubrid_data_seek(req_identifier, row_number)tring = json_encode($data); 
$data_string = json_encode($data); 
$fh = fopen('jsonc','r');
while ($line = fgets($fh)) 
{
 // $data_string=$line;
}
fclose($fh);
echo($data_string);

// set up the curl resource
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, "http://localhost:3000/SamparkServer/main");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data_string);
curl_setopt($ch, CURLOPT_HEADER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, array(                                                                          
    'Accept-Encoding: gzip,deflate','Content-Encoding:deflate',                                                                                
    'Content-Length: ' . strlen($data_string)                                                                       
)); 

$output = curl_exec($ch);


// output the profile information - includes the header
echo($output); // . PHP_EOL;


// close curl resource to free up system resources
curl_close($ch);


