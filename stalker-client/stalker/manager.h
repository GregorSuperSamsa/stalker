#ifndef MANAGER_H
#define MANAGER_H

#include <QObject>
#include <QNetworkAccessManager>
#include <QNetworkReply>
#include <QNetworkRequest>
#include <QList>
#include <QTimer>
#include "datamodel.h"


class Manager : public QObject
{
    Q_OBJECT
public:
    explicit Manager(QObject *parent = nullptr);

    StalkerDataModel* stalkerModel;

private:
    QNetworkAccessManager* networkManager;
    QTimer *timer;

public slots:
    void onTimeout();
    void onNetworkReply(QNetworkReply* reply);

signals:
};

#endif // MANAGER_H
