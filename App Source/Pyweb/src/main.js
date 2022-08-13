const electron = require('electron')
const app = electron.app
const BrowserWindow = electron.BrowserWindow

let mainWindow

function createWindow() {
    mainWindow = new BrowserWindow({ width: 800, height: 600 })
    mainWindow.loadURL('http://localhost:8000/main.html');
    mainWindow.on('closed', function () {
        mainWindow = null
    })
}

app.on('ready', createWindow)

app.on('window-all-closed', function () {
    app.quit()
});

app.on('activate', function () {
    if (mainWindow === null) {
        createWindow()
    }
})




document.querySelector("button").onclick = function summation() {
    var data_1 = document.getElementById("int1").value
    var data_2 = document.getElementById("int2").value
    eel.add(data_1, data_2)(call_Back)
}

function call_Back(output) {
    document.getElementById("res").value = output
}