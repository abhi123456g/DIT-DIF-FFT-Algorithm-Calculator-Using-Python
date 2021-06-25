#//////////////////////////////// -BY ABHINAV GAONKAR  /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


#Developer Name => ABHINAV GAONKAR
#Institution Name => Presidency Univeristy, Bangalore,India


            # # # #   # # # #   #     #   # # # # #
            #     #   #     #   #     #       #
            # # # #   # # # #   # # # #       #
            #     #   #     #   #     #       #
            #     #   # # # #   #     #   # # # # #
from tkinter import*
import numpy as neg
import cmath
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from scipy.fft import fft, ifft

root = Tk()

root.title("DFT")

root.configure(bg='black')

root.state('zoomed')

root.label = Label(root,text='DIT & DIF FFT Algorithm Calculator Using Python',bg ="black",fg='yellow',font=('freemono bold',30))
root.label.place(x=355,y=75)

root.label = Label(root,text='© Abhinav Gaonkar',font=('freemono bold',10),bg ="black",fg='white')
root.label.place(x=690,y=750)

def dit4():
    dord1 = Toplevel()
    dord1.title('4 Point DIT FFT Algorithm')
    dord1.state('zoomed')
    dord1.configure(bg='black')
    a.label = Label(dord1,text='4 Point DIT FFT Algorithm',bg ="black",fg='yellow',font=('freemono bold',17))
    a.label.place(x=635,y=20)
    dord1.label = Label(dord1,text="""Note:Enter the input sequence in the text box
    leaving space after each input Ex:1 2 3 4""",font=10,bg ="black",fg='white')
    dord1.label.place(x=605,y=53)
    ip1 = Entry(dord1, width=30,font=10,borderwidth=2)
    ip1.place(x=625,y=110)

    def sin():
        global lista
        ip11 = ip1.get()
        lista = ip11.split()
        aa = (lista[0])
        bb = (lista[2])
        cc = (lista[1])
        dd = (lista[3])

        d.label = Label(dord1,text="I/P Bit Reversed",font=('freemono bold',17),bg ="black",fg='yellow')
        d.label.place(x=490,y=235)
        d.label = Label(dord1,text=aa,font=10)
        d.label.place(x=550,y=300)
        d.label = Label(dord1,text=bb,font=10)
        d.label.place(x=550,y=350)
        d.label = Label(dord1,text=cc,font=10)
        d.label.place(x=550,y=400)
        d.label = Label(dord1,text=dd,font=10)
        d.label.place(x=550,y=450)

        w40 = float(1)
        w41 = complex(0,-1)

        neg1 = neg.negative(float(bb))
        neg2 = neg.negative(float(dd))

        L1A = float(aa)+(w40*float(bb))
        L2A = float(aa)+(w40*neg1)
        L3A = float(cc)+(w40*float(dd))
        L4A = float(cc)+(w40*neg2)

        d.label = Label(dord1,text="First Stage",font=('freemono bold',17),bg ="black",fg='yellow')
        d.label.place(x=714,y=235)
        d.label = Label(dord1,text=L1A,font=10)
        d.label.place(x=750,y=300)
        d.label = Label(dord1,text=L2A,font=10)
        d.label.place(x=750,y=350)
        d.label = Label(dord1,text=L3A,font=10)
        d.label.place(x=750,y=400)
        d.label = Label(dord1,text=L4A,font=10)
        d.label.place(x=750,y=450)

        aa4 = fft(lista)

        d.label = Label(dord1,text="Second Stage (Output)",font=('freemono bold',17),bg ="black",fg='yellow')
        d.label.place(x=890,y=235)
        d.label = Label(dord1,text=aa4[0],font=10)
        d.label.place(x=950,y=300)
        d.label = Label(dord1,text=aa4[1],font=10)
        d.label.place(x=950,y=350)
        d.label = Label(dord1,text=aa4[2],font=10)
        d.label.place(x=950,y=400)
        d.label = Label(dord1,text=aa4[3],font=10)
        d.label.place(x=950,y=450)

        result = [aa4[0],aa4[1],aa4[2],aa4[3]]

        d.label = Label(dord1,text='Input Sequence = '+str(lista),font=('freemono bold',17),bg ="black",fg='yellow')
        d.label.place(x=615,y=530)
        d.label = Label(dord1,text='Output Sequence = '+str(result),font=('freemono bold',17),bg ="black",fg='yellow')
        d.label.place(x=532,y=600)

        def p4():
            dord11 = Tk()

            dord11.state('zoomed')

            dord11.configure(bg='black')

            fig1 = Figure(figsize = (5,5), dpi = 100)
            fig2 = Figure(figsize = (5,5), dpi = 100)
            fig3 = Figure(figsize = (5,5), dpi = 100)

            a = cmath.polar(aa4[0])
            b = cmath.polar(aa4[1])
            c = cmath.polar(aa4[2])
            d = cmath.polar(aa4[3])

            a1 = a[0]
            b1 = b[0]
            c1 = c[0]
            d1 = d[0]

            aa1 = a[1]
            bb1 = b[1]
            cc1 = c[1]
            dd1 = d[1]

            pk = (a1,b1,c1,d1)
            x  = lista
            xk = (0,1,2,3)
            yk = [aa1,bb1,cc1,dd1] # Phase

            ax1 = fig1.add_subplot(111)
            ax1.stem(xk,pk)#
            ax1.set_xlabel('Frequency Component')
            ax1.set_ylabel('Magntitude x(k)')
            ax1.set_title('Magntitude Plot')
            ax2 = fig2.add_subplot(111)
            ax2.stem(xk,yk)#
            ax2.set_xlabel('Frequency Component')
            ax2.set_ylabel('Phase x(k)')
            ax2.set_title('Phase plot')
            ax3 = fig3.add_subplot(111)
            ax3.set_xlabel('Amplitude')
            ax3.set_ylabel('Time')
            ax3.set_title('Input Sequence')
            ax3.stem(xk,x)#

            canv1 = FigureCanvasTkAgg(fig1, master = dord11)
            canv1.draw()
            canv2 = FigureCanvasTkAgg(fig2, master = dord11)
            canv2.draw()
            canv3 = FigureCanvasTkAgg(fig3, master = dord11)
            canv3.draw()

            get_widz = canv1.get_tk_widget()
            get_widz.place(x=0,y=300)
            get_widz = canv2.get_tk_widget()
            get_widz.place(x=1060,y=300)
            get_widz = canv3.get_tk_widget()
            get_widz.place(x=530,y=50)

            def quit1():
                {
                dord11.destroy()
                }


            a7 = Button(dord11,text='Back to Computation',command=quit1,font=25)
            a7.place(x=1300,y=50)

            dord11.mainloop()



        a1 = Button(dord1,text='Show Graph',command=p4,font=25)
        a1.place(x=1300,y=700)



    def sub():
        dord1.destroy()

    a1 = Button(dord1,text='Compute',command=sin,font=25)
    a1.place(x=720,y=150)

    b1 = Button(dord1,text='Back to Mainmenu',command=sub,font=25)
    b1.place(x=1300,y=20)

def dit8():
    dord2 = Toplevel()
    dord2.title('8 Point DIT FFT Algorithm')
    dord2.state('zoomed')
    dord2.configure(bg='black')
    dord2.label = Label(dord2,text='8 Point DIT FFT Algorithm',bg ="black",fg='yellow',font=('freemono bold',17))
    dord2.label.place(x=636,y=20)
    dord2.label = Label(dord2,text="""Note:Enter the input sequence in the text box
    leaving space after each input Ex:1 2 3 4 5 6 7 8""",font=10,bg ="black",fg='white')
    dord2.label.place(x=578,y=53)
    ip2 = Entry(dord2, width=30,font=10,borderwidth=2)
    ip2.place(x=625,y=110)

    def cos():
        global lists
        ip22 = ip2.get()
        lists = ip22.split()

        a1 = (lists[0])
        b1 = (lists[4])
        c1 = (lists[2])
        d1 = (lists[6])
        e1 = (lists[1])
        f1 = (lists[5])
        g1 = (lists[3])
        h1 = (lists[7])

        d.label = Label(dord2,text="I/P Bit Reversed",font=('freemono bold',17),bg ="black",fg='yellow')
        d.label.place(x=400,y=205)
        d.label = Label(dord2,text=a1,font=10)
        d.label.place(x=460,y=270)
        d.label = Label(dord2,text=b1,font=10)
        d.label.place(x=460,y=320)
        d.label = Label(dord2,text=c1,font=10)
        d.label.place(x=460,y=370)
        d.label = Label(dord2,text=d1,font=10)
        d.label.place(x=460,y=420)
        d.label = Label(dord2,text=e1,font=10)
        d.label.place(x=460,y=470)
        d.label = Label(dord2,text=f1,font=10)
        d.label.place(x=460,y=520)
        d.label = Label(dord2,text=g1,font=10)
        d.label.place(x=460,y=570)
        d.label = Label(dord2,text=h1,font=10)
        d.label.place(x=460,y=620)

        w80 = float(1)
        w81 = complex(0.707,-0.707)
        w82 = complex(0,-1)
        w83 = complex(-0.707,-0.707)

        L1A = float(a1)+(float(b1))
        L2A = float(a1)-(float(b1))
        L3A = float(c1)+(float(d1))
        L4A = float(c1)-(float(d1))
        L5A = float(e1)+(float(f1))
        L6A = float(e1)-(float(f1))
        L7A = float(g1)+(float(h1))
        L8A = float(g1)-(float(h1))

        d.label = Label(dord2,text="First Stage",font=('freemono bold',17),bg ="black",fg='yellow')
        d.label.place(x=625,y=205)
        d.label = Label(dord2,text=L1A,font=10)
        d.label.place(x=660,y=270)
        d.label = Label(dord2,text=L2A,font=10)
        d.label.place(x=660,y=320)
        d.label = Label(dord2,text=L3A,font=10)
        d.label.place(x=660,y=370)
        d.label = Label(dord2,text=L4A,font=10)
        d.label.place(x=660,y=420)
        d.label = Label(dord2,text=L5A,font=10)
        d.label.place(x=660,y=470)
        d.label = Label(dord2,text=L6A,font=10)
        d.label.place(x=660,y=520)
        d.label = Label(dord2,text=L7A,font=10)
        d.label.place(x=660,y=570)
        d.label = Label(dord2,text=L8A,font=10)
        d.label.place(x=660,y=620)

        L1B = L1A+L3A
        L2B = L2A+(L4A*w82)
        L3B = L1A-L3A
        L4B = L2A-(L4A*w82)
        L5B = L5A+L7A
        L6B = L6A+(L8A*w82)
        L7B = L5A-L7A
        L8B = L6A-(L8A*w82)


        d.label = Label(dord2,text="Second Stage",font=('freemono bold',17),bg ="black",fg='yellow')
        d.label.place(x=825,y=205)
        d.label = Label(dord2,text=L1B,font=10)
        d.label.place(x=860,y=270)
        d.label = Label(dord2,text=L2B,font=10)
        d.label.place(x=860,y=320)
        d.label = Label(dord2,text=L3B,font=10)
        d.label.place(x=860,y=370)
        d.label = Label(dord2,text=L4B,font=10)
        d.label.place(x=860,y=420)
        d.label = Label(dord2,text=L5B,font=10)
        d.label.place(x=860,y=470)
        d.label = Label(dord2,text=L6B,font=10)
        d.label.place(x=860,y=520)
        d.label = Label(dord2,text=L7B,font=10)
        d.label.place(x=860,y=570)
        d.label = Label(dord2,text=L8B,font=10)
        d.label.place(x=860,y=620)

        aa8 = fft(lists)

        num1 = round(aa8[0].real,4)+round(aa8[0].imag,4)*1j #X(0)
        num2 = round(aa8[1].real,4)+round(aa8[1].imag,4)*1j #X(4)
        num3 = round(aa8[2].real,4)+round(aa8[2].imag,4)*1j #X(2)
        num4 = round(aa8[3].real,4)+round(aa8[3].imag,4)*1j #X(6)
        num5 = round(aa8[4].real,4)+round(aa8[4].imag,4)*1j #X(1)
        num6 = round(aa8[5].real,4)+round(aa8[5].imag,4)*1j #X(5)
        num7 = round(aa8[6].real,4)+round(aa8[6].imag,4)*1j #X(3)
        num8 = round(aa8[7].real,4)+round(aa8[7].imag,4)*1j #X(7)


        d.label = Label(dord2,text="Third Stage(Output)",font=('freemono bold',17),bg ="black",fg='yellow')
        d.label.place(x=1015,y=205)
        d.label = Label(dord2,text=num1,font=10)
        d.label.place(x=1060,y=270)
        d.label = Label(dord2,text=num2,font=10)
        d.label.place(x=1060,y=320)
        d.label = Label(dord2,text=num3,font=10)
        d.label.place(x=1060,y=370)
        d.label = Label(dord2,text=num4,font=10)
        d.label.place(x=1060,y=420)
        d.label = Label(dord2,text=num5,font=10)
        d.label.place(x=1060,y=470)
        d.label = Label(dord2,text=num6,font=10)
        d.label.place(x=1060,y=520)
        d.label = Label(dord2,text=num7,font=10)
        d.label.place(x=1060,y=570)
        d.label = Label(dord2,text=num8,font=10)
        d.label.place(x=1060,y=620)

        result = [num1,num2,num3,num4,num5,num6,num7,num8]

        d.label = Label(dord2,text='Input Sequence = '+str(lists),font=('freemono bold',17),bg ="black",fg='yellow')
        d.label.place(x=545,y=680)
        d.label = Label(dord2,text='Output Sequence = '+str(result),font=('freemono bold',17),bg ="black",fg='yellow')
        d.label.place(x=275,y=730)

        def p5():
            dord12 = Tk()

            dord12.state('zoomed')

            dord12.configure(bg='black')

            fig1 = Figure(figsize = (5,5), dpi = 100)
            fig2 = Figure(figsize = (5,5), dpi = 100)
            fig3 = Figure(figsize = (5,5), dpi = 100)

            a = cmath.polar(aa8[0])
            b = cmath.polar(aa8[1])
            c = cmath.polar(aa8[2])
            d = cmath.polar(aa8[3])
            e = cmath.polar(aa8[4])
            f = cmath.polar(aa8[5])
            g = cmath.polar(aa8[6])
            h = cmath.polar(aa8[7])

            a1 = a[0]
            b1 = b[0]
            c1 = c[0]
            d1 = d[0]
            e1 = e[0]
            f1 = f[0]
            g1 = g[0]
            h1 = h[0]

            aa1 = a[1]
            bb1 = b[1]
            cc1 = c[1]
            dd1 = d[1]
            ee1 = e[1]
            ff1 = f[1]
            gg1 = g[1]
            hh1 = h[1]


            pk = (a1,b1,c1,d1,e1,f1,g1,h1)
            x  = lists
            xk = (0,1,2,3,4,5,6,7)
            yk = [aa1,bb1,cc1,dd1,ee1,ff1,gg1,hh1] # Phase

            ax1 = fig1.add_subplot(111)
            ax1.stem(xk,pk)#
            ax1.set_xlabel('Frequency Component')
            ax1.set_ylabel('Magntitude x(k)')
            ax1.set_title('Magntitude Plot')
            ax2 = fig2.add_subplot(111)
            ax2.stem(xk,yk)#
            ax2.set_xlabel('Frequency Component')
            ax2.set_ylabel('Phase x(k)')
            ax2.set_title('Phase plot')
            ax3 = fig3.add_subplot(111)
            ax3.set_xlabel('Amplitude')
            ax3.set_ylabel('Time')
            ax3.set_title('Input Sequence')
            ax3.stem(xk,x)#

            canv1 = FigureCanvasTkAgg(fig1, master = dord12)
            canv1.draw()
            canv2 = FigureCanvasTkAgg(fig2, master = dord12)
            canv2.draw()
            canv3 = FigureCanvasTkAgg(fig3, master = dord12)
            canv3.draw()

            get_widz = canv1.get_tk_widget()
            get_widz.place(x=0,y=300)
            get_widz = canv2.get_tk_widget()
            get_widz.place(x=1060,y=300)
            get_widz = canv3.get_tk_widget()
            get_widz.place(x=530,y=50)

            def quit1():
                {
                dord12.destroy()
                }


            a7 = Button(dord12,text='Back to Computation',command=quit1,font=25)
            a7.place(x=1300,y=50)

            dord12.mainloop()



        a1 = Button(dord2,text='Show Graph',command=p5,font=25)
        a1.place(x=1300,y=700)


    def sub1():
        dord2.destroy()

    a1 = Button(dord2,text='Compute',command=cos,font=25)
    a1.place(x=720,y=150)

    b1 = Button(dord2,text='Back to Mainmenu',command=sub1,font=25)
    b1.place(x=1300,y=20)

def dif4():
    dord3 = Toplevel()
    dord3.title('4 Point DIF FFT Algorithm')
    dord3.state('zoomed')
    dord3.configure(bg='black')
    dord3.label = Label(dord3,text='4 Point DIF FFT Algorithm',bg ="black",fg='yellow',font=('freemono bold',17))
    dord3.label.place(x=635,y=20)
    dord3.label = Label(dord3,text="""Note:Enter the input sequence in the text box
    leaving space after each input Ex:1 2 3 4""",font=10,bg ="black",fg='white')
    dord3.label.place(x=605,y=53)
    ip2 = Entry(dord3, width=30,font=10,borderwidth=2)
    ip2.place(x=625,y=110)

    def tan():
        global lists
        ip22 = ip2.get()
        listq = ip22.split()

        aq = (listq[0])
        bq = (listq[1])
        cq = (listq[2])
        dq = (listq[3])

        d.label = Label(dord3,text="Input Stage",font=('freemono bold',17),bg ="black",fg='yellow')
        d.label.place(x=505,y=235)
        d.label = Label(dord3,text=aq,font=10)
        d.label.place(x=550,y=300)
        d.label = Label(dord3,text=bq,font=10)
        d.label.place(x=550,y=350)
        d.label = Label(dord3,text=cq,font=10)
        d.label.place(x=550,y=400)
        d.label = Label(dord3,text=dq,font=10)
        d.label.place(x=550,y=450)

        w40 = float(1)
        w41 = complex(0,-1)

        L1A = float(aq)+float(cq)
        L2A = float(bq)+float(dq)
        L3A = (float(aq)-float(cq))*w40
        L4A = (float(bq)-float(dq))*w41

        d.label = Label(dord3,text="First Stage",font=('freemono bold',17),bg ="black",fg='yellow')
        d.label.place(x=714,y=235)
        d.label = Label(dord3,text=L1A,font=10)
        d.label.place(x=750,y=300)
        d.label = Label(dord3,text=L2A,font=10)
        d.label.place(x=750,y=350)
        d.label = Label(dord3,text=L3A,font=10)
        d.label.place(x=750,y=400)
        d.label = Label(dord3,text=L4A,font=10)
        d.label.place(x=750,y=450)

        aa41 = fft(listq)

        d.label = Label(dord3,text="Second Stage (Output)",font=('freemono bold',17),bg ="black",fg='yellow')
        d.label.place(x=890,y=235)
        d.label = Label(dord3,text=aa41[0],font=10)
        d.label.place(x=950,y=300)
        d.label = Label(dord3,text=aa41[2],font=10)
        d.label.place(x=950,y=350)
        d.label = Label(dord3,text=aa41[1],font=10)
        d.label.place(x=950,y=400)
        d.label = Label(dord3,text=aa41[3],font=10)
        d.label.place(x=950,y=450)

        result = [aa41[0],aa41[1],aa41[2],aa41[3]]

        d.label = Label(dord3,text='Input Sequence = '+str(listq),font=('freemono bold',17),bg ="black",fg='yellow')
        d.label.place(x=615,y=530)
        d.label = Label(dord3,text='(Bit Reversed) Output Sequence = '+str(result),font=('freemono bold',17),bg ="black",fg='yellow')
        d.label.place(x=532,y=600)


        def p4():
            dord13 = Tk()

            dord13.state('zoomed')

            dord13.configure(bg='black')

            fig1 = Figure(figsize = (5,5), dpi = 100)
            fig2 = Figure(figsize = (5,5), dpi = 100)
            fig3 = Figure(figsize = (5,5), dpi = 100)

            a = cmath.polar(aa41[0])
            b = cmath.polar(aa41[1])
            c = cmath.polar(aa41[2])
            d = cmath.polar(aa41[3])

            a1 = a[0]
            b1 = b[0]
            c1 = c[0]
            d1 = d[0]

            aa1 = a[1]
            bb1 = b[1]
            cc1 = c[1]
            dd1 = d[1]

            pk = (a1,b1,c1,d1)
            x  = listq
            xk = (0,1,2,3)
            yk = [aa1,bb1,cc1,dd1] # Phase

            ax1 = fig1.add_subplot(111)
            ax1.stem(xk,pk)#
            ax1.set_xlabel('Frequency Component')
            ax1.set_ylabel('Magntitude x(k)')
            ax1.set_title('Magntitude Plot')
            ax2 = fig2.add_subplot(111)
            ax2.stem(xk,yk)#
            ax2.set_xlabel('Frequency Component')
            ax2.set_ylabel('Phase x(k)')
            ax2.set_title('Phase plot')
            ax3 = fig3.add_subplot(111)
            ax3.set_xlabel('Amplitude')
            ax3.set_ylabel('Time')
            ax3.set_title('Input Sequence')
            ax3.stem(xk,x)#

            canv1 = FigureCanvasTkAgg(fig1, master = dord13)
            canv1.draw()
            canv2 = FigureCanvasTkAgg(fig2, master = dord13)
            canv2.draw()
            canv3 = FigureCanvasTkAgg(fig3, master = dord13)
            canv3.draw()

            get_widz = canv1.get_tk_widget()
            get_widz.place(x=0,y=300)
            get_widz = canv2.get_tk_widget()
            get_widz.place(x=1060,y=300)
            get_widz = canv3.get_tk_widget()
            get_widz.place(x=530,y=50)

            def quit2():
                {
                dord13.destroy()
                }


            a7 = Button(dord13,text='Back to Computation',command=quit2,font=25)
            a7.place(x=1300,y=50)

            dord13.mainloop()



        a1 = Button(dord3,text='Show Graph',command=p4,font=25)
        a1.place(x=1300,y=700)



    def sub3():
        dord3.destroy()

    a1 = Button(dord3,text='Compute',command=tan,font=25)
    a1.place(x=720,y=150)

    b1 = Button(dord3,text='Back to Mainmenu',command=sub3,font=25)
    b1.place(x=1300,y=20)

def dif8():
    dord4 = Toplevel()
    dord4.title('4 Point DIF FFT Algorithm')
    dord4.state('zoomed')
    dord4.configure(bg='black')
    dord4.label = Label(dord4,text='8 Point DIF FFT Algorithm',bg ="black",fg='yellow',font=('freemono bold',17))
    dord4.label.place(x=636,y=20)

    dord4.label = Label(dord4,text="""Note:Enter the input sequence in the text box
    leaving space after each input Ex:1 2 3 4 5 6 7 8""",font=10,bg ="black",fg='white')
    dord4.label.place(x=578,y=53)
    ip2 = Entry(dord4, width=30,font=10,borderwidth=2)
    ip2.place(x=625,y=110)

    def cot():
        global lists
        ip22 = ip2.get()
        listr = ip22.split()

        ar = (listr[0])
        br = (listr[1])
        cr = (listr[2])
        dr = (listr[3])
        er = (listr[4])
        fr = (listr[5])
        gr = (listr[6])
        hr = (listr[7])


        d.label = Label(dord4,text="Input Stage",font=('freemono bold',17),bg ="black",fg='yellow')
        d.label.place(x=400,y=205)
        d.label = Label(dord4,text=ar,font=10)
        d.label.place(x=460,y=270)
        d.label = Label(dord4,text=br,font=10)
        d.label.place(x=460,y=320)
        d.label = Label(dord4,text=cr,font=10)
        d.label.place(x=460,y=370)
        d.label = Label(dord4,text=dr,font=10)
        d.label.place(x=460,y=420)
        d.label = Label(dord4,text=er,font=10)
        d.label.place(x=460,y=470)
        d.label = Label(dord4,text=fr,font=10)
        d.label.place(x=460,y=520)
        d.label = Label(dord4,text=gr,font=10)
        d.label.place(x=460,y=570)
        d.label = Label(dord4,text=hr,font=10)
        d.label.place(x=460,y=620)

        w80 = float(1)
        w81 = complex(0.707,-0.707)
        w82 = complex(0,-1)
        w83 = complex(-0.707,-0.707)

        L1A = float(ar)+float(er)
        L2A = float(br)+float(fr)
        L3A = float(cr)+float(gr)
        L4A = float(dr)+float(hr)
        L5A = (float(ar)-float(er))*w80
        L6A = (float(br)-float(fr))*w81
        L7A = (float(cr)-float(gr))*w82
        L8A = (float(dr)-float(hr))*w83

        d.label = Label(dord4,text="First Stage",font=('freemono bold',17),bg ="black",fg='yellow')
        d.label.place(x=625,y=205)
        d.label = Label(dord4,text=L1A,font=10)
        d.label.place(x=660,y=270)
        d.label = Label(dord4,text=L2A,font=10)
        d.label.place(x=660,y=320)
        d.label = Label(dord4,text=L3A,font=10)
        d.label.place(x=660,y=370)
        d.label = Label(dord4,text=L4A,font=10)
        d.label.place(x=660,y=420)
        d.label = Label(dord4,text=L5A,font=10)
        d.label.place(x=660,y=470)
        d.label = Label(dord4,text=L6A,font=10)
        d.label.place(x=660,y=520)
        d.label = Label(dord4,text=L7A,font=10)
        d.label.place(x=660,y=570)
        d.label = Label(dord4,text=L8A,font=10)
        d.label.place(x=660,y=620)

        L1B = L1A + L3A
        L2B = L2A + L4A
        L3B = (L1A - L3A)*w80
        L4B = (L2A - L4A)*w82
        L5B = L5A + L7A
        L6B = L6A + L8A
        L7B = (L5A - L7A)*w80
        L8B = (L6A - L8A)*w82

        num1 = round(L1B.real,4)+round(L1B.imag,4)*1j
        num2 = round(L2B.real,4)+round(L2B.imag,4)*1j
        num3 = round(L3B.real,4)+round(L3B.imag,4)*1j
        num4 = round(L4B.real,4)+round(L4B.imag,4)*1j
        num5 = round(L5B.real,4)+round(L5B.imag,4)*1j
        num6 = round(L6B.real,4)+round(L6B.imag,4)*1j
        num7 = round(L7B.real,4)+round(L7B.imag,4)*1j
        num8 = round(L8B.real,4)+round(L8B.imag,4)*1j

        d.label = Label(dord4,text="Second Stage",font=('freemono bold',17),bg ="black",fg='yellow')
        d.label.place(x=825,y=205)
        d.label = Label(dord4,text=num1,font=10)
        d.label.place(x=860,y=270)
        d.label = Label(dord4,text=num2,font=10)
        d.label.place(x=860,y=320)
        d.label = Label(dord4,text=num3,font=10)
        d.label.place(x=860,y=370)
        d.label = Label(dord4,text=num4,font=10)
        d.label.place(x=860,y=420)
        d.label = Label(dord4,text=num5,font=10)
        d.label.place(x=860,y=470)
        d.label = Label(dord4,text=num6,font=10)
        d.label.place(x=860,y=520)
        d.label = Label(dord4,text=num6,font=10)
        d.label.place(x=860,y=570)
        d.label = Label(dord4,text=num7,font=10)
        d.label.place(x=860,y=620)

        aa81 = fft(listr)

        num1 = round(aa81[0].real,4)+round(aa81[0].imag,4)*1j #X(0)
        num2 = round(aa81[1].real,4)+round(aa81[1].imag,4)*1j #X(4)
        num3 = round(aa81[2].real,4)+round(aa81[2].imag,4)*1j #X(2)
        num4 = round(aa81[3].real,4)+round(aa81[3].imag,4)*1j #X(6)
        num5 = round(aa81[4].real,4)+round(aa81[4].imag,4)*1j #X(1)
        num6 = round(aa81[5].real,4)+round(aa81[5].imag,4)*1j #X(5)
        num7 = round(aa81[6].real,4)+round(aa81[6].imag,4)*1j #X(3)
        num8 = round(aa81[7].real,4)+round(aa81[7].imag,4)*1j #X(7)


        d.label = Label(dord4,text="Third Stage(Output)",font=('freemono bold',17),bg ="black",fg='yellow')
        d.label.place(x=1015,y=205)
        d.label = Label(dord4,text=num1,font=10)
        d.label.place(x=1060,y=270)
        d.label = Label(dord4,text=num5,font=10)
        d.label.place(x=1060,y=320)
        d.label = Label(dord4,text=num3,font=10)
        d.label.place(x=1060,y=370)
        d.label = Label(dord4,text=num7,font=10)
        d.label.place(x=1060,y=420)
        d.label = Label(dord4,text=num2,font=10)
        d.label.place(x=1060,y=470)
        d.label = Label(dord4,text=num6,font=10)
        d.label.place(x=1060,y=520)
        d.label = Label(dord4,text=num4,font=10)
        d.label.place(x=1060,y=570)
        d.label = Label(dord4,text=num8,font=10)
        d.label.place(x=1060,y=620)

        result = [num1,num2,num3,num4,num5,num6,num7,num8]

        d.label = Label(dord4,text='Input Sequence = '+str(listr),font=('freemono bold',17),bg ="black",fg='yellow')
        d.label.place(x=545,y=680)
        d.label = Label(dord4,text='Output Sequence = '+str(result),font=('freemono bold',17),bg ="black",fg='yellow')
        d.label.place(x=275,y=730)
        d.label = Label(dord4,text="Ouput Is Bit Reversed",bg ="black",fg='white')
        d.label.place(x=700,y=765)
        def p6():
            dord14 = Tk()

            dord14.state('zoomed')

            dord14.configure(bg='black')

            fig1 = Figure(figsize = (5,5), dpi = 100)
            fig2 = Figure(figsize = (5,5), dpi = 100)
            fig3 = Figure(figsize = (5,5), dpi = 100)

            a = cmath.polar(aa81[0])
            b = cmath.polar(aa81[1])
            c = cmath.polar(aa81[2])
            d = cmath.polar(aa81[3])
            e = cmath.polar(aa81[4])
            f = cmath.polar(aa81[5])
            g = cmath.polar(aa81[6])
            h = cmath.polar(aa81[7])

            a1 = a[0]
            b1 = b[0]
            c1 = c[0]
            d1 = d[0]
            e1 = e[0]
            f1 = f[0]
            g1 = g[0]
            h1 = h[0]

            aa1 = a[1]
            bb1 = b[1]
            cc1 = c[1]
            dd1 = d[1]
            ee1 = e[1]
            ff1 = f[1]
            gg1 = g[1]
            hh1 = h[1]


            pk = (a1,b1,c1,d1,e1,f1,g1,h1)
            x  = listr
            xk = (0,1,2,3,4,5,6,7)
            yk = [aa1,bb1,cc1,dd1,ee1,ff1,gg1,hh1] # Phase

            ax1 = fig1.add_subplot(111)
            ax1.stem(xk,pk)#
            ax1.set_xlabel('Frequency Component')
            ax1.set_ylabel('Magntitude x(k)')
            ax1.set_title('Magntitude Plot')
            ax2 = fig2.add_subplot(111)
            ax2.stem(xk,yk)#
            ax2.set_xlabel('Frequency Component')
            ax2.set_ylabel('Phase x(k)')
            ax2.set_title('Phase plot')
            ax3 = fig3.add_subplot(111)
            ax3.set_xlabel('Amplitude')
            ax3.set_ylabel('Time')
            ax3.set_title('Input Sequence')
            ax3.stem(xk,x)#

            canv1 = FigureCanvasTkAgg(fig1, master = dord14)
            canv1.draw()
            canv2 = FigureCanvasTkAgg(fig2, master = dord14)
            canv2.draw()
            canv3 = FigureCanvasTkAgg(fig3, master = dord14)
            canv3.draw()

            get_widz = canv1.get_tk_widget()
            get_widz.place(x=0,y=300)
            get_widz = canv2.get_tk_widget()
            get_widz.place(x=1060,y=300)
            get_widz = canv3.get_tk_widget()
            get_widz.place(x=530,y=50)

            def quit1():
                {
                dord14.destroy()
                }


            a7 = Button(dord14,text='Back to Computation',command=quit1,font=25)
            a7.place(x=1300,y=50)

            dord14.mainloop()



        a1 = Button(dord4,text='Show Graph',command=p6,font=25)
        a1.place(x=1300,y=700)




    def sub4():
        dord4.destroy()

    a1 = Button(dord4,text='Compute',command=cot,font=25)
    a1.place(x=720,y=150)

    b1 = Button(dord4,text='Back to Mainmenu',command=sub4,font=25)
    b1.place(x=1300,y=20)

a = Button(root,text="4 Point DIT FFT",command=dit4,bg ="white",fg='black',borderwidth=15,font=100)
a.place(x=675,y=200)

b = Button(root,text="8 Point DIT FFT",command=dit8,bg ="white",fg='black',borderwidth=15,font=100)
b.place(x=675,y=300)

c = Button(root,text="4 Point DIF FFT",command=dif4,bg ="white",fg='black',borderwidth=15,font=100)
c.place(x=675,y=400)

d = Button(root,text="8 Point DIF FFT",command=dif8,bg ="white",fg='black',borderwidth=15,font=100)
d.place(x=675,y=500)

root.mainloop()

                       # # # #   # # # #   #     #   # # # # #
                       #     #   #     #   #     #       #
                       # # # #   # # # #   # # # #       #
                       #     #   #     #   #     #       #
                       #     #   # # # #   #     #   # # # # #

#////////////////////////// by Abhinav Gaonkar /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#-------------------------- © copyrights owned by ABHINAV GAONKAR-------------#
