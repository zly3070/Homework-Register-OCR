# Homework-Register-OCR
A lightweight OCR-based homework registration system that extracts student IDs from images and checks submission status.<br>
基于 OCR 的作业自动登记工具，支持拍照识别学号并统计未交名单。

# 作业登记助手 (Homework-Register-OCR)

> 通过拍照识别学号，自动统计作业提交情况，帮助老师快速完成作业登记。

## 功能
- 通过微信小程序上传作业照片，自动识别学号
- 与班级名单比对，标记未交学生
- 支持导出未交名单

## 技术栈
- Python + Flask
- 百度OCR（手写文字识别）
- SQLite
- GitHub Pages（展示）

## 运行方式
``` pythom
# 项目进行中……这块暂时用不了
# 克隆项目
git clone https://github.com/你的用户名/Homework-Register-OCR.git

# 安装依赖
pip install -r requirements.txt

# 启动服务
python app.py
```
