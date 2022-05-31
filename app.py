# -*- coding: utf-8 -*-
"""
Created on Tue May 31 00:47:40 2022

@author: abdul
"""

import pandas as pd
import numpy as np
from flask import Flask, request, render_template
import pickle

  
# create the sheet object 
  
  
    


app=Flask(__name__,template_folder='template')
#app = Flask(__name__)
model = pickle.load(open('Regressor_prie_prediction.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
  
    wb = load_workbook('excel.xlsx')
    sheet = wb.active 
    current_row = sheet.max_row 
    current_column = sheet.max_column
    sheet.cell(row=current_row + 1, column=1).value =request.form['Name']
    sheet.cell(row=current_row + 1, column=2).value =request.form['Model Year']
    sheet.cell(row=current_row + 1, column=3).value =request.form['Location']
    sheet.cell(row=current_row + 1, column=4).value =request.form['Mileage']
    sheet.cell(row=current_row + 1, column=5).value =request.form['Registered City']
    sheet.cell(row=current_row + 1, column=6).value =request.form['Engine Type']
    sheet.cell(row=current_row + 1, column=7).value =request.form['Engine Capacity']
    sheet.cell(row=current_row + 1, column=8).value =request.form['Transmission']
    sheet.cell(row=current_row + 1, column=9).value =request.form['Color']
    sheet.cell(row=current_row + 1, column=10).value =request.form['Assembly']
    sheet.cell(row=current_row + 1, column=11).value =request.form['Body Type']
    sheet.cell(row=current_row + 1, column=12).value =request.form['Features']
# save the file 
    wb.save('excel.xlsx')
    df11=pd.read_excel('excel.xlsx')
    df12=df11.to_csv("excel1.csv",index=None , header=True)
    df13=pd.read_csv("excel1.csv")
    df14=df13
    df14['make'] = df14['Name'].str.split(' ').str[0]
    df14['model'] = df14['Name'].str.split(' ').str[1]
    ##df14=del_col(df14,'Name')
    df14=df14.drop("Name",axis=1)
    df14['Engine Capacity'] = df14['Engine Capacity'].str.replace(r' cc$', '')
    df14["State"] = df14["Location"].str.split().str[-1]
    df14=df14.drop("Location",axis=1)
    import warnings
    warnings.filterwarnings('ignore')
    df14['ABS'] = pd.np.where(df14.Features.str.contains("ABS"),"1","0")
    df14['Air_Bags'] = pd.np.where(df14.Features.str.contains("Air Bags"),"1","0")
    df14['Air_Con'] = pd.np.where(df14.Features.str.contains("Air Conditioning"),"1","0")
    df14['A_Rims'] = pd.np.where(df14.Features.str.contains("Alloy Rims"),"1","0")
    df14['CD'] = pd.np.where(df14.Features.str.contains("CD Player"),"1","0")
    df14['DVD'] = pd.np.where(df14.Features.str.contains("DVD Player"),"1","0")
    df14['C_Box'] = pd.np.where(df14.Features.str.contains("CoolBox"),"1","0")
    df14['Cruise'] = pd.np.where(df14.Features.str.contains("Cruise Control"),"1","0")
    df14['Kl_Entry'] = pd.np.where(df14.Features.str.contains("Keyless Entry"),"1","0")
    df14['P_Locks'] = pd.np.where(df14.Features.str.contains("Power Locks"),"1","0")
    df14['P_Mirr'] = pd.np.where(df14.Features.str.contains("Power Mirrors"),"1","0")
    df14['P_Wind'] = pd.np.where(df14.Features.str.contains("Power Windows"),"1","0")
    df14['P_Steer'] = pd.np.where(df14.Features.str.contains("Power Steering"),"1","0")
    df14['S_Roof'] = pd.np.where(df14.Features.str.contains("Sun Roof"),"1","0")
    df14['Nav'] = pd.np.where(df14.Features.str.contains("Navigation System"),"1","0")
    df14['Imm_Key'] = pd.np.where(df14.Features.str.contains("Immobilizer Key"),"1","0")
    df14['Cassette'] = pd.np.where(df14.Features.str.contains("Cassette Player"),"1","0")
    df14['Climate'] = pd.np.where(df14.Features.str.contains("Climate Control"),"1","0")
    df14['R_Cam'] = pd.np.where(df14.Features.str.contains("Rear Camera"),"1","0")
    df14['R_Speak'] = pd.np.where(df14.Features.str.contains("Rear speakers"),"1","0")
    df14['Usb_Aux'] = pd.np.where(df14.Features.str.contains("USB and Auxillary Cable"),"1","0")
    df14['R_Enter'] = pd.np.where(df14.Features.str.contains("Rear Seat Entertainment"),"1","0")
    df14['H_Seats'] = pd.np.where(df14.Features.str.contains("Heated Seats"),"1","0")
    df14['Radio'] = pd.np.where(df14.Features.str.contains("Radio"),"1","0")
    df14=df14.drop("Features",axis=1)
    df14[["ABS","Air_Bags","Air_Con","A_Rims","CD","DVD","C_Box","Cruise","Kl_Entry",
         "P_Locks","P_Mirr","P_Wind","P_Steer","S_Roof","Nav","Imm_Key","Cassette",
         "Climate","R_Cam","R_Speak","Usb_Aux","R_Enter","H_Seats","Radio","Engine Capacity"]] = df14[["ABS","Air_Bags","Air_Con","A_Rims","CD","DVD","C_Box","Cruise","Kl_Entry",
         "P_Locks","P_Mirr","P_Wind","P_Steer","S_Roof","Nav","Imm_Key","Cassette",
         "Climate","R_Cam","R_Speak","Usb_Aux","R_Enter","H_Seats","Radio","Engine Capacity"]].apply(pd.to_numeric)
    df14=pd.get_dummies(df14)
    df14=df14.apply(pd.to_numeric)
    df15=pd.read_csv("Data_Unseen.csv")
    DF16 = pd.concat([df15,df14],ignore_index=True)
    dfA3=DF16.iloc[-1:,0:428]
    dfA3=dfA3.fillna(0)
    
    
    #dfA2.to_csv("testing_data.csv")
    #data_unseen = pd.read_csv('testing_data.csv') 
   #print(data_unseen.tail)
   
    '''
    For rendering results on HTML GUI
    '''
    #output=request.form['Name']
    
    '''
    int_features = [int(x) for x in request.form.values()]
    print(int_features)
    data_unseen = pd.read_csv('Data_Unseen.csv') 
    data_unseen.head
    '''
    #data_unseen = pd.read_csv('Data_Unseen.csv') 
    
    prediction = model.predict(dfA3)
    prediction2 =int(np.asarray(prediction))/-500000
    output = prediction2
    
    return render_template('index.html', prediction_text='Predicted Value of the car in PKR is {}.'.format(output))

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
    
    ##     app.run(debug=True)