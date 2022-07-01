from pprint import pprint
import pandas as pd
import boto3
from botocore.exceptions import ClientError

client = boto3.client('resourcegroupstaggingapi', )
df=pd.DataFrame({'ResourceARN':[],'Key':[],'Value':[]})    
client = boto3.client('resourcegroupstaggingapi', region_name='ap-southeast-2')
        
for x in client.get_resources().get('ResourceTagMappingList'):
    arn=x.get('ResourceARN')
    for i,tags in enumerate(x.get('Tags')):
        if i==0:
            df.loc[len(df.index)]=[arn,tags['Key'],tags['Value']]
        else:
            df.loc[len(df.index)]=['',tags['Key'],tags['Value']]
                
        
df.to_csv('Output.csv')