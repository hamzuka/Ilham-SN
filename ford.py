import pickle
import streamlit as st

model = pickle.load(open('ford_price_prediction.sav', 'rb'))

st.title('Estimasi Harga Mobil Brand Ford')

model1 = st.selectbox('Input Model Mobil',[' Fiesta', ' Focus', ' Puma', ' Kuga', ' EcoSport', ' C-MAX',' Mondeo', ' Ka+', ' Tourneo Custom', ' S-MAX', ' B-MAX', ' Edge',' Tourneo Connect', ' Grand C-MAX', ' KA', ' Galaxy', ' Mustang',' Grand Tourneo Connect', ' Fusion', ' Ranger', ' Streetka',' Escort', ' Transit Tourneo', 'Focus'])
if model1 == ' Fiesta':
    model1 = 1
elif model1 == ' Focus':
    model1 = 2
elif model1 == ' Puma':
    model1 = 3
elif model1 == ' Kuga':
    model1 = 4
elif model1 == ' EcoSport':
    model1 = 5
elif model1 == ' C-MAX':
    model1 = 6
elif model1 == ' Mondeo':
    model1 = 7
elif model1 == ' Ka+':
    model1 = 8
elif model1 == ' Tourneo Custom':
    model1 = 9
elif model1 == ' S-MAX':
    model1 = 10
elif model1 == ' B-MAX':
    model1 = 11
elif model1 == ' Edge':
    model1 = 12
elif model1 == ' Tourneo Connect':
    model1 = 13
elif model1 == ' Grand C-MAX':
    model1 = 14
elif model1 == ' KA':
    model1 = 15
elif model1 == ' Galaxy':
    model1 = 16
elif model1 == ' Mustang':
    model1 = 17
elif model1 == ' Grand Tourneo Connect':
    model1 = 18
elif model1 == ' Fusion':
    model1 = 19
elif model1 == ' Ranger':
    model1 = 20
elif model1 == ' Streetka':
    model1 = 21
elif model1 == ' Escort':
    model1 = 22
elif model1 == ' Transit Tourneo':
    model1 = 23
elif model1 == 'Focus':
    model1 = 24

year = st.selectbox('Input Tahun Mobil',[2017, 2018, 2019, 2015, 2014, 2016, 2013, 2020, 2012, 2008, 2010,
       2009, 2011, 1998, 2007, 2005, 2006, 2002, 2003, 1996, 2004, 2000,
       2060])

transmission = st.selectbox('Input Transmisi Mobil',['Automatic','Manual','Semi-Auto'])
if transmission == 'Automatic':
    transmission = 1
elif transmission == 'Manual':
    transmission = 2
elif transmission == 'Semi-Auto':
    transmission = 3

mileage = st.number_input('Input Jarak Tempuh Mobil')

fuelType = st.selectbox('Input Tipe Bahan Bakar Mobil',['Petrol', 'Diesel', 'Hybrid', 'Electric', 'Other'])
if fuelType == 'Petrol':
    fuelType = 1
elif fuelType == 'Diesel':
    fuelType = 2
elif fuelType == 'Hybrid':
    fuelType = 3
elif fuelType == 'Electric':
    fuelType = 4
elif fuelType == 'Other':
    fuelType = 5

tax = st.number_input('Input Tax')

mpg = st.number_input('Input MPG')

engineSize = st.number_input('Input engineSize')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict (
        [[model1,year,transmission,mileage,fuelType,tax,mpg,engineSize]]
    )
    st.write('Prediksi Harga Mobil Ford (Dalam Rupiah)',predict*15680)