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

                dataObject = self.urlProcess(datas)

        except:
            pass

        return dataObject

    def getCategoryData(self, category):
        #카테고리별 영상 추출
        #추후 항목별 동영상 갯수에 따른 랜덤값 부여
        dataObject = self.getObject()
        try:
            datas = requests.get(self.url+"movies?category_contains="+category)

            if datas.status_code == 200:
                datas = datas.json()
                dataObject = self.urlProcess(datas)

        except:
            pass
        return dataObject

    def postUserMoives(self, movies):
        # 사용자가 시청한 무비 보내기
        print(movies)
        try:
            datas = requests.post(self.url+"userplaymovies", data=movies)

            if datas.status_code == 200 :
                return {
                    "ResultCode" : 200
                }
            else :
                return {
                    "ResultCode" : 500
                }
        except:
            pass

    def randomProcess(self):
        count = random.randint(1, self.moviesCount)
        print(count)
        return count

    def urlProcess(self, datas):

        movieObjects = self.getObject()
        movieObjects["resultCode"] = 200

        for data in datas:
            mObject = {
                "movieId": "",
                "title": "",
                "category": ""
            }
            mObject["movieId"] = data['movieURL'].replace("https://www.youtube.com/watch?v=", "")
            mObject["title"] = data['title']
            mObject["category"] = data['category']
            movieObjects["moviesObject"].append(mObject)
        return movieObjects
    def getObject(self):

        object = {
            "resultCode" : 500,
            "moviesObject" : []
        }
        return object
if __name__=="__main__":
    start = Movies()
    #start.getCategoryData("대인간지능")
    start.getMovieData()