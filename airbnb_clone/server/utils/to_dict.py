def to_dict(hotel):
    return{
        "id" : hotel.id,
        "user_id" : hotel.user_id,
        "title" : hotel.title,
        "description" : hotel.description,
        "price" : hotel.price,
        "created_at": hotel.created_at,
        "updated_at": hotel.updated_at,
    }