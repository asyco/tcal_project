import tkinter

ventana=tkinter.Tk()
ventana.title("Intercambiadores de Calor")
ventana.geometry("260x500")

texto1=tkinter.Label(text="U")
texto1.pack()
u0=tkinter.Entry(ventana)
u0.pack()

texto2=tkinter.Label(text="As")
texto2.pack()
asu0=tkinter.Entry(ventana)
asu0.pack()

texto3=tkinter.Label(text="m_doth")
texto3.pack()
m_doth0=tkinter.Entry(ventana)
m_doth0.pack()

texto4=tkinter.Label(text="m_dotc")
texto4.pack()
m_dotc0=tkinter.Entry(ventana)
m_dotc0.pack()

texto5=tkinter.Label(text="Cph")
texto5.pack()
cph0=tkinter.Entry(ventana)
cph0.pack()

texto6=tkinter.Label(text="Cpc")
texto6.pack()
cpc0=tkinter.Entry(ventana)
cpc0.pack()

texto7=tkinter.Label(text="Th,in")
texto7.pack()
th_in0=tkinter.Entry(ventana)
th_in0.pack()

texto8=tkinter.Label(text="Tc,in")
texto8.pack()
tc_in0=tkinter.Entry(ventana)
tc_in0.pack()




def pide_datos():
    u=float(u0.get())
    asu=float(asu0.get())
    m_doth=float(m_doth0.get())
    m_dotc=float(m_dotc0.get())
    cph=float(cph0.get())
    cpc=float(cpc0.get())
    th_in=float(th_in0.get())
    tc_in=float(tc_in0.get())
    llenas=[u,asu,m_doth,m_dotc,cph,cpc,th_in,tc_in]

    return llenas

def calcula_ntu(llenas):
    c_c=llenas[5]*llenas[3]
    c_h=llenas[2]*llenas[4]
    c_min=min(c_c,c_h)
    c_max=max(c_c,c_h)
    ntu=(llenas[0]*llenas[1])/c_min
    q_max=c_min*(llenas[6]-llenas[7])
    c=c_min/c_max
    return ntu, c,q_max


def calcula_q(ntu,c,q_max):
    e=(1-2.718281828**(-ntu*(1-c)))/(1-c*2.718281828**(-ntu*(1-c)))
    q=e*q_max
    espacio=tkinter.Label(text="-----------------------------")
    espacio.pack()
    result_q=tkinter.Label(text="q_dot = " + str(int(q)) +"W")
    result_q.pack()

    return q
    
def calcula_T(llenas,q):
    th_out=llenas[6]-q/(llenas[2]*llenas[4])
    tc_out=llenas[7]+q/(llenas[3]*llenas[5])
    espacio=tkinter.Label(text="-----------------------------")
    espacio.pack()
    result_tho=tkinter.Label(text="th_out = " + str(int(th_out)) +"°C")
    result_tho.pack()
    espacio2=tkinter.Label(text="-----------------------------")
    espacio2.pack()
    result_tco=tkinter.Label(text="tc_out= " + str(int(tc_out)) +"°C")
    result_tco.pack()


def main():
    llenas=pide_datos()
    ntu,c,q_max=calcula_ntu(llenas)
    q=calcula_q(ntu,c,q_max)
    calcula_T(llenas,q)
    
    



boton1=tkinter.Button(ventana,text= "CALCULAR", command= main)
boton1.pack()



ventana.mainloop()




