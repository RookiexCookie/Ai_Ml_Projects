import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Hospital Appointment Analysis")

st.title("Hospital Appointment Analysis")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.dataframe(df.head())

    cancellation_rate = df.cancelled.mean()
    wait_cancel_corr = (df.wait_days.corr(df.cancelled)) * 100

    st.subheader("Overall Results")
    st.write("Overall Cancellation Rate:", cancellation_rate)
    st.write("Wait Days vs Cancellation Correlation:", wait_cancel_corr)

    dept_cancel = df.groupby("department")["cancelled"].mean()
    st.subheader("Cancellation Rate by Department")
    fig1, ax1 = plt.subplots()
    dept_cancel.plot(kind="bar", ax=ax1)
    plt.ylabel("Cancellation Rate")
    plt.title("Cancellation Rate by Department")
    st.pyplot(fig1)

    day_cancel = df.groupby("appointment_day")["cancelled"].mean()
    st.subheader("Cancellation Rate by Appointment Day")
    fig2, ax2 = plt.subplots()
    day_cancel.plot(kind="bar", ax=ax2)
    plt.ylabel("Cancellation Rate")
    plt.title("Cancellation Rate by Day")
    st.pyplot(fig2)

    booking_cancel = df.groupby("booking_type")["cancelled"].mean()
    st.subheader("Cancellation Rate by Booking Type")
    fig3, ax3 = plt.subplots()
    booking_cancel.plot(kind="bar", ax=ax3)
    plt.ylabel("Cancellation Rate")
    plt.title("Cancellation Rate by Booking Type")
    st.pyplot(fig3)
