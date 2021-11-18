from pprint import pprint
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
import time

credentials = GoogleCredentials.get_application_default()

service = discovery.build('compute', 'v1', credentials=credentials)

region = 'europe-west1'

# Project ID for this request.
project = 'network-demo-1-332510'  # TODO: Update placeholder value.

network_body = {
    "routingConfig": {
        "routingMode": "REGIONAL"
    },
    "autoCreateSubnetworks": False,
    "name": "pnetwork",
    "mtu": 1460,
    "region": f"{region}"
}

subnetwork_body = {
    "enableFlowLogs": False,
    'ipCidrRange': "10.0.0.0/24",
    "name": "snet",
    "network": "projects/network-demo-1-332510/global/networks/pnetwork",
    "privateIpGoogleAccess": False,
    "region": f"{region}"
}


request1 = service.networks().insert(project=project, body=network_body)
response1 = request1.execute()

pprint(response1)

print("creating network...\n")
time.sleep(30)

request2 = service.subnetworks().insert(project=project, region=region, body=subnetwork_body)
response2 = request2.execute()

pprint(response2)
