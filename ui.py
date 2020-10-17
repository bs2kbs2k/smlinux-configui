from PyQt5.QtWidgets import QApplication
import PyQt5.QtWidgets as qw
import PyQt5.uic as uic
import sys
import os.path
app = QApplication(sys.argv)
ui = uic.loadUi(os.path.join(input(),'sml.ui'))
ui.show()
def getStatus(el):
    if isinstance(el, qw.QComboBox):
        return el.itemText(el.currentIndex())
    elif isinstance(el, qw.QCheckBox):
        return el.checkState()//2
    elif isinstance(el, qw.QLineEdit):
        return '"'+el.text().replace('"','\\"')+'"'
    else:
        raise ValueError('')
outcode = app.exec_()
opts = [a[4:] for a in dir(ui) if a[:4]=='opt_']
out = ''
def dog(a):
    ui.opt_GIT.setEnabled(a == 2)
    ui.opt_BRANCH.setEnabled(a == 2)
    ui.opt_PRESET.setEnabled(a == 0)
def cat(a):
    ui.opt_MAXJOBS.setEnabled(a == 2)
ui.do_GIT.stateChanged.connect(dog)
ui.do_MAXJOBS.stateChanged.connect(cat)
for opt in opts:
    if opt == 'PRESET' and getStatus(ui.do_GIT) == 1:
        out += 'PRESET=INVALID\n'
        continue
    if opt == 'MAXJOBS' and getStatus(ui.do_MAXJOBS) == 0:
        continue
    out += opt
    out += '='
    out += str(getStatus(eval('ui.opt_'+opt)))
    out += '\n'
print(out)
sys.exit(outcode)
