# coding:utf-8


import sqlite3
import json,os,time



#-------------------------------------------------------------
def listDirFile():
	lists = []
	listDir = os.listdir()

	for lis in listDir:
		if os.path.splitext(lis)[1] == ".json":
			lists.append(lis)
			print("get %s dir"%lis)
	print(r"has %d file 'json'"%len(lists))
	time.sleep(3)
	return lists


#-------------------------------------------------------------
#单个文件插入数据库。
def inputFileDB(fileName):
	with open(fileName,"r",encoding="utf-8") as f:
		#textJson = f.read()
		jt = json.load(f)

	jsonData1 = jt['cubePatentSearchResponse']['documents']
	#-------------------------------------------------------------
	print("get %s has %d patents"%(fileName,len(jsonData1)))
	i = 0
	while i < len(jsonData1):
		jsonData = jsonData1[i]['field_values'] 
		jsonData.setdefault('id')
		jsonData.setdefault('pn')
		jsonData.setdefault('ti')
		jsonData.setdefault('an')
		jsonData.setdefault('pd')
		jsonData.setdefault('ad')
		jsonData.setdefault('pa')
		jsonData.setdefault('in')
		jsonData.setdefault('ls1')
		jsonData.setdefault('ab')
		jsonData.setdefault('apn')
		jsonData.setdefault('apd')
		jsonData.setdefault('ic2')
		jsonData.setdefault('ic1')
		jsonData.setdefault('pr')
		jsonData.setdefault('aa')
		jsonData.setdefault('agc')
		jsonData.setdefault('agt')
		jsonData.setdefault('cty')
		jsonData.setdefault('ls1_2')
		jsonData.setdefault('ls2_1')
		jsonData.setdefault('cpa')
		jsonData.setdefault('type')
		jsonData.setdefault('lsnt')
		jsonData.setdefault('lsn2')
		jsonData.setdefault('lsn1')
		jsonData.setdefault('lset')
		jsonData.setdefault('lse')
		jsonData.setdefault('ain')
		jsonData.setdefault('co')
		jsonData.setdefault('ac')
	#-------------------------------------------------------------
		id = jsonData['id']
		pn = jsonData['pn']
		ti = jsonData['ti']
		an = jsonData['an']
		pd = jsonData['pd']
		ad = jsonData['ad']
		pa = jsonData['pa']
		in1 = jsonData['in']
		ls1 = jsonData['ls1']
		ab = jsonData['ab']
		apn = jsonData['apn']
		apd = jsonData['apd']
		ic2 = jsonData['ic2']
		ic1 = jsonData['ic1']
		pr = jsonData['pr']
		aa = jsonData['aa']
		agc = jsonData['agc']
		agt = jsonData['agt']
		cty = jsonData['cty']
		ls1_2 = jsonData['ls1_2']
		ls2_1 = jsonData['ls2_1']
		cpa = jsonData['cpa']
		type = jsonData['type']
		lsnt = jsonData['lsnt']
		lsn2 = jsonData['lsn2']
		lsn1 = jsonData['lsn1']
		lset = jsonData['lset']
		lse = jsonData['lse']
		ain = jsonData['ain']
		co = jsonData['co']
		ac = jsonData['ac']

		#-------------------------------------------------------------
		#id,pn,ti,an,pd,ad,pa,in,ls1,ab,apn,apd,ic2,ic1,pr,aa,agc,agt,cty,ls1_2,ls2_1,cpa,type,lsnt,lsn2,lsn1,lset,lse,ain,co,ac,
		sqlText = (str(id),str(pn),str(ti),str(an),str(pd),str(ad),str(pa),str(in1),str(ls1),str(ab),str(apn),str(apd),str(ic2),str(ic1),\
			str(pr),str(aa),str(agc),str(agt),str(cty),str(ls1_2),str(ls2_1),str(cpa),str(type),str(lsnt),str(lsn2),str(lsn1),str(lset),\
			str(lse),str(ain),str(co),str(ac))
		c.execute("REPLACE INTO patents VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",sqlText)
		i += 1
		conn.commit()
		print("insert %s sucssful."%i)
		#time.sleep(0.01)
	#-------------------------------------------------------------
#-------------------------------------------------------------
conn = sqlite3.connect("patents.db")
print("with open sucss")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS	patents(id TEXT PRIMARY KEY NOT NULL,pn,ti,an,pd,ad,pa,in1,ls1,ab,apn,apd,ic2,ic1,pr,aa,\
	agc,agt,cty,ls1_2,ls2_1,cpa,type,lsnt,lsn2,lsn1,lset,lse,ain,co,ac)''')
fileList = listDirFile()
for FL in fileList:
	inputFileDB(FL)
	print("finish %s file"%FL)
	print("*"*50)
	time.sleep(3)
conn.close()
print("***Repl Closed***")