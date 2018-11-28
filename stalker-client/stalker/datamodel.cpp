#include "datamodel.h"


StalkerData::StalkerData() {}

void StalkerData::setHeadline(const QString &headline)
{
    m_headline = headline;
}

QString StalkerData::headline() const
{
    return m_headline;
}

void StalkerData::setText(const QString &text)
{
    m_text = text;
}

QString StalkerData::text() const
{
    return m_text;
}

void StalkerData::setImages(const QStringList &images)
{
    m_images = images;
}

QStringList StalkerData::images() const
{
    return m_images;
}

void StalkerData::setUser(const QString &user)
{
    m_user = user;
}

QString StalkerData::user() const
{
    return  m_user;
}

void StalkerData::setContacts(const QString &contacts)
{
    m_contacts = contacts;
}

QString StalkerData::contacts() const
{
    return m_contacts;
}

void StalkerData::setUniqueId(const QString &uniqueId)
{
    m_uniqueId = uniqueId;
}

QString StalkerData::uniqueId() const
{
    return m_uniqueId;
}

void StalkerData::setDateTime(const QString &dateTime)
{
    m_dateTime = dateTime;
}

QString StalkerData::dateTime() const
{
    return m_dateTime;
}

void StalkerData::setPrice(const QString &price)
{
    m_price = price;
}

QString StalkerData::price() const
{
    return m_price;
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

StalkerDataModel::StalkerDataModel(QObject *parent): QAbstractListModel(parent) {}

void StalkerDataModel::addData(const StalkerData &data)
{
    beginInsertRows(QModelIndex(), rowCount(), rowCount());
    m_dataItems << data;
    endInsertRows();
}

int StalkerDataModel::rowCount(const QModelIndex & parent) const
{
    Q_UNUSED(parent);
    return m_dataItems.count();
}

StalkerData* StalkerDataModel::getItem(const QModelIndex &index)
{
    if (index.row() < 0 || index.row() >= m_dataItems.count())
    {
        return nullptr;
    }

    return &m_dataItems[index.row()];
}

bool StalkerDataModel::setData(const QModelIndex &index, const QVariant &value, int role)
{
    bool result = false;

    if (!(index.row() < 0 || index.row() >= m_dataItems.count()))
    {
        StalkerData &data = m_dataItems[index.row()];
        switch (role)
        {
        case UniqueIdRole:
            if (!value.toString().isEmpty())
            {
                data.setUniqueId(value.toString());
                result = true;
            }
            return true;
            break;
        case DateTimeRole:
            if (!value.toString().isEmpty())
            {
                data.setDateTime(value.toString());
                result = true;
            }
            break;
        case HeadlineRole:
            if (!value.toString().isEmpty())
            {
                data.setHeadline(value.toString());
                result = true;
            }
            break;
        case TextRole:
            if (!value.toString().isEmpty())
            {
                data.setText(value.toString());
                result = true;
            }
            break;
        case ImagesRole:
            if (0 != value.toStringList().count())
            {
                data.setImages(value.toStringList());
                result = true;
            }
            break;
        case PriceRole:
            if (!value.toString().isEmpty())
            {
                data.setPrice(value.toString());
                result = true;
            }
            break;
        case UserRole:
            if (!value.toString().isEmpty())
            {
                data.setUser(value.toString());
                result = true;
            }
            break;
        case ContactsRole:
            if (!value.toString().isEmpty())
            {
                data.setContacts(value.toString());
                result = true;
            }
            break;
        default:
            result = false;
            break;
        }
    }

    if (result)
    {
        emit dataChanged(index, index);
    }

    return result;
}

QVariant StalkerDataModel::data(const QModelIndex &index, int role) const
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
