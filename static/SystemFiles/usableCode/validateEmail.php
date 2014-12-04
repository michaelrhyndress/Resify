function is_valid_email($email, $test_mx = false)  
{  
    if(eregi("^([_a-z0-9-]+)(\.[_a-z0-9-]+)*@([a-z0-9-]+)(\.[a-z0-9-]+)*(\.[a-z]{2,4})$", $email))  
        if($test_mx)  
        {  
            list($username, $domain) = split("@", $email);  
            return getmxrr($domain, $mxrecords);  
        }  
        else  
            return true;  
    else  
        return false;  
}