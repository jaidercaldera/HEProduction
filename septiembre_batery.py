# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 15:13:46 2020

@author: ALEJANDRO
"""


from pyomo.environ import *

ini={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0,24:0}

LimImp={1:155,2:155,3:160,4:200,5:208,6:210,7:102.87,8:0,9:0,10:0,11:0
,12:0,13:0,14:0,15:0,16:0,17:238.29,18:600.43,19:880,20:880,21:800,22:600
,23:250,24:250}








LimExp={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:129.83,9:438.86,10:665.91,11:837.89,12:863.13,13:922.01,14:717.15,15:452.72,16:118.27,
         17:0,18:0,19:0,20:0,21:0,22:0,23:0,24:0}

model = ConcreteModel()

#definicion de variables

model.tempo= Set(initialize=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])

model.Pload=Param(model.tempo, initialize={1:155,2:155,3:160,4:200,5:208,6:210,7:225,8:230
,9:232,10:220,11:230,12:260,13:240,14:310,15:400,16:505,17:600,18:700,19:880,20:880,21:800,22:600,23:250,24:250})



model.Ppv=Param(model.tempo, initialize={1:0,2:0,3:0,4:0,5:0,6:0,7:122.13,8:359.83,9:670.86,10:885.91,11:1067.89,12:1123.13,13:1162.01,
                                         14:1027.15,15:852.72,16:623.27,17:361.71,18:99.57,19:0,20:0,21:0,22:0,23:0,24:0})





model.Prem=Param(model.tempo, initialize={1:-155,2:-155,3:-160,4:-200,5:-208,6:-210
,7:-102.87,8:129.83,9:438.86,10:665.91,11:837.89
,12:863.13,13:922.01,14:717.15,15:452.72,16:118.27
,17:-238.29,18:-600.43,19:-880,20:-880,21:-800,22:-600,23:-250,24:-250})







model.Expt=Var(model.tempo)
model.Pgrid=Var(model.tempo) 

def f(model, i):
   return (ini[i], LimExp[i])
model.Exp2 = Var(model.tempo, bounds=f,doc=' Var Exportacion_2')


def f(model, i):
   return (ini[i], LimImp[i])
model.Exp1 = Var(model.tempo, bounds=f,doc=' Var Exportacion_1')

def f(model, i):
   return (ini[i], LimImp[i])
model.Imp = Var(model.tempo, bounds=f, doc=' Var Importacion')
#------------------------------------------------------------------------------
#variables de la bateria plomo acido GAMS

SOC0=800
Socmax=3420
ata_c=0.95
eta_d=0.9

model.Socbat=Var(model.tempo, bounds=(684,3420), doc=' Socmin y Socmax Bateria')
model.Pcbat=Var(model.tempo,bounds=(0,3078), doc=' Pcarga bateria' )
model.Pdbat=Var(model.tempo,bounds=(0,3078), doc=' Pdescarga bateria' )


#variables binbaria  de la bateria plomo acido
model.Idbat=Var(model.tempo, within=Binary, doc=' variable descarga bateria plomo acido')
model.Icbat=Var(model.tempo, within=Binary, doc=' variable carga bateria plomo acido')
#------------------------------------------------------------------------------


#   ecuacion balance(t)..        Prem(t)=e=Pgrid(t)+Pc(t)-Pd(t);  
def c_init0(model,i):
    return model.Expt[i]==model.Exp2[i]+model.Exp1[i]
model.cond0= Constraint(model.tempo,rule=c_init0)

def c_init01(model,i):
    return model.Pgrid[i]==model.Expt[i]-model.Imp[i]
model.cond01= Constraint(model.tempo,rule=c_init01,doc=' Pgrid')

def c_init02(model,i):
    return model.Exp1[i]<=model.Exp2[i]
model.cond02= Constraint(model.tempo,rule=c_init02,doc=' Pgrid')


def c_init1(model,i):
    return model.Prem[i]==model.Pgrid[i]+model.Pcbat[i]-model.Pdbat[i]
model.cond1= Constraint(model.tempo,rule=c_init1)

#restriciones de la bateria plomo acido

#ecuacion3(t)..      Pc(t)=l= 0.9*SOCmax*Icba(t);
def c_init2(model,i):
    return model.Pcbat[i]<=0.9*Socmax*model.Icbat[i]
model.cond2= Constraint(model.tempo,rule=c_init2)


#ecuacion4(t)..      Pd(t)=l= 0.9*SOCmax*Idba(t);
def c_init3(model,i):
    return model.Pdbat[i]<=0.9*Socmax*model.Idbat[i]
model.cond3= Constraint(model.tempo,rule=c_init3)


#ecuacion5(t)..      (1-Icba(t))+(1-Idba(t))=e=1;
def c_init4(model,i):
    return   (1-model.Icbat[i])+(1-model.Idbat[i])==1
    # return model.Icbat[i]+model.Idbat[i]<=1
model.cond4= Constraint(model.tempo,rule=c_init4)
#------------------------------------------------------------------------------
#restriciones SOC bateria

model.cond5= Constraint(expr=model.Socbat[1]==SOC0+(model.Pcbat[1]*ata_c)-(model.Pdbat[1]/eta_d))

model.cond6= Constraint(expr=model.Socbat[2]==model.Socbat[1]+(model.Pcbat[2]*ata_c)-(model.Pdbat[2]/eta_d))

model.cond7= Constraint(expr=model.Socbat[3]==model.Socbat[2]+(model.Pcbat[3]*ata_c)-(model.Pdbat[3]/eta_d))

model.cond8= Constraint(expr=model.Socbat[4]==model.Socbat[3]+(model.Pcbat[4]*ata_c)-(model.Pdbat[4]/eta_d))

model.cond9= Constraint(expr=model.Socbat[5]==model.Socbat[4]+(model.Pcbat[5]*ata_c)-(model.Pdbat[5]/eta_d))

model.cond10= Constraint(expr=model.Socbat[6]==model.Socbat[5]+(model.Pcbat[6]*ata_c)-(model.Pdbat[6]/eta_d))

model.cond11= Constraint(expr=model.Socbat[7]==model.Socbat[6]+(model.Pcbat[7]*ata_c)-(model.Pdbat[7]/eta_d))

model.cond12= Constraint(expr=model.Socbat[8]==model.Socbat[7]+(model.Pcbat[8]*ata_c)-(model.Pdbat[8]/eta_d))

model.cond13= Constraint(expr=model.Socbat[9]==model.Socbat[8]+(model.Pcbat[9]*ata_c)-(model.Pdbat[9]/eta_d))
 
model.cond14= Constraint(expr=model.Socbat[10]==model.Socbat[9]+(model.Pcbat[10]*ata_c)-(model.Pdbat[10]/eta_d))

model.cond15= Constraint(expr=model.Socbat[11]==model.Socbat[10]+(model.Pcbat[11]*ata_c)-(model.Pdbat[11]/eta_d))
 
model.cond16= Constraint(expr=model.Socbat[12]==model.Socbat[11]+(model.Pcbat[12]*ata_c)-(model.Pdbat[12]/eta_d))

model.cond17= Constraint(expr=model.Socbat[13]==model.Socbat[12]+(model.Pcbat[13]*ata_c)-(model.Pdbat[13]/eta_d))

model.cond18= Constraint(expr=model.Socbat[14]==model.Socbat[13]+(model.Pcbat[14]*ata_c)-(model.Pdbat[14]/eta_d))

model.cond19= Constraint(expr=model.Socbat[15]==model.Socbat[14]+(model.Pcbat[15]*ata_c)-(model.Pdbat[15]/eta_d))

model.cond20= Constraint(expr=model.Socbat[16]==model.Socbat[15]+(model.Pcbat[16]*ata_c)-(model.Pdbat[16]/eta_d))

model.cond21= Constraint(expr=model.Socbat[17]==model.Socbat[16]+(model.Pcbat[17]*ata_c)-(model.Pdbat[17]/eta_d))

model.cond22= Constraint(expr=model.Socbat[18]==model.Socbat[17]+(model.Pcbat[18]*ata_c)-(model.Pdbat[18]/eta_d))

model.cond23= Constraint(expr= model.Socbat[19]==model.Socbat[18]+(model.Pcbat[19]*ata_c)-(model.Pdbat[19]/eta_d))     

model.cond24= Constraint(expr= model.Socbat[20]==model.Socbat[19]+(model.Pcbat[20]*ata_c)-(model.Pdbat[20]/eta_d))  

model.cond25= Constraint(expr= model.Socbat[21]==model.Socbat[20]+(model.Pcbat[21]*ata_c)-(model.Pdbat[21]/eta_d))  

model.cond26= Constraint(expr= model.Socbat[22]==model.Socbat[21]+(model.Pcbat[22]*ata_c)-(model.Pdbat[22]/eta_d))  

model.cond27= Constraint(expr= model.Socbat[23]==model.Socbat[22]+(model.Pcbat[23]*ata_c)-(model.Pdbat[23]/eta_d))  

model.cond28= Constraint(expr= model.Socbat[24]==model.Socbat[23]+(model.Pcbat[24]*ata_c)-(model.Pdbat[24]/eta_d))

model.cond29= Constraint(expr= model.Socbat[24]==800)
#-----------------------------------------------------------------------------

# funcion objetivo
#  Cu/0.4234/,C /0.060/,D /0.159/;    
Cu=0.4234
C=0.060
D=0.159
model.value = Objective(expr = sum( (Socmax-model.Socbat[i])*0.1*Cu for i in model.tempo)+sum((model.Exp1[i]-model.Imp[i])*Cu-(model.Exp1[i]*C)+(model.Exp2[i]*D) for i in model.tempo),sense = minimize )
#-----------------------------------------------------------------------------

def pyomo_postprocess(options=None, instance=None, results=None):
    model.Prem.display()


opt = SolverFactory('glpk')
result_obj = opt.solve(model, tee=True)
model.display()

