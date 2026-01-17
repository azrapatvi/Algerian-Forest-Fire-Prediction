from flask import Flask,render_template,request
import pickle
import pandas as pd

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():

    if request.method=='POST':
        temperature = int(request.form['temperature'])
        rh= int(request.form['rh'])
        ws= int(request.form['ws'])
        rain= float(request.form['rain'])
        ffmc= float(request.form['ffmc'])
        dmc= float(request.form['dmc'])
        isi = float(request.form['isi'])
        region= int(request.form['region'])

        with open('scaler.pkl','rb') as f:
            loaded_scaler=pickle.load(f)

        with open('models.pkl','rb') as f:
            loaded_models=pickle.load(f)

        
        linear_model=loaded_models['linear_reg']

        X_new=[temperature,rh,ws,rain,ffmc,dmc,isi,region]

        X_new_df=pd.DataFrame([
            {
                'temperature': temperature,
                'rh': rh,
                'ws': ws,
                'rain': rain,
                'ffmc': ffmc,
                'dmc': dmc,
                'isi': isi,
                'region': region
            }
        ])
        X_new_scaled=loaded_scaler.transform(X_new_df)

        y_new_pred=linear_model.predict(X_new_scaled)

        return render_template("index.html",predict=y_new_pred[0])
    
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)