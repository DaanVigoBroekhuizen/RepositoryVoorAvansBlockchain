from flask import Flask, request, jsonify
from Block import Block

app = Flask(__name__) # 1

@app.route('/') # 2
def hello():
    block1 = Block("0", "ROOT_BLOCK", "Dit is de data van de hash")
    block2 = Block("1", "secondHash", "Dit is de data van de hash")

    return {
        "chain": [block1.__dict__, block2.__dict__]
    }

app.run(port=8080)