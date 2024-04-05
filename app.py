import pandas as pd
import datetime
import mysql.connector
import time as tm
import json
import datetime as dtm
from datetime import datetime, timedelta
from datetime import time as dt_tm
from flask import Flask, g, redirect, render_template, request, session, url_for, make_response, Response
import os
Meter_id = "GMBS C05_08D"
print(Meter_id)
meterID_H = "GMBS C05_08D"
print(meterID_H)
start_time= 0
end_time= 0
st1= 0
end1= 0

# calculate the previous all day timestamp
midnight = datetime.combine(datetime.today(), dt_tm.min)
yesterday_midnight = midnight - timedelta(days=1)



# print(f"from {yesterday_midnight.timestamp()}......to {midnight.timestamp()}")

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'


users = []  # created a list for the username and password
users.append(
    User(id=1, username='user1', password='pass1'))  # instead of this we can also take username password from db
users.append(User(id=2, username='user2', password='pass2'))
users.append(User(id=3, username='user3', password='pass3'))

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user


print("ok till 70")

@app.route('/totalload', methods=['GET', 'POST'])
def totalload():
    stm = str(int(datetime.now().timestamp() - 900))
    stme = str(int(datetime.now().timestamp()))
    try:
        db = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                     host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                     port="3306")
        db_cursor = db.cursor()
        db_cursor.execute("SELECT Total_kW FROM bokaro_ems.trialbsl where Meter_id= 'GMBS C03_10D' and timest between %s and %s order by  dataid desc limit 1",(stm,stme,))
        data1 = db_cursor.fetchall()

        if (data1 == []):
            data101 = 0.0;
        else:
            data101 = (data1[0][-1])-(data1[0][-1])
        db.commit()
        db.close()

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    try:
        db = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                     host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                     port="3306")
        db_cursor = db.cursor()
        db_cursor.execute("SELECT Total_kW FROM bokaro_ems.trialbsl where Meter_id= 'GMBS C05_08D' and timest between %s and %s order by  dataid desc limit 1",(stm,stme,))
        data2 = db_cursor.fetchall()

        if (data2 == []):
            data20 = 0.0;
        else:
            data20 = data2[0][0]
        db.commit()
        db.close()

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    try:
        db = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                     host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                     port="3306")
        db_cursor = db.cursor()
        db_cursor.execute("SELECT Total_kW FROM bokaro_ems.trialbsl where Meter_id= 'GMBS C06_09D' and timest between %s and %s order by  dataid desc limit 1",(stm,stme,))
        data3 = db_cursor.fetchall()

        if (data3 == []):
            data30 = 0.0;
        else:
            data30 = data3[0][0]
        db.commit()
        db.close()

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    try:
        db = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                     host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                     port="3306")
        db_cursor = db.cursor()
        db_cursor.execute("SELECT Total_kW FROM bokaro_ems.trialbsl where Meter_id= 'GMBS C08_16D' and timest between %s and %s order by  dataid desc limit 1",(stm,stme,))
        data4 = db_cursor.fetchall()

        if(data4==[]):
            data40 = 0.0;
        else:
            data40 = data4[0][0]
        db.commit()
        db.close()


    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    try:
        db = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                     host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                     port="3306")
        db_cursor = db.cursor()
        db_cursor.execute("SELECT Total_kW FROM bokaro_ems.trialbsl where Meter_id= 'GMBS C09_13D' and timest between %s and %s order by  dataid desc limit 1",(stm,stme,))
        data5 = db_cursor.fetchall()

        if (data5 == []):
            data50 = 0.0;
        else:
            data50 = data5[0][0]
        db.commit()
        db.close()

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    try:
        db = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                     host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                     port="3306")
        db_cursor = db.cursor()
        db_cursor.execute("SELECT Total_kW FROM bokaro_ems.trialbsl where Meter_id= 'GMBS C18_14D' and timest between %s and %s order by  dataid desc limit 1",(stm,stme,))
        data6 = db_cursor.fetchall()

        if (data6 == []):
            data60 = 0.0;
        else:
            data60 = data6[0][0]
        db.commit()
        db.close()

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    try:
        db = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                     host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                     port="3306")
        db_cursor = db.cursor()
        db_cursor.execute("SELECT Total_kW FROM bokaro_ems.trialbsl where Meter_id= 'GMBS C19_17D' and timest between %s and %s order by  dataid desc limit 1",(stm,stme,))
        data7 = db_cursor.fetchall()

        if (data7 == []):
            data70 = 0.0;
        else:
            data70 = data7[0][0]
        db.commit()
        db.close()

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    try:
        db = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                     host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                     port="3306")
        db_cursor = db.cursor()
        db_cursor.execute("SELECT Total_kW FROM bokaro_ems.trialbsl where Meter_id= 'GMBS C20_18D' and timest between %s and %s order by  dataid desc limit 1",(stm,stme,))
        data8 = db_cursor.fetchall()

        if (data8 == []):
            data80 = 0.0;
        else:
            data80 = data8[0][0]
        db.commit()
        db.close()

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    try:
        db = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                     host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                     port="3306")
        db_cursor = db.cursor()
        db_cursor.execute("SELECT Total_kW FROM bokaro_ems.trialbsl where Meter_id= 'GMBS C21_11D' and timest between %s and %s order by  dataid desc limit 1",(stm,stme,))
        data9 = db_cursor.fetchall()

        if (data9 == []):
            data90 = 0.0;
        else:
            data90 = data9[0][0]
        db.commit()
        db.close()

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    try:
        db = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                     host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                     port="3306")
        db_cursor = db.cursor()
        db_cursor.execute("SELECT Total_kW FROM bokaro_ems.trialbsl where Meter_id= 'GMBS C21_11D' and timest between %s and %s order by  dataid desc limit 1",(stm,stme,))
        data10 = db_cursor.fetchall()

        if (data10 == []):
            data100 = 0.0;
        else:
            data100 = data10[0][0]
        db.commit()
        db.close()

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    try:
        db = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                     host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                     port="3306")
        db_cursor = db.cursor()
        db_cursor.execute("SELECT Total_kW FROM bokaro_ems.trialbsl where Meter_id= 'GMBS C27_15D' and timest between %s and %s order by  dataid desc limit 1",(stm,stme,))
        data11 = db_cursor.fetchall()

        if (data11 == []):
            data110 = 0.0;
        else:
            data110 = data11[0][0]
        db.commit()
        db.close()
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))



    print("checking data")

    totalload_1 = (data101+data20+data30+data40+data50+data60+data70+data80+data90+data100+data110);

    totalload_2 = (round(totalload_1, 2));

    response1 = make_response(json.dumps(totalload_2))
    response1.content_type = 'application/json'
    return response1
@app.route('/data', methods=["GET", "POST"])
def data():
    print("session valid line no 74")
    global Meter_id
    ok2 = "line64"
    print(ok2)
    print(Meter_id)
    global st1
    global end1
    modbus_tm=0
    voltage_ll=0
    avg_current=0
    frequency=0
    average_pf=0
    net_power=0
    net_energy=0
    apparent_power=0
    apparent_energy=0
    THDP1=0
    meter_info=0
    Current_i1=0
    Current_i2=0
    Current_i3=0
    timest=0
    crtm=str((int(datetime.now().timestamp())-360)*1000)
    st1= str(int(datetime.now().timestamp() - 1500))
    end1= str(int(datetime.now().timestamp()))
    print(crtm)
    try:
        db2 = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                          host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                          port="3306")
        db2_cursor = db2.cursor()
        db2_cursor.execute("SELECT Modbus_time, AVG_voltage_LL, AVG_current, Frequency, AVG_pf, Total_kw, Total_net_kWh, Total_kVA, Total_net_kVAh, THDP1,Current_i1, Current_i2, Current_i3, timest,Total_kVAr,Total_net_kVArh from trialbsl  where Meter_id =%s order by dataid desc limit 1",(Meter_id,))

        data57 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        print(data57)
        print(type(data57))
        print(data57[0])
        print(type(data57[0]))
        print(data57[0][0])
        print(type(data57[0][0]))
        if((data57[0][13])>=crtm):
            modbus_tm = (data57[0][0])
            voltage_ll = (data57[0][1])
            avg_current = (data57[0][2])
            frequency = (data57[0][3])
            average_pf = (data57[0][4])
            net_power = (data57[0][5])
            net_energy = (data57[0][6])
            apparent_power = (data57[0][7])
            apparent_energy = (data57[0][8])
            THDP1 = (data57[0][9])
            Current_i1 = (data57[0][10])
            Current_i2 = (data57[0][11])
            Current_i3 = (data57[0][12])
            timest = (data57[0][13])
            reactpow = (data57[0][14])
            reacten = (data57[0][15])
        else:
            modbus_tm = 0
            voltage_ll = 0
            avg_current = 0
            frequency = 0
            average_pf = 0
            net_power = 0
            net_energy = 0
            apparent_power = 0
            apparent_energy = 0
            THDP1 = 0
            Current_i1 = 0
            Current_i2 = 0
            Current_i3 = 0
            timest = 0
            reactpow = 0
            reacten = 0

        print("line308")
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    meter_info = str(request.form.get("meter_id"))
    # print(type(meter_info))
    data = [modbus_tm, voltage_ll, avg_current, frequency, Meter_id, average_pf, net_power, net_energy, apparent_power,
            apparent_energy, THDP1, meter_info,Current_i1,Current_i2,Current_i3,timest,reactpow,reacten]
    # data=[xx1(not used),average voltage,avg_current,frequency,xx2(thd),averagepf,activepower,activeenergy,apparentpower,apparent energy]
    response1 = make_response(json.dumps(data))
    response1.content_type = 'application/json'
    return response1


@app.route("/currentdata", methods=["GET", "POST"])
def currentdata():
    if not g.user:
        print("session not valid")
        return redirect(url_for('login'))

    print("session valid")
    global Meter_id

    Meter_id = request.form.get("meter_id")
    if (Meter_id==None):
        Meter_id="GMBS C05_08D"
    print(Meter_id)
    print(type(Meter_id))

    try:
        db2 = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                      host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                      port="3306")
        db2_cursor = db2.cursor()
        db2_cursor.execute(
            "SELECT Modbus_time,AVG_voltage_LL,Current_i1,Current_i2,Current_i3,AVG_current,Frequency,AVG_pf,THDP1,Total_kW,Total_net_kWh,Total_kVAr,Total_net_kVArh, Total_kVA, Total_net_kVAh from trialbsl WHERE Meter_id =%s  and timest between %s and %s",
            (Meter_id, str(int(datetime.now().timestamp() - 3000)), str(int(datetime.now().timestamp())),))
        data7 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        print(data7)
        print("fetched data"+"\n")
        # r_values = pd.DataFrame(data7, columns=['meterID', 'time_stamp', 'voltage', 'current', 'frequency',
        #                                         'total_harmonic_distortion', 'apparent_energy', 'power_factor',
        #                                         'energy', 'power', 'apparent_power','Current_i1','Current_i2','Current_i3'])
        r_values = pd.DataFrame(data7, columns=['Modbus_time','AVG_voltage_LL','Current_i1','Current_i2','Current_i3','AVG_current','Frequency','AVG_pf','THDP1','Total_kW','Total_net_kWh','Total_kVAr','Total_net_kVArh', 'Total_kVA', 'Total_net_kVAh'])
        r_val = ((r_values).values.tolist())
        print(r_val)
        print("data transferred to html")
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    response4 = make_response(json.dumps(r_val))
    response4.content_type = 'application/json'

    try:
        db = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                     host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                     port="3306")
        db_cursor = db.cursor()
        # stmt1 = "SELECT pf1 from trialbsl WHERE Modbus_time BETWEEN %s AND %s"
        data_allday_yesterday = (yesterday_midnight.timestamp(), midnight.timestamp())
        print(f"yesterday time {str(int((yesterday_midnight.timestamp()*1000)))}")
        # data5_m = Meter_id
        db_cursor.execute("select Total_net_kWh from bokaro_ems.trialbsl where Meter_id = %s and timest between %s and %s" , (Meter_id, str(int((yesterday_midnight.timestamp()*1000) - 500000)), str(int((yesterday_midnight.timestamp()*1000) + 500000)),))
        data8 = db_cursor.fetchall()
        print(data8)

        db_cursor.execute("select Total_net_kWh from bokaro_ems.trialbsl where Meter_id = %s and timest between %s and %s",(Meter_id, str(int((midnight.timestamp()*1000) - 500000)), str(int((midnight.timestamp()*1000) + 500000)),))
        data99 = db_cursor.fetchall()
        print(data99)
        db.commit()
        db.close()
        if (data99 != [] and data8 != []):
            x_values_en = pd.DataFrame(data8)
            print(x_values_en)
            x_val_en = ((x_values_en.T).values.tolist())
            y_en = (x_val_en[0][0])

            x_values_en_99 = pd.DataFrame(data99)
            print(x_values_en_99)
            x_val_en_99 = ((x_values_en_99.T).values.tolist())
            y_en_99 = (x_val_en_99[0][0])

            final_en = y_en_99-y_en
            print(f"yesterday energy{final_en}")
        else:
            final_en = 0
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    response4 = make_response(json.dumps(final_en))
    response4.content_type = 'application/json'

    try:
        db2 = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                      host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                      port="3306")
        db2_cursor = db2.cursor()
        db2_cursor.execute("SELECT Location from locbsl WHERE Meter_id =%s",(Meter_id,))
        data88 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        x_values12 = pd.DataFrame(data88)
        print(x_values12)
        x_val12 = ((x_values12.T).values.tolist())
        timest12 = x_val12[0][0]
        print("test")
        print(type(timest12))
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    response4 = make_response(json.dumps(timest12))
    print(response4)
    response4.content_type = 'application/json'
    return render_template('ems_test_v22.html', data1=(r_val), data2=(final_en), data3=(timest12))
@app.route("/currentdata1", methods=["GET", "POST"])
def currentdata1():
    if not g.user:
        print("session not valid")
        return redirect(url_for('login'))

    print("session valid")
    global Meter_id

    Meter_id = request.form.get("meter_id")
    if (Meter_id==None):
        Meter_id="GMBS C05_08D"
    print(Meter_id)
    print(type(Meter_id))

    try:
        db2 = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                      host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                      port="3306")
        db2_cursor = db2.cursor()
        db2_cursor.execute(
            "SELECT Modbus_time,AVG_voltage_LL,Current_i1,Current_i2,Current_i3,AVG_current,Frequency,AVG_pf,THDP1,Total_kW,Total_net_kWh,Total_kVAr,Total_net_kVArh, Total_kVA, Total_net_kVAh from trialbsl WHERE Meter_id =%s  and timest between %s and %s",
            (Meter_id, str(int(datetime.now().timestamp() - 3000)), str(int(datetime.now().timestamp())),))
        data7 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        print(data7)
        print("fetched data"+"\n")
        # r_values = pd.DataFrame(data7, columns=['meterID', 'time_stamp', 'voltage', 'current', 'frequency',
        #                                         'total_harmonic_distortion', 'apparent_energy', 'power_factor',
        #                                         'energy', 'power', 'apparent_power','Current_i1','Current_i2','Current_i3'])
        r_values = pd.DataFrame(data7, columns=['Modbus_time','AVG_voltage_LL','Current_i1','Current_i2','Current_i3','AVG_current','Frequency','AVG_pf','THDP1','Total_kW','Total_net_kWh','Total_kVAr','Total_net_kVArh', 'Total_kVA', 'Total_net_kVAh'])
        r_val = ((r_values).values.tolist())
        print(r_val)
        print("data transferred to html")
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    response4 = make_response(json.dumps(r_val))
    response4.content_type = 'application/json'

    try:
        db = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                     host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                     port="3306")
        db_cursor = db.cursor()
        # stmt1 = "SELECT pf1 from trialbsl WHERE Modbus_time BETWEEN %s AND %s"
        data_allday_yesterday = (yesterday_midnight.timestamp(), midnight.timestamp())
        print(f"yesterday time {str(int((yesterday_midnight.timestamp()*1000)))}")
        # data5_m = Meter_id
        db_cursor.execute("select Total_net_kWh from bokaro_ems.trialbsl where Meter_id = %s and timest between %s and %s" , (Meter_id, str(int((yesterday_midnight.timestamp()*1000) - 500000)), str(int((yesterday_midnight.timestamp()*1000) + 500000)),))
        data8 = db_cursor.fetchall()
        print(data8)

        db_cursor.execute("select Total_net_kWh from bokaro_ems.trialbsl where Meter_id = %s and timest between %s and %s",(Meter_id, str(int((midnight.timestamp()*1000) - 500000)), str(int((midnight.timestamp()*1000) + 500000)),))
        data99 = db_cursor.fetchall()
        print(data99)
        db.commit()
        db.close()
        if (data99 != [] and data8 != []):
            x_values_en = pd.DataFrame(data8)
            print(x_values_en)
            x_val_en = ((x_values_en.T).values.tolist())
            y_en = (x_val_en[0][0])

            x_values_en_99 = pd.DataFrame(data99)
            print(x_values_en_99)
            x_val_en_99 = ((x_values_en_99.T).values.tolist())
            y_en_99 = (x_val_en_99[0][0])

            final_en = y_en_99-y_en
            print(f"yesterday energy{final_en}")
        else:
            final_en = 0
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    response4 = make_response(json.dumps(final_en))
    response4.content_type = 'application/json'

    try:
        db2 = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                      host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                      port="3306")
        db2_cursor = db2.cursor()
        db2_cursor.execute("SELECT Location from locbsl WHERE Meter_id =%s",(Meter_id,))
        data88 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        x_values12 = pd.DataFrame(data88)
        print(x_values12)
        x_val12 = ((x_values12.T).values.tolist())
        timest12 = x_val12[0][0]
        print("test")
        print(type(timest12))
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    response4 = make_response(json.dumps(timest12))
    print(response4)
    response4.content_type = 'application/json'
    return render_template('meterstatus.html', data1=(r_val), data2=(final_en), data3=(timest12))





@app.route("/getPlotCSV")
def getPlotCSV():
    if not g.user:
        print("session not valid")
        return redirect(url_for('login'))

    print("session valid")
    try:
        db2 = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                      host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                      port="3306")
        db2_cursor = db2.cursor()
        db2_cursor.execute(
            "SELECT Modbus_time,AVG_voltage_LL,Current_i1,Current_i2,Current_i3,AVG_current,Frequency,AVG_pf,THDP1,Total_kW,Total_net_kWh,Total_kVAr,Total_net_kVArh, Total_kVA, Total_net_kVAh from trialbsl WHERE Meter_id =%s  and timest between %s and %s",
            (Meter_id, str(int(datetime.now().timestamp() - 3000)), str(int(datetime.now().timestamp())),))
        data18 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        if (data18!=[]):
            m_values = pd.DataFrame(data18, columns=['Modbus_time','AVG_voltage_LL','Current_i1','Current_i2','Current_i3','AVG_current','Frequency','AVG_pf','THDP1','Total_kW','Total_net_kWh','Total_kVAr','Total_net_kVArh', 'Total_kVA', 'Total_net_kVAh'])
            m_val = ((m_values.T).values.tolist())
            m_value_c = m_val[0][0]
        else:
            data18=[('N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A', 'N/A', 'N/A')]
            m_values = pd.DataFrame(data18, columns=['Modbus_time','AVG_voltage_LL','Current_i1','Current_i2','Current_i3','AVG_current','Frequency','AVG_pf','THDP1','Total_kW','Total_net_kWh','Total_kVAr','Total_net_kVArh', 'Total_kVA', 'Total_net_kVAh'])
            m_val = ((m_values.T).values.tolist())
            m_value_c = m_val[0][0]
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        sensor_data_frame = pd.DataFrame(m_val)
        csv = m_values.to_string(columns=['Modbus_time','AVG_voltage_LL','Current_i1','Current_i2','Current_i3','AVG_current','Frequency','AVG_pf','THDP1','Total_kW','Total_net_kWh','Total_kVAr','Total_net_kVArh', 'Total_kVA', 'Total_net_kVAh'], header='false', index='false')

    return Response(
        m_values.to_csv(index=False),
        mimetype="text/csv",
        headers={"Content-disposition":
                     "attachment; filename = BSL_EMS_meterdata.csv"})


@app.route("/getexcel")  # , methods=["GET","POST"])
def getexcel():
    if not g.user:
        print("session not valid")
        return redirect(url_for('login'))

    print("session valid")
    try:
        db2 = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                      host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                      port="3306")
        db2_cursor = db2.cursor()
        db2_cursor.execute(
            "SELECT Modbus_time,AVG_voltage_LL, AVG_current,THDP1,Total_kVA,AVG_pf,Total_net_kWh,Total_kW,Total_kVA,Frequency,pf1  from trialbsl WHERE Meter_id =%s",
            (Meter_id,))
        data13 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        t_values = pd.DataFrame(data13, columns=['meterID', 'Modbus_time', 'AVG_voltage_LL', 'THDP1', 'frequency',
                                                 'total_harmonic_distortion', 'apparent_energy', 'power_factor',
                                                 'energy', 'power', 'apparent_power'])
        t_val = ((t_values).values.tolist())
        t_value_c = t_val[0][0]
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    response4 = make_response(json.dumps(t_val))
    response4.content_type = 'application/json'
    # return response4
    return render_template("datasheet.html", data=(t_val))


@app.route("/historicaldata", methods=["GET", "POST"])
def historical():
    if not g.user:
        print("session not valid")
        return redirect(url_for('login'))

    print("session valid")
    global start_time
    global end_time
    global meterID_H
    h_val=[]
    data0=[]
    data1 = []
    data2 = []
    data3 = []
    data4 = []
    data5 = []
    data6 = []
    data7 = []
    data8 = []
    data9 = []
    data10 = []
    data11 = []
    data12 = []
    data13 = []
    data14 = []


    h_val_map=[]
    meterID_H = request.form.get("Meter_id")
    print(meterID_H)
    print(type(meterID_H))

    form_timestamp = [request.form.get("daterange")]
    print(form_timestamp)
    print((form_timestamp[0].split(" - ")))

    start_time = str(int(tm.mktime(dtm.datetime.strptime(((form_timestamp[0].split(" - "))[0]), "%d/%m/%Y %H:%M").timetuple()))*1000)
    end_time = str(int(tm.mktime(dtm.datetime.strptime(((form_timestamp[0].split(" - "))[1]), "%d/%m/%Y %H:%M").timetuple()))*1000)

    print (f"{start_time}  {end_time}")
    print(f"{type(start_time)}  {type(end_time)}")

    try:
        db2 = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                      host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                      port="3306")
        db2_cursor = db2.cursor()
        db2_cursor.execute("SELECT Modbus_time,AVG_voltage_LL,Current_i1,Current_i2,Current_i3,AVG_current,Frequency,AVG_pf,THDP1,Total_kW,Total_net_kWh,Total_kVAr,Total_net_kVArh, Total_kVA, Total_net_kVAh,timest from trialbsl WHERE Meter_id =%s and timest between %s and %s",(meterID_H,start_time,end_time,))

        data8 = db2_cursor.fetchall()
        print(data8)
        if(data8!=[]):
            db2.commit()
            db2.close()
            h_values = pd.DataFrame(data8, columns=['Modbus_time','AVG_voltage_LL','Current_i1','Current_i2','Current_i3','AVG_current','Frequency','AVG_pf','THDP1','Total_kW','Total_net_kWh','Total_kVAr','Total_net_kVArh', 'Total_kVA', 'Total_net_kVAh','timest'])

            h_val = ((h_values).values.tolist())

            print(f"test{h_val}")
            h_value_c = h_val[0][0]
            h_val_map = list(map(json.dumps, h_val))
            print(len(h_val))


            data0 = []
            for i in range(1, 2):
                for j in range(len(h_val)):
                    data0.append(h_val[j][i])

            data1 = []  # selecting the list elements
            for i in range(2, 3):
                for j in range(len(h_val)):
                    data1.append(h_val[j][i])

            data2 = []
            for i in range(3, 4):
                for j in range(len(h_val)):
                    data2.append(h_val[j][i])

            data3 = []
            for i in range(4, 5):
                for j in range(len(h_val)):
                    data3.append(h_val[j][i])

            data4 = []
            for i in range(5, 6):
                for j in range(len(h_val)):
                    data4.append(h_val[j][i])

            data5 = []
            for i in range(6, 7):
                for j in range(len(h_val)):
                    data5.append(h_val[j][i])

            data6 = []
            for i in range(7, 8):
                for j in range(len(h_val)):
                    data6.append(h_val[j][i])

            data7 = []
            for i in range(8, 9):
                for j in range(len(h_val)):
                    data7.append(h_val[j][i])

            data8 = []
            for i in range(9, 10):
                for j in range(len(h_val)):
                    data8.append(h_val[j][i])

            data9 = []
            for i in range(10, 11):
                for j in range(len(h_val)):
                    data9.append(h_val[j][i])

            data10 = []
            for i in range(11, 12):
                for j in range(len(h_val)):
                    data10.append(int(h_val[j][i]))

            data11 = []
            for i in range(12, 13):
                for j in range(len(h_val)):
                    data11.append(int(h_val[j][i]))

            data12 = []
            for i in range(13, 14):
                for j in range(len(h_val)):
                    data12.append(int(h_val[j][i]))

            data13 = []
            for i in range(14, 15):
                for j in range(len(h_val)):
                    data13.append(int(h_val[j][i]))

            data14 = []
            for i in range(15, 16):
                for j in range(len(h_val)):
                    data14.append(int(h_val[j][i]))

        else:
            data14=0




    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    response5 = make_response(json.dumps(h_val_map))
    response5.content_type = 'application/json'






    return render_template("historic.html", data=(h_val),data0=(data0), data1=(data1), data2=(data2), data3=(data3),
                           data4=(data4), data5=(data5), data6=(data6), data7=(data7), data8=(data8), data9=(data9), data10=(data10), data11=(data11), data12=(data12), data13=(data13), data14=(data14))


@app.route("/historicdwnld")
def historicdwnld():
    global start_time
    global end_time
    global meterID_H
    t1_val=[]
    t1_values = []

    if not g.user:
        print("session not valid")
        return redirect(url_for('login'))


    print("session valid")
    try:
        db2 = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                      host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                      port="3306")
        db2_cursor = db2.cursor()
        db2_cursor.execute("SELECT Modbus_time,AVG_voltage_LL,Current_i1,Current_i2,Current_i3,AVG_current,Frequency,AVG_pf,THDP1,Total_kVA,Total_kW,Total_kVA,Total_net_kVArh, Total_kVA, Total_net_kVAh  from trialbsl WHERE Meter_id =%s and timest between %s and %s",(meterID_H,start_time,end_time))
        data5 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        print(data5)
        if(data5!=[]):
            t1_values = pd.DataFrame(data5, columns=['Modbus_time','AVG_voltage_LL','Current_i1','Current_i2','Current_i3','AVG_current','Frequency','AVG_pf','THDP1','Total_kVA','Total_kW','Total_kVA','Total_net_kVArh', 'Total_kVA', 'Total_net_kVAh'])
            t1_val = ((t1_values.T).values.tolist())
            t1_value_c = t1_val[0][0]
        else:
            data5=[('N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A')]
            t1_values = pd.DataFrame(data5, columns=['Modbus_time','AVG_voltage_LL','Current_i1','Current_i2','Current_i3','AVG_current','Frequency','AVG_pf','THDP1','Total_kVA','Total_kW','Total_kVA','Total_net_kVArh', 'Total_kVA', 'Total_net_kVAh'])
            t1_val = ((t1_values.T).values.tolist())
            t1_value_c = t1_val[0][0]
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        sensor_data_frame = pd.DataFrame(t1_val)
        csv = t1_values.to_string(columns=['Modbus_time','AVG_voltage_LL','Current_i1','Current_i2','Current_i3','AVG_current','Frequency','AVG_pf','THDP1','Total_kVA','Total_kW','Total_kVA','Total_net_kVArh', 'Total_kVA', 'Total_net_kVAh'], header='false', index='false')

    return Response(
        t1_values.to_csv(index=False),
        mimetype="text/csv",
        headers={"Content-disposition":
                     "attachment; filename = BSL_EMS_historicdata.csv"})


@app.route("/historic")
def historic():
    return render_template('historic.html')


@app.route("/current_data")
def current_data():
    if not g.user:
        print("session not valid")
        return redirect(url_for('login'))

    print("session valid")
    try:
        db2 = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                      host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                      port="3306")
        db2_cursor = db2.cursor()
        db2_cursor.execute(
            "SELECT Modbus_time,AVG_voltage_LL, AVG_current,THDP1,Total_kVA,AVG_pf,Total_net_kWh,Total_kW,Total_kVA,Frequency,pf1  from trialbsl WHERE Meter_id =%s",
            (Meter_id,))
        data7 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        t2_values = pd.DataFrame(data7, columns=['Modbus Time', 'Modbus_time', 'AVG_voltage_LL', 'THDP1', 'frequency',
                                                 'total_harmonic_distortion', 'apparent_energy', 'power_factor',
                                                 'energy', 'power', 'apparent_power'])
        t2_val = ((t2_values).values.tolist())
        t2_value_c = t2_val[0][0]
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    response4 = make_response(json.dumps(t2_val))
    response4.content_type = 'application/json'

    try:
        db = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                     host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                     port="3306")
        db_cursor = db.cursor()
        stmt1 = "SELECT pf1 from trialbsl WHERE Modbus_time BETWEEN %s AND %s"
        data_allday_yesterday = (yesterday_midnight.timestamp(), midnight.timestamp())
        data5_m = Meter_id
        db_cursor.execute(stmt1, data_allday_yesterday)
        data8 = db_cursor.fetchall()
        db.commit()
        db.close()
        print(data8)
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    response4 = make_response(json.dumps(5))
    response4.content_type = 'application/json'

    return render_template('ems_test_v22.html', data1=(t2_val), data2=(data8))


@app.route("/mapping",methods=["GET", "POST"])
def mapping():
    if not g.user:
        print("session not valid")
        return redirect(url_for('login'))
    print("session valid")
    global Meter_id

    Meter_id = request.form.get("meter_id")
    return render_template('mapping.html')
@app.route("/gmbs",methods=["GET", "POST"])
def gmbs():
    if not g.user:
        print("session not valid")
        return redirect(url_for('login'))
    print("session valid")
    global Meter_id

    Meter_id = request.form.get("meter_id")
    return render_template('gmbs.html')
@app.route("/msds",methods=["GET", "POST"])
def msds():
    if not g.user:
        print("session not valid")
        return redirect(url_for('login'))
    print("session valid")
    global Meter_id

    Meter_id = request.form.get("meter_id")
    return render_template('msds.html')

@app.route("/meterstatus",methods=["GET", "POST"])
def meterstatus():
    stm = str(int(datetime.now().timestamp() - 360))
    stme = str(int(datetime.now().timestamp()))



    try:
        db2 = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                      host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                      port="3306")
        db2_cursor = db2.cursor()
        db2_cursor.execute("select AVG_current From trialbsl where Meter_id ='GMBS C03_10D' and timest between %s and %s",(stm,stme,))
                           #"timest between %s and %s",(stm,stme,))
        data2 = db2_cursor.fetchall()

        d1_values = pd.DataFrame(data2)
        a1= ((d1_values.T).values.tolist())
        if(a1!=[]):
            if(a1[0][0]==0.0):
                a1n = 2
            else:
                a1n = 1
        else:
            a1n = 0

    #         print(voltage_ll)
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        print("line92")
    try:


        db2_cursor.execute(
            "select AVG_current From trialbsl where Meter_id ='GMBS C05_08D' and timest between %s and %s",(stm,stme,))
        data2 = db2_cursor.fetchall()

        d1_values = pd.DataFrame(data2)
        a2 = ((d1_values.T).values.tolist())
        print(a2)
        print("test")
        if(a2!=[]):
            if(a2[0][-1]==0.0):
                a2n = 2
            else:
                a2n = 1
        else:
            a2n = 0

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        print("line92")
    try:

        db2_cursor.execute(
            "select AVG_current From trialbsl where Meter_id ='GMBS C06_09D' and timest between %s and %s",(stm,stme,))
        data2 = db2_cursor.fetchall()

        d1_values = pd.DataFrame(data2)
        a3 = ((d1_values.T).values.tolist())
        if(a3!=[]):
            if(a3[0][-1]==0.0):
                a3n = 2
            else:
                a3n = 1
        else:
            a3n = 0

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        print("line92")
    try:

        db2_cursor.execute(
            "select AVG_current From trialbsl where Meter_id ='GMBS C08_16D' and timest between %s and %s",(stm,stme,))
        data2 = db2_cursor.fetchall()

        d1_values = pd.DataFrame(data2)
        a4 = ((d1_values.T).values.tolist())
        if(a4!=[]):
            if(a4[0][-1]==0.0):
                a4n = 2
            else:
                a4n = 1
        else:
            a4n = 0

    #         print(voltage_ll)
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        print("line92")
    try:

        db2_cursor.execute(
            "select AVG_current From trialbsl where Meter_id ='GMBS C09_13D' and timest between %s and %s",(stm,stme,))
        data2 = db2_cursor.fetchall()

        d1_values = pd.DataFrame(data2)
        a5 = ((d1_values.T).values.tolist())
        if(a5!=[]):
            if(a5[0][-1]==0.0):
                a5n = 2
            else:
                a5n = 1
        else:
            a5n = 0

    #         print(voltage_ll)
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        print("line92")
    try:

        db2_cursor.execute(
            "select AVG_current From trialbsl where Meter_id ='GMBS C18_14D' and timest between %s and %s",(stm,stme,))
        data2 = db2_cursor.fetchall()

        d1_values = pd.DataFrame(data2)
        a6 = ((d1_values.T).values.tolist())
        if(a6!=[]):
            if(a6[0][-1]==0.0):
                a6n = 2
            else:
                a6n = 1
        else:
            a6n = 0

    #         print(voltage_ll)
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        print("line92")
    try:

        db2_cursor.execute(
            "select AVG_current From trialbsl where Meter_id ='GMBS C19_17D' and timest between %s and %s",(stm,stme,))
        data2 = db2_cursor.fetchall()

        d1_values = pd.DataFrame(data2)
        a7 = ((d1_values.T).values.tolist())
        if(a7!=[]):
            if(a7[0][-1]==0.0):
                a7n = 2
            else:
                a7n = 1
        else:
            a7n = 0

    #         print(voltage_ll)
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        print("line92")
    try:

        db2_cursor.execute(
            "select AVG_current From trialbsl where Meter_id ='GMBS C20_18D' and timest between %s and %s",(stm,stme,))
        data2 = db2_cursor.fetchall()

        d1_values = pd.DataFrame(data2)
        a8 = ((d1_values.T).values.tolist())
        if(a8!=[]):
            if(a8[0][-1]==0.0):
                a8n = 2
            else:
                a8n = 1
        else:
            a8n = 0

    #         print(voltage_ll)
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        print("line92")
    try:

        db2_cursor.execute("select AVG_current From trialbsl where Meter_id ='GMBS C21_11D' and timest between %s and %s",(stm,stme,))
        data2 = db2_cursor.fetchall()

        d1_values = pd.DataFrame(data2)
        a9 = ((d1_values.T).values.tolist())
        if(a9!=[]):
            if(a9[0][-1]==0.0):
                a9n = 2
            else:
                a9n = 1
        else:
            a9n = 0

    #         print(voltage_ll)
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        print("line92")
    try:

        db2_cursor.execute(
            "select AVG_current From trialbsl where Meter_id ='GMBS C24_12D' and timest between %s and %s",(stm,stme,))
        data2 = db2_cursor.fetchall()

        d1_values = pd.DataFrame(data2)
        a10 = ((d1_values.T).values.tolist())
        if(a10!=[]):
            if(a10[0][-1]==0.0):
                a10n = 2
            else:
                a10n = 1
        else:
            a10n = 0

    #         print(voltage_ll)
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        print("line92")
    try:

        db2_cursor.execute(
            "select AVG_current From trialbsl where Meter_id ='GMBS C27_15D' and timest between %s and %s",(stm,stme,))
        data2 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        d1_values = pd.DataFrame(data2)
        a11 = ((d1_values.T).values.tolist())
        if(a11!=[]):
            if(a11[0][-1]==0.0):
                a11n = 2
            else:
                a11n = 1
        else:
            a11n = 0


    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        print("line92")
    data1 = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11]
    data = [a1n, a2n, a3n, a4n, a5n, a6n, a7n, a8n, a9n, a10n, a11n]
    print(data1)
    print(data)
    print(type(data[1]))

    # data=[xx1(not used),average voltage,avg_current,frequency,xx2(thd),averagepf,activepower,activeenergy,apparentpower,apparent energy]
    response1 = make_response(json.dumps(data))
    response1.content_type = 'application/json'
    return response1



@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print("right req")
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']

        print(users)

        if len([x for x in users if x.username == username]) == 0:
            print("wrong username")
        else:
            user = [x for x in users if x.username == username][0]
            print(user)
            if user and user.password == password:
                session['user_id'] = user.id
                return redirect(url_for('mapping'))

            print("wrong password")
            return redirect(url_for('login'))

    print("wrong req")
    print(url_for('mapping'))
    return render_template('login.html')



@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        print("right req")
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']

        print(users)

        if len([x for x in users if x.username == username]) == 0:
            print("wrong username")
        else:
            user = [x for x in users if x.username == username][0]
            print(user)
            if user and user.password == password:
                session['user_id'] = user.id
                return redirect(url_for('mapping'))

            print("wrong password")
            return redirect(url_for('login'))

    print("wrong req")
    print(url_for('mapping'))
    return render_template('login.html')
if __name__ == "__main__":
    app.run(port=5000, debug=True)
