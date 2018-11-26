#include "datamodel.h"


StalkerData::StalkerData(const QString &headline
           , const QString &text
           , const QStringList &images
           , const QString &user
           , const QString &contacts)
    : m_headline(headline)
    , m_text(text)
    , m_images(images)
    , m_user(user)
    , m_contacts(contacts) {}



QString StalkerData::headline() const
{
    return m_headline;
}

QString StalkerData::text() const
{
    return m_text;
}

QStringList StalkerData::images() const
{
    return m_images;
}

QString StalkerData::user() const
{
    return  m_user;
}

QString StalkerData::contacts() const
{
    return m_contacts;
}

QString StalkerData::uniqueId() const
{
    return m_uniqueId;
}

QString StalkerData::dateTime() const
{
    return m_dateTime;
}

QString StalkerData::price() const
{
    return m_price;
}

//////////////////////////////////////////////////////////////////////////

StalkerDataModel::StalkerDataModel(QObject *parent): QAbstractListModel(parent) {}

void StalkerDataModel::addData(const StalkerData &data)
{
    beginInsertRows(QModelIndex(), rowCount(), rowCount());
    m_dataItems << data;
    endInsertRows();
}

int StalkerDataModel::rowCount(const QModelIndex & parent) const {
    Q_UNUSED(parent);
    return m_dataItems.count();
}

QVariant StalkerDataModel::data(const QModelIndex & index, int role) const
{
    if (index.row() < 0 || index.row() >= m_dataItems.count())
    {
        return QVariant();
    }

    const StalkerData &data = m_dataItems[index.row()];
    switch (role)
    {
    case UniqueIdRole:
        return data.uniqueId();
        break;
    case DateTimeRole:
        return data.dateTime();
        break;
    case HeadlineRole:
        return data.headline();
        break;
    case TextRole:
        return data.text();
        break;
     case ImagesRole:
        return  data.images();
        break;
    case PriceRole:
        return data.price();
        break;
    case UserRole:
        return data.user();
        break;
    case ContactsRole:
        return data.contacts();
        break;
    default:
        return QVariant();
        break;
    }
}

QHash<int, QByteArray> StalkerDataModel::roleNames() const
{
    QHash<int, QByteArray> roles;

    roles[UniqueIdRole] = "data_uniqueId";
    roles[DateTimeRole] = "date_dateTime";
    roles[HeadlineRole] = "data_headline";
    roles[TextRole]     = "data_text";
    roles[ImagesRole]   = "data_images";
    roles[PriceRole]    = "data_price";
    roles[UserRole]     = "data_user";
    roles[ContactsRole] = "data_contacts";

    return roles;
}
