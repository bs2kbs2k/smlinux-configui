from PyQt5.QtWidgets import QApplication
import PyQt5.QtWidgets as qw
import PyQt5.uic as uic
import sys
import os.path
app = QApplication(sys.argv)
ui = uic.loadUi(os.path.join(input(),'sml.ui'))
def dog(a):
    ui.opt_GIT.setEnabled(a == 2)
    ui.opt_BRANCH.setEnabled(a == 2)
    ui.opt_PRESET.setEnabled(a == 0)
def cat(a):
    ui.opt_MAXJOBS.setEnabled(a == 2)
ui.do_GIT.stateChanged.connect(dog)
ui.do_MAXJOBS.stateChanged.connect(cat)
def getStatus(el):
    if isinstance(el, qw.QComboBox):
        return el.itemText(el.currentIndex())
    elif isinstance(el, qw.QCheckBox):
        return el.checkState()//2
    elif isinstance(el, qw.QLineEdit):
        return el.text().__repr__()
    elif isinstance(el, qw.QSpinBox):
        return el.value()
    else:
        raise ValueError('')
def setStatus(el, data):
    if isinstance(el, qw.QComboBox):
        for item in range(el.count()):
            if el.itemText(item) == data:
                el.setCurrentIndex(item)
                break
    elif isinstance(el, qw.QCheckBox):
        el.setCheckState(int(data)*2)
    elif isinstance(el, qw.QLineEdit):
        if data[0]==data[-1] and data[0] in ('"', "'"):
            el.setText(eval(data))
        else:
            el.setText(data)
    elif isinstance(el, qw.QSpinBox):
        if data == '':
            return
        return el.setValue(int(data))
    else:
        raise ValueError('')
with open(input()) as f:
    for line in f.readlines():
        if line[0] == '#':
            continue
        if '=' in line:
            if line.strip('\n').split('=')[0] == 'O_PRESET':
                setStatus(eval('ui.opt_PRESET', '='.join(line.strip('\n').split('=')[1:]))
                continue
            setStatus(eval('ui.opt_'+line.strip('\n').split('=')[0]),
                      '='.join(line.strip('\n').split('=')[1:]))
ui.show()
outcode = app.exec_()
opts = [a[4:] for a in dir(ui) if a[:4]=='opt_']
out = ''
for opt in opts:
    if opt == 'PRESET' and getStatus(ui.do_GIT) == 1:
        out += 'O_'
    out += opt
    out += '='
    if opt == 'MAXJOBS' and getStatus(ui.do_MAXJOBS) == 0:
        out += '\n'
        continue
    out += str(getStatus(eval('ui.opt_'+opt)))
    out += '\n'
print(out)
sys.exit(outcode)
