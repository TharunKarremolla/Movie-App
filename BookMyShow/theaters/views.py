from django.http  import HttpResponse,JsonResponse
import json
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from  .models import Theater
from django.core.cache import cache
from Show.models import Show

@login_required
def theater_view(request):
    if request.method == 'GET':
        cache_key ="theaters:list"
        cache_response = cache.get(cache_key)
        if cache_response:
            print("cached Data")
            return JsonResponse({"data" : cache_response}, safe=False)
        print("Bpdy ",request.GET.get('id'))
        theaters = list(Theater.objects.all().values())
        # Show.objects.get(movie)
        
        cache.set(cache_key,theaters,300)
        print("Uncached Data")

        return JsonResponse({"data" : theaters,'time': now()})

    elif request.method == 'POST':    
            if not request.user.is_staff:
                return JsonResponse({"data" : "You don't have access to ADD Theaters"})      
            data = json.loads(request.body)  
            name = data.get("name")
            location = data.get('location')
            capacity = data.get('capacity')                   
            theater = Theater(name = name,location = location,capacity = capacity)
            theater.save()
            cache.delete("theaters:list")
            return JsonResponse({'data':"New Theater Created"},status = 201)


@login_required
def theater_details(request,id):
    if request.method == 'GET':
        
        cache_key = f'theaters:list:{id}'
        cache_response = cache.get(cache_key)
        if cache_response:
             print("cached Data")
             return JsonResponse({'data' : cache_response},status=200,safe=False)
        try :
            theater = Theater.objects.filter(id = id).values().first()

        except Exception: 
             return JsonResponse({"Error" : f"Theater with  id : {id} doesn't exist"})
        print("uncached Data")
        cache.set(cache_key,theater,300)
        return JsonResponse({'data': theater },status = 200)
    
    elif request.method == 'PUT':
            if not request.user.is_staff:
                return JsonResponse({"data" : "You don't have access to Update Theaters"})
            try:
                data = json.loads(request.body)
                name = data.get("name")
                location = data.get('location')
                capacity = data.get("capacity")
            except:
                  return JsonResponse({'error':"Invalid"},status = 401)
            theater = Theater.objects.filter(id = id).update(name = name,location = location,capacity = capacity)
            cache.delete('theaters:list')
            cache.delete(f'theaters:list:{id}')
            return JsonResponse({'data':  "updated"},status = 200)
    
    elif request.method == "DELETE":
          if not request.user.is_staff:
            return JsonResponse({"data" : "You don't have access to Delete Theaters"})
          theater = Theater.objects.filter(id=id).values().first()
          if not theater:
               return JsonResponse({"Error" : "Theater doesnt exist with the given id"},status=400)
          Theater.objects.filter(id=id).delete()
          cache.delete('theaters:list')
          cache.delete(f'theaters:list:{id}')
          return JsonResponse({"Deleted" : theater})


