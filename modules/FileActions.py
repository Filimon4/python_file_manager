class ActionsApp():
    def __init__(self, app):
        self.app = app
        self.ui = app.ui

        self.quit_action = self.ui.actionQuit

        self.about_action = self.ui.actionAbout
        self.about_qt_action = self.ui.actionAbout_Qt

        self.newFolder_action = self.ui.actionMake_folder
        self.newFile_action = self.ui.actionNew_File
        self.delete_action = self.ui.actionDelete_folder
        self.rename_action = self.ui.actionRename
        self.move_action = self.ui.actionMove
        self.copy_action = self.ui.actionCopy
        self.paste_action = self.ui.actionPaste
        self.cut_action = self.ui.actionCut

        self.quit_action.triggered.connect(self.app.FileS.quit)
        self.about_qt_action.triggered.connect(self.app.FileS.about_qt)
        self.about_action.triggered.connect(self.app.FileS.about)

        self.newFile_action.triggered.connect(self.app.FileO.newFile)
        self.newFolder_action.triggered.connect(self.app.FileO.newFolder)
        self.delete_action.triggered.connect(self.app.FileO.delete)
        self.rename_action.triggered.connect(self.app.FileO.rename)
        self.move_action.triggered.connect(self.app.FileO.move)
        self.copy_action.triggered.connect(self.app.FileO.copy)
        self.paste_action.triggered.connect(self.app.FileO.paste)
        self.cut_action.triggered.connect(self.app.FileO.cut)
