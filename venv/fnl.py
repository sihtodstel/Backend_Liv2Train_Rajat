from flask import Flask, jsonify, request #import objects from the Flask model
app = Flask(__name__) #define app using Flask

languages = [{'name' : 'JavaScript'}, {'name' : 'Python'}, {'name' : 'Ruby'}]
datamodel=[{'cname': 'rkpuram'},{'ccode','150'},{'daddress':'dwarka delhi'},{'city':'delhi'},{'state':'new delhi'},{'pin':'110075'},
{'scap':'40'},{'courses':'cs'},{'datee':''},{'email':'xyz@gmail.com'},{'phone':'8578329810'}]

@app.route('/', methods=['GET'])
def test():
	return jsonify({'message' : 'It works!'})

@app.route('/lang', methods=['GET'])
def returnAll():
	return jsonify({'languages' : languages})

@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
	langs = [language for language in languages if language['name'] == name]
	return jsonify({'language' : langs[0]})

@app.route('/lang', methods=['POST'])
def addOne():
	language = {'name' : request.json['name']}
	languages.append(language)
	return jsonify({'languages' : languages})

@app.route('/data',methods=['POST'])
def add():
	if request.method == 'POST':
		posted_data = request.get_json()
		data = posted_data['data']
		return jsonify(str("Successfully stored  " + str(data)))

@app.route('/getdata', methods=['GET'])
def returnData():
	posted_data = request.get_json()
	name = posted_data['name']
	return jsonify(" JSON Of fields " + name + "!!!")

if __name__ == '__main__':
	app.run(debug=True, port=8080) #run app on port 8080 in debug mode