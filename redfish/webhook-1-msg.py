import time
from locust import HttpUser, User, task, between, constant, constant_pacing

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

class QuickstartUser(HttpUser):
#    wait_time = between(1, 2.5)
#    wait_time = between(0.1, 0.5)
    wait_time = constant(0.01) # 100 msg per second

    # constant_pacing for an adaptive time that ensures the task runs (at most) once every X seconds
    # Run with user count of 1000 for 100 task/s
    # wait_time = constant_pacing(10) # 1 task per 10 second


    @task
    def temp(self):
        with self.client.post("/webhook", verify=False, json=EVENT_TMP0100, catch_response=True) as response:
          pass
            #if response.status_code == 400:
            #    response.success()

    def on_start(self):
        time.sleep(1)
