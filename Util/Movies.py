import requests
import random
"""
동영상 정보를 가져오는 클래스
동영상은 100개의 동영상만 return 해줌
따라서 maxCount = 총 동영상 갯수 - 100 
1~maxCount 중 랜덤값 ~ 랜덤값 + 100 개의 영상 * 중복방지를 위함.

return {
    resultCode : 200
    movies : ["url1","url2"]
    category : ""
    
}
"""
class Movies:
    def __init__(self):
        self.url = "http://localhost:1337/"
        self.moviesCount = 1

    def getMovieData(self):
        # 모든 영상에 대해 추출
        # movies 전체 갯수 가져오기
        try:
            datas = requests.get(self.url + "movies/count")
            self.moviesCount = int(datas.text)
        except:
            pass

        # 랜덤 값 가져오기
        if self.moviesCount > 100 :
            self.moviesCount -= 100
        self.moviesCount = self.randomProcess()
        dataObject = self.getObject()

        try:

            datas = requests.get(self.url+"movies?_start="+str(self.moviesCount))
            if datas.status_code == 200:
                datas = datas.json()

                movies, category = self.urlProcess(datas)
                dataObject["resultCode"] = 200
                dataObject["movies"] = movies
                dataObject["category"] = category
        except:
            pass

        return dataObject

    def getCategoryData(self, category):
        #카테고리별 영상 추출
        #추후 항목별 동영상 갯수에 따른 랜덤값 부여
        dataObject = self.getObject()
        try:
            datas = requests.get(self.url+"movies?category="+category)

            if datas.status_code == 200:
                datas = datas.json()
                movies, category = self.urlProcess(datas)
                dataObject["resultCode"] = 200
                dataObject["movies"] = movies
                dataObject["category"] = category
        except:
            pass
        return dataObject

    def randomProcess(self):
        count = random.randint(1, self.moviesCount)
        print(count)
        return count

    def urlProcess(self, datas):
        movies = []
        category = []

        for data in datas:
            movies.append(data['movieURL'].replace("https://www.youtube.com/watch?v=", ""))
            category.append(data['category'])

        return movies, category
    def getObject(self):

        object = {
            "resultCode" : 500,
            "movies" : [],
            "category" : []
        }
        return object
if __name__=="__main__":
    start = Movies()
    #start.getCategoryData("대인간지능")
    start.getMovieData()