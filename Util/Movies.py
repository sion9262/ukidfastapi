import requests
"""
동영상 정보를 가져오는 클래스

return {
    resultCode : 200
    movies : ["url1","url2"]
    category : ""
    
}
"""
class Movies:

    def getMovieData(self):
        try:
            datas = requests.get("http://13.124.158.186:1337/movies")
            datas = datas.json()
            print(len(datas))
            print(datas)
        except:
            pass

    def getCategoryData(self, category):

        try:
            datas = requests.get("http://13.124.158.186:1337/movies?category="+category)
            datas = datas.json()
            print(datas)
        except:
            pass
    def dataObject(self):

        object = {
            "resultCode" : 500,
            "movies" : [],
            "category" : ""
        }
        return object
if __name__=="__main__":
    start = Movies()
    start.getCategoryData("대인간지능")