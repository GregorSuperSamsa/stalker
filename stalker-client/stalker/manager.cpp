#include "manager.h"
#include <QtDebug>
#include <QJsonDocument>


Manager::Manager(QObject *parent) : QObject(parent)
{
    networkManager = new QNetworkAccessManager(this);
    QObject::connect(networkManager, SIGNAL(finished(QNetworkReply*)), this, SLOT(onNetworkReply(QNetworkReply*)));

    timer = new QTimer(this);
    QObject::connect(timer, SIGNAL(timeout()), this, SLOT(onTimeout()));
    timer->setInterval(10000);
    timer->start();
}


void Manager::onTimeout()
{
    QNetworkRequest request(QUrl("http://127.0.0.1:5000/olx?query=bmw&query=awo"));
    networkManager->get(request);
}


void Manager::onNetworkReply(QNetworkReply* reply)
{
    QByteArray byteArray = reply->readAll();


    QString s = QString::fromUtf8(byteArray.constData());
    qDebug().noquote() << endl << endl << endl << s;

    QJsonDocument jsonDoc = QJsonDocument::fromJson(s.toUtf8());
    qDebug()<<jsonDoc.toJson();

    reply->deleteLater();
}
