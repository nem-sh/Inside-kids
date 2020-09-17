from rest_framework.views import exception_handler
import requests, json
from matterhook import Webhook

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.

    response = exception_handler(exc, context)
    # Now add the HTTP status code to the response.

    if response is not None:
        response.data['status_code'] = response.status_code
    else:
        mwh = Webhook('https://meeting.ssafy.com', 'wx9hjk1nn3buxr9q7nb1yf1jar')
        json_data1 = json.dumps('##### SEVER ERROR')
        json_data2 = json.dumps(">"+str(exc), ensure_ascii=False)
        attachments = []
        message = {}
        message['color'] = '#88fc03'
        message['image_url'] = 'https://about.mattermost.com/wp-content/uploads/2017/08/Mattermost-Logo-Blue.svg'
        markdown_msg = '##### SERVER ERROR OCCUR\n'
        markdown_msg += str(exc)
        message['text'] = markdown_msg
        attachments.append(message)
        mwh.send(attachments=attachments)

    return response
