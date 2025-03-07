import requests
import json

# Define the API endpoint, refer flk.py 
url = 'http://<ip of server running flk.py>:5000/generate'

# Define the data to send in the request
'''
data = {
    'prompt': 'Hello, how are you today?'
}
'''
data = {
    'prompt': 'summarize the following paragraph -- In his film career, Rajkumar received eleven Karnataka State Film Awards, including nine Best Actor and two Best Singer awards, eight Filmfare Awards South and one National Film Award.[29] He holds the record of receiving Filmfare Award for Best Actor – Kannada and Karnataka State Film Award for Best Actor the highest number of times. He received the NTR National Award in 2002. He was awarded an honorary doctorate from the University of Mysore,[30] and is a recipient of the Padma Bhushan (1983)[31] and the Dadasaheb Phalke Award (1995) for lifetime contribution to Indian cinema.[32] He was also the first Indian actor to be bestowed with an honorary doctorate for acting.[33] A mega icon and a socio-cultural symbol of Kannada,[34] he has been credited with redefining Kannada cinema[35] and also putting the Kannada cinema on the national map.[36] He was the first actor to play the lead role in 100 as well as 200 Kannada movies.[37] His 1986 movie Anuraga Aralithu was the first Indian movie to be remade in seven other languages.[38] He has the distinction of having played the highest number of devotional, mythological and historical characters'
}
# Make the POST request
response = requests.post(url, headers={'Content-Type': 'application/json'}, data=json.dumps(data))

# Check if the request was successful
if response.status_code == 200:
    # Print the response from the server
    print('Response:', response.json())
else:
    # Print an error message if the request failed
    print('Failed to get a response:', response.status_code, response.text)



'''
curl -X POST http://51.16.160.207:5000/generate -H "Content-Type: application/json" -d '{"prompt": "Hello, how are you today?"}'
'''
