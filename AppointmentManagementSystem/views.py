from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . import Google, CreateAudioFile, GmailSendEmail


@csrf_exempt
def index(request):
    context = {}
    context["id"] = "1kVgeejqKW4bj5-qGBWYs1yIyfq5Zh0xM"
    return render(request, "Test/index.html", context=context)

@csrf_exempt
def here(request):
    print("here")

@csrf_exempt
def home(request):
    if request.method == "POST":
        print("post")
        print("a: ",request.GET.get('a'))
        print("b: ",request.GET.get('b'))
        print("c: ",request.GET.get("c"))
        print("d: ",request.GET.get("d"))
    closed_dates = Google.main()
    print(closed_dates)
    return render(request, "Test/index.html")

def uploaded_stream(request):
    context = {}
    if request.method == "POST":
        QueryDict = request.POST
        print(request.POST)
        content_to_speak = CreateAudioFile.prepare_content_for_audio_file(request.POST)
        print(content_to_speak)
        CreateAudioFile.create_audio_file(content_to_speak, request.POST['file_name'])
        context['email'] = QueryDict['email']
        context['fullname'] = QueryDict['fullname']
        context['phone'] = QueryDict['phone']
        context['gender'] = QueryDict['gender']
        context['somedate'] = QueryDict['somedate']
        context['appt'] = QueryDict['appt']
        context['address'] = QueryDict['address']
        context['complaints'] = QueryDict['complaints']
        context['file_name'] = QueryDict['file_name']
    return render(request, "Test/summary.html", context= context)


def confirm(request):
    queryDict = request.POST
    plain_message = GmailSendEmail.create_plain_message(queryDict)
    response = GmailSendEmail.share_details_with_clinic(plain_message)
    return render(request, "Test/ConfirmationScreen.html", context={"response": response})


