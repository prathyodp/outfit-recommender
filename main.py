
from recommender.outfit_recommender import OutfitRecommender

def main():
    recommender = OutfitRecommender("data/outfits.csv")
    print("Recommendations for color='olive', occasion='Formal':")
    print(recommender.recommend(color='olive', occasion='Formal'))

if __name__ == "__main__":
  main()
