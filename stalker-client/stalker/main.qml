import QtQuick 2.9
import QtQuick.Controls 2.2

ApplicationWindow
{
    id: root
    visible: true
    width: 640
    height: 480
    title: qsTr("Stalker")

    Rectangle
    {
        id: control
        width: parent.width
        height: parent.height / 4
        color: "orange"

        MouseArea
        {
            anchors.fill: parent
            onClicked:
            {
                console.log("click")
                listview.forceLayout()
            }

        }


        ScrollView
        {
            id: scroll
            anchors.top: control.bottom
            ListView
            {
                id: listview
                width: parent.width
                model: datamodel
                delegate: delegateItem

                onModelChanged:
                {
                    console.log("Model changed")
                }
            }



        }

        Component
        {
            id: delegateItem
            Rectangle
            {
                anchors.left: parent.left
                anchors.right: parent.right
                color: "transparent"
                Text
                {
                    id: url
                    text: type
                    color: "black"
                }
                Text
                {
                    id: title
                    anchors.top: url.bottom
                    text: size
                    color: "black"
                }
            }
        }
    }
}
