#include "manager.h"
#include <QtDebug>
#include <QJsonDocument>
#include <QJsonArray>
#include <QJsonObject>
#include "datamodel.h"


Manager::Manager(QObject *parent) : QObject(parent)
{
    networkManager = new QNetworkAccessManager(this);
    QObject::connect(networkManager, SIGNAL(finished(QNetworkReply*)), this, SLOT(onNetworkReply(QNetworkReply*)));

    timer = new QTimer(this);
    QObject::connect(timer, SIGNAL(timeout()), this, SLOT(onTimeout()));
    timer->setInterval(1000);
    timer->start();

    stalkerModel = new StalkerDataModel();
}

void Manager::onTimeout()
{
    QNetworkRequest request(QUrl("http://127.0.0.1:5000/olx?query=стоп за аво"));
    networkManager->get(request);
}

void Manager::onNetworkReply(QNetworkReply* reply)
{
    QByteArray byteArray = reply->readAll();

    QString s = QString::fromUtf8(byteArray.constData());
    qDebug().noquote() << endl << endl << endl << s;

    QJsonDocument jsonResponse = QJsonDocument::fromJson(byteArray);
    QJsonArray jsonArray = jsonResponse.array();

    stalkerModel->removeRows(0, stalkerModel->rowCount());

    foreach (const QJsonValue & value, jsonArray)
    {
        QJsonObject obj = value.toObject();
        StalkerData sd;

        sd.setHeadline(obj["headline"].toString());
        sd.setContacts(obj["phone"].toString());
        sd.setDateTime(obj["date"].toString());
        sd.setImages(QStringList(obj["images"].toString()));
        sd.setImages(QStringList(obj["thumbnail"].toString()));
        sd.setPrice(obj["price"].toString());
        sd.setText(obj["text"].toString());
        sd.setUser(obj["user"].toString());

        stalkerModel->addData(sd);
    }

    reply->deleteLater();
}
