import time
import requests
import os
import json
from watson1 import audioToText
filename = 'audio.wav'

def saveFile(content,filename):
    with open(filename, "wb") as handle:
        for data in content.iter_content():
            handle.write(data)
def solve():
    while True:
        headers = {
            'authority': 'api.funcaptcha.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://octocaptcha.com',
            'referer': 'https://octocaptcha.com/',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        }

        data = 'public_key=20782B4C-05D0-45D7-97A0-41641055B6F6&site=https%3A%2F%2Foctocaptcha.com&userbrowser=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F103.0.0.0%20Safari%2F537.36&rnd=0.1693259995067964&data[origin_page]=github_signup_next'

        response = requests.post('https://api.funcaptcha.com/fc/gt2/public_key/20782B4C-05D0-45D7-97A0-41641055B6F6', headers=headers, data=data)
        json_data = json.loads(response.text)
        data = str(json_data['token'])
        session = data.split('|')[0]
        response = requests.get(f'https://api.funcaptcha.com/fc/get_audio/?session_token={session}&analytics_tier=40&r=ap-southeast-1&game=0&language=en', stream=True)
        saveFile(response,filename)
        response = audioToText(os.getcwd() + '/' + filename)

        headers = {
            'authority': 'api.funcaptcha.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://api.funcaptcha.com',
            'referer': 'https://api.funcaptcha.com/fc/gc/?token=93962d61880d04125.1261250504&r=ap-southeast-1&metabgclr=%23ffffff&guitextcolor=%23000000&metaiconclr=%23fff&meta=7&meta_height=380&meta_width=654&pk=20782B4C-05D0-45D7-97A0-41641055B6F6&dc=1&at=40&atp=2&cdn_url=https%3A%2F%2Fapi.funcaptcha.com%2Fcdn%2Ffc&lurl=https%3A%2F%2Faudio-ap-southeast-1.arkoselabs.com&surl=https%3A%2F%2Fapi.funcaptcha.com&smurl=https%3A%2F%2Fapi.funcaptcha.com%2Fcdn%2Ffc%2Fassets%2Fstyle-manager',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'x-newrelic-timestamp': '165819800181190',
            'x-requested-id': '{"ct":"7tXjdaDEPRudvKyqfr5ibg==","iv":"1cb321cddfdb72a4d9667137ddcb3804","s":"5698c5d364013970"}',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'analytics_tier': '40',
            'audio_type': '2',
            'response': f'{response}',
            'r': 'ap-southeast-1',
            'session_token': f'{session}',
            'language': 'en',
            'bio': 'eyJtYmlvIjoiMjQ5LDAsODA3LDI5MjsyNTcsMCw3MzEsMjcxOzI2NCwwLDY1MywyNDk7MjcyLDAsNTc3LDIyNzsyODEsMCw1MDQsMjA2OzI4OCwwLDQzNywxODc7Mjk3LDAsMzc3LDE2OTszMDUsMCwzMjMsMTU1OzMxMywwLDI3NCwxMzk7MzIwLDAsMjM0LDEyODszMjgsMCwyMDEsMTE3OzMzNiwwLDE3NywxMTE7MzQ1LDAsMTU4LDEwNjszNTMsMCwxNDcsMTAwOzM2MSwwLDE0MSw5ODszNjksMCwxMzYsOTc7NDE3LDAsMTQwLDkwOzQyNSwwLDE0NSw4Njs0MzIsMCwxNTQsODA7NDQxLDAsMTY1LDc2OzQ0OSwwLDE3NSw3Mzs0NTYsMCwxODgsNzA7NDY0LDAsMjAwLDY5OzQ3MiwwLDIxNSw2OTs0ODAsMCwyMjYsNjk7NDg4LDAsMjQwLDY5OzQ5NywwLDI1MCw2OTs1MDQsMCwyNjAsNjk7NTEzLDAsMjczLDcwOzUyMSwwLDI4MSw3MDs1MjgsMCwyOTAsNzI7NTM2LDAsMjk3LDczOzU0NSwwLDMwOCw3Mzs1NTMsMCwzMjAsNzM7NTYxLDAsMzI5LDczOzU2OSwwLDMzOSw3Mzs1ODQsMCwzNTAsNzM7NjAxLDAsMzU1LDcyOzYyNCwwLDM2NCw3Mjs2NDIsMCwzNzEsNzM7NjQ5LDAsMzgwLDc3OzY1NywwLDM4Niw4Mjs2NjUsMCwzOTcsODc7NjczLDAsNDExLDk1OzY4MSwwLDQzOSwxMDQ7Njg5LDAsNDYzLDExMTs2OTgsMCw0ODgsMTE4OzcwNSwwLDUxMCwxMjQ7NzEzLDAsNTI0LDEyNTs3MjEsMCw1MzYsMTI2OzcyOCwwLDU0MywxMjY7NzQ0LDAsNTUwLDEyNjs4MzIsMCw1NTMsMTE5Ozg0MSwwLDU1NCwxMTI7ODQ5LDAsNTU1LDEwNjs4NTgsMCw1NTUsOTg7ODc1LDAsNTU2LDkzOzkyMCwwLDU1OSw4Nzs5NDQsMCw1NjIsODI7OTYwLDAsNTY3LDc3Ozk3NiwwLDU3Myw3NDs5OTIsMCw1NzgsNzA7MTAwOCwwLDU4Niw2NTsxMDMzLDAsNTkxLDYwOzExNjAsMCw1ODQsNTk7MTE3NiwwLDU3Nyw1OTsxMTkzLDAsNTcxLDU5OzEyOTAsMSw1NjgsNTk7MTQwNywyLDU2OCw1OTsxNjAxLDAsNTc4LDU5OzE2MDksMCw1ODgsNjA7MTYxNywwLDYwMSw2MzsxNjI0LDAsNjE1LDY4OzE2MzIsMCw2MzgsNzc7MTY0MCwwLDY2NSw4NTsxNjQ4LDAsNzA5LDEwMDsxNjU3LDAsNzYxLDEyMjsxNjY1LDAsODIyLDE0OTsxNjcyLDAsODg4LDE3NTsxNjgwLDAsOTU5LDIwNTsxNjg4LDAsMTAyNywyMzU7MTY5NywwLDExMDIsMjY4OzUzMTQsMCwxMTI5LDI0NDs1MzIxLDAsMTA3NSwyNDQ7NTMyOCwwLDEwMjUsMjQyOzUzMzcsMCw5NjcsMjM0OzUzNTQsMCw4NzUsMjIxOzUzNjEsMCw4MzMsMjEzOzUzNjgsMCw3OTksMjEwOzUzNzYsMCw3NjgsMjA1OzUzODQsMCw3MzgsMTk4OzUzOTIsMCw3MTIsMTk1OzU0MDEsMCw2OTEsMTkxOzU0MDgsMCw2NjksMTg0OzU0MTcsMCw2NTEsMTgwOzU0MjUsMCw2NDEsMTc0OzU0MzIsMCw2MzUsMTcxOzU0NDEsMCw2MjYsMTY3OzU0NTYsMCw2MTksMTYzOzU0ODgsMCw2MTQsMTYxOzU1MjAsMCw2MDksMTU5OzU1NjAsMCw2MDMsMTU5OzU3MjcsMCw1OTgsMTYzOzU3NDMsMCw1OTMsMTU4OzU3NjAsMCw1OTAsMTUyOzU3NzYsMCw1ODQsMTQ0OzU3OTIsMCw1ODAsMTQwOzU4MDAsMCw1NzYsMTM1OzU4MTYsMCw1NzIsMTMwOzU4NTcsMCw1NjgsMTI1OzU5NjAsMCw1NjYsMTIwOzU5OTMsMCw1NjksMTE1OzYwMDgsMCw1NzQsMTExOzYwMjQsMCw1NzgsMTA3OzYwNTYsMCw1ODEsMTAyOzYxNTIsMCw1ODEsMTA4OzYxODQsMCw1ODMsMTEzOzYyNDMsMSw1ODMsMTEzOzYzNTksMiw1ODMsMTEzOzcxNjgsMCw1ODgsMTE3OzcxODUsMCw1OTUsMTIyOzcyMDAsMCw2MDMsMTI1OzcyMTYsMCw2MTMsMTI3OzcyMjQsMCw2MjIsMTI4OzcyMzIsMCw2MzIsMTI5OzcyNDAsMCw2NDMsMTMyOzcyNDksMCw2NTEsMTMzOzcyNTYsMCw2NjYsMTM1OzcyNjUsMCw2NzksMTM3OzcyNzIsMCw2OTAsMTM4OzcyODAsMCw3MDIsMTM5OzcyODgsMCw3MTAsMTM5OzczMDQsMCw3MTgsMTM5OzczMzYsMCw3MjQsMTM5Ozg2MzksMCw3MjksMTQzOzg2NjQsMCw3MzgsMTQ4Ozg2NzIsMCw3NDMsMTUxOzg2ODgsMCw3NTIsMTU2Ozg2OTYsMCw3NTcsMTU5Ozg3MTEsMCw3NjMsMTYyOzg3MjcsMCw3NjgsMTY1Ozg3NjEsMCw3NzMsMTY4Ozg4NDgsMCw3NzUsMTc0Ozg4ODEsMCw3ODEsMTc3Ozg5MDQsMCw3ODYsMTgwOzExMjY1LDAsNzg5LDE2NTsxMTI3MywwLDc3OCwxNDI7MTEyODAsMCw3NjksMTIwOzExMjg4LDAsNzY2LDEwOTsxMTI5NiwwLDc2MywxMDE7IiwidGJpbyI6IiIsImtiaW8iOiI3MzQ0LDAsMTQ7NzQ2NCwxLDE0Ozc3ODQsMCwxNDs3OTI4LDEsMTQ7ODQ0MCwwLDE0Ozg1MjgsMSwxNDs4NzUyLDAsMTI7ODg4MCwxLDEyOzkwNjQsMCwxNDs5MTc1LDEsMTQ7MTY5MjAsMCwxNDsxNzA2NCwxLDE0OzE4MzI4LDAsMTQ7MTg0MTUsMSwxNDsxOTE1MiwwLDE0OzE5MjQ4LDEsMTQ7Mjg2MDgsMCwxMjsyODcwNCwxLDEyOzI4NzEyLDAsMTQ7Mjg4MjQsMCwxNDsyODg3MiwxLDE0OzI4OTYwLDEsMTQ7In0=',
        }

        response = requests.post('https://api.funcaptcha.com/fc/audio/', headers=headers, data=data)
        print(response.text)
        if response.text == '{"response":"correct"}':
            break
        else:
            if response.text == '{"response":"incorrect","error_reply":"Use of the audio challenge for this user has been too high. Please try again."}':
                pass
    token = f'{session}|r=ap-southeast-1|metabgclr=%23ffffff|guitextcolor=%23000000|metaiconclr=%23fff|meta=7|meta_height=380|meta_width=654|pk=20782B4C-05D0-45D7-97A0-41641055B6F6|dc=1|at=40|atp=2|cdn_url=https%3A%2F%2Fapi.funcaptcha.com%2Fcdn%2Ffc|lurl=https%3A%2F%2Faudio-ap-southeast-1.arkoselabs.com|surl=https%3A%2F%2Fapi.funcaptcha.com|smurl=https%3A%2F%2Fapi.funcaptcha.com%2Fcdn%2Ffc%2Fassets%2Fstyle-manager'
    return token