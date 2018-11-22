#ifndef MANAGER_H
#define MANAGER_H

#include <QObject>
#include <QNetworkAccessManager>
#include <QNetworkReply>
#include <QNetworkRequest>
#include <QTimer>


class Manager : public QObject
{
    Q_OBJECT
public:
    explicit Manager(QObject *parent = nullptr);

private:
    QNetworkAccessManager* networkManager;
    QTimer *timer;

public slots:
    void onTimeout();
    void onNetworkReply(QNetworkReply* reply);

signals:
};

#endif // MANAGER_H
