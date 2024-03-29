#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((569, 419))
        self.SetTitle("lab4")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        grid_sizer_1 = wx.FlexGridSizer(3, 2, 8, 16)
        sizer_1.Add(grid_sizer_1, 1, wx.ALL | wx.EXPAND, 120)

        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "Username")
        grid_sizer_1.Add(label_1, 0, wx.ALL | wx.EXPAND, 0)

        self.text_user = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.text_user.SetMinSize((200, 34))
        grid_sizer_1.Add(self.text_user, 0, wx.EXPAND, 0)

        label_2 = wx.StaticText(self.panel_1, wx.ID_ANY, "Password")
        grid_sizer_1.Add(label_2, 0, wx.EXPAND, 0)

        self.text_pass = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        grid_sizer_1.Add(self.text_pass, 0, wx.EXPAND, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        self.button_1 = wx.Button(self.panel_1, wx.ID_ANY, "Login")
        grid_sizer_1.Add(self.button_1, 0, wx.EXPAND, 0)


        grid_sizer_1.AddGrowableRow(0)
        grid_sizer_1.AddGrowableRow(1)
        grid_sizer_1.AddGrowableRow(2)
        grid_sizer_1.AddGrowableCol(0)
        grid_sizer_1.AddGrowableCol(1)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.login, self.button_1)
        # end wxGlade

    def login(self, event):  # wxGlade: MainFrame.<event_handler>
        print("Event handler 'login' not implemented!")
        event.Skip()
# end of class MainFrame
