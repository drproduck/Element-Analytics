# Element-Analytics
about to blow up in the IPO

Error analytics data object (JSON) can be access through this url:
/analytics/\<username\>/\<logfile\>
  
Error analytics:
```
{
  "num_error": some_int,
  "total_entries": some_int,
  "error_rate" : some_float (double)
  "error_by_keyword" : {
    //The list of provided keywords Professor provides
    <keyword1> : count,
    <keyword2> : count,
    ...
  },
  "errors_by_date": {
    <date1> : some_int,
    <date2> : some_int,
    <data3> : some_int,
    ...
  }
}
```

User analytics:
```
{
  "username" : string, // Current username
  "num_log" : int, // Number of log files uploaded by this user
  "num_log_limit" : int, // Number of log files this user allowed to upload
  "storage_limit" : float (in GB), // Max storage capacity for this user
  "storage_used" : float (int GB) // Used storage by this user
}
```
