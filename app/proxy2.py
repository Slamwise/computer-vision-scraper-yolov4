import requests

headers = { 
    "apikey": "bc98f5c0-ae07-11eb-853c-e537dd80e79a"
}

params = (
   ("url","https://www.ebay.com/sch/i.html?_from=R40&_nkw=2014+panini+giannis+antetokounmpo+rookie+194&_sacat=0&rt=nc&LH_Sold=1&LH_Complete=1"),
   ("render","true"),
   ("premium","true"),
);

response = requests.get('https://app.zenscrape.com/api/v1/get', headers=headers, params=params);
print(response.text)