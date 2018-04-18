class SV:
	MSSV=""
	Hoten=""
	Khoa=""
	def __init__(self,MSSV,Hoten,Khoa):
		self.MSSV=MSSV
		self.Hoten=Hoten
		self.Khoa=Khoa
	def toString(self):
		print(self.MSSV,self.Hoten,self.Khoa)
	def getMSSV(self):
		return self.MSSV
	def getHoten(self):
		return self.Hoten
	def getKhoa(self):
		return self.Khoa
class KH:
	Makhoa=""
	Tenkhoa=""
	def __init__(self,Makhoa,Tenkhoa):
		self.Makhoa=Makhoa
		self.Tenkhoa=Tenkhoa
	def toString(self):
		print(self.Makhoa,self.Tenkhoa)
	def getMakhoa(self):
		return self.Makhoa
	def getTenkhoa(self):
		return self.Tenkhoa

a=[]
a.append(SV(001,'Mai A',57))
a.append(SV(002,'Tran b',58))
a.append(SV(003,'Le C',57))
a.append(SV(004,'Phan D',58))
a.append(SV(005,'Ngo A',59))
for i in a:
	i.toString()
b=[]
b.append(KH(56,'Khoa 56 CNTT'))
b.append(KH(57,'Khoa 57 CNTT'))
b.append(KH(58,'Khoa 58 CNTT'))
b.append(KH(59,'Khoa 59 CNTT'))
for i in a:
	if(i.getKhoa() == 57):
		i.toString()
