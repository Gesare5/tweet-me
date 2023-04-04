from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .models import Tweet

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Hello world</h1>")
    return render(request, 'pages/home.html', context={}, status=200)

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    # print(args, kwargs)
    """
    REST API VIEW
    return json data for consumption by JS
    """
    data={
        "id": tweet_id,
        # "content": obj.content,
        # "image_path": obj.image.url
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data["content"]= obj.content
    except:
        data["message"] = "Not found"
        status = 404
        # raise Http404
    
    return JsonResponse(data, status=status) #json.dumps content_type='application/json'
    # return HttpResponse(f"<h1> Hello {tweet_id} - {obj.content}</h1>")
