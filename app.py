import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🚗 Estimasi Waktu Perjalanan (Fisika)")
st.write("Menggunakan konsep fisika: t = s / v")

# Input
jarak = st.number_input("Masukkan jarak (km):", min_value=0.0)
kecepatan = st.number_input("Masukkan kecepatan (km/jam):", min_value=0.1)
kondisi = st.selectbox("Pilih kondisi jalan:", ["Lancar", "Sedang", "Macet"])
berhenti = st.number_input("Waktu berhenti (menit):", min_value=0.0)

if st.button("Hitung"):
    if kondisi == "Macet":
        kecepatan *= 0.5
    elif kondisi == "Sedang":
        kecepatan *= 0.75

    waktu_jam = jarak / kecepatan
    waktu_menit = waktu_jam * 60 + berhenti

    st.success(f"⏱️ Total waktu perjalanan: {waktu_menit:.2f} menit")

    # Grafik
    waktu = np.linspace(0, waktu_menit, 100)
    posisi = (jarak / waktu_menit) * waktu

    fig, ax = plt.subplots()
    ax.plot(waktu, posisi)
    ax.set_xlabel("Waktu (menit)")
    ax.set_ylabel("Jarak (km)")
    ax.set_title("Grafik Perjalanan")

    st.pyplot(fig)
