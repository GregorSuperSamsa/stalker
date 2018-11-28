#ifndef DATAMODEL_H
#define DATAMODEL_H

#include <QObject>
#include <QAbstractListModel>
#include <QStringList>


class StalkerData
{
public:
    StalkerData();

    void setUniqueId(const QString &uniqueId);
    QString uniqueId() const;

    void setDateTime(const QString &dateTime);
    QString dateTime() const;

    void setHeadline(const QString &headline);
    QString headline() const;

    void setText(const QString &text);
    QString text() const;

    void setImages(const QStringList &images);
    QStringList images() const;

    void setPrice(const QString &price);
    QString price() const;

    void setUser(const QString &user);
    QString user() const;

    void setContacts(const QString &contacts);
    QString contacts() const;

private:
    QString m_headline;
    QString m_uniqueId;
    QString m_dateTime;
    QString m_text;
    QString m_user;
    QString m_contacts;
    QString m_price;
    QStringList m_images;
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

    StalkerData* getItem(const QModelIndex &index);

    int rowCount(const QModelIndex & parent = QModelIndex()) const;

    bool setData(const QModelIndex &index, const QVariant &value, int role);

    QVariant data(const QModelIndex & index, int role = Qt::DisplayRole) const;

protected:
    QHash<int, QByteArray> roleNames() const;

private:
    QList<StalkerData> m_dataItems;

};

#endif // DATAMODEL_H
