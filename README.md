# aws elasticsearch-indices-remover
Implementation Example of AWS lambda function in python (3.7) using elasticsearch-curator API to remove old indices by prefix and age

Note:
1. To install pip dependencies, run "pip install -r requirements.txt -t ."
2. In AWS console you must create a new lambda function
3. Zip all files and folder after step #1
4. Upload .zip file to your AWS lambda function
5. You must have access to any Elasticsearch aws domain with some indices (be carefull run this function can delete real elasticsearch indices)
6. You mus define in your aws lambda 3 Environment variables:
  host (e.g: search-mytestawsdomain-db7u2us35tenfp7d6tjspaey123.us-east-1.es.amazonaws.com)
  region: (e.g: us-east-1)
  indices_prefix: (e.g: my-indices.prefix)
