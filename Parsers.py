
def  movie_meta_datas(soup):
    id= soup.find_all('a', class_="showtime ng-binding ng-scope")
    for index, identities in enumerate(id):
        id[index]=id[index].get("id")
    url_data1_arr=[]
    url_data2_arr=[]
    url_data1=""
    url_data2=""
    url_arr=[]
    for idd in range(len(id)):
        for i in range(9,14):
            url_data1=url_data1+ id[idd][i]
        url_data1_arr.append(url_data1)
        url_data1=""

    for idd in range(len(id)):
        for i in range(18,27):
            url_data2=url_data2+ id[idd][i]
        url_data2_arr.append(url_data2)
        url_data2=""
    for i in range(len(url_data1_arr)):
        url_arr.append("https://onlineticketing.cineplex.com/SeatMap.aspx?locationId=1145&vistaSessionId="+url_data1_arr[i]+"&VISTAHOAreaCategoryCode="+url_data2_arr[i]+"&isExternal=True")
    return url_arr