import streamlit as st
# Jika Anda ingin menggunakan st.table untuk tampilan yang lebih rapi, pandas masih berguna.
# Jika tidak, Anda bisa menghapusnya dan mengganti st.table dengan loop st.write.
import pandas as pd 

# ==============================================================================
# === DATA SISWA DARI CSV ANDA ===
# Data ini dihasilkan dari CSV yang Anda berikan.
data_siswa = [
    {'nisn': '0121510217', 'nama': 'ACHMAD KIAN TEGAR', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 89.8, 'PKN': 90.71, 'Bahasa_Indonesia': 91.37, 'Matematika': 88.32, 'IPAS': 88.22, 'PJOK': 92.55, 'Seni_Budaya_dan_Prakarya': 89.36, 'Bahasa_Jawa': 88.52},
    {'nisn': '3126646014', 'nama': 'ADZANIA SHERENA AZSILLA PUTRI', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 91.56, 'PKN': 95.16, 'Bahasa_Indonesia': 92.61, 'Matematika': 91.8, 'IPAS': 92.62, 'PJOK': 90.48, 'Seni_Budaya_dan_Prakarya': 93.66, 'Bahasa_Jawa': 90.62},
    {'nisn': '0134889321', 'nama': 'AFIKA AZIZAH RAMADHANI', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 89.73, 'PKN': 90.44, 'Bahasa_Indonesia': 89.59, 'Matematika': 88.36, 'IPAS': 89.76, 'PJOK': 89.05, 'Seni_Budaya_dan_Prakarya': 88.92, 'Bahasa_Jawa': 88.66},
    {'nisn': '3127586632', 'nama': 'AFIQAH FAIZA GHAISANI', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 96.34, 'PKN': 97.61, 'Bahasa_Indonesia': 95.88, 'Matematika': 94.48, 'IPAS': 95.81, 'PJOK': 94.75, 'Seni_Budaya_dan_Prakarya': 95.64, 'Bahasa_Jawa': 94.69},
    {'nisn': '3122489234', 'nama': 'AHZA HISYAM TAKARA', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 94.07, 'PKN': 95.87, 'Bahasa_Indonesia': 93.92, 'Matematika': 92.28, 'IPAS': 95.74, 'PJOK': 91.68, 'Seni_Budaya_dan_Prakarya': 91.69, 'Bahasa_Jawa': 92.21},
    {'nisn': '0128625389', 'nama': 'ALVIRA JASMINE TIRTA WIJAYA', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 90.83, 'PKN': 93.26, 'Bahasa_Indonesia': 90.84, 'Matematika': 89.41, 'IPAS': 92.14, 'PJOK': 91.03, 'Seni_Budaya_dan_Prakarya': 91.69, 'Bahasa_Jawa': 90.59},
    {'nisn': '3124901959', 'nama': 'AMALIA NATASYA PUTRI', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 89.6, 'PKN': 88.42, 'Bahasa_Indonesia': 89.17, 'Matematika': 87.39, 'IPAS': 87.97, 'PJOK': 89.1, 'Seni_Budaya_dan_Prakarya': 88.61, 'Bahasa_Jawa': 89.59},
    {'nisn': '3127107137', 'nama': 'ANUGERAH GOESTI MAGHFIRROH', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 89.82, 'PKN': 90.16, 'Bahasa_Indonesia': 89.4, 'Matematika': 89.48, 'IPAS': 89.28, 'PJOK': 90.85, 'Seni_Budaya_dan_Prakarya': 89.95, 'Bahasa_Jawa': 89.56},
    {'nisn': '0126654456', 'nama': 'ARMICO ZAKI FERDINAND', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 90.48, 'PKN': 92.31, 'Bahasa_Indonesia': 91.09, 'Matematika': 88.36, 'IPAS': 89.45, 'PJOK': 90.95, 'Seni_Budaya_dan_Prakarya': 90.15, 'Bahasa_Jawa': 89.72},
    {'nisn': '3123690570', 'nama': 'ARYA DANISH WIRATAMA', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 90.1, 'PKN': 91.08, 'Bahasa_Indonesia': 90.72, 'Matematika': 88.87, 'IPAS': 89.31, 'PJOK': 92.52, 'Seni_Budaya_dan_Prakarya': 90.31, 'Bahasa_Jawa': 89.44},
    {'nisn': '3122051447', 'nama': 'BERNARD ORIONT PRASETYO', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 90.61, 'PKN': 90.94, 'Bahasa_Indonesia': 90.63, 'Matematika': 89.12, 'IPAS': 91.23, 'PJOK': 91.25, 'Seni_Budaya_dan_Prakarya': 89.15, 'Bahasa_Jawa': 89.06},
    {'nisn': '3127642782', 'nama': 'DJENAR SYAHADAT', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 92.64, 'PKN': 93.83, 'Bahasa_Indonesia': 92.57, 'Matematika': 91.31, 'IPAS': 90.35, 'PJOK': 90.08, 'Seni_Budaya_dan_Prakarya': 92.51, 'Bahasa_Jawa': 89.79},
    {'nisn': '0137598221', 'nama': 'ELSHINTA KURNIA DANI', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 94.19, 'PKN': 93.18, 'Bahasa_Indonesia': 92.21, 'Matematika': 90.15, 'IPAS': 93.96, 'PJOK': 89.8, 'Seni_Budaya_dan_Prakarya': 91.05, 'Bahasa_Jawa': 90.46},
    {'nisn': '3129118276', 'nama': 'ENDREW DIAVASAN BRAMUNOV', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 93.87, 'PKN': 96.25, 'Bahasa_Indonesia': 94.65, 'Matematika': 92.8, 'IPAS': 96.39, 'PJOK': 93.42, 'Seni_Budaya_dan_Prakarya': 93.54, 'Bahasa_Jawa': 93.42},
    {'nisn': '3137492416', 'nama': 'FITRI EKA BUDIATI', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 90.18, 'PKN': 90.98, 'Bahasa_Indonesia': 91.04, 'Matematika': 88.99, 'IPAS': 89.88, 'PJOK': 89.75, 'Seni_Budaya_dan_Prakarya': 90.97, 'Bahasa_Jawa': 90.41},
    {'nisn': '0135147111', 'nama': 'GENDIS ALMAIRA WIHENDRA', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 92.06, 'PKN': 95.12, 'Bahasa_Indonesia': 93.52, 'Matematika': 92.19, 'IPAS': 94.95, 'PJOK': 91.17, 'Seni_Budaya_dan_Prakarya': 92.42, 'Bahasa_Jawa': 91.85},
    {'nisn': '0126900574', 'nama': 'JELITA ZASKIA SYAKIRA', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 92.05, 'PKN': 90.58, 'Bahasa_Indonesia': 89.9, 'Matematika': 88.82, 'IPAS': 88.35, 'PJOK': 90.87, 'Seni_Budaya_dan_Prakarya': 89.45, 'Bahasa_Jawa': 90.05},
    {'nisn': '3124750659', 'nama': 'KEISHA FADIYAH SYAHPUTRI', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 94.74, 'PKN': 96.48, 'Bahasa_Indonesia': 95.4, 'Matematika': 92.18, 'IPAS': 95.59, 'PJOK': 91.82, 'Seni_Budaya_dan_Prakarya': 93.36, 'Bahasa_Jawa': 93.15},
    {'nisn': '3122846563', 'nama': 'NAURA PUTRI FIKIRAWATI', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 96.86, 'PKN': 97.37, 'Bahasa_Indonesia': 96.26, 'Matematika': 93.98, 'IPAS': 96.39, 'PJOK': 92.17, 'Seni_Budaya_dan_Prakarya': 95.57, 'Bahasa_Jawa': 94.66},
    {'nisn': '3123119911', 'nama': 'NUR AZMEL ZAA GOEVANNI', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 89.56, 'PKN': 90.66, 'Bahasa_Indonesia': 89.78, 'Matematika': 87.76, 'IPAS': 88.8, 'PJOK': 88.55, 'Seni_Budaya_dan_Prakarya': 88.77, 'Bahasa_Jawa': 88.77},
    {'nisn': '0127315641', 'nama': 'RISKI ARDIANSYAH KURNIAWAN', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 91.33, 'PKN': 93.73, 'Bahasa_Indonesia': 90.97, 'Matematika': 89.33, 'IPAS': 94.65, 'PJOK': 90.98, 'Seni_Budaya_dan_Prakarya': 92.29, 'Bahasa_Jawa': 90.71},
    {'nisn': '3125592408', 'nama': 'RISTYO HELSA DIAH ANINDITA', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 91.77, 'PKN': 90.33, 'Bahasa_Indonesia': 90.74, 'Matematika': 88.65, 'IPAS': 92.35, 'PJOK': 90.28, 'Seni_Budaya_dan_Prakarya': 90.76, 'Bahasa_Jawa': 91.81},
    {'nisn': '3129393092', 'nama': 'SATRIYA SURYA ERLANGGA', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 90.02, 'PKN': 88.66, 'Bahasa_Indonesia': 89.05, 'Matematika': 89.22, 'IPAS': 89.22, 'PJOK': 90.82, 'Seni_Budaya_dan_Prakarya': 88.96, 'Bahasa_Jawa': 89.97},
    {'nisn': '0127652913', 'nama': 'SATWIKA PANCAR RAMADHANI', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 95.52, 'PKN': 97.0, 'Bahasa_Indonesia': 95.31, 'Matematika': 94.7, 'IPAS': 95.88, 'PJOK': 91.15, 'Seni_Budaya_dan_Prakarya': 94.36, 'Bahasa_Jawa': 94.19},
    {'nisn': '3128888277', 'nama': 'SHABRINA AQELA ASADEL', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 96.09, 'PKN': 97.36, 'Bahasa_Indonesia': 95.62, 'Matematika': 94.1, 'IPAS': 96.55, 'PJOK': 92.48, 'Seni_Budaya_dan_Prakarya': 94.32, 'Bahasa_Jawa': 93.61},
    {'nisn': '3121968029', 'nama': 'SUGMA WAHYU NURBAZYTH', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 90.43, 'PKN': 90.62, 'Bahasa_Indonesia': 90.08, 'Matematika': 89.95, 'IPAS': 92.63, 'PJOK': 92.29, 'Seni_Budaya_dan_Prakarya': 92.01, 'Bahasa_Jawa': 90.28},
    {'nisn': '3129082751', 'nama': 'YUMNA NURAINI ISMI CHOIRI', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 94.15, 'PKN': 97.41, 'Bahasa_Indonesia': 95.58, 'Matematika': 92.83, 'IPAS': 96.29, 'PJOK': 92.87, 'Seni_Budaya_dan_Prakarya': 94.75, 'Bahasa_Jawa': 93.05},
    {'nisn': '3129670331', 'nama': 'AHMAD DAMAR AL HAFIE', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 93.89, 'PKN': 92.96, 'Bahasa_Indonesia': 93.71, 'Matematika': 92.88, 'IPAS': 94.59, 'PJOK': 93.79, 'Seni_Budaya_dan_Prakarya': 93.28, 'Bahasa_Jawa': 92.87},
    {'nisn': '3129428054', 'nama': 'ALEXANDRA DEBORA TOMASOUW', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 91.79, 'PKN': 93.48, 'Bahasa_Indonesia': 92.7, 'Matematika': 91.0, 'IPAS': 92.3, 'PJOK': 90.81, 'Seni_Budaya_dan_Prakarya': 93.05, 'Bahasa_Jawa': 92.6},
    {'nisn': '0124335128', 'nama': 'ALVIANDRA ARDIANSYAH PUTRA', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 93.36, 'PKN': 92.38, 'Bahasa_Indonesia': 92.75, 'Matematika': 91.11, 'IPAS': 92.08, 'PJOK': 93.84, 'Seni_Budaya_dan_Prakarya': 91.56, 'Bahasa_Jawa': 91.81},
    {'nisn': '3121622335', 'nama': 'ALVIRA PUTRI', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 93.16, 'PKN': 93.75, 'Bahasa_Indonesia': 94.59, 'Matematika': 92.27, 'IPAS': 92.76, 'PJOK': 91.32, 'Seni_Budaya_dan_Prakarya': 93.83, 'Bahasa_Jawa': 92.7},
    {'nisn': '0136872886', 'nama': 'ANGGARA RACHADI SYAH PUTERA', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 94.84, 'PKN': 95.7, 'Bahasa_Indonesia': 95.36, 'Matematika': 94.73, 'IPAS': 94.74, 'PJOK': 92.14, 'Seni_Budaya_dan_Prakarya': 94.67, 'Bahasa_Jawa': 93.48},
    {'nisn': '3122414688', 'nama': 'AQILA BILQIS ANASTASYA', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 91.94, 'PKN': 93.8, 'Bahasa_Indonesia': 93.76, 'Matematika': 92.08, 'IPAS': 93.1, 'PJOK': 90.9, 'Seni_Budaya_dan_Prakarya': 93.07, 'Bahasa_Jawa': 92.96},
    {'nisn': '3134979139', 'nama': 'ARKA YANUAR PUTRA SANGADJI', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 90.14, 'PKN': 90.04, 'Bahasa_Indonesia': 90.17, 'Matematika': 88.95, 'IPAS': 90.37, 'PJOK': 90.31, 'Seni_Budaya_dan_Prakarya': 90.66, 'Bahasa_Jawa': 91.23},
    {'nisn': '0126408749', 'nama': 'BREEN ALIFAH QINANTHI ROCHIM', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 93.7, 'PKN': 95.77, 'Bahasa_Indonesia': 94.25, 'Matematika': 92.57, 'IPAS': 93.52, 'PJOK': 92.15, 'Seni_Budaya_dan_Prakarya': 93.58, 'Bahasa_Jawa': 92.79},
    {'nisn': '3128045374', 'nama': 'CLAUDYA NASCUA ALFA ANINDA', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 89.91, 'PKN': 89.89, 'Bahasa_Indonesia': 90.28, 'Matematika': 89.21, 'IPAS': 90.16, 'PJOK': 89.3, 'Seni_Budaya_dan_Prakarya': 91.03, 'Bahasa_Jawa': 89.58},
    {'nisn': '0138029295', 'nama': 'CUCU NAWA ARDIA SUNDARI', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 91.51, 'PKN': 92.63, 'Bahasa_Indonesia': 92.88, 'Matematika': 90.0, 'IPAS': 90.76, 'PJOK': 91.72, 'Seni_Budaya_dan_Prakarya': 91.78, 'Bahasa_Jawa': 92.31},
    {'nisn': '3129341712', 'nama': 'ELITA SEKAR AYU PUTRI SETIYADI', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 90.65, 'PKN': 90.22, 'Bahasa_Indonesia': 90.42, 'Matematika': 89.23, 'IPAS': 89.94, 'PJOK': 89.65, 'Seni_Budaya_dan_Prakarya': 90.0, 'Bahasa_Jawa': 89.49},
    {'nisn': '0121547612', 'nama': 'EMANNUEL DUTA SAKTI WIDODO', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 92.26, 'PKN': 91.34, 'Bahasa_Indonesia': 90.68, 'Matematika': 89.9, 'IPAS': 90.71, 'PJOK': 92.8, 'Seni_Budaya_dan_Prakarya': 90.74, 'Bahasa_Jawa': 91.84},
    {'nisn': '0123152500', 'nama': 'FAHRI AYDIN AFFANDI', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 92.61, 'PKN': 94.5, 'Bahasa_Indonesia': 93.21, 'Matematika': 91.36, 'IPAS': 92.16, 'PJOK': 90.28, 'Seni_Budaya_dan_Prakarya': 92.42, 'Bahasa_Jawa': 90.58},
    {'nisn': '0121934957', 'nama': 'HABIL ALWI SABTINO', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 90.36, 'PKN': 92.58, 'Bahasa_Indonesia': 90.55, 'Matematika': 90.32, 'IPAS': 91.38, 'PJOK': 89.55, 'Seni_Budaya_dan_Prakarya': 90.32, 'Bahasa_Jawa': 90.77},
    {'nisn': '0122289093', 'nama': 'ICEL OKTAVIANI', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 90.71, 'PKN': 91.16, 'Bahasa_Indonesia': 91.59, 'Matematika': 90.78, 'IPAS': 90.65, 'PJOK': 90.26, 'Seni_Budaya_dan_Prakarya': 91.65, 'Bahasa_Jawa': 91.78},
    {'nisn': '0127941920', 'nama': 'JOAN NOVIANTI', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 91.1, 'PKN': 91.7, 'Bahasa_Indonesia': 92.69, 'Matematika': 90.45, 'IPAS': 91.74, 'PJOK': 90.42, 'Seni_Budaya_dan_Prakarya': 91.52, 'Bahasa_Jawa': 90.56},
    {'nisn': '3128812573', 'nama': 'KEYZA ADYTTYA PUTRI SETYANTO', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 91.98, 'PKN': 92.22, 'Bahasa_Indonesia': 92.51, 'Matematika': 90.8, 'IPAS': 92.21, 'PJOK': 91.24, 'Seni_Budaya_dan_Prakarya': 92.18, 'Bahasa_Jawa': 92.28},
    {'nisn': '3124295967', 'nama': 'LINTANG WAHYU PURNAMA NINGTYAS', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 91.23, 'PKN': 90.15, 'Bahasa_Indonesia': 90.42, 'Matematika': 89.77, 'IPAS': 90.8, 'PJOK': 93.86, 'Seni_Budaya_dan_Prakarya': 90.32, 'Bahasa_Jawa': 91.84},
    {'nisn': '3129993463', 'nama': 'MOHAMMAD ADITYA WICAKSONO', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 92.33, 'PKN': 94.29, 'Bahasa_Indonesia': 91.93, 'Matematika': 89.72, 'IPAS': 91.95, 'PJOK': 90.51, 'Seni_Budaya_dan_Prakarya': 92.5, 'Bahasa_Jawa': 92.79},
    {'nisn': '3129373806', 'nama': 'MUHAMMAD NAHARDIKA RABBANI', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 91.3, 'PKN': 91.05, 'Bahasa_Indonesia': 90.49, 'Matematika': 89.03, 'IPAS': 90.37, 'PJOK': 89.47, 'Seni_Budaya_dan_Prakarya': 91.77, 'Bahasa_Jawa': 90.91},
    {'nisn': '0114520521', 'nama': 'MUKTI HERLAMBANG PUTRA', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 90.94, 'PKN': 90.88, 'Bahasa_Indonesia': 89.96, 'Matematika': 89.45, 'IPAS': 90.32, 'PJOK': 89.65, 'Seni_Budaya_dan_Prakarya': 90.12, 'Bahasa_Jawa': 91.63},
    {'nisn': '3128974773', 'nama': 'PAMBUDI AGUNG SANTIAJI', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 90.62, 'PKN': 91.14, 'Bahasa_Indonesia': 90.43, 'Matematika': 89.95, 'IPAS': 90.44, 'PJOK': 90.95, 'Seni_Budaya_dan_Prakarya': 90.94, 'Bahasa_Jawa': 91.8},
    {'nisn': '3129827744', 'nama': 'RADHITYAN ANIL FRADA', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 91.45, 'PKN': 90.68, 'Bahasa_Indonesia': 90.88, 'Matematika': 88.5, 'IPAS': 90.55, 'PJOK': 91.2, 'Seni_Budaya_dan_Prakarya': 90.54, 'Bahasa_Jawa': 90.7},
    {'nisn': '3122731454', 'nama': 'SALSABILLA LATIFA AZ-ZAHRA', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 91.0, 'PKN': 91.15, 'Bahasa_Indonesia': 91.49, 'Matematika': 89.3, 'IPAS': 90.67, 'PJOK': 91.12, 'Seni_Budaya_dan_Prakarya': 91.86, 'Bahasa_Jawa': 92.16},
    {'nisn': '0124025670', 'nama': 'SUKSMA FIDELA CANDRAWATI', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 94.52, 'PKN': 96.84, 'Bahasa_Indonesia': 96.06, 'Matematika': 95.32, 'IPAS': 94.74, 'PJOK': 91.71, 'Seni_Budaya_dan_Prakarya': 95.3, 'Bahasa_Jawa': 95.27},
    {'nisn': '3121664115', 'nama': 'TRIAFIKA RAMADHANI', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 93.54, 'PKN': 95.93, 'Bahasa_Indonesia': 94.92, 'Matematika': 93.52, 'IPAS': 94.09, 'PJOK': 91.62, 'Seni_Budaya_dan_Prakarya': 94.31, 'Bahasa_Jawa': 94.15},
    {'nisn': '3123146112', 'nama': 'WILDAN OCTAVIANO JENPRATAMA', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 89.63, 'PKN': 88.87, 'Bahasa_Indonesia': 89.48, 'Matematika': 87.92, 'IPAS': 89.32, 'PJOK': 89.39, 'Seni_Budaya_dan_Prakarya': 89.71, 'Bahasa_Jawa': 88.58},
    {'nisn': '0126197012', 'nama': 'ACHMAD MAULANA', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 91.3, 'PKN': 90.21, 'Bahasa_Indonesia': 89.92, 'Matematika': 88.5, 'IPAS': 91.48, 'PJOK': 90.93, 'Seni_Budaya_dan_Prakarya': 90.08, 'Bahasa_Jawa': 90.15},
    {'nisn': '3120046697', 'nama': 'AIRLANGGA ARYA YUDHA', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 92.75, 'PKN': 91.63, 'Bahasa_Indonesia': 91.31, 'Matematika': 92.08, 'IPAS': 92.62, 'PJOK': 92.07, 'Seni_Budaya_dan_Prakarya': 91.57, 'Bahasa_Jawa': 92.35},
    {'nisn': '3126860825', 'nama': 'AISYAH MAHARANI', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Prakerti': 95.49, 'PKN': 95.49, 'Bahasa_Indonesia': 95.37, 'Matematika': 94.37, 'IPAS': 96.2, 'PJOK': 94.73, 'Seni_Budaya_dan_Prakarya': 94.79, 'Bahasa_Jawa': 94.98},
    {'nisn': '0125559798', 'nama': 'ARIANDO ANUGERAH RISWANTO', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 93.81, 'PKN': 93.76, 'Bahasa_Indonesia': 92.6, 'Matematika': 91.85, 'IPAS': 92.85, 'PJOK': 93.67, 'Seni_Budaya_dan_Prakarya': 92.93, 'Bahasa_Jawa': 93.52},
    {'nisn': '3123961930', 'nama': 'ARVINANDA APTA GHAISANI', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 93.92, 'PKN': 93.29, 'Bahasa_Indonesia': 92.79, 'Matematika': 91.99, 'IPAS': 93.29, 'PJOK': 92.85, 'Seni_Budaya_dan_Prakarya': 92.43, 'Bahasa_Jawa': 92.53},
    {'nisn': '0121065877', 'nama': 'AURA ANGEL KUSUMA', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 92.4, 'PKN': 91.42, 'Bahasa_Indonesia': 90.78, 'Matematika': 91.57, 'IPAS': 92.33, 'PJOK': 92.4, 'Seni_Budaya_dan_Prakarya': 91.79, 'Bahasa_Jawa': 92.26},
    {'nisn': '3123557411', 'nama': 'AZKA FABRILIAN CAHYA ARKHAREGA', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 92.95, 'PKN': 91.84, 'Bahasa_Indonesia': 91.09, 'Matematika': 91.48, 'IPAS': 91.33, 'PJOK': 93.25, 'Seni_Budaya_dan_Prakarya': 90.92, 'Bahasa_Jawa': 92.85},
    {'nisn': '3128999279', 'nama': 'CLEARESTA MARVA ZONDA MAHESWARA', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 92.25, 'PKN': 89.77, 'Bahasa_Indonesia': 89.57, 'Matematika': 91.14, 'IPAS': 91.09, 'PJOK': 91.61, 'Seni_Budaya_dan_Prakarya': 89.51, 'Bahasa_Jawa': 91.3},
    {'nisn': '3139783072', 'nama': 'FAREL FEBRI ERWANSYAH', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 89.98, 'PKN': 88.98, 'Bahasa_Indonesia': 89.55, 'Matematika': 89.9, 'IPAS': 89.92, 'PJOK': 90.33, 'Seni_Budaya_dan_Prakarya': 90.11, 'Bahasa_Jawa': 90.49},
    {'nisn': '0128710725', 'nama': 'FATASHA CAHYANING PUSPITASARI', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 91.11, 'PKN': 90.43, 'Bahasa_Indonesia': 89.24, 'Matematika': 89.69, 'IPAS': 89.75, 'PJOK': 91.15, 'Seni_Budaya_dan_Prakarya': 90.98, 'Bahasa_Jawa': 91.09},
    {'nisn': '0123244790', 'nama': 'FIO ANANTA PUTRI', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 90.59, 'PKN': 89.73, 'Bahasa_Indonesia': 88.87, 'Matematika': 90.05, 'IPAS': 89.54, 'PJOK': 91.19, 'Seni_Budaya_dan_Prakarya': 89.23, 'Bahasa_Jawa': 90.53},
    {'nisn': '3121671698', 'nama': 'HELGA RIZKY IBRAHIM PRASETYO', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 93.48, 'PKN': 91.87, 'Bahasa_Indonesia': 91.48, 'Matematika': 91.88, 'IPAS': 93.11, 'PJOK': 93.0, 'Seni_Budaya_dan_Prakarya': 91.31, 'Bahasa_Jawa': 92.95},
    {'nisn': '0133140384', 'nama': 'KHAIRA SYIFA SALSABILA', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 92.7, 'PKN': 91.84, 'Bahasa_Indonesia': 91.44, 'Matematika': 91.37, 'IPAS': 91.79, 'PJOK': 92.98, 'Seni_Budaya_dan_Prakarya': 92.05, 'Bahasa_Jawa': 92.76},
    {'nisn': '3126038717', 'nama': 'MUCHLIS PUTRA RIYADINA', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 89.4, 'PKN': 88.34, 'Bahasa_Indonesia': 87.67, 'Matematika': 87.94, 'IPAS': 89.27, 'PJOK': 92.52, 'Seni_Budaya_dan_Prakarya': 88.3, 'Bahasa_Jawa': 89.23},
    {'nisn': '3122270874', 'nama': 'MUCHSIN PUTRA RIYADINA', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 89.38, 'PKN': 88.54, 'Bahasa_Indonesia': 87.86, 'Matematika': 87.97, 'IPAS': 89.26, 'PJOK': 92.66, 'Seni_Budaya_dan_Prakarya': 88.77, 'Bahasa_Jawa': 89.34},
    {'nisn': '3129361140', 'nama': 'MUHAMMAD JANNED PASHA ISLAMY', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 90.79, 'PKN': 89.39, 'Bahasa_Indonesia': 89.66, 'Matematika': 89.61, 'IPAS': 90.92, 'PJOK': 93.4, 'Seni_Budaya_dan_Prakarya': 89.42, 'Bahasa_Jawa': 90.78},
    {'nisn': '3121790843', 'nama': 'MUHAMMAD ZIDAN ARDHIANSYAH', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 91.21, 'PKN': 89.99, 'Bahasa_Indonesia': 89.97, 'Matematika': 90.21, 'IPAS': 91.13, 'PJOK': 93.14, 'Seni_Budaya_dan_Prakarya': 90.32, 'Bahasa_Jawa': 91.51},
    {'nisn': '3126633975', 'nama': 'MUTIARA SEKAR ARUM', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 90.79, 'PKN': 88.56, 'Bahasa_Indonesia': 88.83, 'Matematika': 87.89, 'IPAS': 89.47, 'PJOK': 90.91, 'Seni_Budaya_dan_Prakarya': 89.91, 'Bahasa_Jawa': 89.12},
    {'nisn': '0122551410', 'nama': 'NURI AULIA SYAFA', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 89.15, 'PKN': 88.0, 'Bahasa_Indonesia': 87.7, 'Matematika': 88.33, 'IPAS': 87.59, 'PJOK': 89.68, 'Seni_Budaya_dan_Prakarya': 88.24, 'Bahasa_Jawa': 88.89},
    {'nisn': '3123146571', 'nama': 'RAHADHIKA RIZKY RABBANI', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 93.04, 'PKN': 93.44, 'Bahasa_Indonesia': 92.65, 'Matematika': 93.73, 'IPAS': 93.24, 'PJOK': 92.75, 'Seni_Budaya_dan_Prakarya': 93.46, 'Bahasa_Jawa': 92.72},
    {'nisn': '3121251235', 'nama': 'RAYZA HOTOTO', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 89.3, 'PKN': 88.35, 'Bahasa_Indonesia': 88.31, 'Matematika': 88.05, 'IPAS': 87.57, 'PJOK': 91.39, 'Seni_Budaya_dan_Prakarya': 89.54, 'Bahasa_Jawa': 88.91},
    {'nisn': '3124026354', 'nama': 'RIFAYA NAURAISHA RIANTO', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 90.8, 'PKN': 88.46, 'Bahasa_Indonesia': 89.06, 'Matematika': 89.89, 'IPAS': 89.88, 'PJOK': 90.98, 'Seni_Budaya_dan_Prakarya': 89.7, 'Bahasa_Jawa': 90.59},
    {'nisn': '0123881787', 'nama': 'RISMA LIBRIAN PUTRI', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 90.98, 'PKN': 88.8, 'Bahasa_Indonesia': 89.27, 'Matematika': 88.59, 'IPAS': 89.86, 'PJOK': 91.63, 'Seni_Budaya_dan_Prakarya': 90.1, 'Bahasa_Jawa': 90.89},
    {'nisn': '3122377844', 'nama': 'SANDIRA BUNGA SAYEKTI', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 94.09, 'PKN': 93.15, 'Bahasa_Indonesia': 92.58, 'Matematika': 92.73, 'IPAS': 92.85, 'PJOK': 93.52, 'Seni_Budaya_dan_Prakarya': 91.9, 'Bahasa_Jawa': 93.66},
    {'nisn': '3129237654', 'nama': 'SATRIA RASYA ADHITYA RASYID', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 92.3, 'PKN': 91.42, 'Bahasa_Indonesia': 90.77, 'Matematika': 91.56, 'IPAS': 92.6, 'PJOK': 94.08, 'Seni_Budaya_dan_Prakarya': 90.6, 'Bahasa_Jawa': 92.17},
    {'nisn': '3133499425', 'nama': 'SHAFIRA AULIA NISA', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 92.6, 'PKN': 91.76, 'Bahasa_Indonesia': 91.34, 'Matematika': 92.48, 'IPAS': 92.63, 'PJOK': 92.82, 'Seni_Budaya_dan_Prakarya': 92.05, 'Bahasa_Jawa': 91.6},
    {'nisn': '0125972861', 'nama': 'SILVIANA REGINA PUTRI', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 90.92, 'PKN': 89.59, 'Bahasa_Indonesia': 89.0, 'Matematika': 88.0, 'IPAS': 89.7, 'PJOK': 91.06, 'Seni_Budaya_dan_Prakarya': 88.9, 'Bahasa_Jawa': 90.43},
    {'nisn': '3126103877', 'nama': 'WAODE ARDEEVA FLOCITA', 'status': 'Lulus', 'Pendidikan_Agama_dan_Budi_Pekerti': 91.36, 'PKN': 90.2, 'Bahasa_Indonesia': 89.14, 'Matematika': 89.9, 'IPAS': 91.21, 'PJOK': 91.32, 'Seni_Budaya_dan_Prakarya': 90.07, 'Bahasa_Jawa': 91.36}
]
# ==============================================================================


# Konfigurasi halaman
st.set_page_config(page_title="Portal Kelulusan SDN 01 Taman Kota Madiun", page_icon="🎓", layout="centered")


# --- Bagian Sambutan ---
st.markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <h2 style="color: #1E8449;">Selamat Datang di Portal Kelulusan</h2>
        <h3 style="color: #239B56;">SDN 01 Taman Kota Madiun</h3>
        <p style="font-size: 1.1em;">Tahun Pelajaran 2024/2025</p>
    </div>
""", unsafe_allow_html=True)
st.markdown("---")

st.markdown("""
    <div style="padding: 15px; border-radius: 5px; margin-bottom:25px;">
        <h4 style="text-align: center; margin-bottom: 15px;">Sambutan Kepala Sekolah</h4>
        <p style="text-align: justify; text-indent: 2em;">
            Dengan penuh rasa syukur dan bangga, saya menyampaikan ucapan selamat kepada seluruh siswa kelas 6 yang telah menyelesaikan perjalanan belajar selama 6 tahun di SDN 01 Taman Kota Madiun.
        </p>
        <p style="text-align: justify; text-indent: 2em;">
            Perjalanan yang kalian tempuh penuh dengan perjuangan, ketekunan, dan kerja keras. Kalian telah tumbuh menjadi pribadi yang cerdas, berakhlak mulia, dan siap menghadapi tantangan di jenjang pendidikan selanjutnya.
        </p>
        <p style="text-align: justify; text-indent: 2em;">
            Selamat melanjutkan ke jenjang pendidikan yang lebih tinggi. Jadilah generasi penerus bangsa yang membanggakan!
        </p>
        <p style="text-align: justify;">Wassalamu'alaikum Wr. Wb.</p>
        <p style="text-align: right; font-style: italic; margin-top: 20px; line-height: 1.5;">
            Sukana, S.Pd., M.Pd.<br>
            Kepala SDN 01 Taman Kota Madiun
        </p>
    </div>
""", unsafe_allow_html=True)

# --- Bagian Cek Kelulusan ---
st.markdown("""
    <div style="text-align: center; padding-top: 10px; padding-bottom:10px;">
        <h1 style="color: #2E86C1;">CEK KELULUSAN SISWA</h1>
        <p style="font-size: 17px;">Masukkan NISN Anda di bawah untuk melihat status kelulusan dan nilai.</p>
    </div>
""", unsafe_allow_html=True)
st.markdown("---")

nisn_input = st.text_input("📌 Masukkan NISN:", placeholder="Ketik NISN Anda di sini...")

if st.button("🔍 Cek Kelulusan"):
    if not data_siswa:
        st.error("Data siswa belum dimasukkan ke dalam kode aplikasi.")
    elif not nisn_input.strip():
        st.warning("⚠️ Masukkan NISN terlebih dahulu.")
    else:
        nisn_cari = nisn_input.strip()
        siswa_ditemukan = None
        for siswa in data_siswa:
            if siswa["nisn"] == nisn_cari:
                siswa_ditemukan = siswa
                break

        if siswa_ditemukan:
            st.success(f"NISN: **{siswa_ditemukan['nisn']}**")
            st.success(f"Nama: **{siswa_ditemukan['nama']}**")

            st.balloons()
            st.markdown(f"<h3 style='color: green;'>🎉 Selamat! Kamu dinyatakan <u>{siswa_ditemukan['status'].upper()}</u>.</h3>", unsafe_allow_html=True)
            st.markdown("---")
            st.markdown("#### Transkrip Nilai:")

            data_nilai_tampil = {}
            kolom_non_nilai_internal = ["nisn", "nama", "status"]
            total_nilai_numerik = 0
            jumlah_mapel_numerik = 0
            semua_nilai_numerik_valid = True # Flag untuk mengecek apakah semua nilai bisa dihitung rata-ratanya

            for key, value in siswa_ditemukan.items():
                if key.lower() not in kolom_non_nilai_internal:
                    nama_mapel_bersih = key.replace("_", " ").title()
                    data_nilai_tampil[nama_mapel_bersih] = value
                    
                    try:
                        nilai_float = float(value)
                        total_nilai_numerik += nilai_float
                        jumlah_mapel_numerik += 1
                    except (ValueError, TypeError):
                        # Jika ada nilai yang tidak bisa dikonversi ke float,
                        # tandai bahwa tidak semua nilai valid untuk rata-rata
                        semua_nilai_numerik_valid = False 
            
            if data_nilai_tampil:
                # Menggunakan pandas untuk st.table agar tampilan lebih rapi
                # Jika pandas tidak ingin digunakan sama sekali, bagian ini bisa diganti loop st.write
                df_tampil_nilai = pd.DataFrame(list(data_nilai_tampil.items()), columns=['Mata Pelajaran', 'Nilai'])
                st.table(df_tampil_nilai.set_index('Mata Pelajaran'))

                if jumlah_mapel_numerik > 0: # Hanya hitung rata-rata jika ada nilai numerik
                    rata_rata = total_nilai_numerik / jumlah_mapel_numerik
                    st.markdown(f"**Rata-rata Nilai (Mapel Ternilai):** **{rata_rata:.2f}**")
                    # Beri catatan jika tidak semua mapel yang ditampilkan memiliki nilai numerik valid
                    if not semua_nilai_numerik_valid or jumlah_mapel_numerik < len(data_nilai_tampil):
                         st.caption("Rata-rata hanya dihitung untuk mata pelajaran dengan nilai numerik yang valid.")
                else: # Jika tidak ada sama sekali nilai numerik
                    st.info("Tidak ada nilai numerik untuk dihitung rata-ratanya.")
            else:
                st.warning("Tidak ada data nilai untuk ditampilkan untuk siswa ini.")

        else:
            st.error(f"🚫 NISN '{nisn_cari}' tidak ditemukan. Pastikan NISN yang Anda masukkan benar.")

# --- Footer ---
st.markdown("---")
st.markdown("""
    <div style="text-align: center; padding-top: 15px; padding-bottom: 5px;">
        <small>© 2025 SDN 01 TAMAN KOTA MADIUN</small><br>
        <small>Dikembangkan dengan ❤️ menggunakan Streamlit</small>
    </div>
""", unsafe_allow_html=True)