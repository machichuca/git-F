import streamlit as st
#標準機能以外の独自UIや外部コードを埋め込む機能
import streamlit.components.v1 as components
import html
import json

#タイトル
st.title("KP用コピペツール")

#本文
st.write("テキストファイルをアップロード")
st.write("読み込んだ文章をクリックするとコピー可能")

uploaded_file=st.file_uploader(
    "シナリオ用のテキストファイルを選択",
    type=["txt","md"]
)

#アップロードしたファイルを受け取る
if uploaded_file is not None:
    #アップロードした中身を文字として読む
    text=uploaded_file.read().decode("utf-8")

    st.subheader("読み込み結果")
    
    #空行を除いて１行ずつに分ける（１行ごとに分解）
    lines=[line.strip() for line in text.splitlines() if line.strip()]

    st.write(f"{len(lines)}行を読み込みました")

    for i, line in enumerate(lines, start=1):
        safe_line=html.escape(line)
        js_line=json.dumps(line)

        components.html(
            f"""
            <button
                onclick="navigator.clipboard.writeText(`{safe_line}`)"
                style="
                    display:block;
                    width:100%;
                    text-align:left;
                    margin:6px 0;
                    padding:10px;
                    border-radius:8px;
                    border:1px solid #ccc;
                    background:#fff;
                    cursor:pointer;
            "
            >
                {i}.{safe_line}
        </button>
        """,
        height=50
        )