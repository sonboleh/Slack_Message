import json
import requests

def convertToSlackRequiredFormat(json_string):
    jsonObject = json.loads(json_string)
    slack_message = {
        "blocks" : [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "Alerts Testing"
                }                          
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*event_time: * {}\n*site_id: * {}\n*site_name: * {}\n*camera_id: * {}\n*camera_name: * {}\n*event_type: * {}\n*temperature_value: * {}\n*temperature_unit: * {}\n*qr_data: * {}\n*person_id: * {}\n".format(jsonObject["data"]["event_time"],jsonObject["data"]["site_id"],jsonObject["data"]["site_name"],jsonObject["data"]["camera_id"],jsonObject["data"]["camera_name"],jsonObject["data"]["event_type"],jsonObject["data"]["temperature_value"],jsonObject["data"]["temperature_unit"],jsonObject["data"]["qr_data"],jsonObject["data"]["person_id"],)
                },
                "accessory": {
                    "type": "image",
                    "image_url": jsonObject["data"]["face_image"],
                    "alt_text": "face image"
                }
            },
            {
                "type": "image",
                "title": 
                    {
                    "type": "plain_text",
                    "text": "Captured Face Image"
                    },
                "image_url": "http://placekitten.com/500/500", 
                "alt_text": "An incredibly cute kitten."
            }
        ]
    }

    return slack_message

def test():
    dataFromBackend = {
        "token":"token_you_provided",
        "data":{
            "event_time":"01/01/2021",
            "site_id":"001",
            "site_name":"San Mateo HQ",
            "camera_id":"003",
            "camera_name":"InStore Camera",
            "event_type":"High Temperature",
            "temperature_value":"100",
            "temperature_unit":"°F",
            "face_image":"http://placekitten.com/500/500",
            "qr_data":"none",
            "person_id":"005"
        }
    }

    json_string = json.dumps(dataFromBackend)

    slack_message = convertToSlackRequiredFormat(json_string)
    url = ''
    r = requests.post(url = url, json=slack_message) 
    print(r.text)


def main():
    test()


if __name__ == '__main__':
    main()
