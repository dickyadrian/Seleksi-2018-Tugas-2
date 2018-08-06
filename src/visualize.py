import json
import matplotlib
matplotlib.use('WebAgg')
import matplotlib.pyplot as plt,mpld3
import numpy as np

def countJumlahPelamar(alldata, key, value):
    sum = 0
    for data in alldata:
        if (data[key] == value):
            sum = sum + data["jumlah_pelamar"]
    return sum

def countJumlahLowongan(alldata, key, value):
    sum = 0
    for data in alldata:
        if (data[key] == value):
            sum = sum + 1
    return sum

def generateListSumPelamar(alldata, key, value_list):
    result = []
    for value in value_list:
        temp = countJumlahPelamar(alldata, key, value)
        result.append(temp)
    return result

def generateListSumLowongan(alldata, key, value_list):
    result = []
    for value in value_list:
        temp = countJumlahLowongan(alldata, key, value)
        result.append(temp)
    return result

if __name__ == "__main__":
    with open("result.json") as f_in:
        dataFrame = json.load(f_in)
    pendidikan = ["SD", "SLTP/Sederajat", "SLTA/Sederajat", "Diploma 3", "Diploma 4", "Sarjana", "Pascasarjana"]
    pengalaman = ["Baru Lulus", "Pengalaman 0-2 Tahun", "Pengalaman 2-5 Tahun", "Pengalaman 5-10 Tahun", "Pengalaman +10 Tahun"]
    tipe = ["Full Time", "Kontrak", "Magang", "Part Time"]

    pelamarPendidikan = generateListSumPelamar(dataFrame, "pendidikan", pendidikan)
    lowonganPendidikan = generateListSumLowongan(dataFrame, "pendidikan", pendidikan)

    pelamarPengalaman = generateListSumPelamar(dataFrame, "pengalaman_min", pengalaman)
    lowonganPengalaman = generateListSumLowongan(dataFrame, "pengalaman_min", pengalaman)

    pelamarTipe = generateListSumPelamar(dataFrame, "tipe", tipe)
    lowonganTipe = generateListSumLowongan(dataFrame, "tipe", tipe)

    index = np.arange(len(pendidikan))
    fig1 = plt.figure(1, figsize=(15,6))
    plt.subplot(121)
    plt.bar(index, pelamarPendidikan)
    for i,v in enumerate(pelamarPendidikan):
        plt.text(i-0.05, v+100, str(v))
    plt.xlabel("Pendidikan", fontsize = 15)
    plt.ylabel("Jumlah Pelamar", fontsize = 15)
    plt.xticks(index, pendidikan, fontsize = 9)
    plt.title("Jumlah Pelamar berdasarkan Pendidikan Minimal", fontsize = 20)

    plt.subplot(122)
    plt.bar(index, lowonganPendidikan, color = "lightgreen")
    for i,v in enumerate(lowonganPendidikan):
        plt.text(i-0.05, v+2, str(v))
    plt.xlabel("Pendidikan", fontsize = 15)
    plt.ylabel("Jumlah Pelamar", fontsize = 15)
    plt.xticks(index, pendidikan, fontsize = 9)
    plt.title("Jumlah Lowongan berdasarkan Pendidikan Minimal", fontsize = 20)

    index = np.arange(len(pengalaman))
    fig2 = plt.figure(2, figsize = (15,6))
    plt.subplot(121)
    plt.bar(index, pelamarPengalaman)
    for i,v in enumerate(pelamarPengalaman):
        plt.text(i-0.05, v+100, str(v))
    plt.xlabel("Pengalaman", fontsize = 15)
    plt.ylabel("Jumlah Pelamar", fontsize = 15)
    plt.xticks(index, pengalaman, fontsize = 7)
    plt.title("Jumlah Pelamar berdasarkan Pengalaman Minimal", fontsize = 20)
    
    plt.subplot(122)
    plt.bar(index, lowonganPengalaman, color = "lightgreen")
    for i,v in enumerate(lowonganPengalaman):
        plt.text(i-0.05, v+2, str(v))
    plt.xlabel("Pengalaman", fontsize = 15)
    plt.ylabel("Jumlah Lowongan", fontsize = 15)
    plt.xticks(index, pengalaman, fontsize = 7)
    plt.title("Jumlah Lowongan berdasarkan Pengalaman Minimal", fontsize = 20)
    
    index = np.arange(len(tipe))
    fig3 = plt.figure(3, figsize = (15,6))
    plt.subplot(121)
    plt.bar(index, pelamarTipe)
    for i,v in enumerate(pelamarTipe):
        plt.text(i-0.05, v+100, str(v))
    plt.xlabel("Tipe Pekerjaan", fontsize = 15)
    plt.ylabel("Jumlah Pelamar", fontsize = 15)
    plt.xticks(index, tipe)
    plt.title("Jumlah Pelamar berdasarkan Tipe Pekerjaan", fontsize = 20)
    
    plt.subplot(122)
    plt.bar(index, lowonganTipe, color = "lightgreen")
    for i,v in enumerate(lowonganTipe):
        plt.text(i-0.05, v+2, str(v))
    plt.xlabel("Tipe Pekerjaan", fontsize = 15)
    plt.ylabel("Jumlah Lowongan", fontsize = 15)
    plt.xticks(index, tipe)
    plt.title("Jumlah Lowongan berdasarkan Tipe Pekerjaan", fontsize = 20)
    
    print('<p align="center"><font face="helvetica", size ="5"> <u>Hubungan Pekerjaan dengan Pendidikan Minimal</u></font></p>')
    print(mpld3.fig_to_html(fig1, d3_url=None, mpld3_url=None, no_extras=False, template_type='general', figid=None, use_http=False))
    print("<hr>")
    print('<p align="center"><font face="helvetica", size ="5"> <u>Hubungan Pekerjaan dengan Pengalaman Minimal</u></font></p>')
    print(mpld3.fig_to_html(fig2, d3_url=None, mpld3_url=None, no_extras=False, template_type='general', figid=None, use_http=False))
    print("<hr>")
    print('<p align="center"><font face="helvetica", size ="5"> <u>Hubungan Pekerjaan dengan Tipe Pekerjaan</u></font></p>')
    print(mpld3.fig_to_html(fig3, d3_url=None, mpld3_url=None, no_extras=False, template_type='general', figid=None, use_http=False))