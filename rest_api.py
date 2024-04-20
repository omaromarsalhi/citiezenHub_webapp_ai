from flask import Flask,request,jsonify
from langchain_helper import generate_produxt_description
import ollama_vesion as ov



app = Flask(__name__)
<<<<<<< HEAD
url='https://ea25-34-122-33-80.ngrok-free.app'
=======
url='https://4175-34-74-156-139.ngrok-free.app'
>>>>>>> 86902ae1e004de4f29fc654de3782bdc98fa4227

@app.route('/get-descreption',methods=['POST'])
def generate():
    text=generate_produxt_description(request.args.get('title'))
    return jsonify(text),200

@app.route('/get-product_image_descreption',methods=['POST'])
def generate_desc_image():
    image_url=request.args.get('image_url')
    commands=f"set OLLAMA_HOST={url}&ollama run llava describe the image content only {image_url}"
    text=ov.execute_cmd(commands)
    tuned_response=ov.finetune_text(text)
    return jsonify(tuned_response),200


<<<<<<< HEAD
@app.route('/get-title_validation',methods=['POST'])
def generate_title_validation():
    desc=request.args.get('desc')
    title=request.args.get('title')
    text=ov.generateBasedOnText(desc,title,url)
    tuned_response=ov.finetune_resp(text)
    return jsonify(tuned_response),200

@app.route('/get-category_validation',methods=['POST'])
def generate_category_validation():
    desc=request.args.get('desc')
    title=request.args.get('category')
    text=ov.generateBasedOnCategory(desc,title,url)
    tuned_response=ov.finetune_resp(text)
    return jsonify(tuned_response),200


=======
>>>>>>> 86902ae1e004de4f29fc654de3782bdc98fa4227

if __name__== '__main__':
    app.run()