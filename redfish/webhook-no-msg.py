import time
from locust import HttpUser, task, between

# disable InsecureRequestWarning: Unverified HTTPS request is being made to host
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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

class QuickstartUser(HttpUser):
#    wait_time = between(1, 2.5)
#    wait_time = between(0.1, 0.5)
    wait_time = between(0.01, 0.01) # 100 msg per second

    @task
    def temp(self):
        self.client.post("/webhook", verify=False, json=EVENT_FAN0001)

    def on_start(self):
        time.sleep(1)
