import streamlit as st
import pandas as pd
import plotly.express as px

st.title('タイトル：テスト')

# サイドバー
# ファイルアップロード
uploaded_file = st.sidebar.file_uploader("ファイルアップロード", type='csv') 

# グラフx軸設定
x_axis = st.sidebar.selectbox('x軸項目',('社員数', '売上', '商品数'))


# メイン画面
st.header('読み込みデータ表示')
if uploaded_file is not None:
    # アップロードファイルをメイン画面にデータ表示
    df = pd.read_csv(uploaded_file)
    st.write(df)

    # 選ばれたx軸の値からグラフ化
    st.header('グラフ表示')
    fig = px.scatter(x=df[x_axis], y=df['y軸ラベル'])
    st.plotly_chart(fig, use_container_width=True)