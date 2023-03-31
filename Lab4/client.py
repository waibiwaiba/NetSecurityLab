from json import JSONDecodeError

import requests
import wx
import os
import scheme
import json
from ui.window import MainFrame

HOST = 'localhost:9527'


class MyFrame(MainFrame):
    def login(self, event):
        try:
            username = self.text_user.Value
            password = self.text_pass.Value
            r = requests.get(f'http://{HOST}')
            if r.text != '"Hello, world!"':
                wx.MessageBox('Server down.')
                return
            salt = os.urandom(16).hex()
            print('salt = os.urandom(16).hex():\n', salt)
            wx.MessageBox(f'auth code: {salt}')
            r = requests.post(f'http://{HOST}/login', timeout=2, data=json.dumps(
                scheme.create_login_request(username, password, salt)))
            # if not r.ok:
            j = json.loads(r.text)
            if msg := j.get('message'):
                if 'data' in j:
                    data = bytes.fromhex(j['data'])
                    response, iv = scheme.decrypt(data[16:],
                                              k=scheme.sha512(username+password).encode('utf-8'),
                                              iv=data[:16])
                    # print(response)
                    # print(iv)
                    response = response.decode('utf-8')
                    print('response:\n', response)
                    # iv = iv.decode('utf-8')
                    wx.MessageBox(f'Server response: {msg}\nData: {response}')
                    file_dir = os.path.dirname(__file__)
                    file_name = 'Authentic_Code.txt'
                    file_path = os.path.join(file_dir, file_name)
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(response)
                else:
                    wx.MessageBox(f'Server response: {msg}' )
            else:
                wx.MessageBox(f'Invalid server response: {r.text}')
        except JSONDecodeError:
            wx.MessageBox('Invalid response from server.')
        except IOError as e:
            wx.MessageBox(f'Cannot connect to server:\n{e}')




class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True


# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
