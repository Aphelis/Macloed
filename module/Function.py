import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
class Design_thinfilm():
    def __init__(self,subtrate,material_1,material_2,layer_num):
        self.subtrate=subtrate
        self.material_1= material_1
        self.material_2= material_2
        self.layer_num = layer_num
    def Layer_10(self,wavelength,thickness_1,thickness_2,thickness_3,thickness_4,thickness_5,
                                 thickness_6,thickness_7,thickness_8,thickness_9,thickness_10):
        ns=self.subtrate.iloc[:, 1]
        ks=self.subtrate.iloc[:, 2]
        n1=self.material_1.iloc[:, 1]
        k1=self.material_1.iloc[:, 2]
        n2=self.material_2.iloc[:, 1]
        k2=self.material_2.iloc[:, 2]
        n3=self.material_1.iloc[:, 1]
        k3=self.material_1.iloc[:, 2]
        n4=self.material_2.iloc[:, 1]
        k4=self.material_2.iloc[:, 2]
        n5=self.material_1.iloc[:, 1]
        k5=self.material_1.iloc[:, 2]
        n6=self.material_2.iloc[:, 1]
        k6=self.material_2.iloc[:, 2]
        n7=self.material_1.iloc[:, 1]
        k7=self.material_1.iloc[:, 2]
        n8=self.material_2.iloc[:, 1]
        k8=self.material_2.iloc[:, 2]
        n9=self.material_1.iloc[:, 1]
        k9=self.material_1.iloc[:, 2]
        n10=self.material_2.iloc[:, 1]
        k10=self.material_2.iloc[:, 2]
       
        T={'wavelength':[],'Transmittance':[],'Reflectance':[]}
        for i in range(len(self.material_1)):
            Ns = ns[i]-1j*ks[i] 
            N1 = n1[i]-1j*k1[i]# layer 1
            delta_1 = 2*np.pi*N1*thickness_1/wavelength[i]
            B1 = np.cos(delta_1)+(1j/N1)*np.sin(delta_1)*Ns
            C1 = 1j*N1*np.sin(delta_1)+np.cos(delta_1)*Ns  
            N2 = n2[i]-1j*k2[i] # layer 2
            delta_2 = 2*np.pi*N2*thickness_2/wavelength[i]
            B2 = B1*np.cos(delta_2)+(1j/N2)*np.sin(delta_2)*C1
            C2 = B1*1j*N2*np.sin(delta_2)+np.cos(delta_2)*C1 
            N3 = n3[i]-1j*k3[i]# layer 3
            delta_3 = 2*np.pi*N3*thickness_3/wavelength[i]
            B3 = B2*np.cos(delta_3)+(1j/N3)*np.sin(delta_3)*C2
            C3 = B2*1j*N3*np.sin(delta_3)+np.cos(delta_3)*C2
            N4 = n4[i]-1j*k4[i]# layer 4
            delta_4 = 2*np.pi*N4*thickness_4/wavelength[i]
            B4 = B3*np.cos(delta_4)+(1j/N4)*np.sin(delta_4)*C3
            C4 = B3*1j*N4*np.sin(delta_4)+np.cos(delta_4)*C3
            N5 = n5[i]-1j*k5[i]# layer 5
            delta_5 = 2*np.pi*N5*thickness_5/wavelength[i]
            B5 = B4*np.cos(delta_5)+(1j/N5)*np.sin(delta_5)*C4
            C5 = B4*1j*N5*np.sin(delta_5)+np.cos(delta_5)*C4
            N6 = n6[i]-1j*k6[i]# layer 6
            delta_6 = 2*np.pi*N6*thickness_6/wavelength[i]
            B6 = B5*np.cos(delta_6)+(1j/N6)*np.sin(delta_6)*C5
            C6 = B5*1j*N6*np.sin(delta_6)+np.cos(delta_6)*C5
            N7 = n7[i]-1j*k7[i]# layer 7
            delta_7 = 2*np.pi*N7*thickness_7/wavelength[i]
            B7 = B6*np.cos(delta_7)+(1j/N7)*np.sin(delta_7)*C6
            C7 = B6*1j*N7*np.sin(delta_7)+np.cos(delta_7)*C6
            N8 = n8[i]-1j*k8[i]# layer 8
            delta_8 = 2*np.pi*N8*thickness_8/wavelength[i]
            B8 = B7*np.cos(delta_8)+(1j/N8)*np.sin(delta_8)*C7
            C8 = B7*1j*N8*np.sin(delta_8)+np.cos(delta_8)*C7
            N9 = n9[i]-1j*k9[i]# layer 9
            delta_9 = 2*np.pi*N9*thickness_9/wavelength[i]
            B9 = B8*np.cos(delta_9)+(1j/N9)*np.sin(delta_9)*C8
            C9 = B8*1j*N9*np.sin(delta_9)+np.cos(delta_9)*C8
            N10 = n10[i]-1j*k10[i]# layer 10
            delta_10 = 2*np.pi*N10*thickness_10/wavelength[i]
            B10 = B9*np.cos(delta_10)+(1j/N10)*np.sin(delta_10)*C9
            C10 = B9*1j*N10*np.sin(delta_10)+np.cos(delta_10)*C9
            if self.layer_num==1:
                Y = C1/B1
                B=B1
                C=C1
            elif self.layer_num==2:
                Y = C2/B2
                B=B2
                C=C2
            elif self.layer_num==3:
                Y = C3/B3
                B=B3
                C=C3
            elif self.layer_num==4:
                Y = C4/B4
                B=B4
                C=C4
            elif self.layer_num==5:
                Y = C5/B5
                B=B5
                C=C5
            elif self.layer_num==6:
                Y = C6/B6
                B=B6
                C=C6
            elif self.layer_num==7:
                Y = C7/B7
                B=B7
                C=C7
            elif self.layer_num==8:
                Y = C8/B8
                B=B8
                C=C8
            elif self.layer_num==9:
                Y = C9/B9
                B=B9
                C=C9
            elif self.layer_num==10:
                Y = C10/B10
                B=B10
                C=C10
            else:
                Y=0
                print('error')
              # 膜面光學導納
            N0=1
            T['wavelength'].append(wavelength[i])
            T['Transmittance'].append(100*np.real((4*N0*Ns.real)/((N0*B + C)*(N0*B + C).conjugate())))
            T['Reflectance'].append(100*np.real(((N0-Y)/(N0+Y))*((N0-Y)/(N0+Y)).conjugate()))
            
        return pd.DataFrame(T)
    def Optimize_Layer_10(self,wavelength,thickness_1 = 0,thickness_2 = 0,thickness_3 = 0,thickness_4 = 0,thickness_5 = 0,
                                 thickness_6 = 0,thickness_7 = 0,thickness_8 = 0,thickness_9 = 0,thickness_10 = 0):
        ns=self.subtrate.iloc[:, 1]
        ks=self.subtrate.iloc[:, 2]
        n1=self.material_1.iloc[:, 1]
        k1=self.material_1.iloc[:, 2]
        n2=self.material_2.iloc[:, 1]
        k2=self.material_2.iloc[:, 2]
        n3=self.material_1.iloc[:, 1]
        k3=self.material_1.iloc[:, 2]
        n4=self.material_2.iloc[:, 1]
        k4=self.material_2.iloc[:, 2]
        n5=self.material_1.iloc[:, 1]
        k5=self.material_1.iloc[:, 2]
        n6=self.material_2.iloc[:, 1]
        k6=self.material_2.iloc[:, 2]
        n7=self.material_1.iloc[:, 1]
        k7=self.material_1.iloc[:, 2]
        n8=self.material_2.iloc[:, 1]
        k8=self.material_2.iloc[:, 2]
        n9=self.material_1.iloc[:, 1]
        k9=self.material_1.iloc[:, 2]
        n10=self.material_2.iloc[:, 1]
        k10=self.material_2.iloc[:, 2]
       
        T={'wavelength':[],'Transmittance':[],'Reflectance':[]}
        for i in range(len(self.material_1)):
            Ns = ns[i]-1j*ks[i] 
            N1 = n1[i]-1j*k1[i]# layer 1
            delta_1 = 2*np.pi*N1*thickness_1/wavelength[i]
            B1 = np.cos(delta_1)+(1j/N1)*np.sin(delta_1)*Ns
            C1 = 1j*N1*np.sin(delta_1)+np.cos(delta_1)*Ns  
            N2 = n2[i]-1j*k2[i] # layer 2
            delta_2 = 2*np.pi*N2*thickness_2/wavelength[i]
            B2 = B1*np.cos(delta_2)+(1j/N2)*np.sin(delta_2)*C1
            C2 = B1*1j*N2*np.sin(delta_2)+np.cos(delta_2)*C1 
            N3 = n3[i]-1j*k3[i]# layer 3
            delta_3 = 2*np.pi*N3*thickness_3/wavelength[i]
            B3 = B2*np.cos(delta_3)+(1j/N3)*np.sin(delta_3)*C2
            C3 = B2*1j*N3*np.sin(delta_3)+np.cos(delta_3)*C2
            N4 = n4[i]-1j*k4[i]# layer 4
            delta_4 = 2*np.pi*N4*thickness_4/wavelength[i]
            B4 = B3*np.cos(delta_4)+(1j/N4)*np.sin(delta_4)*C3
            C4 = B3*1j*N4*np.sin(delta_4)+np.cos(delta_4)*C3
            N5 = n5[i]-1j*k5[i]# layer 5
            delta_5 = 2*np.pi*N5*thickness_5/wavelength[i]
            B5 = B4*np.cos(delta_5)+(1j/N5)*np.sin(delta_5)*C4
            C5 = B4*1j*N5*np.sin(delta_5)+np.cos(delta_5)*C4
            N6 = n6[i]-1j*k6[i]# layer 6
            delta_6 = 2*np.pi*N6*thickness_6/wavelength[i]
            B6 = B5*np.cos(delta_6)+(1j/N6)*np.sin(delta_6)*C5
            C6 = B5*1j*N6*np.sin(delta_6)+np.cos(delta_6)*C5
            N7 = n7[i]-1j*k7[i]# layer 7
            delta_7 = 2*np.pi*N7*thickness_7/wavelength[i]
            B7 = B6*np.cos(delta_7)+(1j/N7)*np.sin(delta_7)*C6
            C7 = B6*1j*N7*np.sin(delta_7)+np.cos(delta_7)*C6
            N8 = n8[i]-1j*k8[i]# layer 8
            delta_8 = 2*np.pi*N8*thickness_8/wavelength[i]
            B8 = B7*np.cos(delta_8)+(1j/N8)*np.sin(delta_8)*C7
            C8 = B7*1j*N8*np.sin(delta_8)+np.cos(delta_8)*C7
            N9 = n9[i]-1j*k9[i]# layer 9
            delta_9 = 2*np.pi*N9*thickness_9/wavelength[i]
            B9 = B8*np.cos(delta_9)+(1j/N9)*np.sin(delta_9)*C8
            C9 = B8*1j*N9*np.sin(delta_9)+np.cos(delta_9)*C8
            N10 = n10[i]-1j*k10[i]# layer 10
            delta_10 = 2*np.pi*N10*thickness_10/wavelength[i]
            B10 = B9*np.cos(delta_10)+(1j/N10)*np.sin(delta_10)*C9
            C10 = B9*1j*N10*np.sin(delta_10)+np.cos(delta_10)*C9
            if self.layer_num==1:
                Y = C1/B1
                B=B1
                C=C1
            elif self.layer_num==2:
                Y = C2/B2
                B=B2
                C=C2
            elif self.layer_num==3:
                Y = C3/B3
                B=B3
                C=C3
            elif self.layer_num==4:
                Y = C4/B4
                B=B4
                C=C4
            elif self.layer_num==5:
                Y = C5/B5
                B=B5
                C=C5
            elif self.layer_num==6:
                Y = C6/B6
                B=B6
                C=C6
            elif self.layer_num==7:
                Y = C7/B7
                B=B7
                C=C7
            elif self.layer_num==8:
                Y = C8/B8
                B=B8
                C=C8
            elif self.layer_num==9:
                Y = C9/B9
                B=B9
                C=C9
            elif self.layer_num==10:
                Y = C10/B10
                B=B10
                C=C10
            else:
                Y=0
                print('error')
              # 膜面光學導納
            N0=1
            T['wavelength'].append(wavelength[i])
            T['Transmittance'].append(100*np.real((4*N0*Ns.real)/((N0*B + C)*(N0*B + C).conjugate())))
            T['Reflectance'].append(100*np.real(((N0-Y)/(N0+Y))*((N0-Y)/(N0+Y)).conjugate()))
            R=100*np.real(((N0-Y)/(N0+Y))*((N0-Y)/(N0+Y)).conjugate())
        return R
    def R_Target(self,RB_target,RA_target,RB_weight): 
        '''
        RB_target : 變色前目標
        RA_target : 變色後目標
        RB_weight ：變色前比重
        '''
        R={'wavelength':[],'Reflectance':[]}
        for i in range(len(RA_target.iloc[:,0])):
            R['wavelength'].append(RA_target.iloc[i,0])
            R['Reflectance'].append((RB_target.iloc[i,1]*RB_weight/100+RA_target.iloc[i,1]*((100-RB_weight)/100)))
        return pd.DataFrame(R)
    def Target_nk(self,WO3,CCWO3,RB_weight): 
        '''
        RB_target : 變色前目標
        RA_target : 變色後目標
        RB_weight ：變色前比重
        '''
        R={'wavelength':[],'n':[],'k':[]}
        for i in range(len(WO3.iloc[:,0])):
            R['wavelength'].append(WO3.iloc[i,0])
            R['n'].append((WO3.iloc[i,1]*RB_weight/100+CCWO3.iloc[i,1]*((100-RB_weight)/100)))
            R['k'].append((WO3.iloc[i,2]*RB_weight/100+CCWO3.iloc[i,2]*((100-RB_weight)/100)))
        return pd.DataFrame(R)
    def Optimization(self,layer,Target,p0,bounds,maxfev):
        popt, pcov = curve_fit(layer, Target.iloc[:,0], Target.iloc[:,1],p0=p0,bounds=bounds,maxfev=100) #
        return popt
    def Plot_spectrum(self,T):
        '''
        Plot Transmittance and reflectance intensity of thinfilm
        '''
        plt.rcParams["figure.figsize"] = (12,4)
        fig, ax1 = plt.subplots() 
        ax1.set_xlabel('Wavelength') 
        ax1.set_ylabel('Transmittance', color = 'black') 
        plot_1 = ax1.plot(T.iloc[:,0],T.iloc[:,1],'r-',label='Transmittance') 
        plt.grid()
        ax1.set_xlim([350,700])
        # Adding Twin Axes
        ax2 = ax1.twinx()  
        ax2.set_ylabel('k', color = 'black') 
        plot_2 = ax2.plot(T.iloc[:,0],T.iloc[:,2],'g-',label='Reflectance') 
        ax2.tick_params(axis ='y', labelcolor = 'black') 
        ax2.set_ylabel('Reflectance', color = 'black') 
        lns = plot_1 + plot_2
        labels = [l.get_label() for l in lns]
        plt.legend(lns,labels,loc=2,prop={'size': 8}) #
        plt.title('Transmittance and Reflectance of thin film')
        plt.show()
        #display(T)
    def Layer_10_Optimi(self, popt, wavelength):
        T=self.Layer_10(wavelength,thickness_1 =popt[0],
                                 thickness_2 =popt[1],
                                 thickness_3 =popt[2],
                                 thickness_4 =popt[3],
                                 thickness_5 =popt[4],
                                 thickness_6 =popt[5],
                                 thickness_7 =popt[6],
                                 thickness_8 =popt[7],
                                 thickness_9 =popt[8],
                                 thickness_10=popt[9])
        # self.Plot_spectrum(T)
        
        return(T)
        
if __name__=='__main__':
    B270ST=pd.read_excel('B270ST.xlsx')
    WO3=pd.read_excel('WO3_01.xlsx')
    W=pd.read_excel('W_01.xlsx')
    wavelength=W.iloc[:,0]
    O=Design_thinfilm(B270ST,material_1=W,material_2=WO3,layer_num=1)
    T=O.Layer_10(wavelength,thickness_1=10,
                 thickness_2 =0,
                 thickness_3 =0,
                 thickness_4 =0,
                 thickness_5 =0,
                 thickness_6 =0,
                 thickness_7 =0,
                 thickness_8 =0,
                 thickness_9 =0,
                 thickness_10=0)

    O.Plot_spectrum(T)