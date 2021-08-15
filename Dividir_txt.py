from tkinter import *

root = Tk()
root.title('Separador de txt')
root.geometry("900x150+800+450")
root.resizable(False, False)
resultado = StringVar()

def dividir():
        with open ('inp.txt') as fo:
            op=''
            cntr=1
            for x in fo.read().split("\n"):
                if x.find("Time") == 0:
                    with open(str(cntr)+' cycle.txt','w') as opf:
                        opf.write(op)
                        opf.close()
                        op=''
                        cntr+=1
                else:
                    op=op+'\n'+x
            fo.close()
        resultado.set("Txt divididos com sucesso!")

#label
lbl_espaco = Label(root, width = 45, ).grid(row=0, columnspan=2)
lbl_notificacao = Label(root, text= 'Se você já colocou os arquivos na mesma pasta e alterou o nome do arquivo para inp.txt, clique no botão dividir: ', font='bold_font',width=100,).grid(columnspan=4, sticky='WE')
lbl_resultado = Label(root, textvariable=resultado, font='bold_font',width=100, height=3, fg='blue').grid(columnspan=2,row=2)

#button
btn = Button(root, text="Dividir",font='bold_font', command=dividir).grid(columnspan=4,row=3)

root.mainloop()