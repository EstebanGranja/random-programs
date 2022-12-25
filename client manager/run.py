import menu
import interfaz
import sys

if __name__ =="__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        menu.iniciar()
    else:
        app = interfaz.MainWindow()
        app.mainloop()

# python run.py -t    EJECUTAR EN CONSOLA
# python run.py       EJECUTAR INTERFAZ
