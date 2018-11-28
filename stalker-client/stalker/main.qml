import QtQuick 2.9
import QtQuick.Controls 2.2

ApplicationWindow
{
    id: root
    visible: true
    width: 640
    height: 480
    title: qsTr("Stalker")
    color: "lightgray"

    Flickable
    {
        anchors.fill: parent
        ListView
        {
            rotation: 180
            id: listview
            width: parent.width
            height: childrenRect.height
            clip: true
            model: stalkerDataModel
            delegate: delegateItem
        }
    }

    Component
    {
        id: delegateItem
        Rectangle
        {
            rotation: 180
            anchors.left: parent.left
            anchors.right: parent.right
            height: childrenRect.height
            radius: 8
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
                text: data_headline
                color: "black"
            }
            Text
            {
                id: text
                anchors.top: headline.bottom
                text: data_text
                color: "black"
            }
            Text
            {
                id: user
                anchors.top: text.bottom
                text: data_user
                color: "black"
            }

            Text
            {
                id: contacts
                anchors.top: user.bottom
                text: data_contacts
                color: "black"
            }
            Text
            {
                id: price
                anchors.top: user.bottom
                text: data_price
                color: "black"
            }
        }
    }
}

