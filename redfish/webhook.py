import time
from locust import HttpUser, task, between

# disable InsecureRequestWarning: Unverified HTTPS request is being made to host
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Expose Redfish HW events: Temp, Fan failure, Disk, Power, Memory
EVENT_TMP0100 = \
{
  "@odata.context": "/redfish/v1/$metadata#Event.Event",
  "@odata.id": "/redfish/v1/EventService/Events/5e004f5a-e3d1-11eb-ae9c-3448edf18a38",
  "@odata.type": "#Event.v1_3_0.Event",
  "Context": "any string is valid",
  "Events": [
    {
      "Context": "any string is valid",
      "EventId": "2162",
      "EventTimestamp": "2021-07-13T15:07:59+0300",
      "EventType": "Alert",
      "MemberId": "615703",
      "Message": "The system board Inlet temperature is less than the lower warning threshold.",
      "MessageArgs": [
        "Inlet"
      ],
      "MessageArgs@odata.count": 1,
      "MessageId": "TMP0100",
      "Severity": "Warning"
    }
  ],
  "Id": "5e004f5a-e3d1-11eb-ae9c-3448edf18a38",
  "Name": "Event Array"
}

EVENT_FAN0001 = \
{
  "@odata.context": "/redfish/v1/$metadata#Event.Event",
  "@odata.id": "/redfish/v1/EventService/Events/5e004f5a-e3d1-11eb-ae9c-3448edf18a38",
  "@odata.type": "#Event.v1_3_0.Event",
  "Context": "any string is valid",
  "Events": [
    {
      "Context": "any string is valid",
      "EventId": "2153",
      "EventTimestamp": "2021-07-13T15:09:55+0300",
      "EventType": "Alert",
      "MemberId": "615711",
      "Message": "Fan 1 RPM is less than the lower critical threshold.",
      "MessageArgs": [
        "1"
      ],
      "MessageArgs@odata.count": 1,
      "MessageId": "FAN0001",
      "Severity": "Critical"
    }
  ],
  "Id": "5e004f5a-e3d1-11eb-ae9c-3448edf18a38",
  "Name": "Event Array"
}


EVENT_STOR1 = \
{
  "@odata.context": "/redfish/v1/$metadata#Event.Event",
  "@odata.id": "/redfish/v1/EventService/Events/5e004f5a-e3d1-11eb-ae9c-3448edf18a38",
  "@odata.type": "#Event.v1_3_0.Event",
  "Context": "any string is valid",
  "Events": [
    {
      "Context": "any string is valid",
      "EventId": "4178",
      "EventTimestamp": "2021-07-13T15:21:27+0300",
      "EventType": "Alert",
      "MemberId": "615744",
      "Message": "A device Disk 5 in Enclosure 0 on Connector 0 of RAID Controller in Slot 5 is in an unknown state.",
      "MessageArgs": [
        "Disk 5 in Enclosure 0 on Connector 0 of RAID Controller in Slot 5"
      ],
      "MessageArgs@odata.count": 1,
      "MessageId": "STOR1",
      "Severity": "Warning"
    }
  ],
  "Id": "5e004f5a-e3d1-11eb-ae9c-3448edf18a38",
  "Name": "Event Array"
}

EVENT_PWR1004 = \
{
  "@odata.context": "/redfish/v1/$metadata#Event.Event",
  "@odata.id": "/redfish/v1/EventService/Events/5e004f5a-e3d1-11eb-ae9c-3448edf18a38",
  "@odata.type": "#Event.v1_3_0.Event",
  "Context": "any string is valid",
  "Events": [
    {
      "Context": "any string is valid",
      "EventId": "2274",
      "EventTimestamp": "2021-07-13T15:24:06+0300",
      "EventType": "Alert",
      "MemberId": "615754",
      "Message": "The system performance degraded because power capacity has changed.",
      "MessageId": "PWR1004",
      "Severity": "Warning"
    }
  ],
  "Id": "5e004f5a-e3d1-11eb-ae9c-3448edf18a38",
  "Name": "Event Array"
}

EVENT_MEM0004 = \
{
  "@odata.context": "/redfish/v1/$metadata#Event.Event",
  "@odata.id": "/redfish/v1/EventService/Events/5e004f5a-e3d1-11eb-ae9c-3448edf18a38",
  "@odata.type": "#Event.v1_3_0.Event",
  "Context": "any string is valid",
  "Events": [
    {
      "Context": "any string is valid",
      "EventId": "2265",
      "EventTimestamp": "2021-07-13T14:56:58+0300",
      "EventType": "Alert",
      "MemberId": "615676",
      "Message": "Memory device at location DIMM1 is disabled.",
      "MessageArgs": [
        "DIMM1"
      ],
      "MessageArgs@odata.count": 1,
      "MessageId": "MEM0004",
      "Severity": "Critical"
    }
  ],
  "Id": "5e004f5a-e3d1-11eb-ae9c-3448edf18a38",
  "Name": "Event Array"
}

class QuickstartUser(HttpUser):
#    wait_time = between(1, 2.5)
    wait_time = between(0.1, 0.5)

    @task
    def temp(self):
        self.client.post("/webhook", verify=False, json=EVENT_TMP0100)

    @task
    def fan(self):
        self.client.post("/webhook", verify=False, json=EVENT_FAN0001)

    @task
    def disk(self):
        self.client.post("/webhook", verify=False, json=EVENT_STOR1)

    @task
    def power(self):
        self.client.post("/webhook", verify=False, json=EVENT_PWR1004)

    @task
    def memory(self):
        self.client.post("/webhook", verify=False, json=EVENT_MEM0004)

    def on_start(self):
        time.sleep(1)
