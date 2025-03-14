import json
import requests
import websocket
import time

url = ""
result = ""
audioPath = ""

def on_open(ws):
	# Start
	ws.send(json.dumps({
		"timestamps": True,
		"content-type": "audio/wav",
		"interim_results": True,
		"keywords":[
			"six",
			"zero",
			"five",
			"three",
			"eight"
			],
		"keywords_threshold": 0.01,
		"word_alternatives_threshold": 0.01,
		"smart_formatting": True,
		"speaker_labels": False,
		"action": "start"
	}))
	# Send audio data
	with open(audioPath, mode='rb') as f:
		audio = f.read()
	ws.send(audio, websocket.ABNF.OPCODE_BINARY)
	# Stop
	ws.send(json.dumps({"action": "stop"}))

def on_message(ws, message):
	data = json.loads(message)

	if data["results"][0]["final"]:
		global result
		result = data["results"][0]["alternatives"][0]["transcript"]
		# This is an error...
		ws.close()

def on_error(ws, error):
    time.sleep(1)

def on_close(ws):
    print('[*] Websocket closed')

def get_url():
	global url
	url = "https://speech-to-text-demo.ng.bluemix.net/api/v1/credentials"
	response = requests.request("GET", url)
	res = json.loads(response.text)
	url = f"wss://{res['serviceUrl'].split('/')[-1]}/v1/recognize?model=en-US_ShortForm_NarrowbandModel&access_token={res['accessToken']}"

def audioToText(path):
	global audioPath
	audioPath = path
	get_url()
	ws = websocket.WebSocketApp(url, on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close)
	ws.run_forever()
	return result
