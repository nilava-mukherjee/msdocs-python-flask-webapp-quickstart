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


@app.route('/data', methods=["GET", "POST"])
def data():
    print("session valid line no 74")
    global Meter_id
    ok2 = "line72"
    print(ok2)
    print(Meter_id)
    try:
        db2 = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                      host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                      port="3306")
        db2_cursor = db2.cursor()
        db2_cursor.execute("SELECT AVG_voltage_LL from trialbsl WHERE Meter_id =%s", (Meter_id,))
        data2 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        d1_values = pd.DataFrame(data2)
        d1_val = ((d1_values.T).values.tolist())
        voltage_ll = d1_val[-1][-1]
    #         print(voltage_ll)
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        print("line92")
    try:
        db2 = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                      host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                      port="3306")
        db2_cursor = db2.cursor()
        db2_cursor.execute("SELECT AVG_current from trialbsl WHERE Meter_id =%s", (Meter_id,))
        data2 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        d2_values = pd.DataFrame(data2)
        d2_val = ((d2_values.T).values.tolist())
        avg_current = d2_val[-1][-1]
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    try:
        db2 = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                      host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                      port="3306")
        db2_cursor = db2.cursor()
        db2_cursor.execute("SELECT Frequency from trialbsl WHERE Meter_id =%s", (Meter_id,))
        data3 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        z_values = pd.DataFrame(data3)
        z_val = ((z_values.T).values.tolist())
        frequency = z_val[-1][-1]
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    try:
        db2 = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                      host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                      port="3306")
        db2_cursor = db2.cursor()
        db2_cursor.execute("SELECT THDP1 from trialbsl WHERE Meter_id =%s", (Meter_id,))
        data4 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        a_values = pd.DataFrame(data4)
        a_val = ((a_values.T).values.tolist())
        THDP1 = a_val[-1][-1]
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    try:
        db2 = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                      host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                      port="3306")
        db2_cursor = db2.cursor()
        db2_cursor.execute("SELECT Total_kVA from trialbsl WHERE Meter_id =%s", (Meter_id,))
        data11 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        x_values = pd.DataFrame(data11)
        x_val = ((x_values.T).values.tolist())
        apparentlocation = x_val[-1][-1]
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    try:
        db2 = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                      host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                      port="3306")
        db2_cursor = db2.cursor()
        db2_cursor.execute("SELECT AVG_pf from trialbsl WHERE Meter_id =%s", (Meter_id,))
        data12 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        x_values = pd.DataFrame(data12)
        x_val = ((x_values.T).values.tolist())
        average_pf = x_val[-1][-1]
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    try:
        db2 = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                      host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                      port="3306")
        db2_cursor = db2.cursor()
        db2_cursor.execute("SELECT Total_kw from trialbsl WHERE Meter_id =%s", (Meter_id,))
        data18 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        x_values = pd.DataFrame(data18)
        x_val = ((x_values.T).values.tolist())
        net_power = x_val[-1][-1]
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    try:
        db2 = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                      host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                      port="3306")
        db2_cursor = db2.cursor()
        db2_cursor.execute("SELECT Total_net_kWh from trialbsl WHERE Meter_id =%s", (Meter_id,))
        data19 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        x_values = pd.DataFrame(data19)
        net_energy = x_val[-1][-1]
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    try:
        db2 = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                      host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                      port="3306")
        db2_cursor = db2.cursor()
        db2_cursor.execute("SELECT Total_kVA from trialbsl WHERE Meter_id =%s", (Meter_id,))
        data20 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        x_values = pd.DataFrame(data20)
        x_val = ((x_values.T).values.tolist())
        apparent_power = x_val[-1][-1]
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    try:
        db2 = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                      host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                      port="3306")
        db2_cursor = db2.cursor()
        db2_cursor.execute("SELECT Total_net_kVAh from trialbsl WHERE Meter_id =%s", (Meter_id,))
        data21 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        x_values = pd.DataFrame(data21)
        x_val = ((x_values.T).values.tolist())
        apparent_energy = x_val[-1][-1]
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    try:
        db2 = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                      host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                      port="3306")
        db2_cursor = db2.cursor()
        db2_cursor.execute("SELECT Modbus_time from trialbsl WHERE Meter_id =%s", (Meter_id,))
        data22 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        x_values = pd.DataFrame(data22)
        x_val = ((x_values.T).values.tolist())
        modbus_time = x_val[-1][-1]
        print(f"modbustime {modbus_time}")
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    try:
        db2 = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                          host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                          port="3306")
        db2_cursor = db2.cursor()
        db2_cursor.execute("SELECT Current_i1 from trialbsl WHERE Meter_id =%s", (Meter_id,))
        data54 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        x_values = pd.DataFrame(data54)
        x_val = ((x_values.T).values.tolist())
        Current_i1 = x_val[-1][-1]
        print(Current_i1)
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    try:
            db2 = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                          host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                          port="3306")
            db2_cursor = db2.cursor()
            db2_cursor.execute("SELECT Current_i2 from trialbsl WHERE Meter_id =%s", (Meter_id,))
            data55 = db2_cursor.fetchall()
            db2.commit()
            db2.close()
            x_values = pd.DataFrame(data55)
            x_val = ((x_values.T).values.tolist())
            Current_i2 = x_val[-1][-1]
            print(Current_i2)
    except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
    try:
        db2 = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                      host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                      port="3306")
        db2_cursor = db2.cursor()
        db2_cursor.execute("SELECT Current_i3 from trialbsl WHERE Meter_id =%s", (Meter_id,))
        data56 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        x_values = pd.DataFrame(data56)
        x_val = ((x_values.T).values.tolist())
        Current_i3 = x_val[-1][-1]
        print(Current_i3)
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    try:
        db2 = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                          host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                          port="3306")
        db2_cursor = db2.cursor()
        db2_cursor.execute("SELECT timest from trialbsl WHERE Meter_id =%s", (Meter_id,))
        data57 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        x_values = pd.DataFrame(data57)
        x_val = ((x_values.T).values.tolist())
        timest = x_val[-1][-1]
        print(timest)
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    meter_info = str(request.form.get("meter_id"))
    # print(type(meter_info))
    data = [modbus_time, voltage_ll, avg_current, frequency, Meter_id, average_pf, net_power, net_energy, apparent_power,
            apparent_energy, THDP1, meter_info,Current_i1,Current_i2,Current_i3,timest]
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
    print(Meter_id)
    print(type(Meter_id))

    try:
        db2 = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                      host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                      port="3306")
        db2_cursor = db2.cursor()
        db2_cursor.execute(
            "SELECT Modbus_time,AVG_voltage_LL,AVG_current,THDP1,Total_kVA,AVG_pf,Total_net_kWh,Total_kW,Total_kVA,Frequency,pf1,Current_i1,Current_i2,Current_i3,timest from trialbsl WHERE Meter_id =%s",
            (Meter_id,))
        data7 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        print(data7)
        print("fetched data"+"\n")
        # r_values = pd.DataFrame(data7, columns=['meterID', 'time_stamp', 'voltage', 'current', 'frequency',
        #                                         'total_harmonic_distortion', 'apparent_energy', 'power_factor',
        #                                         'energy', 'power', 'apparent_power','Current_i1','Current_i2','Current_i3'])
        r_values = pd.DataFrame(data7, columns=['time_stamp', 'voltage', 'current','total_harmonic_distortion',
                                                 'apparent_energy', 'power_factor',
                                                'energy', 'power', 'apparent_power','frequency','power_factor_1','Current_i1','Current_i2','Current_i3','tstmp'])
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
        print(f"yesterday time {str(int(yesterday_midnight.timestamp() - 500))}")
        # data5_m = Meter_id
        db_cursor.execute("select Total_net_kWh from bokaro_ems.trialbsl where Meter_id = %s and timest between %s and %s" , (Meter_id, str(int(yesterday_midnight.timestamp() - 500)), str(int(yesterday_midnight.timestamp() + 500)),))
        data8 = db_cursor.fetchall()
        print(data8)

        db_cursor.execute("select Total_net_kWh from bokaro_ems.trialbsl where Meter_id = %s and timest between %s and %s",(Meter_id, str(int(midnight.timestamp() - 500)), str(int(midnight.timestamp() + 500)),))
        data99 = db_cursor.fetchall()
        print(data99)


        db.commit()
        db.close()

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
            "SELECT Modbus_time,AVG_voltage_LL,AVG_current,THDP1,Total_kVA,AVG_pf,Total_net_kWh,Total_kW,Total_kVA,Frequency,pf1  from trialbsl WHERE Meter_id =%s",
            (Meter_id,))
        data18 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        m_values = pd.DataFrame(data18, columns=['meterID', 'Modbus_time', 'AVG_voltage_LL', 'THDP1', 'frequency',
                                                 'total_harmonic_distortion', 'apparent_energy', 'power_factor',
                                                 'energy', 'power', 'apparent_power'])
        m_val = ((m_values.T).values.tolist())
        m_value_c = m_val[0][0]
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        sensor_data_frame = pd.DataFrame(m_val)
        csv = m_values.to_string(columns=['meterID', 'Modbus_time', 'AVG_voltage_LL', 'THDP1', 'frequency',
                                          'total_harmonic_distortion', 'apparent_energy', 'power_factor',
                                          'energy', 'power', 'apparent_power'], header='false', index='false')

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
    global meterID_H
    meterID_H = request.form.get("Meter_id")
    print(meterID_H)
    print(type(meterID_H))

    form_timestamp = [request.form.get("daterange")]
    print(form_timestamp)
    print(type(form_timestamp[0]))

    start_time = str(int(tm.mktime(dtm.datetime.strptime(((form_timestamp[0].split(" - "))[0]), "%d/%m/%Y %H:%M").timetuple())))
    end_time = str(int(tm.mktime(dtm.datetime.strptime(((form_timestamp[0].split(" - "))[1]), "%d/%m/%Y %H:%M").timetuple())))

    print (f"{start_time}  {end_time}")
    print(f"{type(start_time)}  {type(end_time)}")

    try:
        db2 = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA",
                                      host="server050641860.mysql.database.azure.com", database="bokaro_ems",
                                      port="3306")
        db2_cursor = db2.cursor()
        db2_cursor.execute(
            "SELECT Modbus_time,AVG_voltage_LL, AVG_current,THDP1,Total_kVA,AVG_pf,Total_net_kWh,Total_kW,Total_kVA,Frequency,pf1,timest  from trialbsl WHERE Meter_id =%s and timest between %s and %s",
            (Meter_id,start_time,end_time,))
        data8 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        h_values = pd.DataFrame(data8, columns=['Modbus_time', 'AVG_voltage_LL', 'AVG_current','THDP1','Total_kVA','AVG_pf','Total_net_kWh','Total_kW','Total_kVA','Frequency','pf1',"timest"])

        h_val = ((h_values).values.tolist())
        h_value_c = h_val[0][0]
        h_val_map = list(map(json.dumps, h_val))
        print(len(h_val))

        data0x = []
        for i in range(11, 12):
            for j in range(len(h_val)):
                data0x.append(int(h_val[j][i]))

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


    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    response5 = make_response(json.dumps(h_val_map))
    response5.content_type = 'application/json'
    print(data9)
    print(data0)
    print(data0x[0])

    print(type(data0))
    print(type(data0[0]))





    return render_template("historic.html", data=(h_val),data0=(data0), data1=(data1), data2=(data2), data3=(data3),
                           data4=(data4), data5=(data5), data6=(data6), data7=(data7), data8=(data8), data9=(data9), data0x=(data0x))


@app.route("/historicdwnld")
def historicdwnld():
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
        data5 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        t1_values = pd.DataFrame(data5, columns=['meterID', 'Modbus_time', 'AVG_voltage_LL', 'current', 'frequency',
                                                 'total_harmonic_distortion', 'apparent_energy', 'power_factor',
                                                 'energy', 'power', 'apparent_power'])
        t1_val = ((t1_values.T).values.tolist())
        t1_value_c = t1_val[0][0]
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        sensor_data_frame = pd.DataFrame(t1_val)
        csv = t1_values.to_string(columns=['meterID', 'Modbus_time', 'AVG_voltage_LL', 'THDP1', 'frequency',
                                           'total_harmonic_distortion', 'apparent_energy', 'power_factor',
                                           'energy', 'power', 'apparent_power'], header='false', index='false')

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


@app.route("/mapping")
def mapping():
    if not g.user:
        print("session not valid")
        return redirect(url_for('login'))
    print("session valid")
    return render_template('mapping.html')


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


if __name__ == "__main__":
    app.run(port=5000, debug=True)

