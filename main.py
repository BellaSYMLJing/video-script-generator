import streamlit as st
from utils import generate_script

st.title("🎬视频脚本生成器")

with st.sidebar:
    openai_api_key = st.text_input("🔒请输入Deepseek api密钥：",type="password")
    st.markdown("[获取DeepSeek api密钥](https://platform.deepseek.com/api_keys)")

subject = st.text_input("💡请输入视频的主题")
video_length = st.number_input("🕙请输入视频的大致时常（单位：分钟）",min_value=0.1,step=0.1)
creativity = st.slider("✨请输入视频脚本的创造力（数字越小越严谨，数字越大越多样）",min_value=0.0,max_value=1.0,value=0.2,step=0.1)
submit = st.button("生成脚本")

if submit and not openai_api_key:
    st.info("🔒请输入你的API密钥")
    st.stop()

if submit and not subject:
    st.info("请输入你的视频主题")
    st.stop()

if submit and not video_length >= 0.1:
    st.info("视频长度需要大于等于0.1")
    st.stop()

if submit:
    with st.spinner(("AI正在思考中🤔️，请稍等...")):
        title, script = generate_script(subject,video_length,creativity,openai_api_key)
    st.success("视频脚本已生成！")
    st.subheader("标题：")
    st.write(title)
    st.subheader("脚本内容：")
    st.write(script)