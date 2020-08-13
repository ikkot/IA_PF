import os
import random
from sklearn import svm
from sklearn import metrics
from sklearn import model_selection
from PIL import Image


# Recorta la imagen en tres partes que luego retorna
def process_char(foto):
    a1 = (0, 0, foto.size[0]//3, foto.size[1])
    a2 = (foto.size[0]//3, 0, foto.size[0]-foto.size[0]//3, foto.size[1])
    a3 = (foto.size[0]-foto.size[0]//3, 0, foto.size[0], foto.size[1])

    c1 = foto.crop(a1)
    c2 = foto.crop(a2)
    c3 = foto.crop(a3)

    return (c1, c2, c3)


# Recorta y estandarizacion
def crop_n_l(path_img):
    mat_leter = []
    mat_digit = []
    foto = Image.open(path_img)
    foto = foto.resize((400, 108), Image.ANTIALIAS)
    foto = foto.convert('L')  # Monochromatic

    # Crop digit and leter
    area_leter = (0, 0, (foto.size[0]//2)-23, foto.size[1])
    area_digit = ((foto.size[0]//2)+23, 0, foto.size[0], foto.size[1])
    foto_leter = foto.crop(area_leter)
    foto_digit = foto.crop(area_digit)
    (l1, l2, l3) = process_char(foto_leter)
    (d1, d2, d3) = process_char(foto_digit)

    mat_leter.append(list(l1.getdata()))
    mat_leter.append(list(l2.getdata()))
    mat_leter.append(list(l3.getdata()))

    mat_digit.append(list(d1.getdata()))
    mat_digit.append(list(d2.getdata()))
    mat_digit.append(list(d3.getdata()))

    return(mat_leter, mat_digit)


# Cargar archivos
def load_data():
    contenido = os.listdir(path)
    print(contenido)
    mat_leter = []
    mat_res_leter = []
    mat_digit = []
    mat_res_digit = []
    count = 0
    for ele in contenido:
        count = count+1
        print(str(count)+" de " + str(len(contenido)))
        ele_name = ele.split(".")[0]
        foto = Image.open(path+"/"+ele_name+".png")
        if(ord(ele[0]) < 58):
            mat_digit.append(list(foto.getdata()))
            mat_res_digit.append(ord(ele[0]))
        else:
            mat_leter.append(list(foto.getdata()))
            mat_res_leter.append(ord(ele[0]))
        foto.close()
    print("End")
    return (mat_leter, mat_res_leter, mat_digit, mat_res_digit)


# Parte las listas en train y test siendo test
def split(mat, mat_res):
    X_train, X_test, y_train, y_test = model_selection.train_test_split(
        mat, mat_res, test_size=split_size)
    return(X_train, X_test, y_train, y_test)
    print("End")


# Train Simple vector machine
def train_SVM():
    print("Prosesando...")
    # Digit
    clf_l = svm.SVC(max_iter=-1, kernel='linear',
                    decision_function_shape='ovr', cache_size=800, degree=1, gamma='auto')
    clf_l.fit(X_train_l, y_train_l)

    # Number
    clf_d = svm.SVC(max_iter=-1, kernel='linear',
                    decision_function_shape='ovr', cache_size=800, degree=1, gamma='auto')
    clf_d.fit(X_train_d, y_train_d)

    print("Fin")
    return (clf_l, clf_d)


# **Test dataset**
def analyzeT(y_pred_l, y_pred_d):
    # Letra
    print("---------- Letra ----------")
    print(metrics.classification_report(y_test_l, y_pred_l))

    # Digito
    print("---------- Digito ----------")
    print(metrics.classification_report(y_test_d, y_pred_d))

# Imprimir patente


def print_patente(l, d):
    txt = ""
    for ele in l:
        txt = txt+chr(ele)
    for ele in d:
        txt = txt+chr(ele)
    print(txt)


print("###########################################################################")
print("-------------------------------- IA ---------------------------------------")
print("###########################################################################")
print()
# Ejecutar
while (True):
    print("Ingrese path del dataset (/dataset): ", end="")
    path = input()
    if(path == ""):
        path = "dataset"

    print("Ingrese tamaño conjuntpo Testeo (0.20): ", end="")
    split_size = input()
    if(split_size == ""):
        split_size = 0.20
    else:
        split_size = float(split_size)

    # Load
    (mat_leter, mat_res_leter, mat_digit, mat_res_digit) = load_data()

    # Split
    (X_train_l, X_test_l, y_train_l, y_test_l) = split(mat_leter, mat_res_leter)
    (X_train_d, X_test_d, y_train_d, y_test_d) = split(mat_digit, mat_res_digit)

    # Train
    (clf_l, clf_d) = train_SVM()

    y_pred_l = clf_l.predict(X_test_l)
    y_pred_d = clf_d.predict(X_test_d)

    analyzeT(y_pred_l, y_pred_d)

    while (True):
        print("Desea probar ejemplo (S/n): ", end="")
        opt = input()
        if(opt == "" or opt == "S" or opt == "s"):
            print("Ingrese path ejemplo: ", end="")
            path_tem = input()
            (test_l, test_d) = crop_n_l(path_tem)
            print_patente(clf_l.predict(test_l), clf_d.predict(test_d))
        else:
            break
    print("Desea continuar(s/N): ", end="")
    opt = input()
    if(opt == "" or opt == "N" or opt == "n"):
        break
