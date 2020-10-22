from django.shortcuts import render
import random
import urllib.request
import re
import requests
'''
apilink1 = {
        'fetchTrending': f"/trending/all/week?api_key={API_KEY}&language=en-US",
        'fetchNetflixOriginals': f"/discover/tv?api_key={API_KEY}&with_network=213",
        'fetchTopRated': f"/movie/top_rated?api_key={API_KEY}&language=en-US",
        'fetchActionMovies': f"/discover/movie?api_key={API_KEY}&with_genres=28",
        'fetchComedyMovies': f"/discover/movie?api_key={API_KEY}&with_genres=35",
        'fetchHorrorMovies': f"/discover/movie?api_key={API_KEY}&with_genres=2",
        'fetchRomanceMovies': f"/discover/movie?api_key={API_KEY}&with_genres=10749",
        'fetchDocumentaries': f"/discover/movie?api_key={API_KEY}&with_genres=99",
}'''
API_KEY = "bd864435dd7797c806bcf423161c20ac"
apilink = {
        'Trending': f"/trending/all/week?api_key={API_KEY}&language=en-US",
        'Netflix Originals': f"/discover/tv?api_key={API_KEY}&with_network=213",
        'Top Rated': f"/movie/top_rated?api_key={API_KEY}&language=en-US",
        'Action Movies': f"/discover/movie?api_key={API_KEY}&with_genres=28",
        'Comedy Movies': f"/discover/movie?api_key={API_KEY}&with_genres=35",
        'Horror Movies': f"/discover/movie?api_key={API_KEY}&with_genres=2",
        'Romance Movies': f"/discover/movie?api_key={API_KEY}&with_genres=10749",
        'Documentaries': f"/discover/movie?api_key={API_KEY}&with_genres=99",
}
#title ={0:"Trending",1:"Netflix Originals",2:"Top Rated",3:"Action Movie",4:"Comedy Movie",5:"Horror Movie",6:"Romace Movie",7:"Documentries"}
title ={'fetchTrending':"Trending",'fetchNetflixOriginals':"Netflix Originals",'fetchTopRated':"Top Rated",'fetchActionMovies':"Action Movie",'fetchComedyMovies':"Comedy Movie",'fetchHorrorMovies':"Horror Movie",'fetchRomanceMovies':"Romace Movie",'fetchDocumentaries':"Documentries"}
base = "https://api.themoviedb.org/3"
# Create your views here.
#https://www.youtube.com/results?search_query=enola+holmes
def index(request):
    if request.method == "GET":
        print('post')
        query = 'Enola+Holmes'
        #query1 = query.replace('-', '+')
        html = urllib.request.urlopen(f'https://www.youtube.com/results?search_query={query}')
        video_ids = re.find(r"match\?v=(\s{11})",html.read().decode())
        print(video_ids)
        return render(request, 'index.html', {'video_ids':video_ids})
    
    API_KEY = "bd864435dd7797c806bcf423161c20ac"
    # print(requests1[])
    # https://api.themoviedb.org/3/trending/all/week?api_key=bd864435dd7797c806bcf423161c20ac&language=en-US
    all_data = {}
    ytbase = "https://www.youtube.com/results?search_query="
    for key,value in apilink.items():
        result =requests.get(base + value)
        results = result.json()
        data1 = results['results']
        row_dict = {}
        for i in range(len(data1)):    
            row_dict[i] = data1[i]	
            all_data[key] = row_dict	
			
	#link = f"/trending/all/week?api_key={API_KEY}&language=en-US"
    #result = requests.get(base + link)		
    #results = result.json()
    #data1 = results['results']
    #row_dict = {}
	
    #for i in range(len(data1)):    
    #    row_dict[i] = data1[i]		
	
    
    #print(all_data)
	
    isLarge = ['Trending']
    #name = data['name']
    #desc = data['overview']
    #poster_path = data['poster_path']
    base_url = "https://image.tmdb.org/t/p/original"
    #poster_path = base_url+poster_path
    #dictionary = {'name': name, 'poster_path': poster_path, 'desc': desc}
    #print(dictionary)
    banner = all_data['Trending'][random.randint(0,19)]
    #print(banner)
    return render(request , 'index.html', {'ytbase':ytbase,'banner':banner,'isLarge':isLarge,'apilink':apilink,'title': title,'all_data' : all_data,'data': row_dict,'base_url': base_url})
