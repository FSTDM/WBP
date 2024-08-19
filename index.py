from datetime import datetime
import hashlib
import io
import sys
import time
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import *

#FYI
def Ignore():
    root.after(1234)                    #TKinter way of sleeping for millseconds
    root.update()                       #Updates the Window, don't wait till the process is done
    showinfo(title="T",message="M")     #Displays a MessageBox
    
    file.seek(0,io.SEEK_END)            #Obtener el tamaño de un archivo abierto
    size = file.tell()
    size = file.seek(0,io.SEEK_SET)

# Begin Utilerias --------------------------------------------------------------------------------------------
class U:
    def CurrentTime():
        #RFC 3339, ISO 8601 sans "T"
            #return datetime.utcnow().isoformat(sep=" ",timespec="milliseconds")
            #It returns the time in UTC 0
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
class UT:
    def SetText(tObject,value):
        stype = type(tObject)
        if stype == ttk.Label:
            tObject['text'] = value
            return
        elif stype == Text:
            tObject.delete(1.0,END)
            tObject.insert('end',value)
        else:
            print(stype)
    def AddText(tObject,value):
        stype = type(tObject)
        if stype == ttk.Label:
            tObject['text'] += value
            return
        elif stype == Text:
            tObject.insert('end',value)
        else:
            print(stype)
    def OpenFile():
        filename = fd.askopenfilename()
        return filename
# End Utilerias ----------------------------------------------------------------------------------------------

# Begin Main form --------------------------------------------------------------------------------------------
class MainForm(tk.Tk):
    def __init__(self):
        super().__init__()
        # Begin Populate controls ----------------------------------------------------------------------------
        if True:
            CRO = 1
            BGC = "#C0D0E0"
            PAX = 10
            PAY = 10
            #Window
            self.config(bg=BGC)
            self.title("Scratch testing form 123")
            #Label Instrucciones
            self.lblInstruction = ttk.Label(self, text="Selecione el archivo al cual desea calcular sus Hashes",background=BGC)
            self.lblInstruction.grid(row=CRO,column=1,padx=PAX, pady=PAY,columnspan=1000)
            CRO = CRO + 1
            
            #Boton Archivo
            self.btnFile = ttk.Button(self, text='Abrir archivo')
            self.btnFile['command'] = self.btnFileCommand
            self.btnFile.grid(row=CRO,column=1,padx=PAX,pady=0)
            self.filename = None
            #Label Archivo
            self.lblArchivo = ttk.Label(self, text="Archivo: ",background=BGC)
            self.lblArchivo.grid(row=CRO,column=2,padx=0,pady=0)
            #Display Archivo
            self.lblArchivoSel = ttk.Label(self, text="ninguno",background=BGC)
            self.lblArchivoSel.grid(row=CRO,column=3,padx=0,pady=0)
            self.ArchivoSel = None
            CRO = CRO + 1

            #Blank
            self.B0 = ttk.Label(self,text="",background=BGC)
            self.B0.grid(row=CRO,column=1)
            CRO = CRO + 1
            
            #Textbox Result
            self.txtResult = Text(self,width=150,height=10)
            #---self.txtResult.config(state=DISABLED)
            self.txtResult.grid(row=CRO,column=1,columnspan=1000,padx=PAX,pady=0)
            CRO = CRO + 1

            #Label Status
            self.lblStatus = ttk.Label(self, text="",background=BGC)
            self.lblStatus.grid(row=CRO,column=1,padx=PAX, pady=0,columnspan=1000)
            CRO = CRO + 1
        # End populate controls ------------------------------------------------------------------------------
    def btnFileCommand(self):
        #Clear
        UT.SetText(self.txtResult,"")
        UT.SetText(self.lblStatus,"")
        UT.SetText(self.lblArchivoSel,"ninguno")
        #Display Set
        self.filename = UT.OpenFile()
        if self.filename == None or self.filename == "":
            return
        #Process
        UT.SetText(self.lblArchivoSel,self.filename)
        UT.SetText(self.lblStatus,"Procesando")
        self.update()
        with open(self.filename,"rb") as file:
            file.seek(0,io.SEEK_END)
            filesize = file.tell()
            file.seek(0,io.SEEK_SET)
            md5 = hashlib.md5()
            sha256 = hashlib.sha256()
            sha3_256 = hashlib.sha3_256()
            sha512 = hashlib.sha512()
            sha3_512 = hashlib.sha3_512()
            lCurrent = 0
            lMax = filesize / BUF_SIZE
            timeFrame = time.time()
            while True:
                data = file.read(BUF_SIZE)
                if not data:
                    break
                md5.update(data)
                sha256.update(data)
                sha3_256.update(data)
                sha512.update(data)
                sha3_512.update(data)
                lCurrent += 1
                if time.time() > timeFrame + UPDATE_TIME_SECONDS:
                    timeFrame = time.time()
                    UT.SetText(self.lblStatus,"Procesando: {:.3f} %".format(((lCurrent / lMax) * 100.0)))
                    self.update()
        UT.AddText(self.txtResult,"      MD5 : " + md5.hexdigest().upper() + "\n")
        UT.AddText(self.txtResult,"   SHA256 : " + sha256.hexdigest().upper() + "\n")
        UT.AddText(self.txtResult," SHA3_256 : " + sha3_256.hexdigest().upper() + "\n")
        UT.AddText(self.txtResult,"   SHA512 : " + sha512.hexdigest().upper() + "\n")
        UT.AddText(self.txtResult," SHA3_512 : " + sha3_512.hexdigest().upper() + "\n")
        UT.SetText(self.lblStatus,"Listo")
        self.update()
        #Mess around
# End Main form ----------------------------------------------------------------------------------------------
UPDATE_TIME_SECONDS = 0.09
BUF_SIZE = 1048576          #Buffer Size = 1 MB

if __name__ == "__main__":
    app = MainForm()
    app.mainloop()
