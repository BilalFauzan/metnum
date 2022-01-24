#Nama : Bilal Fauzan
#NIM : 12220023

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image
from math import e

################## title #################
st.set_page_config(
    page_title="Metode Numerik Teknik Perminyakan",
    page_icon="logo.png",
    layout="wide",
    menu_items={
         'About': "Nama : Bilal Fauzan \n NIM : 12220023"
    }
    )
      # this needs to be the first Streamlit command called
colT1,colT2 = st.columns([2,8])
with colT2:
    st.title("Metode Numerik Teknik Perminyakan ")
st.markdown("*Kelas 02")
###########################################

############### sidebar ###############
image2 = Image.open('self.jpg')
st.sidebar.title("Bilal Fauzan (12220023)")
st.sidebar.image(image2)
########################################

##### User inputs on the control panel #####
st.sidebar.header("Pengaturan Konfigurasi Tampilan")
st.sidebar.subheader("Tugas 01")
t=st.sidebar.number_input('Masukkan Nilai T (sekon)', value=12, min_value=0)
interval=st.sidebar.number_input('Masukkan Interval Waktu (sekon)', value=2.0, min_value=1.0)
c=st.sidebar.number_input("Masukkan Nilai C (kg/s)", value=12.5, min_value=0.01)
#################################################

############### Tugas 01 ###############
col1, col2 = st.columns([3,2])
col1.subheader("Tugas 01")

g=9.81
m=68.1
x=0.0
t1=0.0
v1=0.0
t2=interval

list_num=[]
list_analitik=[]
list_t=[]

while x<=t:
    if t1==0.0:
        v2=0.0
    else:
        v2=v1+(g-(c/m*v1))*(t2-t1)
    v_analitik= g*m/c*(1.0-(e**(-(c/m)*t1)))
    list_t.append(t1)
    v1=v2
    t1=t2
    t2=t2+interval
    x+=interval
    list_num.append(v2)
    list_analitik.append(v_analitik)

fig, ax = plt.subplots()
ax.plot(list_t,list_analitik, linestyle="-", marker="o", label="v(t) Solusi Analitik")
ax.plot(list_t,list_num, linestyle="-", marker="o", label="v(t) Solusi Numerik")
ax.set_title(f"Solusi Analitik VS Solusi Numerik (c={c})", fontsize=16)
ax.set_xlabel("t(s)", fontsize=12)
ax.set_ylabel("v(m/s)", fontsize=12)
ax.grid(axis='both')
ax.legend()
ax.set_axisbelow(True)
plt.tight_layout()
col1.pyplot(fig)

col2.subheader("Tabel")
df_view3 = pd.DataFrame(
    {'Waktu (t)': list_t,'Solusi Analitik': list_analitik,
     'Solusi Numerik': list_num
     })
col2.dataframe(df_view3)
########################################
