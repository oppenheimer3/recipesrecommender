import numpy as np

def recipes_recommender(fav_index):
    recipes_ingredients_=np.load('recommender\\tensor.npy')
    user_recipes=np.zeros(13487)
    for i in range(0,len(fav_index)):
        user_recipes[fav_index[i]]=10
    user_ingredients=np.matmul(user_recipes,recipes_ingredients_)
    user_rating=np.matmul(user_ingredients,np.transpose(recipes_ingredients_))
    ind = np.argpartition(user_rating, -(len(fav_index)+10))[-(len(fav_index)+10):]
    ind = np.delete(ind, np.argwhere(np.isin(ind,fav_index)))
    return ind




