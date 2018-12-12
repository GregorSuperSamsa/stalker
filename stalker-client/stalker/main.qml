import QtQuick 2.9
import QtQuick.Controls 2.2
import QtQuick.Layouts 1.3
import Qt.labs.platform 1.0
import QtQuick.Controls.Material 2.0


ApplicationWindow
{
    id: root
    Material.theme: Material.Dark
    visible: true
    width: 640
    height: 480
    title: qsTr("Stalker")

    RowLayout
    {
        anchors.fill: parent
        Pane
        {
            id: navigation
            Layout.fillHeight: true
            Layout.minimumWidth: 50
            Layout.preferredWidth: 100
            Layout.maximumWidth: 200
            Material.elevation: 10
            Material.background: "#424242"
        }

        ListView
        {
            Layout.fillHeight: true
            Layout.fillWidth: true

            id: listview
            clip: true
            spacing: 10
            rotation: 180
            model: stalkerDataModel
            delegate: delegateItem
        }
    }

    Component
    {
        id: delegateItem
        Pane
        {
            anchors.margins: 10
            rotation: 180
            anchors.left: parent.left
            anchors.right: parent.right
            height:  300
            //height: childrenRect.height //250

            Material.elevation: 10
            Material.background: "#424242"

            SwipeView
            {

                id: images
                anchors.top: parent.top
                anchors.left: parent.left
                anchors.right: parent.right
                height: 200
                Repeater
                {
                    model: data_images
                    Image
                    {
                        asynchronous: true
                        source: data_images[index]
                        fillMode: Image.PreserveAspectFit
                    }
                }
            }
            Text
            {
                id: headline
                anchors.top: images.bottom
                width: parent.width
                wrapMode: Text.WordWrap
                text: data_headline
                color: Material.color(Material.Grey)
                font.pixelSize: 15
            }
            Text
            {
                id: text
                width: parent.width
                wrapMode: Text.WordWrap
                anchors.top: headline.bottom
                text: data_text
                color: Material.color(Material.Grey)
            }
            Text
            {
                id: user
                width: parent.width
                wrapMode: Text.WordWrap
                anchors.top: text.bottom
                text: data_user
                color: Material.color(Material.Grey)
            }

            Text
            {
                id: contacts
                width: parent.width
                wrapMode: Text.WordWrap
                anchors.top: user.bottom
                text: data_contacts
                color: Material.color(Material.Grey)
            }
            Text
            {
                id: price
                width: parent.width
                wrapMode: Text.WordWrap
                anchors.top: user.bottom
                text: data_price
                color: Material.color(Material.Grey)
            }
        }
    }

    SystemTrayIcon
    {
        visible: true
        iconSource: "qrc:/images/icon.jpg"
        Component.onCompleted: showMessage("Message title", "Something important came up. Click this to know more.")
        menu: Menu
        {
            MenuItem
            {
                text: qsTr("Quit")
                onTriggered: {
                    notification.show()
                    //Qt.quit()
                }
            }
        }

        onActivated:
        {
            window.show()
            window.raise()
            window.requestActivate()
        }
    }

    Notify
    {
        id: notification
    }

}

