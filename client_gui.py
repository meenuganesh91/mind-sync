#The client gui application
import wxversion
wxversion.select("3.0")
import wx

import socket
import sys

#The main panel
class MainPanel(wx.Frame):
  
    def __init__(self, parent, title):
        super(MainPanel, self).__init__(parent, title=title, 
            size=(500, 500))
        panel = wx.Panel(self)

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        fgs = wx.FlexGridSizer(3, 2, 9, 25)

        userSizer = wx.StaticText(panel, label="User name")
        passSizer = wx.StaticText(panel, label="Password")
	
	loginbut = wx.Button(panel, label='Login', pos=(50, 200))

	signupbut = wx.Button(panel, label='Sign up', pos=(290, 200))

	self.tc1 = wx.TextCtrl(panel, style = wx.TE_PROCESS_ENTER)

        self.tc2 = wx.TextCtrl(panel, style=wx.TE_PASSWORD|wx.TE_PROCESS_ENTER)

	loginbut.Bind(wx.EVT_BUTTON, self.OnConnectInit)
	signupbut.Bind(wx.EVT_BUTTON, self.OnConnectInit)

        fgs.AddMany([(userSizer), (self.tc1, 1, wx.EXPAND), (passSizer), 
            (self.tc2, 1, wx.EXPAND)])

        fgs.AddGrowableRow(2, 1)
        fgs.AddGrowableCol(1, 1)

        hbox.Add(fgs, proportion=1, flag=wx.ALL|wx.EXPAND, border=15)
        panel.SetSizer(hbox)
        self.Centre()
        self.Show()  

    #def OnLogin(self, e):
	
        
    def OnConnectInit(self, e): 
	
	print 'User name: ', self.tc1.GetValue()
	print 'Password: ', self.tc2.GetValue()
	code = ''
	serverFormat = str(code)+':'+self.tc1.GetValue()+':'+self.tc2.GetValue()
	
	print 'Server Format: ', serverFormat
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	host = socket.gethostbyname(sys.argv[1])
	port = int(sys.argv[2])
	serverAddress = (host,port)
	sock.connect(serverAddress)
	sock.send(serverFormat)
	errCode = sock.recv(1024)
	print "Error code : ", errCode
	if(errCode == "USER_NAME_ERROR" or errCode == "PASSWORD_ERROR" ):
		loginbut.Bind(wx.EVT_BUTTON, self.OnConnectInit)
		signupbut.Bind(wx.EVT_BUTTON, self.OnConnectInit)

        #print "You are now logged in."
	
	app2 = SecondPanel(None, title = 'Mind Sync')
	self.Hide()
	app2.Show()
        self.Close(True) 

#The second panel to be shown
class SecondPanel(wx.Frame):

    def __init__(self, parent, title):
        super(SecondPanel, self).__init__(parent, title=title, 
            size=(550, 500))
        pnl = wx.Panel(self)

	self.SetBackgroundColour((0,0,255))

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        fgs = wx.FlexGridSizer(3, 2, 9, 25)

	promptSizer = wx.StaticText(pnl, -1,
		label = "Enter the word that pops up in your mind on reading", pos = (20, 10))
	font = wx.Font(15,wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
	promptSizer.SetFont(font)
	promptSizer.SetForegroundColour((0,0,255))

	wordSizer = wx.StaticText(pnl, -1,label = "Dog", pos = (220, 50))
	font = wx.Font(25,wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
	wordSizer.SetFont(font)
	wordSizer.SetForegroundColour((255,0,0))
	
	enterbut = wx.Button(pnl, label='Enter', pos=(215, 200), size = (100,50))

	self.word = wx.TextCtrl(pnl, style = wx.TE_PROCESS_ENTER, pos = (175,100), 
	size = (200,100))

	enterbut.Bind(wx.EVT_BUTTON, self.OnButtonPress)
	
	timer = wx.Timer(pnl)
	timer.Start(100)	

	
	hbox.Add(fgs, proportion=1, flag=wx.ALL|wx.EXPAND, border=15)
        pnl.SetSizer(hbox)
        self.Centre()
        self.Show()

    def OnButtonPress(self, e):
	print "Entered word: ", self.word.GetValue()
	self.Close(True)


if __name__ == '__main__':
  
    app = wx.App()
    MainPanel(None, title='Mind Sync')
    app.MainLoop()
