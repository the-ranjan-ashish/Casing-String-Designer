import pandas as pd
df=pd.read_csv(r'C:\Users\ashis\OneDrive\Desktop\Casing 7 Inch.csv')
D=8000 #Depth
d=12 #Density of mud
x=0.5 #Formation Pressure Gradient
Pf=D*x
Ph=0.052*1.125*d*D #Hydrostatic Pressure
B=1-d/65.4 #Buoyancy Factor
df_new=df[df['Pb']>Pf]
# First String
df_new2=df_new[df_new['Pc']>Ph]
w1=df_new2.loc[df_new2['Pc'].idxmin()]['w']
Pc1=df_new2.loc[df_new2['Pc'].idxmin()]['Pc'] 
CasingPipe1=df_new2.loc[df_new2['Pc'].idxmin()]['Casing Pipe']
Ls1=D


#Second String
df_new2=df_new[df_new['Pc']<Pc1]
Pc2=df_new2.loc[df_new2['Pc'].idxmax()]['Pc']
w2=df_new2.loc[df_new2['Pc'].idxmax()]['w']
K2=df_new2.loc[df_new2['Pc'].idxmax()]['K']
Fj2=df_new2.loc[df_new2['Pc'].idxmax()]['Fj'] 
CasingPipe2=df_new2.loc[df_new2['Pc'].idxmax()]['Casing Pipe']
Ls2=(Pc2/(0.052*1.125*d))
W1=(w1*B*(D-Ls2))
Pcc2=(Pc2/K2)*((K2**2-3*W1**2)**0.5-W1)
Ls2_new=Pcc2/(0.052*1.125*d)
while Ls2-Ls2_new>=5:
    Ls2=Ls2_new
    W1=w1*B*(8000-Ls2)
    Pcc2=(Pc2/K2)*((K2**2-3*W1**2)**0.5-W1)
    Ls2_new=Pcc2/(0.052*1.125*12)
Ls2=round(Ls2_new)
while Ls2%5!=0:
    Ls2+=1 


#Third String
LM2=((Fj2/2)-W1)/(w2*B)
df_new2=df_new[df_new['Pc']<Pc2]
if df_new2.shape[0]!=0 and LM2>Ls2:
    Pc3=df_new2.loc[df_new2['Pc'].idxmax()]['Pc']
    w3=df_new2.loc[df_new2['Pc'].idxmax()]['w']
    K3=df_new2.loc[df_new2['Pc'].idxmax()]['K']
    Fj3=df_new2.loc[df_new2['Pc'].idxmax()]['Fj']
    CasingPipe3=df_new2.loc[df_new2['Pc'].idxmax()]['Casing Pipe']
    Ls3=(Pc3/(0.052*1.125*d))
    W2=((W1+w2*B*(Ls2-Ls3)))
    Pcc3=(Pc3/K3)*((K3**2-3*W2**2)**0.5-W2)
    Ls3_new=Pcc3/(0.052*1.125*12)
    while Ls3-Ls3_new>=5:
        Ls3=Ls3_new
        W2=(W1+w2*B*(Ls2-Ls3))
        Pcc3=(Pc3/K3)*((K3**2-3*W2**2)**0.5-W2)
        Ls3_new=Pcc3/(0.052*1.125*d)
    Ls3=round(Ls3_new)
    while Ls3%5!=0:
        Ls3+=1 
    LM3=((Fj3/2)-W2)/(w3*B)
    
    
    #Fouth String
    df_new2=df_new[df_new['Pc']<Pc3]
    if df_new2.shape[0]!=0 and LM3>Ls3:
        Pc4=df_new2.loc[df_new2['Pc'].idxmax()]['Pc']
        w4=df_new2.loc[df_new2['Pc'].idxmax()]['w']
        K4=df_new2.loc[df_new2['Pc'].idxmax()]['K']
        Fj4=df_new2.loc[df_new2['Fj'].idxmax()]['Fj']
        CasingPipe4=df_new2.loc[df_new2['Pc'].idxmax()]['Casing Pipe']
        Ls4=(Pc4/(0.052*1.125*d))
        W3=((W2+w3*B*(Ls3-Ls4)))
        Pcc4=(Pc4/K4)*((K4**2-3*W3**2)**0.5-W3)
        Ls4_new=Pcc4/(0.052*1.125*d)
        while Ls4-Ls4_new>=5:
            Ls4=Ls4_new
            W3=(W2+w3*B*(Ls3-Ls4))
            Pcc4=(Pc4/K4)*((K4**2-3*W3**2)**0.5-W3)
            Ls4_new=Pcc4/(0.052*1.125*d)
        Ls4=round(Ls4_new)
        while Ls4%5!=0:
            Ls4+=1 
        LM4=((Fj3/2)-W3)/(w4*B)
        
        
        #Fifth String
        df_new2=df_new[df_new['Pc']<Pc4]
        if df_new2.shape[0]!=0 and LM4>Ls4:
            Pc5=df_new2.loc[df_new2['Pc'].idxmax()]['Pc']
            w5=df_new2.loc[df_new2['Pc'].idxmax()]['w']
            K5=df_new2.loc[df_new2['Pc'].idxmax()]['K'] 
            Fj5=df_new2.loc[df_new2['Pc'].idxmax()]['Fj']
            CasingPipe5=df_new2.loc[df_new2['Pc'].idxmax()]['Casing Pipe']
            Ls5=(Pc5/(0.052*1.125*d))
            W4=((W3+w4*B*(Ls4-Ls5)))
            Pcc5=(Pc5/K5)*((K5**2-3*W4**2)**0.5-W4)
            Ls5_new=Pcc5/(0.052*1.125*d)
            while Ls5-Ls5_new>=5:
                Ls5=Ls5_new
                W4=(W3+w4*B*(Ls4-Ls5))
                Pcc5=(Pc5/K5)*((K5**2-3*W4**2)**0.5-W4)
                Ls5_new=Pcc5/(0.052*1.125*d)
            Ls5=round(Ls5_new)
            while Ls5%5!=0:
                Ls5+=1 
            LM5=((Fj5/2)-W4)/(w5*B)
            
            
            #Sixth String
            df_new2=df_new[df_new['Pc']<Pc5]
            if df_new2.shape[0]!=0 and LM5>Ls5:
                Pc6=df_new2.loc[df_new2['Pc'].idxmax()]['Pc']
                w6=df_new2.loc[df_new2['Pc'].idxmax()]['w']
                K6=df_new2.loc[df_new2['Pc'].idxmax()]['K'] 
                Fj6=df_new2.loc[df_new2['Pc'].idxmax()]['Fj']
                CasingPipe6=df_new2.loc[df_new2['Pc'].idxmax()]['Casing Pipe']
                Ls6=(Pc6/(0.052*1.125*d))
                W5=((W4+w5*B*(Ls5-Ls6)))
                Pcc6=(Pc6/K6)*((K6**2-3*W5**2)**0.5-W5)
                Ls6_new=Pcc6/(0.052*1.125*d)
                while Ls6-Ls6_new>=5:
                    Ls6=Ls6_new
                    W5=(W4+w5*B*(Ls5-Ls6))
                    Pcc6=(Pc6/K6)*((K6**2-3*W5**2)**0.5-W5)
                    Ls6_new=Pcc6/(0.052*1.125*d)
                Ls6=round(Ls6_new)
                while Ls6%5!=0:
                    Ls6+=1 
               
            else:
                df_new2=df_new[df_new['Fj']>Fj5]
                Pc6=df_new2.loc[df_new2['Fj'].idxmin()]['Pc']
                w6=df_new2.loc[df_new2['Fj'].idxmin()]['w']
                K6=df_new2.loc[df_new2['Fj'].idxmin()]['K'] 
                Fj6=df_new2.loc[df_new2['Fj'].idxmin()]['Fj']
                CasingPipe6=df_new2.loc[df_new2['Fj'].idxmin()]['Casing Pipe']
                Ls6=Ls5-LM5
                Ls6=round(Ls6)
                while Ls6%5!=0:
                    Ls6+=1
                W5=((W4+w5*B*(Ls5-Ls6)))
                LM6=((Fj6/2)-W5)/(w6*B)
                if LM6>Ls6:
                    W6=W5+(w6*B*Ls6)
                    
        else:
            df_new2=df_new[df_new['Fj']>Fj4]
            Pc5=df_new2.loc[df_new2['Fj'].idxmin()]['Pc']
            w5=df_new2.loc[df_new2['Fj'].idxmin()]['w']
            K5=df_new2.loc[df_new2['Fj'].idxmin()]['K'] 
            Fj5=df_new2.loc[df_new2['Fj'].idxmin()]['Fj']
            CasingPipe5=df_new2.loc[df_new2['Fj'].idxmin()]['Casing Pipe']
            Ls5=Ls4-LM4
            Ls5=round(Ls5)
            while Ls5%5!=0:
                Ls5+=1
            W4=((W3+w4*B*(Ls4-Ls5)))
            LM5=((Fj5/2)-W4)/(w5*B)
            if LM5>Ls5:
                    W5=W4+(w5*B*Ls5)
            
            else:
                 df_new2=df_new[df_new['Fj']>Fj5]
                 Pc6=df_new2.loc[df_new2['Fj'].idxmin()]['Pc']
                 w6=df_new2.loc[df_new2['Fj'].idxmin()]['w']
                 K6=df_new2.loc[df_new2['Fj'].idxmin()]['K'] 
                 Fj6=df_new2.loc[df_new2['Fj'].idxmin()]['Fj']
                 CasingPipe6=df_new2.loc[df_new2['Fj'].idxmax()]['Casing Pipe']
                 Ls6=Ls5-LM5
                 Ls6=round(Ls6)
                 while Ls6%5!=0:
                   Ls6+=1
                 W5=((W4+w5*B*(Ls5-Ls6)))
                 LM6=((Fj6/2)-W5)/(w6*B)
                 W6=W5+(w6*B*Ls6)
    
    else:
        df_new2=df_new[df_new['Fj']>Fj3]
        Pc4=df_new2.loc[df_new2['Fj'].idxmin()]['Pc']
        w4=df_new2.loc[df_new2['Fj'].idxmin()]['w']
        K4=df_new2.loc[df_new2['Fj'].idxmin()]['K'] 
        Fj4=df_new2.loc[df_new2['Fj'].idxmin()]['Fj']
        CasingPipe4=df_new2.loc[df_new2['Fj'].idxmin()]['Casing Pipe']
        Ls4=Ls3-LM3
        Ls4=round(Ls4)
        while Ls4%5!=0:
            Ls4+=1
        W3=((W2+w3*B*(Ls3-Ls4)))
        LM4=((Fj4/2)-W3)/(w4*B)
        if LM4>Ls4:
                W4=W3+(w4*B*Ls5)
        else:
             df_new2=df_new[df_new['Fj']>Fj4]
             Pc5=df_new2.loc[df_new2['Fj'].idxmin()]['Pc']
             w5=df_new2.loc[df_new2['Fj'].idxmin()]['w']
             K5=df_new2.loc[df_new2['Fj'].idxmin()]['K'] 
             Fj5=df_new2.loc[df_new2['Fj'].idxmin()]['Fj']
             CasingPipe5=df_new2.loc[df_new2['Fj'].idxmin()]['Casing Pipe']
             Ls5=Ls4-LM4
             Ls5=round(Ls5)
             while Ls5%5!=0:
                 Ls5+=1
             W4=((W3+w4*B*(Ls4-Ls5)))
             LM5=((Fj5/2)-W4)/(w5*B)
             if LM5>Ls5:
                     W5=W4+(w5*B*Ls5)
             else:
                  df_new2=df_new[df_new['Fj']>Fj5]
                  Pc6=df_new2.loc[df_new2['Fj'].idxmin()]['Pc']
                  w6=df_new2.loc[df_new2['Fj'].idxmin()]['w']
                  K6=df_new2.loc[df_new2['Fj'].idxmin()]['K'] 
                  Fj6=df_new2.loc[df_new2['Fj'].idxmin()]['Fj']
                  CasingPipe6=df_new2.loc[df_new2['Fj'].idxmin()]['Casing Pipe']
                  Ls6=Ls5-LM5
                  Ls6=round(Ls6)
                  while Ls6%5!=0:
                      Ls6+=1
                  W5=((W4+w5*B*(Ls5-Ls6)))
                  LM6=((Fj6/2)-W5)/(w6*B)
                  W6=W5+(w6*B*Ls6)
        
else:
    df_new2=df_new[df_new['Fj']>Fj2]
    Pc3=df_new2.loc[df_new2['Fj'].idxmin()]['Pc']
    w3=df_new2.loc[df_new2['Fj'].idxmin()]['w']
    K3=df_new2.loc[df_new2['Fj'].idxmin()]['K'] 
    Fj3=df_new2.loc[df_new2['Fj'].idxmin()]['Fj']
    CasingPipe3=df_new2.loc[df_new2['Fj'].idxmin()]['Casing Pipe']
    Ls3=Ls2-LM2
    Ls3=round(Ls3)
    while Ls3%5!=0:
        Ls3+=1
    W2=((W1+w2*B*(Ls2-Ls3)))
    LM3=((Fj3/2)-W2)/(w3*B)
    if LM3>Ls3:
            W3=W2+(w3*B*Ls3)
    else:
         df_new2=df_new[df_new['Fj']>Fj3]
         Pc4=df_new2.loc[df_new2['Fj'].idxmin()]['Pc']
         w4=df_new2.loc[df_new2['Fj'].idxmin()]['w']
         K4=df_new2.loc[df_new2['Fj'].idxmin()]['K'] 
         Fj4=df_new2.loc[df_new2['Fj'].idxmin()]['Fj']
         CasingPipe4=df_new2.loc[df_new2['Fj'].idxmin()]['Casing Pipe']
         Ls4=Ls3-LM3
         Ls4=round(Ls4)
         while Ls4%5!=0:
          Ls4+=1        
         W3=((W2+w3*B*(Ls3-Ls4)))
         LM4=((Fj4/2)-W3)/(w4*B)
         if LM4>Ls4:
                 W4=W3+(w4*B*Ls4)
         else:
             df_new2=df_new[df_new['Fj']>Fj4]
             Pc5=df_new2.loc[df_new2['Fj'].idxmin()]['Pc']
             w5=df_new2.loc[df_new2['Fj'].idxmin()]['w']
             K5=df_new2.loc[df_new2['Fj'].idxmin()]['K'] 
             Fj5=df_new2.loc[df_new2['Fj'].idxmin()]['Fj']
             CasingPipe5=df_new2.loc[df_new2['Fj'].idxmin()]['Casing Pipe']
             Ls5=Ls4-LM4
             Ls5=round(Ls5)
             while Ls5%5!=0:
              Ls5+=1
             W4=((W3+w4*B*(Ls4-Ls5)))
             LM5=((Fj5/2)-W4)/(w5*B)
             if LM5>Ls5:
                     W5=W4+(w5*B*Ls5)
             else:
                 df_new2=df_new[df_new['Fj']>Fj5]
                 Pc6=df_new2.loc[df_new2['Fj'].idxmin()]['Pc']
                 w6=df_new2.loc[df_new2['Fj'].idxmin()]['w']
                 K6=df_new2.loc[df_new2['Fj'].idxmin()]['K'] 
                 Fj6=df_new2.loc[df_new2['Fj'].idxmin()]['Fj']
                 CasingPipe6=df_new2.loc[df_new2['Fj'].idxmin()]['Casing Pipe']
                 Ls6=Ls5-LM5
                 Ls6=round(Ls6)
                 while Ls6%5!=0:
                   Ls6+=1
                 W5=((W4+w5*B*(Ls5-Ls6)))
                 LM6=((Fj6/2)-W5)/(w6*B)
                 W6=W5+(w6*B*Ls6)

#Calculating Length of Sections
L1=Ls1-Ls2
L2=Ls2-Ls3
L3=Ls3-Ls4
L4=Ls4-Ls5
L5=Ls5-Ls6
L6=Ls6

#Tabulating Final Result
Final_dict= {'Section':[1,2,3,4,5,6],
              'Casing Pipe':[CasingPipe1,CasingPipe2,CasingPipe3,CasingPipe4,CasingPipe5,CasingPipe6],
              'Setting Depth':[Ls1,Ls2,Ls3,Ls4,Ls5,Ls6],
              'Max_Length':['NA',LM2,LM3,LM4,LM5,LM6],
              'Section_Len':[L1,L2,L3,L4,L5,L6],
              'Load':[W1,W2,W3,W4,W5,W6]
              }
              
Final_Table=pd.DataFrame(Final_dict)
print(Final_Table.head(20))

    
    


        
   
