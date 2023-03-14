import openai
from tkinter import *


#创建边框类
class Gui_frame:
    #初始化
    def __init__(self):
        self.top = Tk()
        self.top.title('openai')
        self.top.geometry('800x500+500+100')
        self.data_Button = None
        self.data_Label = None
        self.data_Entry = None
        self.data_Text = None

    #发送openai请求
    def openai_req(self):
        #key已经删除"使用需要换成别的key"
        openai.api_key = "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"
        Entry_text =  self.data_Entry.get()
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": Entry_text }
            ]
        )
        # 将返回的信息插入到信息文本框中
        self.data_Text.insert('insert', response.choices[0].message['content'])

    #Gui布局
    def buju(self):
        self.data_Label = Label(self.top, text='请输入内容', width=15, height=2)
        self.data_Entry = Entry(self.top, show=None)
        self.data_Button = Button(self.top, text='提交', command=self.openai_req)
        self.data_Text = Text(self.top)
        self.data_Label.grid(row=5, column=20)
        self.data_Entry.grid(row=5, column=100)
        self.data_Button.grid(row=9, column=300)
        self.data_Text.grid(row=50, column=100)
        self.top.mainloop()


if __name__ == '__main__':
    Gfr = Gui_frame()
    Gfr.buju()








