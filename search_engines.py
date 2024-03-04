import os
import requests
from dotenv import load_dotenv

# LIMIT IS 100 A DAY!!!
def google_search(search_query):
    load_dotenv()
    google_api_key = os.getenv("GOOGLE_API_KEY")
    google_search_id = os.getenv("GOOGLE_SEARCH_ENGINE_ID")

    #search_query = "Hello There."
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'q': search_query,
        'key': google_api_key,
        "cx": google_search_id
    }


    response = requests.get(url, params=params)
    results = response.json()
    return results

# TODO: Make something happen if you get such a error.

test_error_response = {
   "error":{
      "code":429,
      "message":"Quota exceeded for quota metric 'Queries' and limit 'Queries per day' of service 'customsearch.googleapis.com' for consumer 'project_number:'.",
      "errors":[
         {
            "message":"Quota exceeded for quota metric 'Queries' and limit 'Queries per day' of service 'customsearch.googleapis.com' for consumer 'project_number:'.",
            "domain":"global",
            "reason":"rateLimitExceeded"
         }
      ],
      "status":"RESOURCE_EXHAUSTED",
      "details":[
         {
            "@type":"type.googleapis.com/google.rpc.ErrorInfo",
            "reason":"RATE_LIMIT_EXCEEDED",
            "domain":"googleapis.com",
            "metadata":{
               "quota_location":"global",
               "service":"customsearch.googleapis.com",
               "consumer":"projects/",
               "quota_limit_value":"100",
               "quota_metric":"customsearch.googleapis.com/requests",
               "quota_limit":"DefaultPerDayPerProject"
            }
         },
         {
            "@type":"type.googleapis.com/google.rpc.Help",
            "links":[
               {
                  "description":"Request a higher quota limit.",
                  "url":"https://cloud.google.com/docs/quota#requesting_higher_quota"
               }
            ]
         }
      ]
   }
}


def main():
    print("Running: search_engines")

    print(google_search("Hello There Mr Google"))


if __name__ == '__main__':
    main()