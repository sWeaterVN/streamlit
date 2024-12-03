    import streamlit as st
    import time
    bt = st.button("start")

    time.sleep(1)
    if bt:
        bar = st.progress(0, text="Loading..")
        for i in range(0, 100):
            time.sleep(0.01)
            bar.progress(i+1, text="Loading..")
        time.sleep(1)
        st.balloons()

