# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

# Setting Layout
st.set_page_config(layout="wide")

# Add Title and Tabs
st.title("Proyek Analisis Data: Bike Sharing Dataset")
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(
    ["Pertanyaan 1", "Pertanyaan 2", "Pertanyaan 3", "Pertanyaan 4", 
     "Pertanyaan 5", "Pertanyaan 6", "Pertanyaan 7", "Pertanyaan 8", "Pertanyaan 9"])

# Import Dataframe
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

# Change the Data Type of the "dteday" Column 
day_df["dteday"] = pd.to_datetime(day_df["dteday"])
hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

# Define bins for temperature
temp_bins = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
temp_labels = ['Very Low', 'Low', 'Medium', 'High', 'Very High']

# Create a new column 'temp_category' based on the bins
day_df['temp_category'] = pd.cut(day_df['temp'], bins=temp_bins, labels=temp_labels, include_lowest=True)

# Add Content to Tab
with tab1:
    st.header("Pada tahun berapa permintaan penyewaan sepeda terbanyak?")
    yearly_df = day_df.resample('YE', on='dteday').sum(numeric_only=True)
    yearly_df = yearly_df.reset_index()

    yearly_df['dteday'] = ["2011", "2012"]

    plt.figure(figsize=(12, 8))
    plt.bar(yearly_df['dteday'], yearly_df['cnt'], color='#ff9800')

    for i in range(len(yearly_df['dteday'])):
        plt.text(i, yearly_df['cnt'][i],
                str(yearly_df['cnt'][i]), ha='center', va='bottom')

    plt.xlabel('Tahun')
    plt.ylabel('Jumlah Penyewaan Sepeda')
    plt.title('Penyewaan Sepeda Sepanjang Waktu (Berdasarkan Tahun)')
    plt.grid(axis='y')
    plt.tight_layout()
    plt.gca().yaxis.set_major_formatter(
        plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    plt.show()

    st.pyplot(plt)

    st.caption("Kesimpulan: Tren penyewaan sepeda menunjukkan peningkatan signifikan dari 1.243.103 penyewaan pada 2011 menjadi 2.049.576 pada 2012. Kenaikan ini menandakan bahwa terjadi kenaikan peminat dalam kurun 1 tahun.")

with tab2:
    st.header("Pada bulan apa saja permintaan penyewaan sepeda biasanya mencapai puncaknya?")
    monthly_df = day_df.resample('ME', on='dteday').sum(numeric_only=True)
    monthly_df = monthly_df.reset_index()

    monthly_df['dteday'] = ["Jan 2011", "Feb 2011", "Mar 2011",
                            "Apr 2011", "Mei 2011", "Jun 2011",
                            "Jul 2011", "Agu 2011", "Sep 2011",
                            "Okt 2011", "Nov 2011", "Des 2011",
                            "Jan 2012", "Feb 2012", "Mar 2012",
                            "Apr 2012", "Mei 2012", "Jun 2012",
                            "Jul 2012", "Agu 2012", "Sep 2012",
                            "Okt 2012", "Nov 2012", "Des 2012"]

    plt.figure(figsize=(12, 8))
    plt.plot(monthly_df['dteday'], monthly_df['cnt'], color='#ff9800')
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Penyewaan Sepeda')
    plt.title('Penyewaan Sepeda Sepanjang Waktu (Berdasarkan Bulan dan tahun)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    st.pyplot(plt)

    st.caption("Kesimpulan: tren penyewaan sepeda dari Q1 2011 hingga Q4 2012, dengan jumlah penyewaan mengalami fluktuasi. Terdapat peningkatan signifikan pada Q2 2012, mencapai puncaknya di atas 600.000 penyewaan, sebelum mengalami penurunan di Q4 2012. Kenaikan ini mencerminkan minat yang tinggi terhadap layanan penyewaan sepeda, sementara penurunan di akhir tahun mungkin disebabkan oleh faktor musiman.")

with tab3:
    st.header("Pada Kuartil apa saja permintaan penyewaan sepeda biasanya mencapai puncaknya?")
    quartilery_df = day_df.resample('QE', on='dteday').sum(numeric_only=True)
    quartilery_df = quartilery_df.reset_index()

    quartilery_df['dteday'] = ["Q1 2011", "Q2 2011", "Q3 2011", "Q4 2011",
                            "Q1 2012", "Q2 2012", "Q3 2012", "Q4 2012"]

    plt.figure(figsize=(12, 8))
    plt.plot(quartilery_df['dteday'], quartilery_df['cnt'], color='#ff9800')
    plt.xlabel('Kuartal')
    plt.ylabel('Jumlah Penyewaan Sepeda')
    plt.title('Penyewaan Sepeda Sepanjang Waktu (Berdasarkan Kuartal dan tahun)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    st.pyplot(plt)

    st.caption("Kesimpulan: tren penyewaan sepeda dari Januari 2011 hingga Desember 2012, dengan jumlah penyewaan meningkat secara signifikan dari awal 2011 hingga pertengahan 2012. Puncak penyewaan terjadi pada pertengahan 2012.")

with tab4:
    st.header("Pada bulan apa saja yang memiliki permintaan penyewaan sepeda paling sedikit dan paling banyak?")
    monthly_agg = day_df.groupby(by="mnth").agg({
    "instant": "nunique",
    "cnt": ["max", "min"]
    })

    monthly_agg = monthly_agg.reset_index()

    monthly_agg['mnth'] = ["Jan", "Feb", "Mar", "Apr",
                        "Mei", "Jun", "Jul", "Agu",
                        "Sep", "Okt", "Nov", "Des"]

    plt.figure(figsize=(12, 8))
    plt.bar(monthly_agg['mnth'], monthly_agg['cnt']['max'],
            label= "Nilai Maksimal", color='#ff9800')
    plt.bar(monthly_agg['mnth'], monthly_agg['cnt']['min'],
            label= "Nilai Minimal", color='#ffeb3b')

    for i in range(len(monthly_agg['mnth'])):
        plt.text(i, monthly_agg['cnt']['max'][i],
                str(monthly_agg['cnt']['max'][i]),
                ha='center', va='bottom')
        plt.text(i, monthly_agg['cnt']['min'][i],
                str(monthly_agg['cnt']['min'][i]),
                ha='center', va='bottom')

    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Penyewaan Sepeda')
    plt.title('Penyewaan Sepeda Sepanjang Waktu (Berdasarkan Bulan)')
    plt.legend(loc="upper left")
    plt.grid(axis='y')
    plt.tight_layout()
    plt.gca().yaxis.set_major_formatter(
        plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    plt.show()

    st.pyplot(plt)

    st.caption("Kesimpulan: jumlah penyewaan sepeda per bulan dengan puncak tertinggi pada bulan September dengan 8.714 penyewaan dan permintaan penyewaan paling sedikit terdapat pada bulan Oktober dengan 22 penyewaan.")

with tab5:
    st.header("Pada hari apa saja yang memiliki permintaan penyewaan sepeda paling sedikit dan paling banyak?")
    dayly_agg = day_df.groupby(by="weekday").agg({
    "instant": "nunique",
    "cnt": ["max", "min"]
    })

    dayly_agg = dayly_agg.reset_index()

    dayly_agg['weekday'] = ["Minggu", "Senin", "Selasa",
                            "Rabu", "Kamis", "Jumat", "Sabtu"]

    plt.figure(figsize=(12, 8))
    plt.bar(dayly_agg['weekday'], dayly_agg['cnt']['max'],
            label= "Nilai Maksimal", color='#ff9800')
    plt.bar(dayly_agg['weekday'], dayly_agg['cnt']['min'],
            label= "Nilai Minimal", color='#ffeb3b')

    for i in range(len(dayly_agg['weekday'])):
        plt.text(i, dayly_agg['cnt']['max'][i],
                str(dayly_agg['cnt']['max'][i]), ha='center', va='bottom')
        plt.text(i, dayly_agg['cnt']['min'][i],
                str(dayly_agg['cnt']['min'][i]), ha='center', va='bottom')

    plt.xlabel('Hari')
    plt.ylabel('Jumlah Penyewaan Sepeda')
    plt.title('Penyewaan Sepeda Sepanjang Waktu (Berdasarkan Hari)')
    plt.legend(loc="upper left")
    plt.grid(axis='y')
    plt.tight_layout()
    plt.gca().yaxis.set_major_formatter(
        plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    plt.show()

    st.pyplot(plt)

    st.caption("Kesimpulan: jumlah penyewaan sepeda berdasarkan hari dengan puncak tertinggi pada hari Sabtu dengan 8.714 penyewaan dan permintaan penyewaan paling sedikit terdapat pada hari Senin dengan 22 penyewaan.")

with tab6:
    st.header("Pada jam berapa saja yang memiliki permintaan penyewaan sepeda paling sedikit dan paling banyak?")
    hourly_agg = hour_df.groupby(by="hr").agg({
    "instant": "nunique",
    "cnt": ["max", "min"]
    })

    hourly_agg = hourly_agg.reset_index()
    hourly_agg['hr'] = ["00.00", "01.00", "02.00", "03.00",
                        "04.00", "05.00", "06.00", "07.00",
                        "08.00", "09.00", "10.00", "11.00",
                        "12.00", "13.00", "14.00", "15.00",
                        "16.00", "17.00", "18.00", "19.00",
                        "20.00", "21.00", "22.00", "23.00"]

    plt.figure(figsize=(12, 8))
    plt.bar(hourly_agg['hr'], hourly_agg['cnt']['max'],
            label= "Nilai Maksimal", color='#ff9800')
    plt.bar(hourly_agg['hr'], hourly_agg['cnt']['min'],
            label= "Nilai Minimal", color='#ffeb3b')

    for i in range(len(hourly_agg['hr'])):
        plt.text(i, hourly_agg['cnt']['max'][i],
                str(hourly_agg['cnt']['max'][i]), ha='center', va='bottom')
        plt.text(i, hourly_agg['cnt']['min'][i],
                str(hourly_agg['cnt']['min'][i]), ha='center', va='bottom')

    plt.xlabel('Jam')
    plt.ylabel('Jumlah Penyewaan Sepeda')
    plt.title('Penyewaan Sepeda Sepanjang Waktu (Berdasarkan Jam)')
    plt.legend(loc="upper left")
    plt.grid(axis='y')
    plt.tight_layout()
    plt.gca().yaxis.set_major_formatter(
        plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    plt.show()

    st.pyplot(plt)

    st.caption("Kesimpulan: jumlah penyewaan sepeda berdasarkan jam dengan puncak tertinggi pada jam 18.00 dengan 977 penyewaan dan permintaan paling sedikit terdapat pada jam 01.00 - 07.00 dengan 1 penyewaan")

with tab7:
    st.header("Pada musim apa saja yang memiliki permintaan penyewaan sepeda paling sedikit dan paling banyak?")
    seasonly_df = day_df.groupby(by="season", observed=False).agg({
    "instant": "nunique",
    "cnt": ["max", "min"]
    })

    seasonly_df = seasonly_df.reset_index()

    seasonly_df['season'] = ["Springer", "Summer", "Fall", "Winter"]
    plt.figure(figsize=(12, 8))
    plt.bar(seasonly_df['season'], seasonly_df['cnt']['max'],
            label= "Nilai Maksimal", color='#ff9800')
    plt.bar(seasonly_df['season'], seasonly_df['cnt']['min'],
            label= "Nilai Minimal", color='#ffeb3b')

    for i in range(len(seasonly_df['season'])):
        plt.text(i, seasonly_df['cnt']['max'][i],
                str(seasonly_df['cnt']['max'][i]), ha='center', va='bottom')
        plt.text(i, seasonly_df['cnt']['min'][i],
                str(seasonly_df['cnt']['min'][i]), ha='center', va='bottom')

    plt.xlabel('Musim')
    plt.ylabel('Jumlah Penyewaan Sepeda')
    plt.title('Penyewaan Sepeda Sepanjang Waktu (Berdasarkan Musim)')
    plt.legend(loc="upper left")
    plt.grid(axis='y')
    plt.tight_layout()
    plt.gca().yaxis.set_major_formatter(
        plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    plt.show()

    st.pyplot(plt)

    st.caption("Kesimpulan: jumlah penyewaan sepeda berdasarkan musim dengan puncak tertinggi pada musim Fall/Musim gugur dengan 8.714 penyewaan dan permintaan paling sedikit terdapat pada musim Winter/Musim dingin dengan 22 penyewaan.")

with tab8:
    st.header("Pengaruh permintaan penyewaan sepeda berdasarkan cuaca?")
    weather_agg = day_df.groupby(by="weathersit", observed=False).agg({
    "instant": "nunique",
    "cnt": ["max", "min"]
    })

    weather_agg = weather_agg.reset_index()

    weather_agg["weathersit"] = ["Clear", "Mist", "Heavy Rain"]
    plt.figure(figsize=(12, 8))
    plt.bar(weather_agg['weathersit'], weather_agg['cnt']['max'],
            label= "Nilai Maksimal", color='#ff9800')
    plt.bar(weather_agg['weathersit'], weather_agg['cnt']['min'],
            label= "Nilai Minimal", color='#ffeb3b')

    for i in range(len(weather_agg['weathersit'])):
        plt.text(i, weather_agg['cnt']['max'][i],
                str(weather_agg['cnt']['max'][i]), ha='center', va='bottom')
        plt.text(i, weather_agg['cnt']['min'][i],
                str(weather_agg['cnt']['min'][i]), ha='center', va='bottom')

    plt.xlabel('Cuaca')
    plt.ylabel('Jumlah Penyewaan Sepeda')
    plt.title('Penyewaan Sepeda Sepanjang Waktu (Berdasarkan Cuaca)')
    plt.grid(axis='y')
    plt.tight_layout()
    plt.legend(loc="upper left")
    plt.gca().yaxis.set_major_formatter(
        plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    plt.show()

    st.pyplot(plt)

    st.caption("Kesimpulan: jumlah penyewaan sepeda berdasarkan cuaca dengan puncak tertinggi pada saat cuaca Clear/Cerah dengan 8.714 penyewaan dan permintaan paling sedikit terdapat pada saat cuaca Heavy Rain/Hujan deras dengan 22 penyewaan.")

with tab9:
    st.header("Saat suhu temperatur apa yang mempengaruhi permintaan penyewaan sepeda?")
    temp_df = day_df.groupby(by="temp_category", observed=False).agg({
    "instant": "nunique",
    "cnt": ["max", "min"]
    })

    temp_df = temp_df.reset_index()

    temp_df['temp_category'] = ["Very Low", "Low",
                                "Medium", "High", "Very High"]

    plt.figure(figsize=(12, 8))
    plt.bar(temp_df['temp_category'], temp_df['cnt']['max'],
            label= "Nilai Maksimal", color='#ff9800')
    plt.bar(temp_df['temp_category'], temp_df['cnt']['min'],
            label= "Nilai Minimal", color='#ffeb3b')

    for i in range(len(temp_df['temp_category'])):
        plt.text(i, temp_df['cnt']['max'][i],
                str(temp_df['cnt']['max'][i]), ha='center', va='bottom')
        plt.text(i, temp_df['cnt']['min'][i],
                str(temp_df['cnt']['min'][i]), ha='center', va='bottom')

    plt.xlabel('Temperatur')
    plt.ylabel('Jumlah Penyewaan Sepeda')
    plt.title('Penyewaan Sepeda Sepanjang Waktu (Berdasarkan Temperatur)')
    plt.grid(axis='y')
    plt.tight_layout()

    st.pyplot(plt)

    st.caption("Kesimpulan:  jumlah penyewaan sepeda berdasarkan suhu temperatur dengan puncak tertinggi pada suhu High dengan 8.714 penyewaan dan permintaan paling sedikit terdapat pada suhu Medium dengan 22 penyewaan. Ini juga menyatakan bahwa suhu yang nyaman (Medium & High) meningkatkan penyewaan sepeda, sementara suhu ekstrem (sangat dingin atau panas) cenderung menurunkan jumlah penyewaan.")
    