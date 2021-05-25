from django.shortcuts import render
from recipeapp import models
# Create your views here.
def index(request):
    return render(request,"recipe/index.html")

def recipeList(request):
    #web => 모든 데이터가 문자열이다
    page=request.GET['page']
    curpage=int(page)
    #데이터베이스 연결
    list=models.recipeListData(curpage) #튜플 => 전송 (딕트)
    totalpage=models.recipeTotalPage()
    '''
         튜플 => (값,값....)
         딕트 => {"키":값....}
         (1, '묵은지 김치김밥 만들기 도시락싸기 점심메뉴로 딱', 
         'https://recipe1.ezmember.co.kr/cache/recipe/2021/03/26/acc98862411d58eb5a2cc923b0a52d201_m.jpg', 
         '햇살머금은집', 1), (2, '간식 저녁메뉴로도 좋은 토마토 미트볼스파게티 만들기', 'https://recipe1.ezmember.co.kr/cache/recipe/2021/03/26/f8a6c9623ac463f564114d1b78bb763d1_m.jpg', '햇살머금은집', 2), (3, '자취생의 일주일 밑반찬만들기', 'https://recipe1.ezmember.co.kr/cache/recipe/2021/03/26/8c3bf866ea9ab8a6ad853fb3ef73d6041_m.jpg', '꼼지락걸', 3), (4, '두부면으로 만든 볶음면 고단백, 저칼로리 요리', 'https://recipe1.ezmember.co.kr/cache/recipe/2021/03/26/21d6dc26ec4e77330a26c6fe049b003d1_m.jpg', '아름다울가', 4), (5, '백종원 감자전', 'https://recipe1.ezmember.co.kr/cache/recipe/2021/03/26/579c9719e9d0d58083ad19c057d83efa1_m.jpg', '꼼지락걸', 5), (6, '향기롭고 쫄깃한 쑥 찹쌀전 #친정엄마 레시피', 'https://recipe1.ezmember.co.kr/cache/recipe/2021/03/26/28af5e049d634cf149665e8ae65bed361_m.jpg', 'hiisu', 6), (7, '초간단 쪽파김치 담그는방법', 'https://recipe1.ezmember.co.kr/cache/recipe/2021/03/26/ac746e0f92fd37262527c3967a19482e1_m.jpg', '꼼지락걸', 7), (8, '오븐 군밤', 'https://recipe1.ezmember.co.kr/cache/recipe/2021/03/26/ccb70f1770d6825a20f33e638a36a51a1_m.jpg', '밥심은국력', 8), (9, '콩자반 만들기/기본 밑반찬/달콤짭쪼름한 맛/beans cooked in soy sauce', 'https://recipe1.ezmember.co.kr/cache/recipe/2021/03/26/45849b64428c7f8a2793fb542bbb10851_m.png', '자연주부', 9), (10, '유채나물 물김치~봄나물김치', 'https://recipe1.ezmember.co.kr/cache/recipe/2021/03/21/b81ded226fe3312ac248b2a242f25ecd1_m.jpg', '왕눈이의맛있는이야기', 10), (11, '알면 알수록 신기한 무수분 돼지고기 김치찜', 'https://recipe1.ezmember.co.kr/cache/recipe/2021/03/25/ed231df7435dafa9a2a29dee05d7d6c01_m.jpg', '요알남Mingstar', 11), (12, '에어프라이어 매콤순살치킨 만들기! " 고추바사삭치킨 "', 'https://recipe1.ezmember.co.kr/cache/recipe/2021/03/23/b7a81040394506a42d64860596332b801_m.jpg', '만개의레시피', 12)]

    '''
    recipe_list=[]
    for r in list:
        rr={"no":r[0],"title":r[1],"poster":r[2],"chef":r[3]}
        recipe_list.append(rr)

    block=10
    startPage=((curpage-1)/block*block)+1
    endPage=((curpage-1)/block*block)+block
    if endPage>totalpage:
        endPage=totalpage

    return render(request,"recipe/recipe_list.html",{"block":int(block),"startPage":int(startPage),"endPage":int(endPage),"curpage":int(curpage),"totalpage":int(totalpage) , "list":recipe_list})

def recipeDetail(request):
    no=request.GET['no']
    #no,poster,chef,chef_poster,title,content,info1,info2,info3,food_make,chef_info
    detail=models.recipeDetailData(no)
    recipe_detail={"no":detail[0],"poster":detail[1],"chef":detail[2],"chef_poster":detail[3],
                      "title":detail[4],"content":detail[5],"info1":detail[6],"info2":detail[7],
                      "info3":detail[8],"chef_info":detail[9]}
    return render(request,'recipe/recipe_detail.html',{"rd":recipe_detail})