from flask import Flask, request, jsonify
import subprocess
app = Flask(__name__)


@app.route('/generate', methods=['POST'])
def generate_text():
    data = request.json
    prompt = data['prompt']
    # Run the Ollama model with the prompt
    result = subprocess.run(['ollama', 'run', 'llama3.2', prompt], capture_output=True, text=True)

    response = result.stdout
    return jsonify({'response': response})


#####main()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)



'''
systemctl edit ollama.service
Environment="OLLAMA_HOST=0.0.0.0:11434"
'''
