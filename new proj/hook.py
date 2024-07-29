import pluggy
hookspec = pluggy.HookspecMarker("GetBigFile")
hookimpl = pluggy.HookimplMarker("GetBigFile")

@hookspec(firstresult=True)
def makeaUi():
    pass

@hookspec(firstresult=True)
def filesearch():
    pass

@hookspec
def others():
    pass

@hookspec(firstresult=True)
def plug_manage():
    pass

@hookspec(firstresult=True)
def plug_sql_ask():
    pass

