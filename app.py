from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('predict.html')

# @app.route("/predict",methods=['GET'])
# def check():
#     return render_template('predict.html')

standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    # Fuel_Type_Diesel=0
    if request.method == 'POST':
        # Year = int(request.form['Year'])
        # Present_Price=float(request.form['Present_Price'])
        # Kms_Driven=int(request.form['Kms_Driven'])
        # Kms_Driven2=np.log(Kms_Driven)
        # Owner=int(request.form['Owner'])
        Team1_Name = request.form['Team1']
        Team2_Name = request.form['Team2']
        city = request.form['City']
        team_dict = {'Australia': 0, 'Bangladesh': 1, 'Canada': 2, 'England': 3, 'India': 4, 'Ireland': 5, 'Kenya': 6, 'Malaysia': 7, 'Morocco': 8, 'Netherlands': 9, 'New Zealand': 10, 'Pakistan': 11, 'Qatar': 12, 'Scotland': 13, 'Singapore': 14, 'South Africa': 15, 'Sri Lanka': 16, 'United Arab Emirates': 17, 'West Indies': 18, 'Zimbabwe': 19}
        city_dict = {'Abu Dhabi': 0, 'Adelaide': 1, 'Ahmedabad': 2, 'Amritsar': 3, 'Amstelveen': 4, 'Auckland': 5, 'Ballarat': 6, 'Basseterre': 7, 'Belfast': 8, 'Bengaluru': 9, 'Benoni': 10, 'Birmingham': 11, 'Bloemfontein': 12, 'Bogra': 13, 'Bridgetown': 14, 'Brighton': 15, 'Brisbane': 16, 'Bristol': 17, 'Bulawayo': 18, 'Cairns': 19, 'Canberra': 20, 'Canterbury': 21, 'Cape Town': 22, 'Cardiff': 23, 'Centurion': 24, 'Chandigarh': 25, 'Chattogram': 26, 'Chelmsford': 27, 'Chennai': 28, 'Chester-le-Street': 29, 'Christchurch': 30, 'Colombo': 31, 'Cuttack': 32, 'Dambulla': 33, 'Darwin': 34, 'Delhi': 35, 'Derby': 36, 'Dhaka': 37, 'Dharamsala': 38, 'Doha': 39, 'Dubai': 40, 'Dublin': 41, 'Dunedin': 42, 'Durban': 43, 'East London': 44, 'Faisalabad': 45, 'Faridabad': 46, 'Fatullah': 47, 'Galle': 48, 'Glasgow': 49, 'Gqeberha': 50, 'Gros Islet': 51, 'Gujranwala': 52, 'Guwahati': 53, 'Gwalior': 54, 'Hambantota': 55, 'Hamilton': 56, 'Harare': 57, 'Hobart': 58, 'Hyderabad': 59, 'Indore': 60, 'Jaipur': 61, 'Jalandhar': 62, 'Jamshedpur': 63, 'Johannesburg': 64, 'Kandy': 65, 'Kanpur': 66, 'Karachi': 67, 'Kimberley': 68, 'Kingston': 69, 'Kochi': 70, 'Kolkata': 71, 'Kuala Lumpur': 72, 'Lahore': 73, 'Launceston': 74, 'Leeds': 75, 'London': 76, 'Lucknow': 77, 'Mackay': 78, 'Manchester': 79, 'Margao': 80, 'Melbourne': 81, 'Moratuwa': 82, 'Mount Maunganui': 83, 'Multan': 84, 'Mumbai': 85, 'Nagpur': 86, 'Nairobi': 87, 'Napier': 88, 'Nelson': 89, 'North Sound': 90, 'Northampton': 91, 'Nottingham': 92, 'Paarl': 93, 'Perth': 94, 'Peshawar': 95, 'Pietermaritzburg': 96, 'Port of Spain': 97, 'Potchefstroom': 98, 'Providence': 99, 'Pune': 100, 'Queenstown': 101, 'Quetta': 102, 'Raipur': 103, 'Rajkot': 104, 'Ranchi': 105, 'Rawalpindi': 106, 'Rotterdam': 107, 'Sahiwal': 108, 'Sargodha': 109, 'Scarborough': 110, 'Sharjah': 111, 'Sialkot': 112, 'Singapore': 113, 'Southampton': 114, 'Srinagar': 115, "St George's": 116, 'Swansea': 117, 'Sydney': 118, 'Tangier': 119, 'Taunton': 120, 'Taupo': 121, 'The Hague': 122, 'Thiruvananthapuram': 123, 'Toronto': 124, 'Vadodara': 125, 'Visakhapatnam': 126, 'Wellington': 127}
        Team1 = team_dict.get(Team1_Name)
        Team2 = team_dict.get(Team2_Name)
        city2 = city_dict.get(city)
        # Fuel_Type_Petrol=request.form['Fuel_Type_Petrol']
        # if(Fuel_Type_Petrol.lower()=='petrol'):
        #         Fuel_Type_Petrol=1
        #         Fuel_Type_Diesel=0
        # else:
        #     Fuel_Type_Petrol=0
        #     Fuel_Type_Diesel=1
        # Year=2020-Year
        # Seller_Type_Individual=request.form['Seller_Type_Individual']
        # if(Seller_Type_Individual.lower()=='individual'):
        #     Seller_Type_Individual=1
        # else:
        #     Seller_Type_Individual=0	
        # Transmission_Mannual=request.form['Transmission_Manual']
        # if(Transmission_Mannual.lower()=='manual'):
        #     Transmission_Mannual=1
        # else:
        #     Transmission_Mannual=0
        prediction=model.predict([[Team1,Team2,city2]])
        output=round(prediction[0],2)
        if output==0:
            return render_template('predict.html',prediction_texts=f"Winner is {Team1_Name}")
        else:
            return render_template('predict.html',prediction_text=f"Winner is {Team2_Name}")
    else:
        return render_template('predict.html')

if __name__=="__main__":
    app.run(debug=True)
