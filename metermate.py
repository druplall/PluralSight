import pypyodbc
import os
import shutil
import glob

configuration_file = r"\\Q17001r1\DataDirs\meter shop\Engineering\Field Projects\FieldHHF\MeterandTest\Deo\Metermate_config.txt"
src_fldr = None
dst_fldr = None
db_location = None

if os.path.exists(configuration_file):
    print("Configuration File exist")
    with open(configuration_file) as cf:
        for line in cf:
            if 'Source_Folder:' in line:
                src_fldr = line.split(":", 1)[1]
            if 'Destination_Folder' in line:
                dst_fldr = line.split(":", 1)[1]
            if 'Database_Location' in line:
                db_location = line.split(":", 1)[1]
else:
    print("Configuration File does not exist")

# Create connection
try:
    con = pypyodbc.connect(
        'DRIVER={Microsoft Access Driver (*.mdb)};UID=admin;UserCommitSync=Yes;Threads=3;SafeTransactions=0;PageTimeout=5;MaxScanRows=8;MaxBufferSize=2048;{FIL=MS Access};DriverId=25;DefaultDir=C:/Users/Deodat/Desktop/Metermate v2/Database/metermateDB.mdb;DBQ=C:/Users/Deodat/Desktop/Metermate v2/Database/metermateDB.mdb;')
    cursor = con.cursor()
    updateCursor = con.cursor()

    global timestamp, status, meter_stat, HW, FW, ID, SN, ER, CA, Prog, ovr_code, prog_status1, prog_status2, prog_status3, SM, ST
    src_fldr = r"C:\Users\Deodat\Desktop\Metermate v2\Source_Folder"  ## Edit this
    dst_fldr = r"C:\Users\Deodat\Desktop\Metermate v2\Destination_Folder"  ## Edit this

    # with open("C:/Users/Deodat/Desktop/Metermate_v1.0/Database/Input/log-file-Comm.txt") as f:
    for txt_file in glob.glob(src_fldr + "\\*Comm*.txt"):
        with open(txt_file) as f:
            for line in f:
                var_condition = 1
                # Find the index of the 'Configure Meter'
                if 'Configure Meter' in line and 'Configure Meter ID' not in line:
                    timestamp = line[0:14]
                    timestamp.replace(" ", "")
                    int(timestamp)
                    status = line.split("\t", 1)[1]
                    # print(timestamp)
                if 'Read Meter' in line:
                    timestamp = line[0:14]
                    timestamp.replace(" ", "")
                    int(timestamp)
                    status = line.split("\t", 1)[1]
                    # print(timestamp)
                if 'Meter:' in line:
                    meter_stat = line.split(":", 1)[1]
                    # print(meter)
                if 'HW:' in line:
                    HW = line.split(":", 1)[1]
                    if 'N/A' in HW:
                        HW = 0
                    # print(HW)
                if 'FW:' in line:
                    FW = line.split(":", 1)[1]
                    if 'N/A' in FW:
                        FW = 0
                    # print(FW)
                if 'ID:' in line:
                    ID = line.split(":", 1)[1]
                    if 'N/A' in ID:
                        ID = 0
                    int(ID)
                    # print(ID)
                if 'SN:' in line:
                    SN = line.split(":", 1)[1]
                    if 'N/A' in SN or '   ' in SN:
                        SN = 0
                    int(SN)
                    # print(SN)
                if 'ER:' in line:
                    ER = line.split(":", 1)[1]
                    int(ER)
                    # print(ER)
                if 'CA:' in line:
                    CA = line.split(":", 1)[1]
                    int(CA)
                    # print(CA)
                if 'Full Program' in line:
                    Prog = line.split(":", 1)[1]
                    # print(Prog)
                if 'Ovr:' in line:
                    ovr_code = line.split(":", 2)[2]
                if 'Disable Manual' in line or 'Disable Extended' in line:
                    prog_status1 = line.split(":", 1)[1]
                    # print(prog_status1)
                if 'Disable Extended' in line or 'Disable Manual' in line:
                    prog_status2 = line.split(":", 1)[1]
                    # print(prog_status2)
                if 'kV2c' in line or 'I201' in line:
                    prog_status3 = line.split(":", 1)[1]
                    # print(prog_status1)
                if 'Full Meter Configuration successful' in line:
                    SM = line.split(":", 1)[1]
                    var_condition = 2
                    # print(var_condition)
                if 'Full Meter Read successful' in line:
                    SM = line.split(":", 1)[1]
                    ST = 0
                    var_condition = 3
                    # print(var_condition)
                if 'ST' in line:
                    ST = line.split(":", 1)[1]
                    # print(ST)
                if var_condition == 2:  # if true only insert data
                    cursor.execute("Select TimeStamp FROM ProgramData_ConfigureMeter WHERE TimeStamp = ?", (timestamp,))
                    row = cursor.fetchone()
                    if row is not None:  # If the timestamp is found do an update
                        while row is not None:
                            updateCursor.execute(
                                "UPDATE ProgramData_ConfigureMeter SET Status = ?, MeterType = ?, HW = ?, FW = ?, ID = ?, SN = ? , ER = ? , CA = ? WHERE TimeStamp = ?",
                                (status, meter_stat, HW, FW, ID, SN, ER, CA, timestamp))
                            row = cursor.fetchone()
                        updateCursor.commit()
                    else:  # if it is not found insert into the table
                        sql = "Insert into ProgramData_ConfigureMeter ([Timestamp],Status,MeterType,HW,FW,ID,SN,ER,CA,Program,Ovr,ProgramStatus_1,ProgramStatus_2,ProgramStatus_3,SM,ST) " \
                              "values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
                              % (timestamp, status, meter_stat, HW, FW, ID, SN, ER, CA, Prog, ovr_code, prog_status1,
                                 prog_status2, prog_status3, SM, ST)
                        cursor.execute(sql)
                        cursor.commit()

                if var_condition == 3:
                    cursor.execute("Select TimeStamp FROM ProgramData_ReadMeter WHERE TimeStamp = ?", (timestamp,))
                    row = cursor.fetchone()
                    if row is not None:  # If the timestamp is found do an update
                        while row is not None:
                            updateCursor.execute(
                                "UPDATE ProgramData_ReadMeter SET Status = ?, MeterType = ?, HW = ?, FW = ?, ID = ?, SN = ? , ER = ? , CA = ? WHERE TimeStamp = ?",
                                (status, meter_stat, HW, FW, ID, SN, ER, CA, timestamp))
                            row = cursor.fetchone()
                        updateCursor.commit()
                    else:  # if it is not found insert into the table
                        sql = "Insert into ProgramData_ReadMeter ([Timestamp],Status,MeterType,HW,FW,ID,SN,ER,CA,SM,ST) " \
                              "values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
                              % (timestamp, status, meter_stat, HW, FW, ID, SN, ER, CA, SM, ST)
                        cursor.execute(sql)
                        cursor.commit()

        shutil.copy(txt_file, dst_fldr)
        os.remove(txt_file)
        print('Moving Files from: ' + src_fldr + ' to location: ' + dst_fldr)
        # cursor.execute("SELECT * FROM ProgramData")
    # for row in cursor.fetchall():
    #     print(row)

    cursor.close()
    con.close()

except pyodbc.Error as ex:
    print(ex)

