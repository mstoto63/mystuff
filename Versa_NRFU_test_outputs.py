import requests
import json
import versa_api

def output_interface_errors(text):

    # print out interfaces along with the error rate
    interface_data = json.loads(text)

    # If there is no interface in that tenant, print information
    if interface_data["collection"]["interfaces"] == []:
            print("No interface in this tenant")
    else:
        for interface in interface_data["collection"]["interfaces"]:
            print (f'Interface: {interface["interface"]}, tx-errors: {interface["tx-errors"]}, rx-errors: {interface["rx-errors"]}')


def list_physical_interfaces(text):

    # List out physical interfaces

    interface_data = json.loads(text)

    for vni_int in interface_data['interfaces']['vni']:
        if 'description' in vni_int.keys():
            print(f'{vni_int["name"]}, {vni_int["description"]}')
        else:
            print(f'{vni_int["name"]}')

def list_vnf_managers(text):

    # List out physical interfaces

    vnf_data = json.loads(text)

    print ("VNF Manager IP addressess: ", vnf_data['system']['vnf-manager']['ip-addresses'])

headers = {
    'Connection': 'Close', 'Accept': 'application/json',
    'Content-Type': 'application/json'
}

controllers = [
"AUSYD2SDC1DC01A",
"AUSYD1SDR1DC01A",
"AUSYD1SDR1DC01B",
"AUSYD2SDR1DC01A",
"AUSYD2SDR1DC01B",
"DEFRA1SDC1DC01A",
"DEFRA1SDR1DC01A",
"DEFRA1SDR1DC01B",
"DEFRA2SDR1DC01A",
"DEFRA2SDR1DC01B",
"USCHI2SDCEDG01A",
"USCHI2SDREDG01A",
"USCHI2SDREDG01B",
"USDAL3SDREDG01A",
"USDAL3SDREDG01B"
]

tenants = [
    "GL-FDC",
    "GL-RMO",
    "AP-CNT",
    "EM-CNT",
    "NA-CNT",
]

Tests = [
# This test to list the interface errors
# https://10.116.160.73/versa/ncs-services/vnms/dashboard/appliance/DEFRA1SDR1DC01B/pageable_interfaces?uuid=b9f50ce7-2c79-43d4-9dac-4e408c8b75fd&orgName=GL-FDC&limit=25
#    {"Test":"Interface errors",
#    "URL":"https://127.0.0.1:9182/vnms/dashboard/appliance/DEVICE_NAME/pageable_interfaces?&orgName=TENANT&limit=25",
#     "Output_format": "output_interface_errors"},

# This test to list the NTP server associations
#https://10.116.160.73/versa/ncs-services/vnms/dashboard/appliance/AUSYD1SDR1DC01A/live?uuid=c6d0c379-d0d0-444d-98b4-42266bc56410&command=ntp/statistics
    {"Test":"NTP settings for device",
     "URL": "/vnms/dashboard/appliance/DEVICE_NAME/live?command=ntp/statistics"},

# This test to list the physical interfaces
#https://10.116.160.73/versa/ncs-services/api/config/devices/device/AUSYD1SDR1DC01B/config/interfaces?deep&offset=0&limit=25
#    {"Test":"List all physical interfaces",
#     "URL":"https://127.0.0.1:9182/api/config/devices/device/DEVICE_NAME/config/interfaces?deep&offset=0&limit=25",
#     "Output_format": "list_physical_interfaces"}

# This test to list all VNF configurations
# /versa/ncs-services/api/config/devices/device/AUSYD2SDC1DC01A/config/system
  #  {"Test": "List VNF settings",
  #  "URL": "/api/config/devices/device/DEVICE_NAME/config/system",
  #   "Output_format": "list_vnf_managers"}

#Check syslog settings
#https://10.116.160.73/versa/ncs-services/api/config/devices/device/DEFRA2SDR1DC01B/config/system/syslog?deep=true&pageOffset=0&pageSize=25
#  {"Test": "List syslog settings",
#    "URL": "/api/config/devices/device/DEVICE_NAME/config/system/syslog"}
    #   "Output_format": "list_vnf_managers"}

]




for test_item in Tests:
    print("Performing NRFU test: ", test_item["Test"])
    print("Sample URL: ", test_item["URL"])

    for controller in controllers:

        url = test_item['URL'].replace("DEVICE_NAME",controller)

        # Check if we have to iterate over the tenants
        if url.find("TENANT") != -1:
            for tenant in tenants:
                url_tenant = url.replace("TENANT", tenant)
                resp = versa_api.get(url_tenant)
                print(f'---------- Results for: {controller}, Tenant: {tenant} ------------')
        else:
#            url = test_item['URL'].replace("DEVICE_NAME",controller)
            resp = versa_api.get(url)
            print (f'---------- Results for: {controller} ------------')

        if "Output_format" in test_item.keys():
            globals()[test_item['Output_format']](resp.text)
        else:
            print(resp.text)
