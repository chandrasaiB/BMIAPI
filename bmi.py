from flask import Flask,jsonify,request
app=Flask(__name__)
@app.route('/',methods=['POST'])
def bmi():
    data=request.get_json()
    weight=data['weight']
    height=data['height']
    res=(int(weight)/(float(height)*float(height)))
    if res<20:
        return(jsonify({"bmi (you are lean) ":res}))
    elif res>25:
         return(jsonify({"bmi (you are fast) ": res}))
    else:
         return(jsonify({"bmi (you are normal) ": res}))

@app.route('/details',methods=['get'])
def abx():
    return ("hello")
if __name__ == "__main__":
        app.run(port=5000,debug=True)