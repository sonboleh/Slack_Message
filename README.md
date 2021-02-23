# Slack_Message

There are two ways to send messages to a slack channel, one is making an HTTP POST request to Incoming Webhook URL and another one is to utilize Slack API. Both has their advantages and disadvantages. 

|  | Webhook | Slack API |
|------|-------|-------------|
| Advantage| Easy to use and little to no code requirement. Developers only need to compose the POST payload based on the Slack's requirement and make the POST request. | Slack API offers developer more features to interact with Slack, such as uploading files. |
|Disadvantage| Features are limited by the supported POST request payload, webhook is mainly used for sending text and image* to slack channel. | Required more coding and cannot use tools, such as curl and Postman, to quickly test the result. |

\* image cannot be send along with the message, it has to be uploaded to an external storage and send the image_url along with the message.

In this README, we will focus on how to use the webhook to send a message to Slack channel.

<details>
  <summary>1. Create and obtain Webhook url</summary>

You could ask your manager to provide you an existing one. Or, you can follow the steps in [Link](https://api.slack.com/messaging/webhooks) to set up one for yourself.
</details>


<details>
  <summary>2. Design POST payload</summary>
  
How you design and structure the payload(a *JSON* object) will determine how your message will look like in the channel message.

Slack have an exhaustive documentation on this topic, see [Link](https://api.slack.com/messaging/composing#message_structure)
  
Following are a payload example and respective slack message:
```java
{
  "blocks": [
    {
      "type": "header",
      "text": {
        "type": "plain_text",
        "text": "This is header"
      }
    },
    {
      "type": "context",
      "elements": [
        {
          "type": "plain_text",
          "text": "Showing text and image in Message"
        }
      ]
    },
    {
      "type": "section",
      "fields": [
        {
          "type": "mrkdwn",
          "text": "*Left part of a section:*\n left"
        },
        {
          "type": "mrkdwn",
          "text": "*Right part:*\n<https://google.com|google link>"
        }
      ]
    },
    {
      "type": "divider"
    },
    {
      "type": "image",
      "title": 
        {
          "type": "plain_text",
          "text": "Please enjoy this photo of a kitten"
        },
      "block_id": "image4",
      "image_url": "http://placekitten.com/500/500", 
      "alt_text": "An incredibly cute kitten."
    }
  ]
}
```
<img src="slack-result.png" width="600"> 

</details>

<details>
  <summary>3. Make POST request</summary>
  
There are plenty of tools you could use to make the POST request, in the following, we will introduce two of them, *cURL* and *Postman*.

**cURL** is a light yet powerful command line tool to get and send data using URL syntax.

A basic POST request example using cURL:
```
curl -X POST -H 'Content-type:application/json' --data "{\"text\":\"Hello, World!\"}" https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX
```
<img src="curl-example.png" width="600">
-X, --request \<command\>: Specify request command to use

-H, --header \<header/@file\>: Pass custom header(s) to server

-d, --data \<data\>: HTTP POST data.




**Postman** is a commercial API testing tool with Graphical User Interface. It offers free version but requires user to create an account.
  
A basic POST request example using Postman:
<img src="postman-example.png" width="600"> 

</details>
  
