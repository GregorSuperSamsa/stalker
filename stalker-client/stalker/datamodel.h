#ifndef DATAMODEL_H
#define DATAMODEL_H

#include <QObject>
#include <QAbstractListModel>
#include <QStringList>


class StalkerData
{
public:
    StalkerData(const QString &headline, const QString &text, const QStringList &images, const QString &user,  const QString &contacts);

    QString uniqueId() const;
    QString dateTime() const;
    QString headline() const;
    QString text() const;
    QStringList images() const;
    QString price() const;
    QString user() const;
    QString contacts() const;

private:
    QString m_uniqueId;
    QString m_dateTime;
    QString m_headline;
    QString m_text;
    QStringList m_images;
    QString m_user;
    QString m_contacts;
    QString m_price;
};

class StalkerDataModel : public QAbstractListModel
{
    Q_OBJECT
public:
    enum DataRoles
    {
        UniqueIdRole = Qt::UserRole + 1,
        DateTimeRole,
        HeadlineRole,
        TextRole,
        ImagesRole,
        PriceRole,
        UserRole,
        ContactsRole
    };

    StalkerDataModel(QObject *parent = 0);

    void addData(const StalkerData &data);

    int rowCount(const QModelIndex & parent = QModelIndex()) const;

    QVariant data(const QModelIndex & index, int role = Qt::DisplayRole) const;

protected:
    QHash<int, QByteArray> roleNames() const;

private:
    QList<StalkerData> m_dataItems;

};

#endif // DATAMODEL_H
