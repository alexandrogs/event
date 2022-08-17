import win32api
import win32con
import win32evtlog
import win32security
import win32evtlogutil
ph = win32api.GetCurrentProcess()
th = win32security.OpenProcessToken(ph, win32con.TOKEN_READ)
sid = win32security.GetTokenInformation(th, win32security.TokenUser)[0]
ApplicationName = "Free"
EventID = 0
EventCategory = 0
EventType = win32evtlog.EVENTLOG_INFORMATION_TYPE
Inserts = "test"
Data = b"test"
SID = sid
win32evtlogutil.ReportEvent(ApplicationName, EventID, EventCategory,
    EventType, Inserts, Data, SID)
